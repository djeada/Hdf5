import numpy as np
import h5py

PATH = "example_groups.h5"
NUM_DATASETS = 3
NUM_ROWS = 100
NUM_COLS = 10


def random_data():
    return [np.random.random(size=(NUM_ROWS, NUM_COLS)) for i in range(NUM_DATASETS)]


def save_data(_path, data):
    with h5py.File(_path, "w") as hdf:
        group = hdf.create_group("Group1")

        subgroups = [
            group.create_group(name)
            for name in ["Group1/SubGroup1", "Group1/SubGroup2"]
        ]

        for subgroup in subgroups:
            for i, matrix in enumerate(data):
                subgroup.create_dataset(f"dataset {i}", data=matrix)


def read_data(path):
    with h5py.File(path, "r") as hdf:
        base_items = list(hdf.items())
        print(f"Items in the base directory: {base_items}")

        dataset_list = list(hdf.keys())
        print(f"List of datasets in this file: \n {dataset_list}")

        for key in dataset_list:
            for item in hdf.get(key).items():
                print(list(item[1].keys()))


def main():
    data = random_data()
    save_data(PATH, data)
    read_data(PATH)


if __name__ == "__main__":
    main()
