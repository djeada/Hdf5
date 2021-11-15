# HDF5
Code examples for processing HDF5 files.

<h1>About HDF5 </h1>
HDF5 is a file format for storing data that is highly extensible and flexible.
For example, you can store a large number of images in a single HDF5 file.

* Stands for "Hierarichal Data Format".
* Current version is 5.
* It is a file format for storing data that is highly extensible and flexible.
* Open-source and free.
* Core accesible from C, C++ and java. There are wrappers for many other languages including Python.

<h1>Using HDF5 </h1>
To use HDF5, you need to install the h5py module.
Then you can use it to read and write HDF5 files.
For example, to read a file called "myfile.h5"

```Python
  import h5py
  f = h5py.File('myfile.h5', 'r')
  print(f.keys())
  print(f['data'].shape)
  print(f['data'][:])
  f.close()
```

To save a file, you need to create a new file object.
For example, to create a new file called "myfile.h5"

```Python
    import h5py
    f = h5py.File('myfile.h5', 'w')
    data_set = f.create_dataset('data', (100,), dtype='i')
    data_set[:] = np.arange(100)
    f.close()
```

<h1>Structure </h1>

* Groups (a concept similar to directories)
  - Groups can contain datasets and other groups.
  
* Datasets (a concept similar to files)
  - Shape (ex. 1D, 2D, 5D)
  - Datatype (ex. float, int32)
  - Attributes (ex. compression, chunking, compression)
  - Data (ex. data[:])
  - Subdatasets (ex. subdataset[:])

<h1>Linear vs Chunked </h1>
This concept diffrentiaties HDF5 from other data formats. 
Chunked datasets are stored in a more compact way.
It allows for faster access to data.

Linear:
  - Data is stored in a single file.
  - Data is stored in a single chunk.
  - Data is stored in a single block.

Chunked:
  - Data is stored in multiple chunks.
  - Data is stored in multiple blocks.
  - Data is stored in multiple files.

Chunk size must strike a balance:
 - maximizing i/o speed.
 - minimizing non-used data i/o.
 - minimizing chunking i/o overhead cost.

<h1>Filter</h1>
Filter is a way to compress data.
  - Can be applied to datasets.
  - It is a layer betwen program and data.

Program <- Filter (CPU) <- data (Disk).

Examples:
* Gzip (compression filter)
* ScaleOffset (stores data subtracted by median, then while reading median is added back)
* Szip (compression filter)
* Shuffle (shuffles data)
* Fletcher32 (checksum)

<h1>Code Samples</h1>

* <a href="https://github.com/djeada/Hdf5/blob/main/src/basic_io.py">Basic IO</a>
* <a href="https://github.com/djeada/Hdf5/blob/main/src/groups.py">Groups</a>
* <a href="https://github.com/djeada/Hdf5/blob/main/src/compression.py">Compression</a>
* <a href="https://github.com/djeada/Hdf5/blob/main/src/attributes.py">Attributes</a>
