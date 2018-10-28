import csv

def extractitemsfromknownList(csvlist):
    with open (csvlist) as KnownList:
        items = csv.reader(KnownList, delimiter=';', quotechar='|')
        for List in items:
            List
    return List

def main():
    FoodGroup = 'Einkauf,Essen,%,'
    HygieneGroup = 'Beauty,Hygiene,%,'
    SparetimeGroup = 'Freizeit,Restaurant,%,'
    CarGroup = 'Auto,%,%,'
    TravelingGroup = 'Tickets,Reisekosten,%,'
    MiscellaneousGroup = 'Sonstiges,%,%,'
    ClothingGroup = 'Kleidung,Schmuck,%'
    SubHeadings = 'Ort,Betrag,ZA,'
    with open ('KnownHygiene.csv') as KnownHygiene:
        hygieneItems = csv.reader(KnownHygiene, delimiter=';', quotechar='|')
        for hygieneList in hygieneItems:
            hygieneList

    SpareTimeList = extractitemsfromknownList('KnownSpareTime.csv')
    CarList = extractitemsfromknownList('KnownCar.csv')
    TravelingList = extractitemsfromknownList('KnownTraveling.csv')
    RegularCostsList = extractitemsfromknownList('KnownRegularCosts.csv')
    ClothingList = extractitemsfromknownList('KnownClothing.csv')
    einkauflist = extractitemsfromknownList('Einkauf.csv')

    open('Parsed.csv', 'w').close()
    with open('Umsatzanzeige1.csv', newline='') as BankStatementCSV, open ('Parsed.csv', 'w') as ParsedCSV, open('RegluarCosts.csv','w') as regularcostsCSV, open('Income.csv','w') as IncomeCSV :
        ParsedCSV.write('Datum,'+ FoodGroup + HygieneGroup + SparetimeGroup + CarGroup + 
        TravelingGroup + MiscellaneousGroup + ClothingGroup +'\n')

        ParsedCSV.write('Datum,' + 7*SubHeadings + '\n')
        tBankStatement = csv.reader(BankStatementCSV, delimiter=';', quotechar='|')
        for row in tBankStatement:
            # print (row[0]+ "\n")
            row[2] = row[2].replace("\"", "")
            row[5] = row[5].replace(".", "")
            row[5] = row[5].replace(",", ".")
            bHandled = False
            if float(row[5]) > 0:
                IncomeCSV.write(row[0] + "," + row[2] + ','+ row[5] + "\n")
            for item in einkauflist:
                if item in row[2]:
                    ParsedCSV.write(row[0] + "," + row[2] + ','+ row[5] + "\n")
                    bHandled = True
            for item in hygieneList:
                if item in row[2]:
                    ParsedCSV.write(row[0] + 3 * ',' + "," + row[2] + ','+ row[5] + "\n")
                    bHandled = True
            for item in SpareTimeList:
                if item in row[2]:
                    ParsedCSV.write(row[0] + 2*3 * ',' + "," + row[2] + ','+ row[5] + "\n")
                    bHandled = True
            for item in CarList:
                if item in row[2]:
                    ParsedCSV.write(row[0] + 3*3* ',' + "," + row[2] + ','+ row[5] + "\n")
                    bHandled = True
            for item in TravelingList:
                if item in row[2]:
                    ParsedCSV.write(row[0] + 4*3* ',' + "," + row[2] + ','+ row[5] + "\n")
                    bHandled = True
            for item in RegularCostsList:
                if item in row[2]:
                    regularcostsCSV.write(row[0] + ',' + "," + row[2] + ','+ row[5] + "\n")
                    bHandled = True
            for item in ClothingList:
                if item in row[2]:
                    ParsedCSV.write(row[0] + 5*3* ',' + "," + row[2] + ','+ row[5] + "\n")
                    bHandled = True
            if (bHandled == False):
                ParsedCSV.write(row[0] + 3 * 6 * ',' + "," + row[2] + ',' + row[5] + "\n")

if __name__ == "__main__":
    main()
