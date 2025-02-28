#STREAMLIT
import streamlit as st

st.set_page_config( page_title="Growth Mindset", page_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges and achievements! 💎")

#quote section
st.header("💡 Today's Growth Mind Quote")
st.write("A growth mindset sees failure not as an obstacle, but as a stepping stone to success.""-Winston Churchill") 
st.header("🔨What's Your Challenge Today?")

user_input = st.text_input( "Describe a challenge you're facing")


#condition
if user_input:
    st.success( f"💪🏻 You're facing: {user_input}. Keep looking forward towards your goal! 🚀")
else:
    st.warning(" The challenge isn’t starting, it’s having the mindset to keep going.")

#reflection
st.header("🧠 Reflect on Your Learning")
reflection = st.text_area("write your reflections here!")

if reflection:
    st.success(f"🎉Great your insight! reflaction: {reflection} ")
else:
    st.info("Looking back helps you move forward—growth comes from reflection.")  


#success
st.header("🏆celebrate your wins ")
acheivment = st.text_input("Share something you've recently accomplished")


if acheivment:
    st.success(f"🎉 Amazing! you achieved: {acheivment}")
else: 
    st.info("Big or small, every achievement counts! Share one now! 🥰")

#footer

st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination⭐")
st.write("⊜ Created by daresh mohn")