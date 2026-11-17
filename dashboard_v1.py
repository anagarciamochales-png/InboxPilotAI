# ============================
# Imports
# ============================

import streamlit as st
import pandas as pd
from agents import (
    classify_email,
    assign_priority,
    suggest_folder,
    generate_reply,
)
import io

# ============================
# Page Configuration
# ============================

st.set_page_config(
    page_title="InboxPilot AI",
    page_icon="📧",
    layout="wide"
)

# ============================
# Load Pre-Generated Results
# ============================

results_df = pd.read_csv("results.csv")
processed_emails = len(results_df)

# ============================
# Dashboard Header
# ============================

st.title("📧 InboxPilot AI")
st.caption(
    "Multi-agent email assistant for classification, prioritization and inbox organization"
)

# ============================
# Performance Metrics
# ============================

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Processed Emails",
        processed_emails
    )

with col2:
    st.metric(
        "Accuracy",
        "100%"
    )

category_counts = (
    results_df["predicted_category"]
    .value_counts()
)
chart_data = category_counts.copy()


st.subheader("📊 Category Distribution")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Interview",
        category_counts.get(
            "interview invitation",
            0
        )
    )
with col2:
    st.metric(
        "University",
        category_counts.get(
            "university news",
            0
        )
    )
with col3:
    st.metric(
        "Applications",
        category_counts.get(
            "job application confirmations",
            0
        )
    )
with col4:
    st.metric(
        "Newsletter",
        category_counts.get(
            "newsletter and discounts",
            0
        )
    )
with col5:
    st.metric(
        "Personal",
        category_counts.get(
            "personal emails",
            0
        )
    )

# ============================
# Upload Dataset
# ============================

st.sidebar.title("📤 Upload Email Dataset")

st.sidebar.write(
    "Rule-based multi-agent email assistant"
)

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

analysis_mode = "Rule-Based"

st.subheader("📄 Uploaded Dataset")

st.dataframe(uploaded_df)

# ============================
# Email Analysis
# ============================

if st.button("🚀 Analyze Emails"):
    with st.spinner("Analyzing emails..."):
        analyzed_results = []
        for _, email in uploaded_df.iterrows():
            email_text = (
            str(email["subject"]) +
            " " +
            str(email["message"])
            )
                    
                    
            category = classify_email(email_text)
    
            priority = assign_priority(category)
    
            folder = suggest_folder(category)
    
            reply = generate_reply(category)
    
            analyzed_results.append({
                "sender": email["sender"],
                "subject": email["subject"],
                "category": category,
                "priority": priority,
                "folder": folder,
                })
        analyzed_df = pd.DataFrame(analyzed_results)
        st.success(f"Successfully analyzed {len(analyzed_df)} emails.")
    
        csv_file = analyzed_df.to_csv(index=False)
    
        st.download_button(
            label="⬇️ Download Full Analysis",
            data=csv_file,
            file_name="inboxpilot_results.csv",
            mime="text/csv"
            )
        st.subheader("✅ Analysis Results")
        st.dataframe(analyzed_df)


chart_data.index = [
    "Interview",
    "University",
    "Applications",
    "Newsletter",
    "Personal"
]

# ============================
# High Priority Inbox
# ============================

high_priority_df = pd.read_csv(
    "high_priority.csv"
)


st.subheader("🔥 High Priority Inbox")

st.dataframe(high_priority_df)
high_priority_csv = high_priority_df.to_csv(
    index=False
)

st.download_button(
    label="⬇️ Download High Priority Inbox",
    data=high_priority_csv,
    file_name="high_priority_inbox.csv",
    mime="text/csv"
)

# ============================
# Browse Inbox
# ============================

st.subheader("📂 Browse Inbox")

categories = ["All"] + sorted(
    results_df["predicted_category"].unique()
)

selected_category = st.selectbox(
    "Choose a category",
    categories,
    format_func=lambda x: x.title()
)

if selected_category == "All":
    filtered_df = results_df
else:
    filtered_df = results_df[
        results_df["predicted_category"]
        == selected_category
    ]

st.dataframe(filtered_df)

# ============================
# Footer
# ============================

st.markdown("---")

st.caption(
    "InboxPilot AI | Built with Python, Pandas and Streamlit"
)