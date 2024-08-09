import streamlit
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




