# 📧 InboxPilot AI

InboxPilot AI is a multi-agent email assistant built with Python and Streamlit.

The application automatically analyzes emails, assigns categories, prioritizes important messages, suggests folders for organization, and generates response drafts.

## 🚀 Live Demo

Streamlit App: https://inboxpilot-ana.streamlit.app/

## Features

✅ Email Classification

- Interview Invitations
- University News
- Job Application Confirmations
- Newsletter and Discounts
- Personal Emails

✅ Priority Assignment

- High
- Medium
- Low

✅ Folder Suggestions

- Career
- Education
- Application Confirmation
- Promotions
- Personal

✅ Reply Generation

Automatically generates appropriate reply templates based on the detected category.

✅ High Priority Inbox

Identifies important emails and creates a focused inbox view.

✅ CSV Upload and Analysis

Users can upload their own email datasets directly through the dashboard.

✅ CSV Export

Download:

- Full Analysis Results
- High Priority Inbox

## Tech Stack

- Python
- Pandas
- Streamlit
- CSV Data Processing
## Project Structure
```
InboxPilotAI/

  ├── agents.py
  ├── cleaner.py
  ├── data_loader.py
  ├── main.py
  ├── dashboard.py
  ├── raw_emails.csv
  ├── clean_emails.csv
  ├── results.csv
  ├── high_priority.csv
  ├── requirements.txt
  └── .gitignore
```

## How It Works

### 1. Upload Dataset

Upload a CSV file containing email data.

### 2. Email Analysis

InboxPilot analyzes each email using multiple agents:

- Classification Agent
- Priority Agent
- Folder Agent
- Reply Agent

### 3. Results

The system returns:

- Email Category
- Priority Level
- Suggested Folder
- Suggested Reply

### 4. Download

Users can download results as CSV files.

## Dashboard

The Streamlit dashboard provides:

- Email statistics
- Category distribution
- High priority inbox
- Email browser
- Dataset upload
- CSV downloads

## Results

Dataset Size:

- 105 Emails

Classification Accuracy:

- 100%

Categories:

- Interview Invitations
- University News
- Job Application Confirmations
- Newsletter and Discounts
- Personal Emails

## Future Improvements

### Version 2

- AI-powered email classification
- AI-generated replies
- Claude/OpenAI integration
- Improved analytics
- Email provider integration

### Version 3

- Gmail integration
- Outlook integration
- Automatic folder creation
- Real-time inbox management

## Author

Ana García Mochales Ortiz

Built as a portfolio project to learn:

- Python Development
- Data Processing
- Streamlit
- Multi-Agent Systems
- AI Application Development