<h1>💬 WhatsApp Chat Analyzer</h1>

<p>A <b>Streamlit web application</b> that analyzes WhatsApp chat exports and provides interactive insights like message statistics, timelines, most active users, activity heatmaps, wordclouds, and emoji usage.</p>

<hr>

<h2>🔗 Live Demo</h2>
<p>Try the app on Streamlit Cloud: <a href="YOUR_STREAMLIT_LINK_HERE" target="_blank">Click here</a></p>

<hr>

<h2>📌 Project Objective</h2>
<ul>
    <li>Explore messaging patterns</li>
    <li>Identify most active users and peak activity times</li>
    <li>Visualize most common words and emojis</li>
    <li>Understand weekly and monthly chat trends</li>
</ul>

<hr>

<h2>🛠️ Tools & Technologies</h2>
<ul>
    <li>Python, Pandas, NumPy, Matplotlib, Seaborn, Wordcloud, Streamlit</li>
    <li>Frontend: Streamlit for interactive UI</li>
    <li>Environment: Jupyter Notebook, VS Code</li>
    <li>Version Control: Git & GitHub</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>
<pre>
Whatsapp-Chat-Analyzer/
│── app.py              # Main Streamlit app
│── preprocessor.py     # Chat preprocessing functions
│── helper.py           # Analysis functions
│── chat/               # Sample WhatsApp chat .txt files
│── requirements.txt    # Dependencies
│── README.in           # Project documentation (HTML)
</pre>

<hr>

<h2>📊 Methodology</h2>
<ol>
    <li><b>Data Preprocessing</b>
        <ul>
            <li>Load exported WhatsApp .txt files</li>
            <li>Extract timestamps, users, messages, media, and links</li>
        </ul>
    </li>
    <li><b>Analysis</b>
        <ul>
            <li>Calculate total messages, words, media, and links</li>
            <li>Identify most active users</li>
            <li>Create daily & monthly timelines</li>
            <li>Map weekly activity</li>
        </ul>
    </li>
    <li><b>Visualization</b>
        <ul>
            <li>Bar plots for busiest users</li>
            <li>Line plots for timelines</li>
            <li>Heatmaps for weekly activity</li>
            <li>Wordclouds for common words</li>
            <li>Pie charts for emoji usage</li>
        </ul>
    </li>
</ol>

<hr>

<h2>📌 Features</h2>
<ul>
    <li>Upload or select WhatsApp chat files</li>
    <li>Interactive message and word statistics</li>
    <li>Monthly & daily timelines</li>
    <li>Most active users analysis</li>
    <li>Weekly activity heatmap</li>
    <li>Wordcloud of frequent words</li>
    <li>Emoji analysis and visualization</li>
</ul>

<hr>

<h2>🚀 How to Run Locally</h2>
<ol>
    <li>Clone the repository
        <pre>git clone https://github.com/pratiksutar841/Whatsapp-Chat-Analyzer.git</pre>
    </li>
    <li>Navigate to the project folder
        <pre>cd Whatsapp-Chat-Analyzer</pre>
    </li>
    <li>Install dependencies
        <pre>pip install -r requirements.txt</pre>
    </li>
    <li>Run the Streamlit app
        <pre>streamlit run app.py</pre>
    </li>
</ol>

<hr>

<h2>🙋‍♂️ Author</h2>
<p>
<b>Pratik Sutar</b><br>
B.Tech in Computer Science & Engineering (Data Science)<br>
GitHub: <a href="https://github.com/pratiksutar841">pratiksutar841</a><br>
LinkedIn: <a href="https://www.linkedin.com/in/pratik-sutar-/">Pratik Sutar</a>
</p>

</body>
</html>
