class CsvManager:
    def print_csv(object, csv_datei):
        import csv
        object = open(csv_datei)
        csvreader = csv.reader(object)
        header = next(csvreader)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(header)
        for row in rows:
            print(row)
        object.close
