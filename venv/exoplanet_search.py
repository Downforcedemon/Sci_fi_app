from lightkurve import search_targetpixelfile, TessTargetPixelFile
import lightcurve as lk
import numpy as np
from astropy.time import Time 

# Define your target and paramaters
TARGET = 'KIC 6922244'
AUTHOR = "Kepler"
CADENCE = "long"
QUARTER = 4
FRAME = 42
PERIOD_START = 1
PERIOD_END = 5
PERIOD_NUM = 10000
FREQUENCY_FACTOR = 500

# Download the pixel file
pixel_file = search_targetpixelfile(TARGET,author=AUTHOR,cadence=CADENCE,quarter=QUARTER).download()

# plot a single fram from the pixel file
pixel_file.plot(frame=FRAME)

# Extract the light curve from the pixel file in graph. pixel_file.pipeline_mask is used to remove bad pixels
lc=pixel_file.to_lightcurve(aperture_mask=pixel_file.pipeline_mask)
lc.plot()

# Flatten the light curve to remove long term trends
flat_lc = lc.flatten()
flat_lc.plot()

# Perform a periodogram analysis to find the period with highest power
period = np.linspace(PERIOD_START,PERIOD_END,PERIOD_NUM)
bls_periodogram = lc.to_periodogram(method="bls",period=period, frequency_factor=FREQUENCY_FACTOR)
bls_periodogram.plot()

# Get the period for the strongest signal in the periodogram
planet_period = bls_periodogram.period_at_max_power
planet_t0 = bls_periodogram.transit_time_at_max_power
planet_duration = bls_periodogram.duration_at_max_power

# Fold the light curve at the period of the strongest signal to look for transits
folded_lc = flat_lc.fold(period=planet_period, epoch_time=planet_t0)
folded_lc.plot()

# convert the transit time to julian date
transit_date= Time(planet_t0, format='jd', scale='utc') 

# print out the period,transit time and duration
print(f"Period: {planet_period}")
print(f"Transit Time (Human-Readable): {transit_date.iso}")
print(f"Duration: {planet_duration}")

