import numpy as np
import h5py

PATH = "example_attributes.h5"
NUM_DATASETS = 3
NUM_ROWS = 100
NUM_COLS = 10


def random_data() -> list:
    """
    Generates random data. 
    Returns a list of numpy arrays.
    """
    return [np.random.random(size=(NUM_ROWS, NUM_COLS)) for i in range(NUM_DATASETS)]


def save_data(file_path: str, data: list) -> None:
    """
    Saves provided data to hdf5 file. Data is stored in groups.
    File is created if it does not exist.
    File is overwritten if it exists.
    File path is relative to the current working directory.
    """
    with h5py.File(file_path, "w") as hdf:
        for i, matrix in enumerate(data):
            dataset = hdf.create_dataset(f"dataset {i}", data=matrix)
            dataset.attrs["CLASS"] = "DATA MATRIX"
            dataset.attrs["VERSION"] = "0.1"


def read_data(path: str, n: int = 3) -> list:
    """
    Reads data from hdf5 file and prints it to standard output.
    """
    with h5py.File(path, "r") as hdf:
        dataset_list = list(hdf.keys())
        print(f"List of datasets in this file: \n {dataset_list}")

        for key in dataset_list:
            print("")
            dataset = hdf.get(key)
            print(f"Shape of {key} : {dataset.shape}")
            print(f"Attributes : {list(dataset.attrs)}")
            print(f"Contents of {n} first rows of the dataset:")
            print(dataset[:n, :])


def main():
    """
    Main function.
    """
    data = random_data()
    save_data(PATH, data)
    read_data(PATH)


if __name__ == "__main__":
    main()
