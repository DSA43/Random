import streamlit as st
import random
from PIL import Image
import time

# Title with emojis
st.title("💖 Random SEX Position Picker 👉👌🍑OO")
st.write("Dare to do this in online vc or offline with Boyfriend Isu")

# ✅ Corrected CSS embedding for snowfall effect
st.markdown(
    """
    <style>
    @keyframes fall {
        0% { transform: translateY(-10vh); opacity: 1; }
        100% { transform: translateY(100vh); opacity: 0; }
    }

    .snowflake {
        position: fixed;
        top: -10vh;
        font-size: 24px;
        user-select: none;
        pointer-events: none;
        animation-name: fall;
        animation-timing-function: linear;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ Generating falling emoji elements dynamically
emoji_list = ['💖','💋','😘',
    "🍆",  # Eggplant
    "🍑",  # Peach
    "👉",  # Pointed Finger
    "👌",  # Okay Hand
    "👅",  # Tongue
    "💦",  # Sweat Droplets
    "😈",  # Smiling Devil
    "🙈",  # Hiding Monkey Face
    "😉",  # Wink Face
    "🤤"  # Drooling Face
    # "Boobs",
    # "Dhudho",
    # "Lund",
    # "Chut",
    # "Gand",
    # "Chuchi",
    # "penis",
    # "navel",
    # "fuck you",
    # "chudimi",
    # "boobs squeezing",
    # "pussy eating"

]
num_emojis = 50  # Number of falling emojis

falling_emojis = ""
for i in range(num_emojis):
    emoji = random.choice(emoji_list)
    left_position = random.randint(0, 100)  # Random horizontal position
    duration = random.uniform(3, 6)  # Random fall speed

    falling_emojis += f"""
    <div class="snowflake" style="
        left: {left_position}vw;
        animation-duration: {duration}s;
        animation-delay: {random.uniform(0, 5)}s;
        position: fixed;
    ">{emoji}</div>
    """

st.markdown(falling_emojis, unsafe_allow_html=True)
videos = {
    "Video 1": "boobbouncing.mp4",  # Replace with actual file paths
    "Video 2": "boobpressing.mp4"
}

# List of offline positions with image paths and descriptions
offline_positions = [
    {"name": "Missionary", "image": "missionary.jpg", "description": "A classic face-to-face position allowing deep connection."},
    {"name": "Cowgirl", "image": "cowgirl.jpg", "description": "One partner sits while the other is on top, allowing control."},
    {"name": "Doggy Style", "image": "doggy_style.jpg", "description": "A position offering deeper intimacy from behind."},
    {"name": "Spooning", "image": "spooning.jpg", "description": "A comfortable side-lying position great for relaxation."},
    {"name": "Facesitting", "image": "Facesitting.jpg", "description": "A deeply intimate position with both partners sitting closely."},
    {"name": "fingering", "image": "fingering.jpg", "description": "A deeply intimate position with both partners sitting closely."},
    {"name": "HeadRush", "image": "HeadRush.jpg", "description": "A deeply intimate position with both partners sitting closely."},
    {"name": "Standing", "image": "Standing.jpg", "description": "  A position that requires flexibility and strength."},
    {"name": "Butt Doggy Style", "image": "bouncingbuttdoggystyle.jpg", "description": "A position offering deeper intimacy from behind."},
    {"name": "Backshots", "image": "Backshots.jpg", "description": "A position offering deeper intimacy from behind."},
    {"name": "BedFucking", "image": "Bedfucking.jpg", "description": "A position offering deeper intimacy from behind."},
    {"name": "onfucking", "image": "onfucking.jpg", "description": "A position offering deeper intimacy from behind."},
    {"name": "tablefucking", "image": "tablefucking.jpg", "description": "A position offering deeper intimacy from behind."},
    {"name": "lAPSITTING", "image": "Lapsitting.jpg", "description": "."},
    {"name": "Behindfuck", "image": "behindfuck.jpg", "description": "."},
    {"name": "Pussy Rubbing", "image": "pussyrubb.jpg", "description": "."},
    {"name": "Sitting Fuck", "image": "sitting.jpg", "description": "."},
    {"name": "Pussy sitting eat", "image": "sittingeat.jpg", "description": "."}

]

# List of online positions with image URLs
online_positions = [
    {"name": "Opening Bra and cloth while sitting", "image": "openingshirt.jpg", "description": "A classic face-to-face position allowing deep connection."},
    {"name": "While sitting Boobs bouncing", "image": "boobs.jpg", "description": ""},
    {"name": "While sitting sucking boobs", "image": "boobs.jpg", "description": "."},
    {"name": "Rubbing hands on panties while standing", "image": "rubinpant.jpg", "description": "."},
    {"name": "Leaning and bounching boobs", "image": "bend.jpg", "description": "."},
    {"name": "hand up after opeing bra and top", "image": "standing.jpg", "description": "."},
    {"name": "Bouncing boobs", "image": "boobs.jpg", "description": "."},
    {"name": "Legs showing", "image": "boobs.jpg", "description": "."},
    {"name": "Boobs pressing hard", "image": "boobs.jpg", "description": "."},
    {"name": "Boobs exploring", "image": "boobs.jpg", "description": "."},
    {"name": "Naked standing", "image": "naked.jpg", "description": "."},
    {"name": "Blow job", "image": "blowjob.jpg", "description": "."},
    {"name": "sitting and holding boobs", "image": "boobhold.jpg", "description": "."},
    {"name": "Moaning", "image": "moaning.jpg", "description": "."},
    {"name": "DARE:Boob Showing Now","description":"right now show your boobs"},
    {"name": "DARE:Penis Showing Now","description":"right now show your Penis"},
    {"name": "DARE:Bra showing","description":"right now show your bra"}
    # {"name": "DARE:","description":"right now show your boobs"},
    
    
]

# Select between online or offline positions
option = st.radio("Choose a mode:", ("Offline", "Online"))

# Button to pick a random position
if st.button("👉👌🍑 Pick a Position"):
    placeholder = st.empty()
    st.markdown(falling_emojis, unsafe_allow_html=True)
    
    # Rolling dice animation effect
    for i in range(3):
        placeholder.subheader(f"🎲 Rolling the dice{'.' * (i+1)}")
        time.sleep(0.5)
    
    placeholder.empty()  # Clear the rolling text
    
    if option == "Offline":
        selected = random.choice(offline_positions)
    else:
        selected = random.choice(online_positions)
    
    st.subheader(f"✨ Selected Position: {selected['name']} ✨")
    st.write(selected["description"])
    
    # Display the image
    try:
        if option == "Offline":
            image = Image.open(selected["image"])
            st.image(image, caption=selected["name"], use_container_width=True)
        else:
            st.image(selected["image"], caption=selected["name"], use_container_width=True)
    except FileNotFoundError:
        st.error("Image not found. Please check the file path.")

import streamlit as st

# Footer with resources
st.markdown("---")

# Made By Section
made_by = st.markdown("### ❤️ Made with Love by **Rawsi or baby or chua or isu** ❤️")  

# Why Made Section
why_made = st.markdown("🌟 *Because some things are worth creating, just like this...* 🌟")  

# Space for writing a paragraph for another person
st.markdown("---")
message_for_someone = st.markdown(
    "💖 **For Someone Special** 💖  \n"
    "_Some words are unspoken, some feelings are unseen,_  \n"
    "_But this little creation is a piece of my heart on the screen._ 💕 \n"
    "I always love your soul and body and I always will.  \n"       
    "I love you more than anything in this world.  \n"
    "Your body is a wonderland and I want to explore it more and more. \n"
    "I want to make you feel special and loved. \n"

    "Ok lets get naughty and have some fun👅.  \n"
    "Lets have some sex and love my baby.  \n"
    "Yours boobies are so gorgeous and I want to explore them more.  \n"
)

st.markdown("---")
st.title("💖WARNING:- ONLY IF YOU ARE COMFORTABLE THEN PROCEED TO VIDEO BECAUSE I RESPECT YOU AND LOVE YOU 💖.")
st.write("All are these for fun only between you and me and i love you gorgeous no one is sexy than you")

videos = {
    "Video 1": "boobpressing.mp4", 
    "Video 2":"boobbouncing.mp4",
    "Video 3":"rub.mp4",
    "Video 4":"standing.mp4",
    "Video 5":"fi.mp4",
    "Video 6":".mp4",
    "Video 7":".mp4",
    "Video 8":".mp4"

     # Replace with actual file paths
}
selected_video = st.selectbox("Choose a video to play:", list(videos.keys()))

# Display authorization message
st.warning("This video is Not authorized to view. Do you want to proceed?")

# Ask user if they want to proceed
play_video = st.radio("Do you want to watch Boobpressing video?", ("No", "Yes"))

# Display the selected video only if user agrees
if play_video == "Yes":
    st.video(videos[selected_video])
else:
    st.write("You are not authorized to view the video.")
