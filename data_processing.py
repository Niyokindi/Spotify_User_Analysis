import pandas as pd

# Function for loading and preprocessing data
def load_and_preprocess_data(file_path):
    spotify_data = pd.read_csv(file_path)
    spotify_data['ts'] = pd.to_datetime(spotify_data['ts'], errors='coerce')
    spotify_data['year_month'] = spotify_data['ts'].dt.to_period('M')
    spotify_data['minutes_played'] = spotify_data['ms_played'] / 60000
    return spotify_data

# Function for aggregating and preparing data

def aggregate_monthly_listening_time(data):
    monthly_data = data.groupby('year_month')['minutes_played'].sum().reset_index()
    monthly_data.columns = ['ds', 'y']
    monthly_data['ds'] = monthly_data['ds'].dt.to_timestamp()
    return monthly_data
