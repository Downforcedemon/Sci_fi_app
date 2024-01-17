from astroquery.mast import Observations

try:
    # Log in to MAST (ensure you have the correct token)
    my_session = Observations.login(token="new token")

    # Query for objects around "V4046 Sgr"
    t = Observations.query_object("V4046 Sgr", radius=".2 deg")

    # Check if any data is returned
    if len(t) > 0:
        # If data is present, print the length and specific data of interest
        print(f"Number of results: {len(t)}")
        hst_data = t[t['obs_collection'] == 'HST']['obs_collection', 'target_name', 'obs_id']
        print(hst_data)
    else:
        # If no data is present, print a message indicating this
        print("No data found for the given query.")

except Exception as e:
    # Print out any errors that occur during the process
    print(f"An error occurred: {e}")
