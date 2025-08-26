import streamlit as st
import pickle

# Load your saved pipeline (vectorizer + model)
with open("spam.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📧 Spam Message Classifier")
st.write("Enter a message below and find out if it's spam or not!")

# User input
message = st.text_area("Type your message here:")

if st.button("Predict"):
    if message.strip() == "":
        st.warning("⚠️ Please enter a message first.")
    else:
        # Predict using the pipeline
        prediction = model.predict([message])[0]

        if prediction == 1:  # assuming 1 = spam, 0 = not spam
            st.error("🚨 This message is **SPAM**!")
        else:
            st.success("✅ This message is **NOT SPAM**.")
