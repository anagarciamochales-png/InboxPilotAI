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
                category = ai_classify_email(email_text)
            

# ============================
# AI Reply Assistant
# ============================

            ai_reply = ""
            if (
                analysis_mode == "AI-Powered"
                and category == "interview invitation"
                ):
                ai_reply = ai_generate_reply(email_text)

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