import csv 

def load_emails():

    emails = []

    with open("clean_emails.csv", "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:
            emails.append(row)

    return emails
