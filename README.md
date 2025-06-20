# Weather Forecasting LSTM

This repository demonstrates a simple approach to forecasting the next day's temperature using a Long Short Term Memory (LSTM) network. The dataset contains the last ten years of daily weather data for Istanbul collected via the Meteostat API. Jupyter notebooks are provided for data exploration and model training.

## Project Structure

- `data/`
  - `get_data.py` &ndash; Download 10 years of daily weather data for Istanbul using [Meteostat](https://open-meteo.com/).
  - `istanbul_weather_last_10_years.csv` &ndash; Raw data fetched from the API.
  - `cleaned_weather_data.csv` &ndash; Preprocessed dataset used for model training.
- `models/`
  - `final_model.h5` &ndash; Trained LSTM model.
  - `scaler.save` &ndash; Corresponding `MinMaxScaler` used during training.
- `notebooks/`
  - `01_data_exploration.ipynb` &ndash; Data cleaning and exploratory analysis.
  - `02_model_experiments.ipynb` &ndash; Training experiments with an LSTM network.

## Setup

1. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   pip install pandas numpy matplotlib seaborn tensorflow joblib
   ```

2. **Fetch the dataset**

   ```bash
   python data/get_data.py
   ```

   This script downloads the latest ten years of weather observations and saves them to `data/istanbul_weather_last_10_years.csv`.

3. **Run the notebooks**

   Use Jupyter or an equivalent environment to execute the notebooks in the `notebooks/` directory. `01_data_exploration.ipynb` walks through data cleaning to produce `cleaned_weather_data.csv`, while `02_model_experiments.ipynb` trains the forecasting model and saves the results to the `models/` directory.

## Using the Trained Model

The `models/` directory contains a saved Keras model and its scaler. A short example to load the model and make a prediction:

```python
import joblib
import pandas as pd
import tensorflow as tf

# Load scaler and model
scaler = joblib.load('models/scaler.save')
model = tf.keras.models.load_model('models/final_model.h5')

# Prepare a sample of past observations (same features as the training data)
# `data` should be a DataFrame with columns ['avg_temp', 'min_temp', 'max_temp', 'wind_speed']
scaled = scaler.transform(data)
prediction = model.predict(scaled)
print('Next day temperature:', prediction.ravel()[0])
```

## License

This project is licensed under the [MIT License](LICENSE).
