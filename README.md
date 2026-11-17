# 📧 InboxPilot AI

InboxPilot AI is a multi-agent email assistant built with Python and Streamlit.

The application automatically analyzes emails, assigns categories, prioritizes important messages, suggests folders for organization, and generates response drafts.

## 🚀 Live Demo
Streamlit App: https://inboxpilot-ana.streamlit.app/

The dashboard supports both Rule-Based and AI-Powered analysis modes.

## Features

### ✅ Rule-Based Email Classification

Classifies emails into:
- Interview Invitations
- University News
- Job Application Confirmations
- Newsletter and Discounts
- Personal Emails

### ✅ AI-Powered Email Classification

Uses Requesty and Large Language Models (LLMs) to understand the meaning of emails and classify them semantically instead of relying solely on keyword matching.

### ✅ AI Reply Assistant

Generates professional interview replies directly within the dashboard.

### ✅ Priority Assignment

Assigns High, Medium, or Low priority levels.

### ✅ Folder Suggestions

Recommends inbox organization folders automatically

### ✅ High Priority Inbox

Identifies important emails and creates a focused inbox view.

### ✅ CSV Upload and Analysis

Analyze custom email datasets directly from the dashboard.

### ✅ CSV Export

Download analysis results and high-priority inbox views.

### ✅ Public Web Application

Deployed using Streamlit Cloud and accessible from any device through a public URL.

## Tech Stack

- Python
- Streamlit
- Pandas
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

InboxPilot started as a rule-based multi-agent email assistant and evolved into an AI-powered system using Requesty and Large Language Models (LLMs).

The screenshots below illustrate the progression from deterministic keyword classification to semantic AI understanding and AI-generated interview responses.

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
Overview of the original rule-based dashboard showing processed emails, classification metrics, and category distribution.

#### Rule-Based Analysis

<img width="1468" height="1178" alt="v1_rule_based_analysis" src="https://github.com/user-attachments/assets/c9fdbb3a-13f5-4184-882c-fba8358ee8e0" />
Email classification results generated using keyword matching and deterministic rule-based agents.

#### High Priority Inbox

<img width="1123" height="536" alt="v1_high_priority_inbox" src="https://github.com/user-attachments/assets/0e29a682-ae02-426d-883a-0ac17f85d832" />
Focused inbox view highlighting important emails that require immediate attention.

#### Browse Inbox

<img width="1356" height="666" alt="v1_browse_inbox" src="https://github.com/user-attachments/assets/c7aca115-50b0-4eb2-b32e-85b7ef6dbca4" />
Interactive email browser with category-based filtering for easier inbox exploration and organization.

### Version 2 - AI-Powered Dashboard
#### Empty Dashboard

<img width="1254" height="499" alt="v2_home_dashboard" src="https://github.com/user-attachments/assets/d28e04cf-3b2f-430f-93bf-1da5c4adc808" />
Initial application state before dataset upload, providing a clean starting point for analysis.

#### AI Classification. Rule-Based vs AI

<img width="1607" height="1170" alt="v2_rule_based_analysis" src="https://github.com/user-attachments/assets/3e150ce3-cf5c-475f-b336-dca8dc2581bc" />
Comparison between traditional rule-based classification and AI-powered semantic email understanding.
<img width="1287" height="865" alt="v2_ai_analysis" src="https://github.com/user-attachments/assets/ef39eb34-fe99-4904-bfae-dd504bf04104" />
AI-enhanced email categorization using Requesty and Large Language Models (LLMs) to understand email context beyond keyword matching.

#### AI Reply Assistant

<img width="1223" height="498" alt="v2_ai_reply_assistant" src="https://github.com/user-attachments/assets/1bcc3068-a41e-438d-9c26-9a42771acdfa" />
Professional interview response automatically generated by the AI Reply Assistant directly within the Streamlit dashboard.

## Evaluation Results

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
  
## System Architecture
### Version 1:

Email → Classification Agent → Priority Agent → Folder Agent → Reply Agent

### Version 2:

Email → AI Classification Agent → Priority Agent → Folder Agent → AI Reply Assistant

## Future Improvements

### Version 3

- Gmail integration
- Outlook integration
- Automatic folder creation
- Real-time inbox management


## Author

Ana García Mochales Ortiz

Built as a portfolio project to explore traditional rule-based automation, AI-powered classification, multi-agent workflows, and web application deployment.

- Python Development
- Data Processing
- Streamlit
- Multi-Agent Systems
- AI Application Development
