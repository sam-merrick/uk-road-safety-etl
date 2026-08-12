import pandas as pd
from roadsafety_etl_pipeline import run_pipeline

# Run the pipeline to get the cleaned data
df = run_pipeline()

# Then answer the 5 analysis questions:

# 1. How many total casualties in 2025?

# 2. Breakdown by casualty_severity?

# 3. Which day of week has most accidents?

# 4. What percentage of casualties were fatal?

# 5. Which age_band_of_casualty has highest casualties?