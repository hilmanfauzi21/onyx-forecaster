import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from datetime import timedelta

class OnyxForecaster:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.is_trained = False

    def _prepare_features(self, df):
        \"\"\"
        Feature engineering: Extract time-based features from the date.
        \"\"\"
        df['date'] = pd.to_datetime(df['date'])
        df['day_of_week'] = df['date'].dt.dayofweek
        df['month'] = df['date'].dt.month
        df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
        return df

    def train(self, historical_data):
        \"\"\"
        historical_data: List of dicts with 'date' and 'sales' keys
        \"\"\"
        df = pd.DataFrame(historical_data)
        df = self._prepare_features(df)
        
        X = df[['day_of_week', 'month', 'is_weekend']]
        y = df['sales']
        
        self.model.fit(X, y)
        self.is_trained = True
        self.last_date = df['date'].max()

    def forecast(self, days=7):
        if not self.is_trained:
            raise Exception(\"Model must be trained before forecasting.\")
        
        forecast_dates = [self.last_date + timedelta(days=x) for x in range(1, days + 1)]
        forecast_df = pd.DataFrame({'date': forecast_dates})
        forecast_df = self._prepare_features(forecast_df)
        
        X_forecast = forecast_df[['day_of_week', 'month', 'is_weekend']]
        predictions = self.model.predict(X_forecast)
        
        result = []
        for date, pred in zip(forecast_dates, predictions):
            result.append({
                \"date\": date.strftime(\"%Y-%m-%d\"),
                \"predicted_sales\": round(float(pred), 2)
            })
        return result