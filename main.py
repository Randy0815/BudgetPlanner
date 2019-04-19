from BankStatementParser import BankStatementParser
import glob
from dateutil import parser

separator = ';'

def main():
    parser = BankStatementParser.BankStatementParser()

    #Get the known lists
    CategoryList = parser.extract_items_from_known_list('InputData/KnownLocations.csv')
    RegularCostsList = parser.extract_items_from_known_list('InputData/KnownRegularCosts.csv')
    namelist = parser.extract_items_from_known_list('InputData/Names.csv')

    tBankStatement = PrepareBankStatement(parser)

    # open('Parsed.csv', 'w').close()
    with open('Parsed.csv', 'w') as ParsedCSV, open('RegluarCosts.csv', 'w') as regularcostsCSV, open('Income.csv',
                                                                                                      'w') as IncomeCSV, open(
        'RegularSavings.csv', 'w') as RegularSavings, open('BarAuszahlung.csv', 'w') as barCSV:

        writeHeadings(ParsedCSV)

        WriteParsedDebits(CategoryList, IncomeCSV, ParsedCSV, RegularCostsList, RegularSavings, namelist, parser,
                          regularcostsCSV, tBankStatement, barCSV)


def WriteParsedDebits(CategoryList, IncomeCSV, ParsedCSV, RegularCostsList, RegularSavings, namelist, parser,
                      regularcostsCSV, tBankStatement, barCSV):
    print("Locations:" + str(CategoryList))

    for row in tBankStatement:
        bHandled = False
        if float(row[5].replace(",", ".")) > 0:
            #row[5] =
            IncomeCSV.write(row[0] + separator + row[2] + separator + row[5] + "\n")
            bHandled = True
        if "BARGELDAUSZAHLUNG" in row[4] or "Bargeldauszahlung" in row[4]:
            barCSV.write(row[0] + 7 * 3 * separator + separator+separator + row[2] + separator + row[5] + "\n")
            bHandled = True
        for x in range(0, len(CategoryList)):
            bHandled |= parser.parse_list(CategoryList[x], ParsedCSV, row, x)
        for item in RegularCostsList[0]:
            if item in row[2]:
                regularcostsCSV.write(row[0] + separator + separator + item + separator + str(row[5]).replace('-','') + "\n")
                bHandled = True
        if (bHandled == False):
            if (namelist[0][0] in row[2]) or (namelist[0][1] in row[2]):
                RegularSavings.write(row[0] + separator + separator + row[2] + separator + row[5] + "\n")
            else:
                if ("AMAZON" in row[2]):
                    row[2] = "AMAZON"
                ParsedCSV.write(row[0] + 3 * 5 * separator + separator + str(row[2]).capitalize() + separator + str(row[5]).replace('-','') + "\n")


def writeHeadings(parsedCSV):
    food_group = 'Einkauf;Essen;%;'
    HygieneGroup = 'Beauty;Hygiene;%;'
    SparetimeGroup = 'Freizeit;Restaurant;%;'
    Mobility_Group = 'Auto;Tickets;Reisekosten;'
    MiscellaneousGroup = 'Sonstiges;%;%;'
    ClothingGroup = 'Kleidung;Schmuck;%;'
    SubHeadings = 'Ort;Betrag;ZA;'
    parsedCSV.write('Datum;' + food_group + HygieneGroup + SparetimeGroup + Mobility_Group
                     + ClothingGroup + MiscellaneousGroup + '\n')
    parsedCSV.write('Datum;' + 7 * SubHeadings + '\n')


def DateSort(e):
    #print(parser.parse(e[1],dayfirst=True))
    return parser.parse(e[1],dayfirst=True)


def PrepareBankStatement(parser):
    filepath = "C:/Users/kaefe/Desktop/UmsatzanzeigeTESTS/*.csv"
    files = glob.glob(filepath)
    tBankStatement = list()
    for file in files:
        tBankStatement.extend(parser.extract_items_from_bankstatement_list(file))
    tBankStatement.sort(reverse= False, key=DateSort)
    for row in tBankStatement:
        row[2] = row[2].replace("\"", "")
        row[2] = row[2].replace(",", ".")
        #print("Before" + row[5])
        row[5] = row[5].replace(".", "")
        #row[5] = row[5].replace(",", ".")
        #print("fixed" + row[5])
    return tBankStatement


if __name__ == "__main__":
    main()
