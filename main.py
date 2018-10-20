import csv

def main():
    listentry = list()
    with open('Umsatzanzeige.csv', newline='') as BankStatementCSV:
        spamreader = csv.reader(BankStatementCSV, delimiter=';', quotechar='|')

        for row in spamreader:
            listentry['Buchung'] = row[0]
            print(', '.join(row))
            listentry.append(row)

    print(listentry)



if __name__ == "__main__":
    main()
