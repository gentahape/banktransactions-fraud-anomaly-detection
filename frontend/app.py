import streamlit as st
import requests
import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

BASE_DIR = Path(__file__).resolve().parent

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Bank Transaction Fraud & Anomaly Detection System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CUSTOM CSS INJECTION
# ==========================================
st.markdown("""
    <style>
        .hero-title {
            text-align: center;
            font-size: 3.2rem;
            font-weight: 800;
            margin-bottom: 0px;
            padding-top: 2rem;
        }
        .hero-subtitle {
            text-align: center;
            font-size: 1.2rem;
            color: #666;
            margin-top: 15px;
            margin-bottom: 40px;
            padding: 0 10%;
            line-height: 1.6;
        }
        
        .challenge-card {
            background-color: #f8f9fa;
            padding: 2.5rem;
            border-radius: 12px;
            border-left: 6px solid #0068c9;
            margin-bottom: 2rem;
        }
        .challenge-card h4 {
            margin-top: 0;
            color: #0068c9;
        }
        
        @media (prefers-color-scheme: dark) {
            .challenge-card {
                background-color: #1e1e1e;
                border-left: 6px solid #4facfe;
            }
            .challenge-card h4 {
                color: #4facfe;
            }
            .hero-subtitle {
                color: #aaaaaa;
            }
        }
            
        .tech-card {
            background-color: #f1f3f6;
            padding: 1.5rem;
            border-radius: 10px;
            height: 100%;
        }
        @media (prefers-color-scheme: dark) {
            .tech-card {
                background-color: #262730;
            }
        }
            
        .result-box-safe { background-color: #d4edda; color: #155724; padding: 20px; border-radius: 10px; border-left: 8px solid #28a745; margin-top: 10px; }
        .result-box-danger { background-color: #f8d7da; color: #721c24; padding: 20px; border-radius: 10px; border-left: 8px solid #dc3545; margin-top: 10px;}
        .result-box-neutral { background-color: #e9ecef; color: #495057; padding: 20px; border-radius: 10px; text-align: center; margin-top: 10px;}
            
        .footer {
            text-align: center;
            padding: 20px;
            color: #666;
            border-top: 1px solid #eaeaea;
            margin-top: 50px;
        }
        .footer a {
            color: #0068c9;
            text-decoration: none;
            margin: 0 10px;
            font-weight: 500;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SECTION: HERO
# ==========================================
st.markdown('<h1 class="hero-title">Bank Transaction Fraud & Anomaly Detection System</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">A Hybrid Machine Learning approach. Transforming Unsupervised Clustering into Supervised Classification to detect suspicious bank transaction patterns in real-time.</p>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([2.5, 1.5, 1.5, 2.5])

with col2:
    st.markdown("""
    <a href="#interactive-detection-simulator" target="_self" style="text-decoration: none;">
        <div style="
            background-color: #0068c9; 
            color: white; 
            padding: 0.45rem 1rem; 
            border-radius: 0.5rem; 
            text-align: center; 
            font-weight: 600;
            border: 1px solid #0068c9;
            transition: 0.3s;
        ">
            Start Simulation
        </div>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.link_button("View Research Notebook", url="https://colab.research.google.com/drive/1mLZoYslNTcrvJrkH6m2nBAux5KU2z-ni?usp=sharing", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()

# ==========================================
# SECTION: THE CHALLENGE
# ==========================================
st.header("The Challenge")

st.markdown("""
<div class="challenge-card">
    <h4>Business Context</h4>
    <p>The massive volume of digital transactions makes manual verification nearly impossible and highly inefficient.</p>
    <br>
    <h4>Problem Statement</h4>
    <p>How can we distinguish between premium customers, conservative users, and cyber attacks using only raw transaction data?</p>
    <br>
    <h4>Dataset Source</h4>
    <p><a href="https://drive.google.com/file/d/163av8kALAjxoV2ZneEG5NGsHCE6Iqvj2/view?usp=sharing" target="_blank">Bank Transaction Dataset</a></p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# SECTION: METHODOLOGY & RESEARCH JOURNEY
# ==========================================
st.header("Methodology & Research Journey")
st.markdown("A structured analytical thinking process to transform raw transaction data into a production-ready system.")

with st.expander("Phase 1: Data Preparation & Discovery", expanded=True):
    st.markdown("""
    * **Step 1: EDA (Exploratory Data Analysis):** Explaining the search for duplicate values, missing values, check outliers, and discovering correlations among dataset features.
    * **Step 2: Data Cleaning & Processing:** Handling duplicate values, missing values, remove irrelavant features, scapping outliers, and engineering critical temporal features to prepare data for modeling.
    """)

with st.expander("Phase 2: Unsupervised Learning (Model Clustering)", expanded=True):
    st.markdown("""
    * **Step 3: Clustering:** Utilizing K-Means + PCA to group customers into 5 distinct personas without initial labels.
    * **Step 4: Cluster Interpretation:** Profiling each generated cluster using statistical aggregation to define distinct customer personas and pinpoint high-risk anomalies like Velocity Attacks.
    * **Step 5: Inverse Transform:** Reversing the scaling process to translate standardized machine metrics back into real-world business values for clear stakeholder communication.
    """)

with st.expander("Phase 3: Supervised Learning (Model Classification)", expanded=False):
    st.markdown("""
    * **Step 6: Data Splitting:** Applying one-hot encoding and stratified train-test splits to ensure a balanced distribution of target classes before training the supervised models.
    * **Step 7: Supervised Learning (Classification):** Training 3 baseline models (Decision Tree, Random Forest, and XGBoost) using the generated clustering labels to achieve the highest predictive accuracy.
    * **Step 8: Evaluation:** Comparing the baseline models across key classification metrics (Accuracy, Precision, Recall, and F1-Score) to identify the most effective algorithm.
    * **Step 9: Hyperparameter Tuning:** Optimizing the best-performing model using GridSearchCV to achieve the maximum F1-Score.
    """)

with st.expander("Phase 4: Deployment", expanded=False):
    st.markdown("""
    * **Step 10: Build Pipeline:** Encapsulating the custom feature engineering, data preprocessing, and the tuned model into a single, production-ready scikit-learn Pipeline for seamless API deployment.
    """)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

# ==========================================
# SECTION: THE ENGINE (TECH STACK)
# ==========================================
st.header("The Engine (Tech Stack)")
st.markdown("Showcasing the full-stack architecture and machine learning tools powering this application.")

col_t1, col_t2, col_t3, col_t4 = st.columns(4)

with col_t1:
    st.markdown("""
    <div class="tech-card">
        <h4>Backend</h4>
        <ul>
            <li><b>FastAPI</b></li>
            <li>High-Performance Python Framework</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_t2:
    st.markdown("""
    <div class="tech-card">
        <h4>Frontend</h4>
        <ul>
            <li><b>Streamlit</b></li>
            <li>Interactive Data Web App</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_t3:
    st.markdown("""
    <div class="tech-card">
        <h4>ML Libraries</h4>
        <ul>
            <li>Scikit-Learn & XGBoost</li>
            <li>Pandas, Matplotlib, Plotly, SHAP</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_t4:
    st.markdown("""
    <div class="tech-card">
        <h4>DevOps & Tools</h4>
        <ul>
            <li>Joblib</li>
            <li>Git, Pipenv</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()

# ==========================================
# SECTION: INTERACTIVE FRAUD SIMULATOR
# ==========================================
st.header("Interactive Detection Simulator")
st.markdown("Test the machine learning model in real-time. Use the preset scenarios below or enter manually custom transaction data.")

# 1. INISIALISASI SESSION STATE (Nilai Default)
if 'preset_loaded' not in st.session_state:
    st.session_state.update({
        'TransactionAmount': 150.0,
        'CustomerAge': 45,
        'TransactionDuration': 120,
        'LoginAttempts': 1,
        'AccountBalance': 5000.0,
        'Location': 'Jakarta',
        'Channel': 'Online',
        'CustomerOccupation': 'Engineer',
        'TransactionType': 'Debit',
        'TimeGapSeconds': 86400
    })
    st.session_state['preset_loaded'] = True

def load_preset(scenario):
    if scenario == "Normal":
        st.session_state.update({
            'TransactionAmount': 277.0,
            'CustomerAge': 45, 
            'LoginAttempts': 1, 
            'TimeGapSeconds': 35000000,
            'AccountBalance': 5230.0 
        })
    elif scenario == "Fraud":
        st.session_state.update({
            'TransactionAmount': 291.0,
            'CustomerAge': 34, 
            'LoginAttempts': 2, 
            'TimeGapSeconds': 0,
            'AccountBalance': 4218.0 
        })

st.markdown("**Quick Load Scenarios:**")
col_p1, col_p2, col_p3 = st.columns([1, 1, 2])
with col_p1:
    st.button("✅ Sample: Normal", on_click=load_preset, args=("Normal",), use_container_width=True)
with col_p2:
    st.button("🚨 Sample: Fraud", on_click=load_preset, args=("Fraud",), use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

col_form, col_result = st.columns([1.2, 1])

with col_form:
    st.markdown("#### Transaction Data")
    with st.form("prediction_form"):
        fc1, fc2 = st.columns(2)
        with fc1:
            amount = st.number_input("Transaction Amount ($)", min_value=0.0, key='TransactionAmount')
            age = st.number_input("Customer Age", min_value=17, max_value=100, key='CustomerAge')
        with fc2:
            balance = st.number_input("Account Balance ($)", min_value=0.0, key='AccountBalance')
            login_att = st.number_input("Login Attempts", min_value=1, max_value=10, key='LoginAttempts')
        
        fc3, fc4 = st.columns(2)
        with fc3:
            channel = st.selectbox("Channel", ["ATM", "Online", "Branch"], key='Channel')
            location = st.selectbox("Location", ["Jakarta", "Bandung", "Surabaya"], key='Location')
        with fc4:
            occupation = st.selectbox("Occupation", ["Student", "Doctor", "Engineer", "Retired"], key='CustomerOccupation')
            trans_type = st.selectbox("Transaction Type", ["Debit", "Credit"], key='TransactionType')
        
        time_gap = st.number_input("Time Since Last Transaction (Seconds)", min_value=0, key='TimeGapSeconds', help="0 seconds indicates simultaneous transactions (High Risk).")
        duration = st.number_input("Session Duration (Seconds)", min_value=1, key='TransactionDuration')

        submit_button = st.form_submit_button("Analyze Transaction", type="primary", use_container_width=True)

with col_result:
    st.markdown("#### Live Analysis Result")

    if submit_button:
        with st.spinner("Analyzing transaction patterns via API..."):
            try:
                now = datetime.datetime.now()
                future_time = now + datetime.timedelta(seconds=time_gap)

                payload = {
                    "TransactionAmount": amount,
                    "CustomerAge": age,
                    "TransactionDuration": duration,
                    "LoginAttempts": login_att,
                    "AccountBalance": balance,
                    "Location": location,
                    "Channel": channel,
                    "CustomerOccupation": occupation,
                    "TransactionType": trans_type,
                    "TransactionDate": now.strftime("%Y-%m-%d %H:%M:%S"),
                    "PreviousTransactionDate": future_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "TransactionID": "TRX123", "AccountID": "ACC123", "DeviceID": "DEV123", "IP Address": "192.168.1.1", "MerchantID": "MCH123"
                }
                
                response = requests.post(f"{API_URL}/predict", json=payload)
                
                if response.status_code == 200:
                    res_data = response.json()
                    interpretation = res_data.get('interpretation', 'Unknown Pattern')
                    cluster_id = res_data.get('cluster_id')
                    
                    if cluster_id == 2:
                        st.markdown(f"""
                        <div class="result-box-danger">
                            <h3 style="margin-top:0; color:#721c24;">🚨 CRITICAL RISK</h3>
                            <p><b>Cluster Label:</b> {interpretation}</p>
                            <p><b>Recommended Action:</b> Block transaction immediately and freeze account.</p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="result-box-safe">
                            <h3 style="margin-top:0; color:#155724;">✅ VERIFIED SAFE</h3>
                            <p><b>Cluster Label:</b> {interpretation}</p>
                            <p><b>Recommended Action:</b> Proceed transaction normally.</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("⚠️ Connection Error: Cannot connect to the FastAPI Backend.")
                st.info(f"Make sure the FastAPI server is running on `{API_URL}`.")
    else:
        st.markdown('<div class="result-box-neutral">Waiting for transaction data...<br>Click "Analyze Transaction" to begin.</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()

# ==========================================
# SECTION: EXPLAINABLE AI (XAI) INSIGHT
# ==========================================
st.header("Explainable AI (XAI) Insight")
st.markdown("Demonstrating model transparency and business value.")

col_xai1, col_xai2 = st.columns([1, 1.2])

with col_xai1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    #### Why did the AI make this decision?
    Using **SHAP (SHapley Additive exPlanations)**, we reveal which underlying factors contribute most to the risk score.
    
    Whether it's the exact time gap between `TimeSinceLastTransaction`,`TransactionAmount`, `AccountBalance`, and `TransactionDuration`. The model provides fully transparent and interpretable insights for fraud analysts.
    """)

with col_xai2:
    st.image(f"{BASE_DIR.parent}/frontend/assets/shap_summary.png", caption="Global Feature Importance using SHAP", width="stretch")

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()

# ==========================================
# SECTION: PROJECT ORIGIN & CERTIFICATION
# ==========================================
st.header("Project Origin & Certification")
st.markdown("Serves as proof of foundational ML skills and proactive engineering initiative.")

col_cert_img, col_cert_text = st.columns([1, 1.5])

with col_cert_img:
    st.image(f"{BASE_DIR.parent}/frontend/assets/certificate.png", width="stretch")

with col_cert_text:
    st.markdown("This Machine Learning project originated as a final submission for the **'Belajar Machine Learning untuk Pemula'** (Learn Machine Learning for Beginners) certification at Dicoding. It was thoroughly reviewed by industry experts, and I actively implemented their feedback to further deepen my understanding of core ML concepts.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        st.link_button("View Course Syllabus", "https://www.dicoding.com/academies/184", use_container_width=True) 
    with btn_col2:
        st.link_button("Verify Certificate Credential", "https://www.dicoding.com/certificates/0LZ053YV3X65", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==========================================
# SECTION: FOOTER & PROJECT META
# ==========================================
st.markdown("""
    <div class="footer">
        <p>Built by <b>Genta Haetami Putra</b> — Fullstack Web Developer & ML Enthusiast</p>
        <p>
            <a href="https://gentahp.my.id" target="_blank">Personal Website</a> | 
            <a href="https://linkedin.com/in/gentahp" target="_blank">LinkedIn</a> | 
            <a href="https://github.com/gentahape/banktransactions-fraud-anomaly-detection.git" target="_blank">GitHub Repository</a> | 
            <a href="https://colab.research.google.com/drive/1mLZoYslNTcrvJrkH6m2nBAux5KU2z-ni?usp=sharing" target="_blank">Google Colab Research</a>
        </p>
    </div>
""", unsafe_allow_html=True)