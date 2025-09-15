import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import preprocessor, helper

# ------------------------ PAGE CONFIG ------------------------
st.set_page_config(
    page_title="WhatsApp Chat Analyzer",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------ SIDEBAR ------------------------
st.sidebar.markdown(
    """
    <h1 style="text-align:center; color:#4a4a4a;">💬 WhatsApp Chat Analyzer</h1>
    <p style="text-align:center; font-size:14px; color:gray;">
        Upload your exported WhatsApp chat text file and explore insights.
    </p>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.sidebar.file_uploader("📁 Choose a WhatsApp chat file")

# Sidebar Footer
st.sidebar.markdown(
    """
    <hr style="margin-top:20px;margin-bottom:15px; border: 1px solid #ddd;">

    <div style="text-align:center; color:gray; font-size:13px; line-height:1.6;">
        <b style="font-size:14px; color:#4a4a4a;">© 2025 Pratik Sutar</b><br>
        Made with ❤️ using <b>Streamlit</b><br><br>

        <a href="https://www.linkedin.com/in/your-linkedin-username" target="_blank" style="margin:0 8px; text-decoration:none;">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="22" />
        </a>
        <a href="https://github.com/your-github-username" target="_blank" style="margin:0 8px; text-decoration:none;">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="22" />
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------ MAIN CONTENT ------------------------
st.title("📊 WhatsApp Chat Analyzer Dashboard")
st.markdown(
    "<p style='color:gray; font-size:16px;'>Explore chat statistics, timelines, activity maps, most common words, and emojis.</p>",
    unsafe_allow_html=True
)

if uploaded_file is not None:
    data = uploaded_file.getvalue().decode("utf-8")
    df = preprocessor.preprocess(data)

    # Get unique users
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, 'Overall')

    selected_user = st.sidebar.selectbox("Show analysis for", user_list)

    if st.sidebar.button("🚀 Show Analysis"):
        # ---------- Top Stats ----------
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

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

        # ---------- Most Busy Users ----------
        if selected_user == 'Overall':
            st.subheader("👥 Most Busy Users")
            x, new_df = helper.most_busy_users(df)
            col1, col2 = st.columns(2)
            with col1:
                fig, ax = plt.subplots()
                ax.bar(x.index, x.values, color='#ffa94d')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        # ---------- Monthly Timeline ----------
        st.subheader("🗓️ Monthly Timeline")
        monthly_timeline = helper.monthly_time_line(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(monthly_timeline['time'], monthly_timeline['message'], color='#51cf66', marker='o')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # ---------- Daily Timeline ----------
        st.subheader("📅 Daily Timeline")
        daily_timeline = helper.daily_time_line(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='#5c7cfa', marker='.')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # ---------- Activity Maps ----------
        st.subheader("📍 Weekly Activity Map")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Most Busy Day**")
            busy_day = helper.weekly_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='#ff6b6b')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.markdown("**Most Busy Month**")
            busy_month = helper.monthly_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='#ff8787')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # ---------- Activity Heatmap ----------
        st.subheader("🔥 Weekly Activity Heatmap")
        activity_map = helper.activity_heat_map(selected_user, df)
        fig, ax = plt.subplots()
        sns.heatmap(activity_map, cmap="YlOrRd", linewidths=.5, annot=False)
        st.pyplot(fig)

        # ---------- Wordcloud ----------
        st.subheader("☁️ Wordcloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        ax.axis('off')
        st.pyplot(fig)

        # ---------- Most Common Words ----------
        st.subheader("💬 Most Common Words")
        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1], color='#66d9e8')
        st.pyplot(fig)

        # ---------- Emoji Analysis ----------
        st.subheader("😄 Emoji Analysis")
        emoji_df = helper.emoji_helper(selected_user, df)
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct='%0.2f')
            st.pyplot(fig)
