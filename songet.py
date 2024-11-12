from flask import Flask, redirect, request, session,  url_for
import random
import string
import time
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

CLIENT_ID = "8dafe80271644fcdaf587c49f2b1069f" # Amaris id
CLIENT_SECRET = "43a89c7655bd45b7afca764f348efd3e" # Amaris Secret
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
sp_au = Spotify(auth_manager=sp_oauth)


if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Spotify Login', on_click=click_button)

if st.session_state.clicked:
  st.write('Button clicked!')
  with open(r"C:\\Users\\amari\Downloads\\Login.py") as file:
    exec(file.read())
    
    

    
  
  #http://127.0.0.1:5000
  
  #st.slider('Select a value')


'''my_expander = st.expander()
#my_expander.write('See Playlists')
clicked = my_expander.button('See Playlists')'''


  
 