import numpy as np
import h5py
import random

path = 'example_hdf5.h5'

def random_data():
	return [np.random.random(size = (random.randint(1,1000), random.randint(1,1000))) for i in range(3)]

def save_data(_path, data):
	with h5py.File(_path, 'w') as hdf:
		G1 = hdf.create_group('Group1')
		
		subgroups = [G1.create_group(name) for name in ['Group1/SubGroup1', 'Group1/SubGroup2']]

		for subgroup in subgroups:
			for matrix in data:
				subgroup.create_dataset('dataset {}'.format(data.index(matrix) + 1), data=matrix)

def read_data(_path):
	with h5py.File(_path,'r') as hdf:
		base_items = list(hdf.items())
		print('Items in the base directory:', base_items)
		ls = list(hdf.keys())
		print('List of datasets in this file: \n', ls)

		for key in ls:
			for item in hdf.get(key).items():
				print(item[1].keys())

def main():
	data = random_data()
	save_data(path, data)
	read_data(path)

if __name__ == "__main__":
	main()
