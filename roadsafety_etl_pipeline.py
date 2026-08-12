import pandas as pd

def extract(collisions_path, casualties_path):
    collisions_df = pd.read_csv(collisions_path)
    casualties_df = pd.read_csv(casualties_path)
    return collisions_df, casualties_df

def transform(collisions_df, casualties_df):
    df = pd.merge(collisions_df, casualties_df, how="inner", on="collision_index")
    df = df.dropna(subset=['casualty_severity'])
    severity_map = {1: "Fatal", 2: "Serious", 3: "Slight"}
    df['casualty_severity'] = df['casualty_severity'].map(severity_map)
    day_map = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
    df['day_of_week'] = df['day_of_week'].map(day_map)
    return df

def load(df, filepath="collision_casualties_2025.parquet"):
        df.to_parquet(filepath, index=False)
        df =  pd.read_parquet(filepath)
        print(f'Saved to {filepath}, here\'s a summary:')
        print(f'Total rows processed: {len(df)}')
        fatal_count = int((df['casualty_severity'] == "Fatal").sum())
        print(f'Fatal casualties: {fatal_count}')
        dangerous_day = df.drop_duplicates(subset='collision_index')['day_of_week'].value_counts().idxmax()
        print(f'Most dangerous day of the week: {dangerous_day}')
        distinct_accidents = df['collision_index'].nunique()
        avg_casualties = len(df) / distinct_accidents
        print(f'Average casualties per accident: {avg_casualties}')
        return df

def run_pipeline():
    collisions_df, casualties_df = extract("dft-road-casualty-statistics-collision-2025.csv", "dft-road-casualty-statistics-casualty-2025.csv")
    clean_df = transform(collisions_df, casualties_df)
    df = load(clean_df)
    return df

if __name__ == "__main__":
    run_pipeline()