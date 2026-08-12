# UK Road Safety ETL Pipeline

A Python ETL pipeline that processes UK road safety data from the 
Department for Transport, combining collision and casualty records 
to produce a cleaned dataset with key safety insights.

## What it does

- Extracts collision and casualty data from DfT CSV files (2025)
- Merges datasets on collision index
- Cleans and transforms severity and day of week codes into 
  readable labels
- Loads cleaned data to Parquet format
- Outputs a summary including fatal casualties, most dangerous 
  day of the week, and average casualties per collision

## Key findings (2025 data)

- Most dangerous day of the week: Friday
- Fatal casualties: 1538
- Average casualties per collision: 1.26

## Tech stack

- Python
- Pandas

## Project structure

├── roadsafety_etl_pipeline.py # ETL pipeline

├── analysis.py # Additional analysis

├── exploration.ipynb # Data exploration notebook

└── README.md

## Data source

Department for Transport — Road Safety Data
https://www.gov.uk/government/statistical-data-sets/road-safety-open-data

## How to run

pip install pandas pyarrow
python roadsafety_etl_pipeline.py

## Notes

CSV data files are not included in this repository due to file size.
Download directly from the data source link above.
