import streamlit as st
from textblob import TextBlob

# App Title
st.set_page_config(page_title="AI Text Summarizer", page_icon="🤖")
st.title("🤖 Smart AI Text Summarizer & Sentiment Analyzer")
st.write("Built by **Ahmad Raza Jajja** for Hack-Nation Global AI Hackathon 2025 🌍")

# Input Text
text = st.text_area("📝 Paste or write your paragraph below:")

# Buttons
if st.button("✨ Summarize & Analyze"):
    if len(text.strip()) == 0:
        st.warning("Please enter some text first!")
    else:
        # Dummy summarization (you can replace with OpenAI API)
        summary = " ".join(text.split()[:max(1, len(text.split()) // 3)]) + "..."
        st.subheader("📄 Summary:")
        st.success(summary)

        # Sentiment Analysis using TextBlob
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        mood = "Positive 😊" if sentiment > 0 else "Negative 😔" if sentiment < 0 else "Neutral 😐"
        st.subheader("💬 Sentiment:")
        st.info(f"The overall mood is **{mood}**")

st.divider()
st.caption("⚡ Built in under an hour during Hack-Nation Global AI Hackathon by Ahmad Raza Jajja 🇵🇰")
