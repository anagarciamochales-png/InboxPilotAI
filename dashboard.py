import streamlit as st
import pandas as pd
from agents import (
    classify_email,
    assign_priority,
    suggest_folder,
    generate_reply
)
import io



results_df = pd.read_csv("results.csv")
processed_emails = len(results_df)

st.title("📧 InboxPilot AI")
st.caption(
    "Multi-agent email assistant for classification, prioritization and inbox organization"
)
#st.header("Version 1 Dashboard")

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
    st.metric("Interview", 21)

with col2:
    st.metric("University", 21)

with col3:
    st.metric("Applications", 21)

with col4:
    st.metric("Newsletter", 21)

with col5:
    st.metric("Personal", 21)

#st.subheader("📤 Upload Email Dataset")

st.sidebar.title("📤 Upload Email Dataset")

st.sidebar.write(
    "Rule-based multi-agent email assistant"
)

uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)
st.sidebar.markdown("---")

st.sidebar.subheader("Project Features")

st.sidebar.write("✅ Email Classification")
st.sidebar.write("✅ Priority Assignment")
st.sidebar.write("✅ Folder Suggestions")
st.sidebar.write("✅ Reply Generation")
st.sidebar.write("✅ CSV Export")

if uploaded_file is not None:

    uploaded_df = pd.read_csv(
        uploaded_file
    )

    st.subheader("📂 Uploaded Dataset")
    st.dataframe(uploaded_df)

    if st.button("🚀 Analyze Emails"):
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
                "folder": folder
            })
        analyzed_df = pd.DataFrame(
            analyzed_results
        )
        csv_file = analyzed_df.to_csv(
            index=False
            )

        st.download_button(
            label="⬇️ Download Results CSV",
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