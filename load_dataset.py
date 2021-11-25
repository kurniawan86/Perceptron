import pandas as pd

class loadDataset:
    __file = ''
    __df = pd.DataFrame
    X = []
    y = []

    def __init__(self, file):
        self.__file = r'{}'.format(file)
        self.fromExcel()

    def fromExcel(self):
        df = pd.read_excel(self.__file)
        df = pd.DataFrame(df, columns=(['x', 'y', 'target']))
        self.__df = df

    def getData(self):
        return self.__df[['x','y']].values.tolist()

    def getTarget(self):
        return self.__df['target'].values.tolist()