import csv 
import csv
clean_rows = []

with open("raw_emails.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:

        # Skip empty rows
        if not row:
            continue

        # Split the giant string into columns
        fixed_row = next(csv.reader([row[0]]))

        clean_rows.append(fixed_row)

with open("clean_emails.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerows(clean_rows)

print("✅ clean_emails.csv created")



with open("clean_emails.csv", "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)
        break