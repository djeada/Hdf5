import numpy as np
import h5py

class CustomClass:
    '''
    An artificial custom class used to present
    the serialization and deserialization with hdf5.
    '''

    def __init__(self, name: str, number: int, data: np.ndarray, nested_dict: dict):
        self.name = name
        self.number = number
        self.data = data
        self.nested_dict = nested_dict
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return f"Name: {self.name}, \nNumber: {self.number}, \nData: {self.data}, \nNested dict: {self.nested_dict}"

    def __eq__(self, other: 'CustomClass'):
        return self.name == other.name and self.number == other.number and \
               (self.data == other.data).all() and self.nested_dict == other.nested_dict

    def __ne__(self, other: 'CustomClass'):
        return not self.__eq__(other)

    def save_to_hdf5(self, file_path: str) -> None:
        '''
        Save the current instance to an hdf5 file.
        '''
        print(f"Saving {self.name} to {file_path}")
        with h5py.File(file_path, 'w') as f:
            f.create_dataset('name', 1, dtype=h5py.special_dtype(vlen=str))
            f['name'][:] = self.name
            f.create_dataset('number', 1, dtype=int)
            f['number'][:] = self.number
            f.create_dataset('data', data=self.data)
            # for nested dict use group
            f.create_group('nested_dict')
            for key, value in self.nested_dict.items():
                if isinstance(value, dict):
                    f.create_group(f'nested_dict/{key}')
                    for key2, value2 in value.items():
                        f.create_dataset(f'nested_dict/{key}/{key2}', 1,  dtype=h5py.special_dtype(vlen=str))
                        f[f'nested_dict/{key}/{key2}'][:] = value2
                else:
                    f.create_dataset(f'nested_dict/{key}', 1, dtype=h5py.special_dtype(vlen=str))
                    f[f'nested_dict/{key}'][:] = value

            
    @classmethod
    def load_from_hdf5(cls, file_path: str) -> 'CustomClass':
        '''
        Load an instance from an hdf5 file.
        '''
        with h5py.File(file_path, 'r') as f:
            name = f['name'].asstr()[0]
            number = int(f['number'][0])
            data = np.array(f['data'])
            nested_dict = {}
            for key, value in f['nested_dict'].items():
                if isinstance(value, h5py.Group):
                    nested_dict[int(key)] = {}
                    for key2, value2 in value.items():
                        nested_dict[int(key)][key2] = value2.asstr()[0]
                else:
                    nested_dict[int(key)] = value.asstr()[0]
            
        print(f"Loading {name} from {file_path}")
        return cls(name, number, data, nested_dict)


def main():
    '''
    Main function.
    '''
    custom_obj = CustomClass('test',55, np.array([1, 2, 3]), {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}})  
    file_path = 'temp.h5'

    custom_obj.save_to_hdf5(file_path)
    new_obj = CustomClass.load_from_hdf5(file_path)

    print(f'Objects are identical: {custom_obj == new_obj}')

if __name__ == '__main__':
    main()
