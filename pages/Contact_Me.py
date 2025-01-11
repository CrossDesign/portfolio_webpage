import streamlit as st
from email_functions import send_email, validEmail

st.header("Contact Me")



with st.form(enter_to_submit=False,key='email_form'):
    user_email = st.text_input("Your Email Address", max_chars=100, placeholder='email')
    subject = st.text_input("Subject", max_chars=100, placeholder='Optional')
    email_body = st.text_area("Your Message", max_chars=1000, placeholder='Services or inquiries')
    button = st.form_submit_button(label='Submit')
    if button:
        if validEmail(user_email) and len(email_body) > 5:
            send_email(sender=user_email,message=email_body,subject=subject)
            st.info("Your email has been sent!")
        else:
            st.info("Please make sure your email and message are correct.")
