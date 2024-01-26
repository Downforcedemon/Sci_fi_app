import psycopg2
from lightkurve import search_targetpixelfile
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import matplotlib 

matplotlib.use('Agg')  # Use a non-interactive backend

# Database connection parameters
db_params = {
    "host": "192.168.0.45",
    "database": "Star_light",
    "user": "postgres",
    "password": "password"
}

def save_figure_to_base64(fig):
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return base64.b64encode(buf.read()).decode('utf-8')

def fetch_all_star_data():
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    cur.execute("SELECT ticid FROM star_light ORDER BY ticid")
    all_star_data = cur.fetchall()
    cur.close()
    conn.close()
    return all_star_data

def process_star(ticid):
    diagrams = {
        "snapshot": None,
        "lightcurve": None,
        "flatlightcurve": None,
        "foldedlightcurve": None
    }
    try:
        search_result = search_targetpixelfile(f"TIC {ticid}", mission='TESS')
        tpf_collection = search_result.download_all(quality_bitmask='default')

        if not tpf_collection:
            print(f"No target pixel files found for TIC ID {ticid}")
            return diagrams

        for tpf in tpf_collection:
            # Process the first TPF to create diagrams
            fig, ax = plt.subplots()
            tpf.plot(ax=ax)
            diagrams["snapshot"] = save_figure_to_base64(fig)

            lc = tpf.to_lightcurve()
            fig, ax = plt.subplots()
            lc.plot(ax=ax)
            diagrams["lightcurve"] = save_figure_to_base64(fig)

            flat_lc = lc.flatten(window_length=401)
            fig, ax = plt.subplots()
            flat_lc.plot(ax=ax)
            diagrams["flatlightcurve"] = save_figure_to_base64(fig)

            periodogram = flat_lc.to_periodogram(oversample_factor=1)
            fig, ax = plt.subplots()
            periodogram.plot(ax=ax)
            diagrams["foldedlightcurve"] = save_figure_to_base64(fig)
            break  # Only process the first TPF for simplicity

        with psycopg2.connect(**db_params) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE star_light 
                    SET diagram_snapshot = %s, 
                        diagram_lightcurve = %s,
                        diagram_flatlightcurve = %s,
                        diagram_foldedlightcurve = %s
                    WHERE ticid = %s
                """, (diagrams["snapshot"], diagrams["lightcurve"], 
                      diagrams["flatlightcurve"], diagrams["foldedlightcurve"], ticid))

    except Exception as e:
        print(f"Error processing TIC ID {ticid}: {e}")

    return diagrams


