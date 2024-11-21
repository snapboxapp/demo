import streamlit as st
from PIL import Image

# Hide Streamlit’s menu and set the app to fullscreen
st.markdown(
    """
    <style>
    /* Make app fullscreen */
    /* Optional: Set the Streamlit container background */
    .css-18e3th9 {
        padding-top: 1rem;
    }
    .css-1d391kg {
        padding-top: 0rem;
    }
    /* Hide the top Streamlit header */
    .css-1adrfps {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the logo at the top
logo = Image.open("logo.png")
st.image(logo, use_container_width=False, width=300)
st.subheader("Automate photo sharing, sorting, and filtering")

# Display a brief app description
st.write("Snapbox is a cross-platform cloud photo storage solution that helps you effortlessly organize, manage, and share your photos using advanced automation features.")

# Load and display images in one row using Streamlit columns
images = [("1.png", "Backup photos to the cloud securely. Access them from anywhere."), ("2.png", "Inbox/Outbox makes sharing photos convenient, while ensuring you stay in control."), ("3.png", "Get notified when we detect your friends in images. Share photos in a tap.") ]
col1, col2, col3 = st.columns((2, 2, 3))
for i, (image, text) in enumerate(images):
    with locals()[f"col{i+1}"]:
        st.image(Image.open(image), use_container_width=True)
        st.write(text)


# Add placeholders for sorting, sharing, and filtering options (future features)
st.write("### Planned Features")
st.write("- **Automated Photo Sharing**")
st.write("Using facial recognition, we automatically detect your friends in photos and suggest sharing with the right people—all with just one tap.")
st.write("- **Smarter Photo Library**")
st.write("Photos are organized intelligently: similar images are grouped, events are automatically created, and unwanted photos like screenshots are hidden.")
st.write("- **AI Photo Scoring**")
st.write("No more scrolling through hundreds of similar photos. We'll pick the ones that make you look your best for easy sharing on Instagram or other platforms.")
st.write("- **Purge Junk Photos**")
st.write("Automatically identify and delete clutter from your library, including screenshots, documents, saved TikToks, blurry photos, duplicates, and more.")
st.write("- **Shared Albums**")
st.write("Create albums with friends and family and let us suggest photos to add based on who’s in them, making album creation effortless.")
st.write("- **Find The Moments You Care About**")
st.write("Smart search helps you find photos by location, date, people, and objects. Photos are automatically tagged with mood, holidays, vacations, events, and more.")
st.write("- **Relive Your Memories**")
st.write("We'll automatically create customizable photo stories, slideshows, and collages for you to share with friends and family.")
st.write("- **Secure Cloud Backup**")
st.write("Your photos are securely backed up to the cloud, so you never have to worry about losing them. Access them from anywhere, anytime, on any device.")



# Run with `streamlit run app.py`