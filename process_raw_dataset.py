from book.Chapter2.CreateDataset import CreateDataset
from pathlib import Path
import pandas as pd
import os

DATASET_PATH = Path("raw_datasets/tara_raw/")
RESULT_PATH = Path("./datasets/")
RESULT_FILENAME = "tara.csv"
GRANULARITY = 601000

notebook_path = os.path.realpath("tara")

# We can call Path.mkdir(exist_ok=True) to make any required directories if they don"t already exist.
[path.mkdir(exist_ok=True, parents=True)
 for path in [DATASET_PATH, RESULT_PATH]]

print("Please wait, this will take a while to run!")

create_dataset_object: CreateDataset = CreateDataset(DATASET_PATH, GRANULARITY)

create_dataset_object.add_numerical_dataset(
    "Accelerometer.csv",
    "time",
    ["z", "y", "x"],
    "avg",
    "accel_"
)

create_dataset_object.add_numerical_dataset(
    "Gyroscope.csv",
    "time",
    ["z", "y", "x"],
    "avg",
    "gyro_"
)

create_dataset_object.add_numerical_dataset(
    "Gravity.csv",
    "time",
    ["z", "y", "x"],
    "avg",
    "gravity_"
)

create_dataset_object.add_numerical_dataset(
    "Orientation.csv",
    "time",
    ["qz", "qy", "qx", "qw"],
    "avg",
    "ori_"
)

create_dataset_object.add_numerical_dataset(
    "Magnetometer.csv",
    "time",
    ["z", "y", "x"],
    "avg",
    "magne_"
)

create_dataset_object.add_numerical_dataset(
    "Barometer.csv",
    "time",
    ["relativeAltitude", "pressure"],
    "avg",
    "bar_"
)

create_dataset_object.add_numerical_dataset(
    "Location.csv",
    "time",
    ["altitude", "latitude", "longitude"],
    "avg",
    "gps_"
)


create_dataset_object.add_event_dataset_with_start_timestamp(
    "Annotation.csv", "time", "seconds_elapsed", "text", "binary"
)

dataset: pd.DataFrame = create_dataset_object.data_table
target_dataset_path = f"{RESULT_PATH}/{RESULT_FILENAME}"
print(f"Writing processed dataset to {target_dataset_path}")
dataset.to_csv(target_dataset_path)
