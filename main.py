from BankStatementParser import BankStatementParser

def main():
    FoodGroup = 'Einkauf,Essen,%,'
    HygieneGroup = 'Beauty,Hygiene,%,'
    SparetimeGroup = 'Freizeit,Restaurant,%,'
    CarGroup = 'Auto,%,%,'
    TravelingGroup = 'Tickets,Reisekosten,%,'
    MiscellaneousGroup = 'Sonstiges,%,%,'
    ClothingGroup = 'Kleidung,Schmuck,%'
    SubHeadings = 'Ort,Betrag,ZA,'
    parser = BankStatementParser.BankStatementParser()

    CategoryList = parser.extractitemsfromknownList('InputData/KnownLocations.csv')
    tBankStatement = parser.extractitemsfromknownList('Umsatzanzeige_MP18-11-17.csv')
    RegularCostsList = parser.extractitemsfromknownList('InputData/KnownRegularCosts.csv')
    namelist = parser.extractitemsfromknownList('InputData/Names.csv')
    tBankStatement.reverse()
    # open('Parsed.csv', 'w').close()
    with open('Parsed.csv', 'w') as ParsedCSV, open('RegluarCosts.csv', 'w') as regularcostsCSV, open('Income.csv',
                                                                                                      'w') as IncomeCSV, open(
            'RegularSavings.csv', 'w') as RegularSavings:
        ParsedCSV.write('Datum,' + FoodGroup + HygieneGroup + SparetimeGroup + CarGroup +
                        TravelingGroup + MiscellaneousGroup + ClothingGroup + '\n')

        ParsedCSV.write('Datum,' + 7 * SubHeadings + '\n')
        for row in tBankStatement:
            row[2] = row[2].replace("\"", "")
            row[2] = row[2].replace(",", ".")
            row[5] = row[5].replace(".", "")
            row[5] = row[5].replace(",", ".")
            bHandled = False
            if float(row[5]) > 0:
                IncomeCSV.write(row[0] + "," + row[2] + ',' + row[5] + "\n")
                bHandled = True
            if "BARGELDAUSZAHLUNG" in row[4]:
                ParsedCSV.write(row[0] + 7 * 3 * "," + ',,' + row[2] + ',' + row[5] + "\n")
            for x in range(0, 6):
                bHandled |= parser.parselist(CategoryList[x], ParsedCSV, row, x)
            for item in RegularCostsList[0]:
                if item in row[2]:
                    regularcostsCSV.write(row[0] + ',' + "," + item + ',' + row[5] + "\n")
                    bHandled = True
            if (bHandled == False):
                if (namelist[0][0] in row[2]) or (namelist[0][1] in row[2]):
                    RegularSavings.write(row[0] + ',' + "," + row[2] + ',' + row[5] + "\n")
                else:
                    if ("AMAZON" in row[2]):
                        row[2] = "AMAZON"
                    ParsedCSV.write(row[0] + 3 * 6 * ',' + "," + row[2] + ',' + row[5] + "\n")


if __name__ == "__main__":
    main()
