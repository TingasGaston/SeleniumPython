from selenium import webdriver
import locale
import csv

# fileLocation = "C:\AFAR 2018\Informes\00-PFecha.csv"
# workbook = xlrd.open_workbook(fileLocation)

# hoja1 = workbook.sheet_by_index(0)
# workbook.nsheets


# with open('C:\AFAR 2018\Informes\00-PFecha.csv', newline='') as csvfile:
# 	proxFecha = csv.reader(csvfile)
# 	print(proxFecha)



def guess_encoding(csv_file):
    """guess the encoding of the given file"""
    import io
    import locale
    with io.open(csv_file, "rb") as f:
        data = f.read(5)
    if data.startswith(b"\xEF\xBB\xBF"):  # UTF-8 with a "BOM"
        return "utf-8-sig"
    elif data.startswith(b"\xFF\xFE") or data.startswith(b"\xFE\xFF"):
        return "utf-16"
    else:  # in Windows, guessing utf-8 doesn't work, so we have to try
        try:
            with io.open(csv_file, encoding="utf-8") as f:
                preview = f.read(222222)
                return "utf-8"
        except:
            return locale.getdefaultlocale()[1]


proxFecha_open = open('C:\AFAR 2018\Informes\00-PFecha.csv', encoding=guess_encoding('C:\AFAR2018\Informes\00-PFecha.csv'))
proxFecha_content = proxFecha_open.read()
