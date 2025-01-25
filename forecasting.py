from prophet import Prophet

# Functions for forecasting using Prophet
def forecast_listening_time(monthly_data, periods=12, freq='M'):
    prophet = Prophet(changepoint_prior_scale=0.5, seasonality_prior_scale=10)
    prophet.fit(monthly_data)
    future = prophet.make_future_dataframe(periods=periods, freq=freq)
    forecast = prophet.predict(future)
    return forecast, prophet
