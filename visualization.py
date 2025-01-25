import matplotlib.pyplot as plt

def plot_forecast(prophet, forecast):
    fig = prophet.plot(forecast)
    plt.title("Forecast of Total Listening Time (Minutes)")
    plt.xlabel("Date")
    plt.ylabel("Minutes Played")
    plt.show()

def compare_actual_and_predicted(data, forecast):
    data['year'] = data['ts'].dt.year
    data['month'] = data['ts'].dt.month
    actual_2024 = data[data['year'] == 2024].groupby('month')['minutes_played'].sum()
    forecast_2025 = forecast[forecast['ds'].dt.year == 2025]
    predicted_2025 = forecast_2025.groupby(forecast_2025['ds'].dt.month)['yhat'].sum()

    # Plot the comparison
    plt.figure(figsize=(12, 6))
    plt.plot(actual_2024.index, actual_2024.values, marker='o', label='2024 (Actual)', color='blue')
    plt.plot(predicted_2025.index, predicted_2025.values, marker='o', label='2025 (Predicted)', color='orange')
    plt.title('Comparison of Listening Time: 2024 (Actual) vs 2025 (Predicted)')
    plt.xlabel('Month')
    plt.ylabel('Total Minutes')
    plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.legend(title='Year')
    plt.grid(True)
    plt.show()
