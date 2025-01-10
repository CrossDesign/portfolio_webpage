""" Main File """

import streamlit as st
import pandas
from PIL import Image, ImageOps


st.set_page_config("Cross Design - Projects",page_icon="assets/cross_design_icon.jpg",layout='wide')
col1, col2 = st.columns([1,1.5])

with col1:
    profilePicture = Image.open("images/profile_picture.jpg") # PIL is needed to do any Image redering changes
    profilePicture = ImageOps.exif_transpose(profilePicture) # PIL can read the orientation of the photo using exif_transpose

    st.image(profilePicture,"Photo of Thomas Cross hiking with a vista of rolling foothills.",width=350)

with col2:
    st.header("Thomas Cross")
    aboutMeText = """
This is a secttion that is all about me. I am the best in the world and this is the brief summary of how I'm the most interesting person in the whold entire world.
"""
    st.text(aboutMeText)


st.header("Project History")
projectsDescriptionText = """
    Over the year, several projects from automation to web development have 
    made Thomas Cross an expert in many fields of computer science.
    """
st.text(projectsDescriptionText)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5],gap='medium', 
                                   vertical_alignment='center')
df = pandas.read_csv("data/portfolio_data.csv", sep=",")


with col3:
    for index, row in df[:3].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'],width=260)
        st.write(f"[Source Code]({row['url']})")
        
with col4:
    for indes,row in df[3:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'],width=260)
        st.write(f"[Source Code]({row['url']})")


if __name__ == "__main__":
    print("main.py is running")
