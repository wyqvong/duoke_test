import pandas as pd

def read_csv_file(file_path):
    path = file_path
    data = pd.read_csv(path, skiprows=1, encoding='gb18030')
    for i in data:
        print(i)

if __name__ == '__main__':
    read_csv_file("testdata/test_sku.csv")