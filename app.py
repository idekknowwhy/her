import streamlit as st
# Add custom CSS for background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #B88A86   ;  /* Pale Blue color */
    }
    </style>
    """, 
    unsafe_allow_html=True
)
def image_gallery():
    st.markdown(
         """
         <div class="content-box">
             <h1 style='color: #550000;'>Ashii's gallery </h1>
         </div>
         """,
         unsafe_allow_html=True
     )
    
    # Load and display images in multiple rows of 3 images each
    images = [
        "images/1.jpeg", "images/2.jpeg", "images/3.jpeg", 
        "images/4.jpeg", "images/5.jpeg", "images/6.jpeg", 
        "images/7.jpeg", "images/8.jpeg", "images/9.jpeg", 
        "images/10.jpeg", "images/11.jpeg", "images/12.jpeg", 
        "images/13.jpeg", "images/14.jpeg"
    ]
    
    # Loop through the images and display them 3 per row
    for i in range(0, len(images), 3):
        cols = st.columns(3)  # Create 3 columns per row
        for j in range(3):
            if i + j < len(images):
                cols[j].image(images[i + j],use_column_width=True)


def about_page():
    st.markdown("<h1 class='title'>About Us</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='background-color: white; padding: 20px; border-radius: 15px; box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3); max-width: 800px; margin: auto;'>
        <p style='font-size: 18px; color: #A24857; text-align: center;'>Ummmm about us? I saw you for the first time in bus.. didnt really think we would ever end up talking, you were in a completely different world... you seemed so bring and confident I was scared to talk to you. A year latter <strong>Hi</strong>..... We have been through a lot, misunderstandings, petty arguments, paranoia, overthinking... Darling? <strong>I love you</strong>, I wont lose you</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Image Gallery", "About"])

# Navigation logic
if page == "Image Gallery":
    image_gallery()
elif page == "About":
    about_page()