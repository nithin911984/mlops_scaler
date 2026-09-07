import pandas as pd
import pytest

from pathlib import Path

<<<<<<< HEAD
# to automatically find the root directory of your project folder relative to the file running the code
ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = ROOT / "data" / "car_data.csv"
=======
ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = ROOT / "data" / "cars24-car-price-cleaned-new.csv"
>>>>>>> a15694a9f1680cfc41f3fa573beb8025217ce988
MODEL_PATH = ROOT / "models" / "xgb_car_price_model.pkl"

FEATURE_COLUMNS = ['km_driven', 'mileage', 'age', 'Petrol', 'Diesel', 'Electric']
TARGET_COLUMN = 'selling_price'


<<<<<<< HEAD
@pytest.fixture(scope="module") # pytest decorator
=======
@pytest.fixture(scope="module")
>>>>>>> a15694a9f1680cfc41f3fa573beb8025217ce988
def cars_df():
    return pd.read_csv(DATA_PATH)


def test_data_is_not_empty(cars_df):
    assert len(cars_df) > 0


def test_required_columns_exist(cars_df):
    for col in FEATURE_COLUMNS + [TARGET_COLUMN]:
        assert col in cars_df.columns


def test_no_missing_values_in_model_columns(cars_df):
    assert cars_df[FEATURE_COLUMNS + [TARGET_COLUMN]].isnull().sum().sum() == 0


def test_selling_price_is_positive(cars_df):
    assert (cars_df[TARGET_COLUMN] > 0).all()


def test_km_driven_is_non_negative(cars_df):
    assert (cars_df['km_driven'] >= 0).all()


def test_fuel_columns_are_binary(cars_df):
    for col in ['Petrol', 'Diesel', 'Electric']:
<<<<<<< HEAD
        assert cars_df[col].isin([0, 1]).all()
=======
        assert cars_df[col].isin([0, 1]).all()
>>>>>>> a15694a9f1680cfc41f3fa573beb8025217ce988
