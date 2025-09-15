import streamlit as st
import matplotlib.pyplot as plt
import preprocessor, helper
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# Sidebar Title
st.sidebar.title("📊 Whatsapp Chat Analyzer")

# --- FRONT PAGE ---
st.title("💬 WhatsApp Chat Analyzer")
st.markdown(
    """
    <div style='background-color:#f0f4f8; padding:20px; border-radius:15px;'>
        <h2 style='color:#333;'>Welcome to WhatsApp Chat Analyzer</h2>
        <p style='font-size:18px; color:#555;'>
        Upload your exported WhatsApp chat (.txt file) to explore:
        </p>
        <ul style='font-size:17px; color:#444;'>
            <li>📈 Message and word statistics</li>
            <li>📅 Daily & Monthly timelines</li>
            <li>🔥 Most active users</li>
            <li>🌡️ Weekly activity heatmap</li>
            <li>☁️ Wordcloud and 📝 Most common words</li>
            <li>😀 Emoji usage analysis</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# File Uploader
uploaded_file = st.sidebar.file_uploader("📁 Choose a WhatsApp chat file (.txt)")

# --- If file is uploaded ---
if uploaded_file is not None:
    # Read file
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")

    # Preprocess
    df = preprocessor.preprocess(data)

    # Fetch unique users
    user_list = df["user"].unique().tolist()
    if "group_notification" in user_list:
        user_list.remove("group_notification")
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("📌 Show analysis for", user_list)

    # Stats Area
    if st.sidebar.button("🚀 Show Analysis"):
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(
            selected_user, df
        )

        st.subheader("📌 Top Statistics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Messages", num_messages)
        with col2:
            st.metric("Total Words", words)
        with col3:
            st.metric("Media Shared", num_media_messages)
        with col4:
            st.metric("Links Shared", num_links)

        # Busiest users
        if selected_user == "Overall":
            st.subheader("👥 Most Busy Users")
            x, new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()
            col1, col2 = st.columns(2)
            with col1:
                ax.bar(x.index, x.values, color="#ffa94d")
                plt.xticks(rotation="vertical")
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        # Monthly timeline
        st.subheader("📅 Monthly Timeline")
        monthly_timeline = helper.monthly_time_line(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(monthly_timeline["time"], monthly_timeline["message"], color="#51cf66")
        plt.xticks(rotation="vertical")
        st.pyplot(fig)

        # Daily timeline
        st.subheader("📆 Daily Timeline")
        daily_timeline = helper.daily_time_line(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline["only_date"], daily_timeline["message"], color="#5c7cfa")
        plt.xticks(rotation="vertical")
        st.pyplot(fig)

        # Weekly activity map
        st.subheader("📌 Activity Map")
        col1, col2 = st.columns(2)
        with col1:
            st.caption("Most Busy Day")
            busy_day = helper.weekly_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color="#ff6b6b")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)
        with col2:
            st.caption("Most Busy Month")
            busy_month = helper.monthly_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color="#ff6b6b")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        # Heatmap
        st.subheader("🌡️ Weekly Activity Heatmap")
        activity_map = helper.activity_heat_map(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(activity_map)
        st.pyplot(fig)

        # Wordcloud
        st.subheader("☁️ Wordcloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        plt.axis("off")
        ax.imshow(df_wc)
        st.pyplot(fig)

        # Most Common Words
        st.subheader("📝 Most Common Words")
        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1], color="#66d9e8")
        st.pyplot(fig)

        # Emoji analysis
        st.subheader("😀 Emoji Analysis")
        emoji_df = helper.emoji_helper(selected_user, df)
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f")
            st.pyplot(fig)

# --- Footer ---
st.markdown(
    """
    <hr style="margin-top:40px;"/>
    <div style="text-align:center; color:gray; font-size:15px;">
        © 2025 Created by <b>Pratik Sutar</b>
    </div>
    """,
    unsafe_allow_html=True
)
