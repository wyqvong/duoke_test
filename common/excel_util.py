import pandas as pd

def read_excel(file_path):
    # 读取 Excel 文件
    df = pd.read_excel(file_path)
    records = df.to_dict(orient='records')
    for record in records:
        print(record)
    return records
 