import streamlit as st
import re

# Title and Description
st.title("Phishing Detection System")
st.write("🚨 **Analyze phishing factors from email content**")

# Input Fields
email_content = st.text_area("📧 Enter Email Content", height=200)
sender_email = st.text_input("✉️ Enter Sender's Email")

# Phishing Factors Functions
def extract_f_index(email_content):
    # Example: Extracting URL count as a phishing factor
    urls = re.findall(r'(https?://\S+)', email_content)
    return len(urls)

def extract_spam_words(email_content):
    # Example: Counting suspicious words
    spam_words = ['win', 'free', 'prize', 'urgent', 'limited']
    count = sum(1 for word in spam_words if word in email_content.lower())
    return count

def extract_email_length(email_content):
    # Example: Length of the email
    return len(email_content)

def extract_sender_reputation(sender_email):
    # Placeholder for reputation check
    if sender_email.endswith("@trusted.com"):
        return 1  # Good reputation
    else:
        return 0  # Bad reputation

# Analyze Button
if st.button("🔍 Analyze"):
    if email_content and sender_email:
        f_index = extract_f_index(email_content)
        spam_count = extract_spam_words(email_content)
        email_length = extract_email_length(email_content)
        reputation = extract_sender_reputation(sender_email)
        
        # Results
        st.subheader("📊 Phishing Factors")
        st.write(f"1. **F-Index (URL Count):** {f_index}")
        st.write(f"2. **Spam Words Count:** {spam_count}")
        st.write(f"3. **Email Length:** {email_length} characters")
        st.write(f"4. **Sender Reputation:** {'✅ Good' if reputation == 1 else '⚠️ Bad'}")
    else:
        st.warning("Please enter both **Email Content** and **Sender's Email**.")