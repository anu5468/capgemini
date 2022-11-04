import xlrd
from library.config import Config

class ReadExcel:

    def read_testdata(self, sheetname):
        #f_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\testdata\pp.xlsx"
        wb = xlrd.open_workbook(Config.TESTDATA_PATH)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()
        header = next(rows)
        data = []

        for row in rows:
            values = ()
            for j in range(columns):
                values += (rows[j].value,)
            data.append(values)
        return data

    def read_locators(self, sheetname):
        #f_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\testdata\uu1.xlsx"
        wb = xlrd.open_workbook(Config.LOCATORS_PATH)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()  # generate object
        header = next(rows)
        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)
        return d