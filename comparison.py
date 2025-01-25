import pandas as pd

#Function for comparison of actual and predicted data
def save_comparison_data(data, forecast, output_path):
    data['year'] = data['ts'].dt.year
    data['month'] = data['ts'].dt.month
    filtered_2024 = data[(data['year'] == 2024) & (data['month'] != 12)]
    actual_2024 = filtered_2024.groupby('month')['minutes_played'].sum()
    forecast_2025 = forecast[forecast['ds'].dt.year == 2025]
    predicted_2025 = forecast_2025.groupby(forecast_2025['ds'].dt.month)['yhat'].sum()
    comparison_df = pd.DataFrame({
        'Month': range(1, 12),
        'Actual_2024': actual_2024.values,
        'Predicted_2025': predicted_2025.values[:11]
    })
    comparison_df.to_csv(output_path, index=False)
    return comparison_df
