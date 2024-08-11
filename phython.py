import streamlit as st
import datetime
from datetime import date


st.title("Omar Abdullah Gill's Birthday")
birthday = datetime.date(2024, 8, 15)
today = date.today()
days_remaining = (birthday - today).days


if days_remaining > 0:
    st.subheader(f"Only {days_remaining} days left until Omar's Abdullah Gill's birthday!")
else:
    st.subheader("🎂 Happy Birthday Omar Abdullah Gill! 🎂")
    st.balloons()


if days_remaining == 0:
    st.markdown("""
    ## 🎉 Happy Birthday, Brother! 🎉
    - Wishing you a day filled with love, joy, and lots of cake!
    - You are the best brother anyone could ask for, and I’m so lucky to have you in my life.
    - Here's to many more birthdays together!
    - May Allah Success you in every step of your life.
    - Always Stay Happy.
    """)

if days_remaining == 0:
    st.snow()


st.markdown(" Regards: Usman Gill ❤️")



