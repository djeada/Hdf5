import numpy as np
import h5py
import random

path = 'example_hdf5.h5'

data = [ np.random.random(size = (random.randint(1,1000), random.randint(1,1000))) for i in range(3)]

with h5py.File(path, 'w') as hdf:
	for matrix in data:
		hdf.create_dataset('dataset {}'.format(data.index(matrix) + 1), data=matrix)

with h5py.File(path,'r') as hdf:
	ls = list(hdf.keys())
	print('List of datasets in this file: \n', ls)

	for key in ls:
		print('')
		data = hdf.get(key)
		print(data)
		dataset = np.array(data)
		print('Shape of {} : {}'.format(key, dataset.shape))
		print('Contents of the dataset')
		print(dataset)


