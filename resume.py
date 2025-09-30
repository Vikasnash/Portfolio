import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import random


# Pastel color palette
pastel_colors = [
    "#fbb4ae", "#b3cde3", "#ccebc5", "#decbe4",
    "#fed9a6", "#ffffcc", "#e5d8bd", "#fddaec", "#f2f2f2"
]


def pastel_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return random.choice(pastel_colors)

# Page config
st.set_page_config(page_title="Vikas Resume", layout="centered", initial_sidebar_state="expanded")

# WordCloud
text = """Data Data Science Data Analytics Python Python Machine Learning AML CFT Econometrics Model Risk Management Risk Statistical Modelling Time Series Fraud Detection Data Visualization Data Engineering Exploratory Data Analysis Financial Crime Compliance FCC Limited Dependent Variable Analysis Hypothesis Testing Sampling Data Science Python Econometrics Machine Learning AI Python Risk Modeling Compliance Analytics Python SAS Analytics Data Modeling Machine Learning Compliance Fraud Detection Forecasting Time Series Statistical Visualization Tableau Automation Risk Project Management Teamwork Econometrics Regulatory"""

wc = WordCloud(
    width=800, height=600, max_font_size=80, min_font_size=10,background_color=None, mode="RGBA",
    color_func=pastel_color_func, prefer_horizontal=1.0, random_state=42
).generate(text)

buffer = BytesIO()
wc.to_image().save(buffer, format="PNG")
encoded_wc = base64.b64encode(buffer.getvalue()).decode()

# Custom CSS
st.markdown(f"""
<style>
/* Sidebar & Toolbar Dark */
[data-testid="stSidebar"] {{
    background-color: #1c1c1c;
    color: #f1f1f1;
}}
[data-testid="stToolbar"] {{
    background-color: #1c1c1c;
}}

/* Main app background */
.stApp {{
    background-color: #f5f5f5;
    background-image: url("data:image/png;base64,{encoded_wc}");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}}

/* Main content cards */
.block-container {{
    background: rgba(255, 250, 245, 0.85); /* Offwhite with opacity */
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}}

/* Headers & text */
h1, h2, h3, h4, h5, h6, p, li {{
    color: #0D1B2A; /* Dark blue */
    font-family: 'Segoe UI', sans-serif;
}}

/* Progress bars */
.stProgress .st-bo {{
    height: 10px;
    border-radius: 15px;
    background-color: #1f77b4; /* Blue progress bars */
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);}}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style="text-align: center;">
    <h1>Vikas Dharam Pal, CAMS</h1>
    <p><b>8+ Years Experience</b> | FCC - AML/CFT | Model Risk Developer | Data Science & AI/ML | Econometrics</p>
    <p>📧 nehravikas100@gmail.com | 📱 +971-554129599 | 📍 Dubai, UAE</p>
</div>
""", unsafe_allow_html=True)

# Career Accomplishments
st.subheader("Career Accomplishments")
st.markdown("""
- Led AML/CFT monitoring systems with SAS 8.3
- Built stress testing models in Python
- Fraud detection with Isolation Forest & One-Class SVM
- Automated compliance workflows (1 day → 1 hour)
- Forecasted risk events using ARIMAX & time series
- Multi-country surveillance tuning (IN, AE, DE, TW, etc.)
- Predictive models for churn & demand forecasting
- Conducted Python & PySpark training
- Produced regulatory dashboards in Tableau
""")

# Work Experience
st.subheader("Work Experience")
st.markdown("""
**Asst Manager, Compliance – RAKBANK (Feb 2023 – Present)**  
- Deployed SAS 8.3 AML/CFT surveillance
- Designed GMM segmentation for customers
- Authored compliance docs per CBUAE guidelines
- Delivered training workshops

**Manager – Stress Test Modelling, HSBC (Feb 2022 – Feb 2023)**  
- Built stress testing models with macroeconomic drivers
- Automated cash flow projections in Python

**Manager/Associate Manager – FCC, Standard Chartered (2019 – 2022)**  
- AML parameter tuning (Oracle Mantas)
- Forecasted risk events with ARIMAX
- Developed fraud detection POCs

**Analyst – Data Science, Infosys (2017 – 2019)**  
- Built churn prediction & demand forecasting models
- Migrated ETL pipelines from SAS → Python
- Data storytelling with Tableau
""")

# Skills
st.subheader("Technical Skills & Focus Areas")
col1, col2 = st.columns([1,1])

with col1:
    skills = {
        "Python": 90,
        "R": 70,
        "SAS": 85,
        "SQL": 80,
        "Spark/PySpark": 75,
        "Tableau/Power BI": 85
    }
    for skill, level in skills.items():
        st.markdown(f"**{skill}**")
        st.progress(level/100)

with col2:
    st.markdown("**Focus Areas**")
    st.markdown("Data Science, Machine Learning, AML/CFT, Econometrics, AI, Python, Risk Modeling, Compliance, Analytics")

# Education
st.subheader("Education")
st.markdown("""
- **M.Sc. Economics**, Madras School of Economics (2015 – 2017)  
- **B.A. Economics**, Delhi University (2011 – 2014)
""")

# Certifications
st.subheader("Courses & Certifications")
st.markdown("""
- Certified Anti-Money Laundering Specialist (CAMS), ACAMS (2025)
- Agentic AI for Developers (Enterprise Applications)
- OpenAI API for Python Developers – LinkedIn
- SAS Programming 1: Essentials – Credly
- Python for Data Science – Microsoft
""")

# Personal Details
st.subheader("Personal Details")
st.markdown("""
- **Nationality**: Indian  
- **Location**: Dubai, UAE
""")

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 40px;">
    <p>© 2023 Vikas Dharam Pal. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
