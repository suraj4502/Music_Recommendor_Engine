import streamlit as st
import pandas as pd
import numpy as np



class Spotify_Recommendation():
    def __init__(self, dataset):
        self.dataset = dataset
    def recommend(self, songs, amount=1):
        distance = []
        song = self.dataset[(self.dataset.name.str.lower() == songs.lower())].head(1).values[0]
        dataset_without_the_song = self.dataset[self.dataset.name.str.lower() != songs.lower()]
        for i in (dataset_without_the_song.values):
            d = 0
            for col in np.arange(len(dataset_without_the_song.columns)):
                if not col in [1, 6, 12, 14, 18]:
                    d = d + np.absolute(float(song[col]) - float(i[col]))
            distance.append(d)
        # dataset_without_the_song['distance'] = distance
        dataset_without_the_song.loc[:, ('distance')] = distance
        dataset_without_the_song = dataset_without_the_song.sort_values('distance')
        columns = ['artists', 'name']
        return dataset_without_the_song[columns][:amount]
        


data = pd.read_csv('Data/finaldata.csv')
recommendations = Spotify_Recommendation(data)


st.set_page_config(page_title="A Sk_Y product", page_icon="🎼", layout="centered")

# st.markdown(
#     f"""
#     <style>
#          .stApp {{
#              background-image: url("https://burst.shopifycdn.com/photos/black-and-white-black-headphones.jpg?width=925&format=pjpg&exif=1&iptc=1");
             
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )

st.markdown(
    f"""
    <style>
         .stApp {{
             background-image: url("https://burst.shopifycdn.com/photos/headphones-in-an-orange-glow.jpg?width=925&format=pjpg&exif=1&iptc=1");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )



st.title("Music Recommendor Engine 🎶")

st.markdown('---')

col1, col2 = st.columns([2,1])
with col1:
    input_song=st.text_input("Enter a Song you like.")
with col2:
    no_of_values = st.number_input("Enter count of output values.",value=10,min_value=1,max_value=20)




col1, col2,col3= st.columns([1.5,2,1])
with col1:
    pass
with col2:
    button = st.button(label="Click to get similar songs.")
with col3:
    pass

if button:
    try:
        output=recommendations.recommend(input_song, no_of_values)
        output = pd.DataFrame(output)
        output = output.reset_index(drop=True)
        st.dataframe(output[['name','artists']],use_container_width=True)
        # st.table(output[['name','artists']])
    except:
        st.info('No data is availabe for the song You entered in our database, Please try with a different song.')



