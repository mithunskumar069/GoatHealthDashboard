import streamlit as st

import json

st.set_page_config(page_title="Goat Health IoT & ML", layout="wide")

# Custom Style
custom_css = """
<style>
body {
    font-family: 'Poppins', sans-serif;
}
.big-title {
    font-size: 40px;
    font-weight: 700;
    background: -webkit-linear-gradient(45deg, #6a11cb, #2575fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #0f172a;
    color: white;
    box-shadow: 0px 4px 12px rgba(255,255,255,0.1);
    transition: 0.3s;
}
.card:hover {
    transform: scale(1.02);
}
.gradient-text {
    font-size: 22px;
    background: linear-gradient(90deg, #FF8A00, #E52E71);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar Navigation
page = st.sidebar.radio("📌 Navigation", ["Home","Architecture","Prediction Demo","Results","Future Scope"])

# Lottie Loader Function
def load_lottie(path):
    with open(path, "r") as f:
        return json.load(f)

# ------------------ HOME ------------------
if page == "Home":
    st.markdown("<h1 class='big-title'>🐐 IoT + ML Goat Health Monitoring</h1>", unsafe_allow_html=True)
    st.write("### Smart Agriculture • Intelligent Livestock • Real-time Analytics")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.write("""
        ### 📌 Project Summary  
        A smart necklace system powered by IoT sensors and ML to detect goat health conditions, 
        alert breeders, and visualize real-time vitals with predictive insight.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.write("""
        ### 🎯 Objectives
        - Real-time monitoring  
        - Predict illness early  
        - Cloud based visualization  
        - Alerts for anomalies  
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("---")
    st.write("## ✨ Dashboard Preview")
    st.write("🎥 Your app screens will showcase live data, ML logic and interactive demo!")

# ---------------- ARCHITECTURE --------------
elif page == "Architecture":
    st.markdown("<h1 class='big-title'>📌 System Architecture</h1>", unsafe_allow_html=True)

    st.write("### 🧠 IoT → Bluetooth → Cloud → ML Prediction")
    
    st.success("This architecture ensures remote analysis + automatic alerts!")

# ---------------- PREDICTION DEMO --------------
elif page == "Prediction Demo":
    st.markdown("<h1 class='big-title'>🩺 Live Health Prediction</h1>", unsafe_allow_html=True)

    with st.expander("📌 Enter Goat Vital Stats"):
        temp = st.number_input("🌡 Temperature (°C)", 36.0, 42.0, 39.0)
        hr = st.number_input("❤️ Heart Rate (beats/min)", 50, 120, 80)
        rr = st.number_input("💨 Respiratory Rate (breaths/min)", 8, 30, 15)
        weight = st.number_input("⚖ Estimated Weight (kg)", 5, 150, 40)

    if st.button("🔮 Predict Health Condition", use_container_width=True):
        condition = "Healthy ✔"

        if temp > 40 or hr > 100 or rr > 20:
            condition = "⚠️ ALERT: Possible Illness / Stress ❗"

        st.metric("Prediction Result", condition)

# ---------------- RESULTS --------------
elif page == "Results":
    st.markdown("<h1 class='big-title'>📊 Results & Insights</h1>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("""
    ✔ Smart device successfully tracked vitals  
    ✔ Alerts enabled proactive medicine  
    ✔ Weight estimation helped growth monitoring  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    

# ---------------- FUTURE SCOPE --------------
elif page == "Future Scope":
    st.markdown("<h1 class='big-title'>🚀 Future Enhancements</h1>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("""
    🔷 AI-based disease prediction  
    🔷 GPS herd tracking  
    🔷 Mobile alerts + dashboard app  
    🔷 Automated medicine planner  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

