__author__ = 'pretymoon'
import sys
import xlwt

def make_table():
    ff = open("\\projects\\justCapital\\RETURNS_1.xlsx","r")

    for case in range(11):
        strLine = ff.readline()
        print(strLine)

make_table()