import numpy as np
import h5py

PATH = "example_io.h5"
NUM_DATASETS = 3
NUM_ROWS = 100
NUM_COLS = 10


def random_data():
    return [np.random.random(size=(NUM_ROWS, NUM_COLS)) for i in range(NUM_DATASETS)]


def save_data(path, data):
    with h5py.File(path, "w") as hdf:
        for i, matrix in enumerate(data):
            hdf.create_dataset(f"dataset {i}", data=matrix)


def read_data(path, n=3):
    with h5py.File(path, "r") as hdf:
        dataset_list = list(hdf.keys())
        print("List of datasets in this file: \n", dataset_list)

        for key in dataset_list:
            print("")
            data = hdf.get(key)
            dataset = np.array(data)
            print(f"Shape of {key} : {dataset.shape}".format())
            print(f"Contents of {n} first rows of the dataset:")
            print(dataset[:n, :])


def main():
    data = random_data()
    save_data(PATH, data)
    read_data(PATH)


if __name__ == "__main__":
    main()
