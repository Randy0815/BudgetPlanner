import csv

def extractitemsfromknownList(csvlist):
    lines = list()
    with open (csvlist, newline='') as KnownList:
        items = csv.reader(KnownList, delimiter=';', quotechar='|')
        for List in items:
            lines.append(List)
    return lines

def main():
    FoodGroup = 'Einkauf,Essen,%,'
    HygieneGroup = 'Beauty,Hygiene,%,'
    SparetimeGroup = 'Freizeit,Restaurant,%,'
    CarGroup = 'Auto,%,%,'
    TravelingGroup = 'Tickets,Reisekosten,%,'
    MiscellaneousGroup = 'Sonstiges,%,%,'
    ClothingGroup = 'Kleidung,Schmuck,%'
    SubHeadings = 'Ort,Betrag,ZA,'

    CategoryList = extractitemsfromknownList('InputData/KnownLocations.csv')
    tBankStatement = extractitemsfromknownList('Umsatzanzeige1.csv')
    RegularCostsList = extractitemsfromknownList('KnownRegularCosts.csv')
    namelist = extractitemsfromknownList('InputData/Names.csv')

    open('Parsed.csv', 'w').close()
    with open ('Parsed.csv', 'w') as ParsedCSV, open('RegluarCosts.csv','w') as regularcostsCSV, open('Income.csv','w') as IncomeCSV, open('RegularSavings.csv','w') as RegularSavings :
        ParsedCSV.write('Datum,'+ FoodGroup + HygieneGroup + SparetimeGroup + CarGroup + 
        TravelingGroup + MiscellaneousGroup + ClothingGroup +'\n')

        ParsedCSV.write('Datum,' + 7*SubHeadings + '\n')
        for row in tBankStatement:
            row[2] = row[2].replace("\"", "")
            row[2] = row[2].replace(",", ".")
            row[5] = row[5].replace(".", "")
            row[5] = row[5].replace(",", ".")
            bHandled = False
            if float(row[5]) > 0:
                IncomeCSV.write(row[0] + "," + row[2] + ','+ row[5] + "\n")
                bHandled = True
            if "BARGELDAUSZAHLUNG" in row[4]:
                ParsedCSV.write(row[0] + 7*3*"," + ',' + row[2] + ','+ row[5] + "\n")
            for item in CategoryList[0]:
                if item in row[2]:
                    ParsedCSV.write(row[0] + "," + item + ',' + row[5] + "\n")
                    bHandled = True
            for item in CategoryList[1]:
                if item in row[2]:
                    ParsedCSV.write(row[0] + 3 * ',' + "," + item + ','+ row[5] + "\n")
                    bHandled = True
            for item in CategoryList[2]:
                if item in row[2]:
                    ParsedCSV.write(row[0] + 2*3 * ',' + "," + item + ','+ row[5] + "\n")
                    bHandled = True
            for item in CategoryList[3]:
                if item in row[2]:
                    ParsedCSV.write(row[0] + 3*3* ',' + "," + item + ','+ row[5] + "\n")
                    bHandled = True
            for item in CategoryList[4]:
                if item in row[2]:
                    ParsedCSV.write(row[0] + 4*3* ',' + "," + item + ','+ row[5] + "\n")
                    bHandled = True
            for item in CategoryList[5]:
                if item in row[2]:
                    ParsedCSV.write(row[0] + 6*3* ',' + "," + item + ','+ row[5] + "\n")
                    bHandled = True
            for item in RegularCostsList[0]:
                if item in row[2]:
                    regularcostsCSV.write(row[0] + ',' + "," + item + ','+ row[5] + "\n")
                    bHandled = True
            if (bHandled == False):
                if (namelist[0][0] in row[2]) or (namelist[0][1] in row[2]):
                    RegularSavings.write(row[0] + ',' + "," + row[2] + ',' + row[5] + "\n")
                else:
                    if ("AMAZON" in row[2]):
                        row[2] = "AMAZON"
                    ParsedCSV.write(row[0] + 3 * 5 * ',' + "," + row[2] + ',' + row[5] + "\n")

if __name__ == "__main__":
    main()
