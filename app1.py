import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Vikas Resume", layout="centered")

# Custom background with library theme
st.markdown(
    """
    <style>
        .stApp {
            background-image: url('https://images.unsplash.com/photo-1519681393784-d120267933ba?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            color: #ffffff;
        }
        .block-container {
            background: rgba(0, 0, 0, 0.7);
            padding: 2rem;
            border-radius: 12px;
        }
        h1, h2, h3, h4, h5, h6, p, li {
            color: #f1f1f1;
        }
        .stProgress .st-bo { height: 8px; border-radius: 10px; background-color: #1f77b4; }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("""
<div style="text-align: center;">
    <h1>Vikas (Vikas Dharam Pal), CAMS</h1>
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

# Skills and Word Cloud
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
    st.markdown("**Word Cloud**")
    text = "Data Science Machine Learning AML CFT Econometrics AI Python Risk Modeling Compliance Analytics"
    wc = WordCloud(width=400, height=300, background_color="black", colormap="Blues").generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

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
- **DOB**: 29th June 1993  
- **Nationality**: Indian  
- **Location**: Dubai, UAE
""")