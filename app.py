import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genz
from youtube_transcript_api import YouTubeTranscriptApi


load_dotenv()

genz.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = ''' you are a yt video summarizer. i will upload youtube video link and you will access the link and summarize the content of video for me giving important summary in brief with around 300 words. Please provide the summary of video here:   '''


def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]

        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript
    
    except Exception as e:
        raise e
    

def generate_gemini_content(transcript_text,prompt):
    model = genz.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt+transcript_text)
    return response.text

st.title("Youtube Transcript to detailed Notes Converter")
yt_link = st.text_input("Enter your youtube video link : ")


if yt_link :
    video_id = yt_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)


if st.button("Get Detailed Notes"):
    transcript_text= extract_transcript_details(yt_link)


    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)








