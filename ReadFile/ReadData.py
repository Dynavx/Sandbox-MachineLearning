import pandas as pd

class loader():
    # Function untuk Load File CSV
    def loadcsv(self, csvdir):
        csv = pd.read_csv(csvdir)
        print(csv)
        
    # Function untuk Load File Excel
    def loadexcel(self, exceldir):
        excel = pd.read_excel(exceldir, sheet_name="TI-3A") # sheet_name digunakan untuk menentukan page/sheet apa yang ingin dibuka dalam sebuah file excel
        print(excel)  
          
if __name__ == '__main__':
    load = loader()
    load.loadcsv(csvdir = "grocery_data.csv")
    load.loadexcel(exceldir = "TI-3_Absen.xlsx")