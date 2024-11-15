from flask import Flask, redirect, request, session,  url_for
import random
import string
from pathlib import Path
import urllib.parse
import os
import sys
import spotipy
import configparser
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from spotipy.cache_handler import FlaskSessionCacheHandler
import df_from_sp as dfsp
import streamlit as st
import spotipy.util as util
import pandas as pd
import subprocess
import kn as kn

#file location to run with stream lit
#streamlit run c:\Users\amari\Downloads\songet.py

app = Flask(__name__)
app.secret_key = "15s5156a1-354f-2384-g365-2a5248621475"
'''
CLIENT_ID = "4a92811c8a5c418fbbe3a7ecd99d1632" # Amaris id
CLIENT_SECRET = "02573e96f63449feafc886f8f89d4236" # Amaris Secret
REDIRECT_URI = "http://localhost:5000/callback"
SCOPE = 'user-library-read user-read-email'
cache_handler = FlaskSessionCacheHandler(session)


sp_oauth = SpotifyOAuth(
  client_id = CLIENT_ID,
  client_secret=CLIENT_SECRET,
  redirect_uri=REDIRECT_URI,
  scope=SCOPE,
  cache_handler=cache_handler,
  show_dialog=True
)
sp_au = Spotify(auth_manager=sp_oauth)'''

# Initialize session state
if 'button' not in st.session_state:
    st.session_state.button = False

# Define the click function
def click_button():
    st.session_state.button = not st.session_state.button
    # Run Login.py as a subprocess
    login_script_path = Path(r"C:\\Users\\amari\Downloads\\Login.py")
    if login_script_path.exists():
        subprocess.run(["python", str(login_script_path)])

# Streamlit button
st.button('Spotify Login', on_click=click_button)

# Conditional content based on button state
if st.session_state.button:
    st.write('Button is on!')
else:
    st.write('Button is off!')
  
 