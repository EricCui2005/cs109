import numpy as np
import csv

def example_csv_reader():
    print('CSV reading example:\n')
    # Create a reader
    reader = csv.DictReader(open('toy-csv.csv'))
    for row in reader:
        # get each row as a dictionary
        print(row) 

        # keys are the column names
        print('Name:', row['Player_Name']) 

        # all values are initially strings
        has_ability = row['Has_Special_Ability'] == 'True' 
        print('Special Ability:', has_ability)
        print('')


def example_matrix_reader():
    print('Matrix reading example:\n')

    # Read in the data
    data = np.genfromtxt(
        'toy-matrix.csv', # filename
        delimiter=',', # csv cells are demarcated with commas
        names=None, # There is no header information in the first row
        dtype=np.float32 # This informs how all data should be interpreted
    )

   
    print(f'Data:\n{data}') # this is a normal numpy array of floats
    print(f'Data shape:\n{data.shape}')
    print(f'Data type(s):\n{data.dtype}')
    print(f'Summing of the matrix:\n{data.sum()}')
    print(f'Indexing row 0 column 1:\n{data[0,1]}') # first index is row, second index is column
    print(f'Summing over column 2:\n{data[:,2].sum()}')
    print(f'Which rows are less than 0.6 in the first column?\n{data[:,0] < 0.6}')

def main():
    example_csv_reader()
    print('\n\n')
    example_matrix_reader()
    
    

if __name__ == '__main__':
    main()
