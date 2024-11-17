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
import Login

#file location to run with stream lit
#streamlit run c:\Users\amari\Downloads\songet.py

app = Flask(__name__)
app.secret_key = "15s5156a1-354f-2384-g365-2a5248621475"

import streamlit as st

if st.button('Spotify Login'):
    st.write('Generating Your Vibe')
    login_script_path = Path(r"C:\\Users\\amari\Downloads\\Login.py")
    if login_script_path.exists():
        subprocess.run(["python", str(login_script_path)])
        
    for uri in Login.playlists_uri_arr:
        st.write(uri)
        
#if st.button('Show Playlists'):


    
  


