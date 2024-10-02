import streamlit as st  
import yaml

if st.session_state['authentication_status'] == True:
            try:
                authenticator = st.session_state['authenticator']
                username = st.session_state['username']
                config = st.session_state['config']
                if authenticator.reset_password(username, location = 'main', clear_on_submit = True):
                    st.success('Password modified successfully')
                    with open('config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
                        # st.write(file.name)
            except Exception as e:
                st.error(e)