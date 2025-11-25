import streamlit as st
import requests
import subprocess

st.title(":rainbow[APP/GAME PRODUCTION WEB APPLICATION]")

prompt = st.text_area("Please enter the prompt to create a APP/Game", placeholder = "Describe your App/Game")

url = "https://sagardesktopn8n.app.n8n.cloud/webhook-test/00fd01b4-943a-47c0-a295-db9996f7ef68"

if st.button("Generate APP"):
    if prompt :
        response = requests.post(url = url, json = {"prompt" : prompt})

        if response.status_code == 200:
            st.write("success")

            with open("app_code.py","w") as file :
                file.write(response.json()[0]["output"].strip("```python"))
                
            subprocess.run(["python","app_code.py"])
            
        else :
            st.write(f"ERROR : {response.status_code}")

