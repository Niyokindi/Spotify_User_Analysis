from data_processing import load_and_preprocess_data, aggregate_monthly_listening_time
from forecasting import forecast_listening_time
from visualization import plot_forecast, compare_actual_and_predicted
from comparison import save_comparison_data
from evaluation import evaluate_model

def main():
    file_path = "Spotify+Streaming+History/spotify_history.csv"
    output_path = "listening_minutes_comparison_2024_2025_no_december.csv"

    spotify_data = load_and_preprocess_data(file_path)


    monthly_listening_time = aggregate_monthly_listening_time(spotify_data)

    
    forecast, prophet = forecast_listening_time(monthly_listening_time)

    
    plot_forecast(prophet, forecast)

  
    compare_actual_and_predicted(spotify_data, forecast)


    comparison_df = save_comparison_data(spotify_data, forecast, output_path)
    print(comparison_df)

    evaluate_model(spotify_data, forecast, output_path="evaluation_results.csv")

if __name__ == "__main__":
    main()
