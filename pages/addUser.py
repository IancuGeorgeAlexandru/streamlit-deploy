import streamlit as st  
import yaml

if st.session_state['authentication_status'] == True and st.session_state['username']=="georgei":
            try:
                authenticator = st.session_state['authenticator']
                username = st.session_state['username']
                config = st.session_state['config']
                if authenticator.register_user(pre_authorization=False, clear_on_submit = True, location = 'main'):
                    with open('config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
                    st.success('User registered successfully')

            except Exception as e:
                st.error(e)