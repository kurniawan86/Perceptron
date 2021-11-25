# This is a sample Python script.
from load_dataset import loadDataset

if __name__ == '__main__':
    print("Hello World")
    load = loadDataset('dataset.xlsx')
    print(load.getTarget())