import Streamlit as st
from datetime import date

st.set_page_config(page_title="Celebrate Bonds 💖", layout="centered")

st.title("💝 Celebrate Special Bonds 💝")
st.write("Choose an occasion, a message, and make it personal with a photo!")

# Occasion selector
occasion = st.selectbox("🎉 Select the Occasion", ["Friendship Day", "Raksha Bandhan"])

# Name input
name = st.text_input("👤 Enter the name of your friend/sibling:")

# Pre-written message selector
if occasion == "Friendship Day":
    messages = [
        "You’re not just a friend, you're my chosen family! 🫂",
        "Through thick and thin, you've always been there.",
        "Friendship isn't about who you’ve known the longest — it’s who walked in and never left. 💕",
    ]
else:
    messages = [
        "No matter how far we are, you're always in my heart. 🧵",
        "You're my protector, guide, and best friend. Happy Raksha Bandhan! 🤗",
        "This Rakhi is a thread of love, protection, and endless memories. 💫",
    ]

selected_message = st.selectbox("💌 Choose a pre-written message:", messages)

# Custom message
custom_message = st.text_area("📝 Or write your own message (optional):")

# Image uploader
uploaded_image = st.file_uploader("📸 Upload a photo (optional)", type=["jpg", "jpeg", "png"])

# Generate greeting
if st.button("✨ Generate Greeting ✨"):
    if not name:
        st.warning("Please enter a name to continue.")
    else:
        st.success(f"🎊 Here's your {occasion} Greeting for {name}!")

        st.markdown(f"### 🎁 Dear {name},")

        # Use custom message if provided
        if custom_message.strip():
            st.markdown(f"**{custom_message}**")
        else:
            st.markdown(f"**{selected_message}**")

        if uploaded_image:
            st.image(uploaded_image, caption=f"Special memory with {name} 📸", use_column_width=True)

        st.markdown(f"🗓️ *Generated on:* `{date.today()}`")
        st.markdown("---")
        st.caption("Made with ❤️ by Atharva")

