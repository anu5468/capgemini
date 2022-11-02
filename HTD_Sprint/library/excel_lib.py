import xlrd
from selenium import webdriver
from library.config import Config


class ReadExcel:

    def read_testdata(self, sheetname):
        wb = xlrd.open_workbook(Config.TESTDATA_PATH)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()
        header = next(rows)
        data = []

        for row in rows:
            data.append((row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value,
                         row[6].value))

        return data

    def read_locators(self, sheetname):
        wb = xlrd.open_workbook(Config.TESTDATA_PATH)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()  # generate object
        header = next(rows)
        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)
        return d


# n = ReadExcel()
# data1 = n.read_testdata("testcase1_data")
# print(data1)
