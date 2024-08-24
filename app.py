import streamlit as st
import yt_dlp
import io

# Naslov aplikacije
st.title("Preuzimanje videozapisa sa YouTube-a")

# Unos URL-a videozapisa
url = st.text_input("Unesite URL videozapisa sa YouTube-a:")

if url:
    try:
        # Preuzimanje videozapisa
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': 'temp_video.mp4',
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
        
        # Učitaj video u memoriju za prikaz i preuzimanje
        with open('temp_video.mp4', 'rb') as video_file:
            video_data = video_file.read()

        # Prikaz videozapisa u aplikaciji
        st.video(video_data)

        # Dugme za preuzimanje videozapisa
        st.download_button(
            label="Preuzmi videozapis",
            data=video_data,
            file_name="video.mp4",
            mime="video/mp4"
        )
        
    except Exception as e:
        st.error(f"Došlo je do greške: {e}")
