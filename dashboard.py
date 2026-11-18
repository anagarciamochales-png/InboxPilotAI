# ============================
# Imports
# ============================

import streamlit as st
import pandas as pd
from agents import (
    classify_email,
    ai_classify_email,
    assign_priority,
    suggest_folder,
    ai_generate_reply
)
from pathlib import Path
import json
import streamlit as st

try:
    from config import REQUESTY_API_KEY, ADMIN_CODE
except ImportError:
    REQUESTY_API_KEY = st.secrets["REQUESTY_API_KEY"]
    ADMIN_CODE = st.secrets["ADMIN_CODE"]

USAGE_FILE = Path("request_counter.json")

used = 0

if USAGE_FILE.exists():
    with open(USAGE_FILE, "r") as f:
        data = json.load(f)

    used = data["count"]

st.sidebar.info(f"AI requests used today: {used}/100")

# ============================
# Page Configuration
# ============================

st.set_page_config(
    page_title="InboxPilot AI",
    page_icon="📧",
    layout="wide"
)

# ============================
# Dashboard Header
# ============================

st.title("📧 InboxPilot AI")
st.caption(
    "Multi-agent email assistant for classification, prioritization and inbox organization"
)
# ============================
# Sidebar
# ============================

st.sidebar.title("📤 Upload Email Dataset")

st.sidebar.write(
    "Rule-based multi-agent email assistant"
)
with st.sidebar.expander("⚙️ Settings"):
    demo_code = st.text_input(
        "Admin Code",
        type="password"
    )

is_admin = demo_code == ADMIN_CODE
if is_admin:
    st.sidebar.success("✅ Admin Mode Active")

# ============================
# File Upload
# ============================

uploaded_file = st.sidebar.file_uploader(
    "Upload an email dataset (CSV)",
    type=["csv"]
)
if uploaded_file is None:

    st.info(
        "📤 Upload an email dataset and click Analyze Emails to begin."
    )

    st.stop()
st.sidebar.markdown("---")

st.sidebar.subheader("Project Features")

st.sidebar.write(
    "InboxPilot automatically classifies emails, assigns priorities, suggests folders and generates response drafts."
)
st.sidebar.write("✅ Email Classification")
st.sidebar.write("✅ Priority Assignment")
st.sidebar.write("✅ Folder Suggestions")
st.sidebar.write("✅ Reply Generation")
st.sidebar.write("✅ CSV Export")

uploaded_df = pd.read_csv(
    uploaded_file
)
analysis_mode = st.radio(
    "Analysis Mode",
    [
        "Rule-Based",
        "AI-Powered"
        ]
        )
st.subheader("📄 Uploaded Dataset")
st.dataframe(uploaded_df)
    
if analysis_mode == "AI-Powered":
    uploaded_df = uploaded_df.head(5)

# ============================
# Email Analysis
# ============================

if st.button("🚀 Analyze Emails"):
    with st.spinner(f"Analyzing emails using {analysis_mode} mode..."):
        analyzed_results = []
        for _, email in uploaded_df.iterrows():
            email_text = (
            str(email["subject"]) +
            " " +
            str(email["message"])
            )
                
            if analysis_mode == "Rule-Based":
                category = classify_email(email_text)
            else:
                category = ai_classify_email(email_text,is_admin=is_admin)
            
            if category == "AI_LIMIT_REACHED":
                st.error("Daily AI demo limit reached. Please use Rule-Based mode.")
                st.stop()

# ============================
# AI Reply Assistant
# ============================

            ai_reply = ""
            if (
                analysis_mode == "AI-Powered"
                and category == "interview invitation"
                ):
                ai_reply = ai_generate_reply(email_text,is_admin=is_admin)

            priority = assign_priority(category)

            folder = suggest_folder(category)

            analyzed_results.append({
                "sender": email["sender"],
                "subject": email["subject"],
                "category": category,
                "priority": priority,
                "folder": folder,
                "ai_reply": ai_reply
                })
        analyzed_df = pd.DataFrame(analyzed_results)
        st.success(f"Successfully analyzed {len(analyzed_df)} emails.")

        csv_file = analyzed_df.to_csv(
            index=False
            )
    st.download_button(
        label="⬇️ Download Full Analysis",
        data=csv_file,
        file_name="inboxpilot_results.csv",
        mime="text/csv"
        )

    st.subheader("✅ Analysis Results")
            
    if analysis_mode == "Rule-Based":
        display_df = analyzed_df.drop(
            columns=["ai_reply"],
            errors="ignore"
            )
    else:
        display_df = analyzed_df

    st.dataframe(display_df)

    if analysis_mode == "AI-Powered":
        st.subheader("💬 AI Reply Assistant")
        interview_emails = analyzed_df[
            analyzed_df["category"] == "interview invitation"]

        for _, row in interview_emails.iterrows():

            with st.expander(f"📩 {row['subject']}"):

                st.write(row["ai_reply"])

st.markdown("---")

st.caption(
    "InboxPilot AI | Built with Python, Pandas and Streamlit"
)