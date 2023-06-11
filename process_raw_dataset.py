from book.Chapter2.CreateDataset import CreateDataset
from pathlib import Path
import pandas as pd
import os

DATASET_PATH = Path("raw_datasets/tara_raw/")
RESULT_PATH = Path("./datasets/")
RESULT_FILENAME = "tara.csv"
GRANULARITY = 1000

notebook_path = os.path.realpath("tara")

# We can call Path.mkdir(exist_ok=True) to make any required directories if they don"t already exist.
[path.mkdir(exist_ok=True, parents=True)
 for path in [DATASET_PATH, RESULT_PATH]]

print("Please wait, this will take a while to run!")

dataset: CreateDataset = CreateDataset(DATASET_PATH, GRANULARITY)

dataset.add_numerical_dataset(
    "Accelerometer.csv",
    "time",
    ["z", "y", "x"],
    "avg",
    "accel_"
)

dataset.add_numerical_dataset(
    "Gyroscope.csv",
    "time",
    ["z", "y", "x"],
    "avg",
    "gyro_"
)

dataset.add_numerical_dataset(
    "Gravity.csv",
    "time",
    ["z", "y", "x"],
    "avg",
    "gravity_"
)

dataset.add_numerical_dataset(
    "Orientation.csv",
    "time",
    ["qz", "qy", "qx", "qw"],
    "avg",
    "ori_"
)

dataset.add_numerical_dataset(
    "Magnetometer.csv",
    "time",
    ["z", "y", "x"],
    "avg",
    "magne_"
)

dataset.add_numerical_dataset(
    "Barometer.csv",
    "time",
    ["relativeAltitude", "pressure"],
    "avg",
    "bar_"
)

dataset.add_numerical_dataset(
    "Location.csv",
    "time",
    ["altitude", "latitude", "longitude"],
    "avg",
    "gps_"
)


dataset.add_event_dataset_with_start_timestamp(
    "Annotation.csv", "time", "seconds_elapsed", "text", "binary"
)

dataset = dataset.data_table
target_dataset_path = f"{RESULT_PATH}/{RESULT_FILENAME}"
print(f"Writing processed dataset to {target_dataset_path}")
dataset.to_csv(target_dataset_path)
