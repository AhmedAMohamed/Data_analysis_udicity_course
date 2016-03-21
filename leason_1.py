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
def findUniqueStudentList(list):
    unique = set()
    for i in list:
        unique.add(i['account_key'])
    return unique
def filterEngagementData(all):
    for i in all:
        val = i['acct']
        i['account_key'] = val
        del i['acct']
    return all

all = readCsvFiles('C://Users//AhmedA//Desktop//Data//enrollments.csv')
en_all = readCsvFiles('C://Users//AhmedA//Desktop//Data//daily_engagement.csv')
en_all = filterEngagementData(en_all)
unique_enroll = findUniqueStudentList(all)

unique_eng = findUniqueStudentList(en_all)
print(len(all),"   ", len(unique_enroll))

sur = set()
for i in all:
    student = i['account_key']
    if student not in unique_eng :
        sur.add(student)

print(len(sur))