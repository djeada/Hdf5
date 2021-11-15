import numpy as np
import h5py
from pathlib import Path

PATH_1 = "example_without_compression.h5"
PATH_2 = "example_with_compression.h5"
NUM_DATASETS = 3
NUM_ROWS = 1000
NUM_COLS = 1000


def random_data() -> list:
    '''
    Generates random data. 
    Returns a list of numpy arrays.
    '''
    return [np.random.random(size=(NUM_ROWS, NUM_COLS)) for i in range(NUM_DATASETS)]


def save_data(file_path: str, data: list, with_compression: bool = False) -> None:
    '''
    Saves provided data to hdf5 file. Data is stored in groups.
    File is created if it does not exist.
    File is overwritten if it exists.
    File path is relative to the current working directory.
    '''
    with h5py.File(file_path, "w") as hdf:
        for i, matrix in enumerate(data):
            kwargs = (
                {"data": matrix, "compression": "gzip", "compression_opts": 9}
                if with_compression
                else {"data": matrix}
            )
            hdf.create_dataset(f"dataset {i}", **kwargs)


def main():
    '''
    Main function.
    '''
    data = random_data()
    save_data(PATH_1, data)
    save_data(PATH_2, data, True)
    uncompressed_file_size = Path(PATH_1).stat().st_size
    compressed_file_size = Path(PATH_2).stat().st_size
    print(f"uncompressed file size: {uncompressed_file_size}")
    print(f"compressed file size: {compressed_file_size}")
    print(
        f"The compressed file size is smaller than the uncompressed file size: {compressed_file_size < uncompressed_file_size}"
    )


if __name__ == "__main__":
    main()
