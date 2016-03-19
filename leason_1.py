__author__ = 'AhmedA'


import unicodecsv as csvReader

def readCsvFiles (fileName):
    with open(fileName, 'rb') as f:
        reader = csvReader.DictReader(f)
        return list(reader)

def possible_int(field):
    if (field == ''):
        return None
    else:
        try:
            return int(field)
        except:
            return None

def possible_bool(field):
    if(field == 'true' or field == 'True'):
        return True
    return False
print (readCsvFiles('C://Users//AhmedA//Desktop//Data//daily_engagement.csv')[0])
#print(possible_int('1501'))