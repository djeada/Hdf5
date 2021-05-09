# HDF5
Examples of code for processing  HDF5 files.

<h1>About HDF5 </h1>

* Stands for "Hierarichal Data Format".
* Current version is 5.
* It is a file format for storing data that is highly extensible and flexible.
* Open-source and free.
* Core accesible from C, C++ and java. There are wrappers for many other languages including Python.

<h1>Structure </h1>
* Groups (like directories)
* Datasets (like files)
  * Shape (ex. 1D, 2D, 5D)
  * Datatype (ex. float, int32)

<h1>Linear vs Chunked </h1>
This concept diffrentiaties HDF5 from other data formats.
Chunked: faster reading.

Chunk size must strike a balance:
* maximizing i/o speed.
* minimizing non-used data i/o.
* minimizing chunking i/o overhead cost.

<h1>Filter</h1>
Transparently act on datasets.
Layer between program and data.
Program <- Filter (CPU) <- data (Disk).

Examples:
* Gzip (compression filter)
* ScaleOffset (stores data subtracted by median, then while reading median is added back)
