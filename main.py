import csv

def main():
    listentry = list()
    Group1 = 'Einkauf,Essen,%'
    Group2 = 'Beauty,Hygiene,%'
    SubHeadings = 'Datum, Ort,ZA,'
    open('Parsed.csv', 'w').close()
    with open('Umsatzanzeige.csv', newline='') as BankStatementCSV, open ('Parsed.csv', 'w') as Parsed,open ('Einkauf.csv') as einkauf:
        Parsed.write('Datum,'+ Group1 +','+ Group2 + ',' +'Freizeit,Restaurant,%,Auto,%,%,Tickets,Reisekosten,%,Sonstiges,%,%,Kleidung,Schmuck,%\n')
        Parsed.write(7*SubHeadings)
        spamreader = csv.reader(BankStatementCSV, delimiter=';', quotechar='|')
        einkaufitems = csv.reader(einkauf, delimiter=';', quotechar='|')
        for einkauflist in einkaufitems:
            einkauflist

        for row in spamreader:
            # print (row[0]+ "\n")
            row[2] = row[2].replace("\"", "")
            row[5] = row[5].replace(",", ".")
            for item in einkauflist:
                if item in row[2]:
                    Parsed.write(row[0] + "," + row[2] + ','+ row[5] + "\n")
            else:
                Parsed.write(row[0] + " ,/,/,/,/,/,/" + "," + row[2] + ',' + row[5] + "\n")
            # listentry['Buchung'] = row[0]
            # print(', '.join(row))
            # listentry.append(row)

    # print(listentry)

if __name__ == "__main__":
    main()
