from pywebcopy import save_webpage

url = 'http://localhost:8501'  # The URL where your Streamlit app is hosted
download_folder = 'F:/snapbox/demo'  # The folder where you want to save the HTML file

save_webpage(url, download_folder)