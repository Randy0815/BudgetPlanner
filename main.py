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
        'RegularSavings.csv', 'w') as RegularSavings:

        writeHeadings(ParsedCSV)

        WriteParsedDebits(CategoryList, IncomeCSV, ParsedCSV, RegularCostsList, RegularSavings, namelist, parser,
                          regularcostsCSV, tBankStatement)


def WriteParsedDebits(CategoryList, IncomeCSV, ParsedCSV, RegularCostsList, RegularSavings, namelist, parser,
                      regularcostsCSV, tBankStatement):
    for row in tBankStatement:
        bHandled = False
        if float(row[5].replace(",", ".")) > 0:
            #row[5] =
            IncomeCSV.write(row[0] + separator + row[2] + separator + row[5] + "\n")
            bHandled = True
        if "BARGELDAUSZAHLUNG" in row[4]:
            ParsedCSV.write(row[0] + 7 * 3 * separator + separator+separator + row[2] + separator + row[5] + "\n")
        for x in range(0, 6):
            bHandled |= parser.parse_list(CategoryList[x], ParsedCSV, row, x)
        for item in RegularCostsList[0]:
            if item in row[2]:
                regularcostsCSV.write(row[0] + separator + separator + item + separator + row[5] + "\n")
                bHandled = True
        if (bHandled == False):
            if (namelist[0][0] in row[2]) or (namelist[0][1] in row[2]):
                RegularSavings.write(row[0] + separator + separator + row[2] + separator + row[5] + "\n")
            else:
                if ("AMAZON" in row[2]):
                    row[2] = "AMAZON"
                ParsedCSV.write(row[0] + 3 * 6 * separator + separator + row[2] + separator + row[5] + "\n")


def writeHeadings(parsedCSV):
    FoodGroup = 'Einkauf;Essen;%;'
    HygieneGroup = 'Beauty;Hygiene;%;'
    SparetimeGroup = 'Freizeit;Restaurant,%,'
    CarGroup = 'Auto;%;%;'
    TravelingGroup = 'Tickets;Reisekosten;%;'
    MiscellaneousGroup = 'Sonstiges;%;%;'
    ClothingGroup = 'Kleidung;Schmuck;%'
    SubHeadings = 'Ort;Betrag;ZA;'
    parsedCSV.write('Datum;' + FoodGroup + HygieneGroup + SparetimeGroup + CarGroup +
                    TravelingGroup + MiscellaneousGroup + ClothingGroup + '\n')
    parsedCSV.write('Datum;' + 7 * SubHeadings + '\n')


def DateSort(e):
    print(parser.parse(e[1],dayfirst=True))
    return parser.parse(e[1],dayfirst=True)


def PrepareBankStatement(parser):
    filepath = "C:/Users/kaefe/Desktop/UmsatzanzeigeTESTS/*.csv"
    files = glob.glob(filepath)
    tBankStatement = list()
    for file in files:
        tBankStatement.extend(parser.extract_items_from_known_list(file))
        print(tBankStatement)
        print("\n")
    tBankStatement.sort(reverse= True, key=DateSort)
    print(tBankStatement)
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
