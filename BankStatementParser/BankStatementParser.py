import csv
import datetime

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
                    #print(List[1])
                    List[0] = datetime.datetime.strptime(List[0], "%d.%m.%Y").date().isoformat()
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
                self.write_bank_statement(ParsedCSV, i, item, row)
                bHandled = True
        return bHandled

    def write_bank_statement(self, ParsedCSV, i, item, row):
        if 'VISA' in item:
            item.replace('VISA', '')
            ParsedCSV.write(
                row[0] + i * ';' * 3 + ';' + str(item).capitalize() + ';' + str(row[5]).replace('-', '') + ';V' + "\n")
        else:
            ParsedCSV.write(
                row[0] + i * ';' * 3 + ';' + str(item).capitalize() + ';' + str(row[5]).replace('-', '') + ';LV' + "\n")