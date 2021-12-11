import pandas as pd

if __name__ == '__main__':
    '''
    pandas是一个科学计算的包，但是我们可以借助于它对表格数据的读写
    在使用前使用pip install pandas xlwt xlrd
    read_excel读取表格pd.read_excel('example.xlsx', sheet_name='Sheet1')
    read_csv读取csv pd.read_excel('example.csv')
    读取的是pd的专属的dataframe格式，转为字典list需要调用to_dict(orient='records')
    '''
    dataframe = pd.read_excel('pandas_output.xlsx',sheet_name='Test01')
    items = dataframe.to_dict(orient='records')
    print(items)