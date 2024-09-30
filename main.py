import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

# Hash password and store in YAML file. Only once!
# hashed_pwd = stauth.Hasher(['12345']).generate()
# st.write(hashed_pwd)

# Open YAML file
with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create auth object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Render login widget
name, authentication_status, username = authenticator.login(location='main')

# Authenticate users
if st.session_state['authentication_status']:
    authenticator.logout("Logout", 'main', key='unique_key')
    st.write(f'Welcome {st.session_state["name"]}')
    st.title("Some content")
elif st.session_state['authentication_status'] is False:
    st.error("Username/password is incorrect")
elif st.session_state['authentication_status'] is None:
    st.warning("Please enter your username and password")
