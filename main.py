import streamlit as st
import pickle
import pandas as pd

def recommend(songs):
  song_index = sing[sing['song'] == songs].index[0]
  distance = cs[song_index]
  top_song = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

  recommended_song = []
  for i in top_song:
    recommended_song.append(sing.iloc[i[0]]['song'])
  return recommended_song

song_list = pickle.load(open('song.pkl','rb'))
sing = pd.DataFrame(song_list)
st.title('Song Recommend Model')
cs = pickle.load(open('cs.pkl','rb'))

song_name = st.selectbox(
    'Write Song Name',sing['song'].values
)
if st.button('Recommend'):
    recomendations = recommend(song_name)
    for i in recomendations:
        st.write(i)

git add .
git commit -m
  git push


