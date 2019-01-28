import csv

class BankStatementParser:
    def extractitemsfromknownList(self, csvlist=''):
        lines = list()
        with open(csvlist, newline='') as KnownList:
            items = csv.reader(KnownList, delimiter=';', quotechar='|')
            for List in items:
                lines.append(List)
        return lines


    def parselist(self, parameter_list, ParsedCSV, row, i):
        bHandled = False
        for item in parameter_list:
            if item in row[2]:
                ParsedCSV.write(row[0] + i * ',' + ',' + item + ',' + row[5] + "\n")
                bHandled = True
        return bHandled