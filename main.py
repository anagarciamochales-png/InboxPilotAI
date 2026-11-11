import csv
from data_loader import load_emails

from agents import (
    classify_email,
    assign_priority,
    suggest_folder,
    generate_reply
)
# ============
# SETUP
# ============

emails = load_emails()

results = []
correct = 0
wrong = 0
category_counts = {}
folder_counts = {}
high_priority_emails = []
high_priority_results = []

# ==========================================
# ANALYZE EMAILS, SAVE RESULTS AND ACCURACY
# ==========================================

for email in emails:

    #analyze emails
    email_text = (
        email["subject"] +
        " " +
        email["message"]
    )
    category = classify_email(email_text)
    priority = assign_priority(category)
    
    folder = suggest_folder(category)
    if folder in folder_counts:
        folder_counts[folder] += 1
    else:
        folder_counts[folder] = 1
    reply = generate_reply(category)

    # save reuslts

    results.append({
        "sender": email["sender"],
        "subject": email["subject"],
        "predicted_category": category,
        "priority": priority,
        
        "folder": folder,
        "reply": reply
    })
    if priority == "High":
        high_priority_emails.append(
            email["subject"]
        )
        high_priority_results.append({
            "subject": email["subject"],
            "priority": priority,
            "folder": folder
        })

    # accuracy
    expected = email["category"].lower()
    predicted = category.lower()

    if expected == predicted:
        correct += 1
    else:
        wrong += 1
        
        print("\n❌ Wrong Prediction")
        print(f"Expected: {email['category']}")
        print(f"Predicted: {predicted}")
        print(f"Subject: {email['subject']}")

    # category stadistics
    if category in category_counts:
        category_counts[category] += 1
    else:
        category_counts[category] = 1
# accuracy calculation ALWAYS outside loop, because it has to be done once all the emails have been processed         
accuracy = (correct / len(emails)) * 100

# ============
# final report
# ============
print("\nInboxPilot Report")
print("=================")  
print(f"Processed Emails: {len(emails)}")
print(f"Correct Predictions: {correct}")
print(f"Wrong Predictions: {wrong}")
print(f"Accuracy: {accuracy:.1f}%")

# ============
# category stadictics
# ============

print("\nCategory Statistics")
print("===================")


for category, count in category_counts.items():
    print(f"{category}: {count}")

print("\nHigh Priority Inbox")
print("===================")

for subject in high_priority_emails:
    print(subject)
print("\nFolder Statistics")
print("=================")

for folder, count in folder_counts.items():
    print(f"{folder}: {count}")

# example results  
for result in results[:5]:

    print("\n--------------")
    print(f"Subject: {result['subject']}")
    print(f"Category: {result['predicted_category']}")
    print(f"Priority: {result['priority']}")
    print(f"Folder: {result['folder']}")



# csv export
with open(
    "results.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "sender",
            "subject",
            "predicted_category",
            "priority",
            "folder",
            "reply"
        ]
    )

    writer.writeheader()

    writer.writerows(results)

with open(
    "high_priority.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "subject",
            "priority",
            "folder"
        ]
    )

    writer.writeheader()

    writer.writerows(high_priority_results)




