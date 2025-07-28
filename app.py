import streamlit as st
from emotion_utils import predict_emotion
from spotify_utils import get_recommendations

st.set_page_config(page_title="Moodify", page_icon="🎧")
st.title("🎵 Moodify: A Mood Ring 4 Your Ears 🎵")

user_mood = st.text_area("How are you feeling?", height=150)

if user_mood:
    with st.spinner("Analyzing your emotion..."):
        emotion = predict_emotion(user_mood)
        st.success(f"Detected emotion: {emotion}")
        tracks = get_recommendations(emotion)
        if tracks:
            if len(tracks) == 1:
                st.subheader("Your Playlist ▶️")
            else:
                st.subheader("Your Playlists ▶️")
            #for item in tracks:
             #   st.markdown(item)
              #  st.markdown(type(item))
            for name, description, _, url in tracks:
                st.markdown(f"- *Title*: **{name}**", unsafe_allow_html=True)
                st.markdown(f"*Artist*: {description}", unsafe_allow_html=True)
                st.markdown(f"*URL*: {url}", unsafe_allow_html=True)
        else:
            st.warning("No tracks found. Try again with a different mood!")