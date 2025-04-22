import re
import streamlit as st
import random
import time

def main():
    st.set_page_config(page_title="Password Strength Metre", layout="centered")
    
    st.markdown(
        """
        <style>
            .main-title { text-align: center; font-size: 36px; font-weight: bold; color: #4CAF50; }
            .d { font-size: 18px; color: #FF5733; }
            .result { font-size: 20px; font-weight: bold; }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<h1 class='main-title'>🔒 Password Strength Meter</h1>", unsafe_allow_html=True)
    
    with st.container():
        password = st.text_input("Enter your password:", type="password")
        submit = st.button("Check Strength", key="button")
    
    if submit:
        with st.spinner("Analyzing password..."):
            time.sleep(0.8)  # Simulating delay for user experience
        score = check_password_strength(password)
        show_progress_bar(score)
        if score < 4:
            st.session_state.suggested_password = suggest_password(password)
        # st.button("Check New Password",key='refresh_button',on_click=st.rerun)


    if "suggested_password" in st.session_state:
        st.subheader("🔑 Suggested Password:")
        st.code(st.session_state.suggested_password, language='plaintext')

def suggest_password(password=""):
    lower_chars = "abcdefghijklmnopqrstuvwxyz"
    upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_chars = "!@#$%^&*(_+=-)"
    number_chars = "0123456789"
    
    if not re.search(r'[a-z]', password):
        password += random.choice(lower_chars)
    if not re.search(r'[A-Z]', password):
        password += random.choice(upper_chars)
    if not re.search(r'\d', password):
        password += random.choice(number_chars)
    if not re.search(r'[!@#$%^&*]', password):
        password += random.choice(special_chars)
    
    while len(password) < 8:
        password += random.choice(lower_chars + upper_chars + special_chars + number_chars)
    
    return password

def check_password_strength(password):
    score = 0
    feedback = ""
    
    if password:
        if len(password) >= 8:
            score += 1
        else:
            feedback += "❌ Password should be at least 8 characters long.\n"
        
        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
        else:
            feedback += "❌ Include both uppercase and lowercase letters.\n"
        
        if re.search(r"\d", password):
            score += 1
        else:
            feedback += "❌ Add at least one number (0-9).\n"
        
        if re.search(r"[!@#$%^&*()]", password):
            score += 1
        else:
            feedback += "❌ Include at least one special character (!@#$%^&*).\n"
        
        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the d below.")
            st.markdown(f"<p ><span class='suggestions'>{feedback.replace('.','\n')}</span></p>", unsafe_allow_html=True)
    else:
        st.error("❌ No password entered.")
    
    return score

def show_progress_bar(score):
    st.markdown("### Password Strength")
    progress = st.progress(0)
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    progress.progress(score / 4)  # Normalizing to 0-1 range
    st.write(f"🔵 {strength_levels[score]}")



if __name__ == "__main__":
    main()