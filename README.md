# 📧 InboxPilot AI

InboxPilot AI is a multi-agent email assistant built with Python and Streamlit.

The application automatically analyzes emails, assigns categories, prioritizes important messages, suggests folders for organization, and generates response drafts.

## 🚀 Live Demo

Streamlit App: https://inboxpilot-ana.streamlit.app/

## Features

### ✅ Email Classification

- Interview Invitations
- University News
- Job Application Confirmations
- Newsletter and Discounts
- Personal Emails

### ✅ AI Classification

Uses LLMs through Requesty to classify email content semantically instead of relying solely on keyword matching.

### ✅ AI Reply Assistant

Generates professional interview replies directly within the dashboard.

### ✅ Priority Assignment

- High
- Medium
- Low

### ✅ Folder Suggestions

- Career
- Education
- Application Confirmation
- Promotions
- Personal

### ✅ High Priority Inbox

Identifies important emails and creates a focused inbox view.

### ✅ CSV Upload and Analysis

Users can upload their own email datasets directly through the dashboard.

### ✅ CSV Export

Download:

- Full Analysis Results
- High Priority Inbox

## Tech Stack

- Python
- Pandas
- Streamlit
- Requesty API
- Large Language Models (LLMs)
- CSV Data Processing
## Project Structure
```
InboxPilotAI/

  ├── agents.py
  ├── cleaner.py
  ├── data_loader.py
  ├── main.py
  ├── dashboard.py
  ├── dashboard_v1.py
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
  
## Evolution of InboxPilot

InboxPilot was developed in two stages.

### Version 1 – Rule-Based System

The original version used keyword matching and rule-based agents to:

- Classify emails
- Assign priorities
- Suggest folders
- Generate template responses

This version provided fast and deterministic results using traditional Python logic.

### Version 2 – AI-Powered System

The second version integrates AI through Requesty and Large Language Models (LLMs).

New capabilities include:

- Semantic email classification
- AI-generated interview responses
- Rule-Based vs AI comparison mode
- Interactive AI Reply Assistant

The AI version can understand the meaning of emails even when specific keywords are not present.

## Screenshots
### Version 1 - Rule-Based Dashboard
#### Dashboard Overview

<img width="1469" height="716" alt="v1_home_dashboard" src="https://github.com/user-attachments/assets/ab60990a-7eca-4be4-bbcc-557b3f3aaea2" />

#### Rule-Based Analysis

<img width="1468" height="1178" alt="v1_rule_based_analysis" src="https://github.com/user-attachments/assets/dc68e3ff-bfb8-41c1-8a81-85e43389ca23" />

#### High Priority Inbox

<img width="1123" height="536" alt="v1_high_priority_inbox" src="https://github.com/user-attachments/assets/0e29a682-ae02-426d-883a-0ac17f85d832" />

### Version 2 - AI-Powered Dashboard
#### Empty Dashboard

<img width="1254" height="499" alt="v2_home_dashboard" src="https://github.com/user-attachments/assets/d28e04cf-3b2f-430f-93bf-1da5c4adc808" />

#### AI Classification

<img width="1287" height="865" alt="v2_ai_analysis" src="https://github.com/user-attachments/assets/ef39eb34-fe99-4904-bfae-dd504bf04104" />

#### AI Reply Assistant

<img width="1223" height="498" alt="v2_ai_reply_assistant" src="https://github.com/user-attachments/assets/1bcc3068-a41e-438d-9c26-9a42771acdfa" />

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

### Version 3

- Gmail integration
- Outlook integration
- Automatic folder creation
- Real-time inbox management

## System Architecture
### Version 1:

Email → Classification Agent → Priority Agent → Folder Agent → Reply Agent

### Version 2:

Email → AI Classification Agent → Priority Agent → Folder Agent → AI Reply Assistant

## Author

Ana García Mochales Ortiz

Built as a portfolio project to learn:

- Python Development
- Data Processing
- Streamlit
- Multi-Agent Systems
- AI Application Development
