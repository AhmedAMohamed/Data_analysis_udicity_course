__author__ = 'AhmedA'


import unicodecsv as csvReader

def readCsvFiles (fileName):
    with open(fileName, 'rb') as f:
        reader = csvReader.DictReader(f)
        elements = list(reader)
        return elements

print (len(readCsvFiles('Data/enrollments.csv')))