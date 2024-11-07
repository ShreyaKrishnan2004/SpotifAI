from flask import Flask, redirect, request, session,  url_for
import random
import string
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

app = Flask(__name__) 
app.secret_key = "15s5156a1-354f-2384-g365-2a5248621475"

client_id = '8dafe80271644fcdaf587c49f2b1069f'
client_secret = '43a89c7655bd45b7afca764f348efd3e'
redirect_uri = 'http://localhost:5000/callback' 
scope = 'playlist-read-private'

cache_handler = FlaskSessionCacheHandler(session)

sp_oauth = SpotifyOAuth(
  client_id = client_id,
  client_secret=client_secret,
  redirect_uri=redirect_uri,
  scope=scope,
  cache_handler=cache_handler,
  show_dialog=True
)
sp_au = Spotify(auth_manager=sp_oauth)



@app.route('/')
def home():
  if not sp_oauth.validate_token(cache_handler.get_cached_token()):
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url) # login to spotify
  return redirect(url_for('input_playlist'))

@app.route('/callback')
def callback():
  sp_oauth.get_access_token(request.args['code'])
  return redirect ( url_for('get_playlists'))


#@app.route('/get_playlists')
def get_playlists():
  if not sp_oauth.validate_token(cache_handler.get_cached_token()):
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)
  
  playlists = sp_au.current_user_playlists()
  
  #names with uris
  playlists_info = [(pl['name'], pl['external_urls']['spotify']) for pl in playlists['items']]
  
  #just uris
  playlists_uri = [(pl['external_urls']['spotify']) for pl in playlists['items']]
  #playlists_html = '<br>'.join([f'{name}:{url}' for name, url in playlists_info])
  return playlists_info


if __name__ =='__main__':
  app.run(debug=False)