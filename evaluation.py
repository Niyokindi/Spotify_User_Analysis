
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

#Functions for evaluating the model

def evaluate_model(spotify_data, forecast, output_path="evaluation_results.csv"):
    # Filter forecast for 2024 and actuals for 2024
    forecast_2024 = forecast[forecast['ds'].dt.year == 2024]
    actual_2024 = spotify_data[spotify_data['year'] == 2024].groupby('month')['minutes_played'].sum()

    # Ensure alignment of actuals and predictions
    evaluation_df = pd.DataFrame({
        'Month': actual_2024.index,
        'Actual_2024': actual_2024.values,
        'Predicted_2024': forecast_2024.groupby(forecast_2024['ds'].dt.month)['yhat'].sum().values
    })

    # Calculate residuals
    evaluation_df['Residuals'] = evaluation_df['Actual_2024'] - evaluation_df['Predicted_2024']

    # Compute evaluation metrics
    mae = mean_absolute_error(evaluation_df['Actual_2024'], evaluation_df['Predicted_2024'])
    rmse = np.sqrt(mean_squared_error(evaluation_df['Actual_2024'], evaluation_df['Predicted_2024']))
    mape = np.mean(np.abs((evaluation_df['Actual_2024'] - evaluation_df['Predicted_2024']) / evaluation_df['Actual_2024'])) * 100

    # Print metrics
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Root Mean Square Error (RMSE): {rmse:.2f}")
    print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")

    # Save evaluation results to a CSV file
    evaluation_df.to_csv(output_path, index=False)
    print(f"Evaluation results saved to {output_path}")

    # Plot residuals
    plt.figure(figsize=(10, 6))
    plt.bar(evaluation_df['Month'], evaluation_df['Residuals'], color='skyblue', edgecolor='black')
    plt.axhline(0, linestyle='--', color='black')
    plt.title("Residuals (Actual - Predicted) for 2024")
    plt.xlabel("Month")
    plt.ylabel("Residuals")
    plt.grid(True)
    plt.show()

   
