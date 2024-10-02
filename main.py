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

    st.session_state['config'] = config
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
    st.header(f'Welcome {st.session_state["name"]}')
    
    st.session_state['authenticator'] = authenticator

    if authentication_status == True and username=="georgei":
            try:
                if authenticator.register_user(pre_authorization=False):
                    with open('config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
                    st.success('User registered successfully')

            except Exception as e:
                st.error(e)
        
elif st.session_state['authentication_status'] is False:
    st.error("Username/password is incorrect")
elif st.session_state['authentication_status'] is None:
    st.warning("Please enter your username and password")
