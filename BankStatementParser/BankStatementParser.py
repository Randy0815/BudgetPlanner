import csv

CSVLineOffset = 14

class BankStatementParser:

    def extract_items_from_known_list(self, csvlist=''):
        lines = list()
        with open(csvlist, newline='') as KnownList:
            items = csv.reader(KnownList, delimiter=';', quotechar='|')
            for List in items:
                lines.append(List)
        return lines

    def extract_items_from_bankstatement_list(self, csvlist=''):
        lines = list()
        with open(csvlist, newline='') as KnownList:
            items = csv.reader(KnownList, delimiter=';', quotechar='|')
            for List in items:
                if items.line_num > CSVLineOffset:
                    lines.append(List)
        return lines


    def parse_list(self, parameter_list, ParsedCSV, row, i):
        '''

        :param parameter_list:
        :type parameter_list:
        :param ParsedCSV:
        :type ParsedCSV:
        :param row:
        :type row:
        :param i:
        :type i:
        :return:
        :rtype:
        '''
        bHandled = False
        for item in parameter_list:
            if item in row[2]:
                if 'VISA' in row[2]:
                    row[2].replace('VISA','')
                    ParsedCSV.write(row[0] + i * ';'*3 + ';' + str(item).capitalize() + ';' + str(row[5]).replace('-','') + ';V' + "\n")
                else:
                    ParsedCSV.write(row[0] + i * ';'*3 + ';' + str(item).capitalize() + ';' + str(row[5]).replace('-','') + ';LV'+ "\n")
                bHandled = True
        return bHandled