import psycopg2
from lightkurve import search_targetpixelfile, search_lightcurvefile
import numpy as np
from astropy.time import Time

# Database connection parameters
db_params = {
    "host": "192.168.0.48",
    "database": "Star_light",
    "user": "postgres",
    "password": "password" 
}

# Function to fetch star data from the database
def fetch_star_data():
    conn = None
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        cur.execute("SELECT ticid FROM star_light LIMIT 1")  
        star_data = cur.fetchone()
        cur.close()
        return star_data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Function to process the light curve of a star
def process_star(ticid):
    try:
        print(f"Processing TIC ID {ticid}")

        # Retrieve the target pixel file. 
        search_result = search_targetpixelfile(f"TIC {ticid}")
        tpf_collection = search_result.download_all(quality_bitmask='hardest')

        # Check if the target pixel file is available
        if tpf_collection is None or len(tpf_collection) == 0:
            print(f"No target pixel file found for TIC ID {ticid}")
            return
        
        # process each target pixel file in the collection
        for tpf in tpf_collection:
            print(f"Processing file {tpf.path}")

            # plot a single frame
            tpf.plot(frame=42)

            #Extract and flatten the curve
            lc = tpf.to_lightcurve(aperture_mask=tpf.pipeline_mask).flatten()

            # perform a periodogram analysis to find the period with highest power
            period = np.linspace(0.5,15,10000)
            bls_periodogram = lc.to_periodogram(method = "bls", period=period,frequency_factor= 500)

            # Get the period, transit, and duration for the strongest signal in the periodogram
            planet_period = bls_periodogram.period_at_max_power
            planet_t0 = bls_periodogram.transit_time_at_max_power
            planet_duration = bls_periodogram.duration_at_max_power

            # Fold the light curve at the period of the strongest signal to look for transits
            folded_lc = lc.fold(period=planet_period, epoch_time=planet_t0)
            folded_lc.plot()

            # covert the transit time to a human readable format
            transit_date = Time(planet_t0, format='jd', scale='utc')

            # print out the period, transit time, and duration
            print(f"Period: {planet_period}")
            print(f"Transit Time (Human-Readable): {transit_date.iso}")
            print(f"Duration: {planet_duration}")

    except Exception as e:
            print(f"Error processing file {tpf.path}: {e}")
            
    except Exception as e:
        print(f"Error processing TIC ID {ticid}: {e}") 

# Main function
star_data = fetch_star_data()
if star_data: 
      process_star(star_data[0])
else:
      print("No star data found in the database")



   
