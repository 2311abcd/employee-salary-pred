import streamlit as st
import pandas as pd
import joblib


# =========================================================
# LOAD MODEL
# =========================================================
model = joblib.load("best_model.pkl")


# =========================================================
# APP CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="💼 Employee Salary Predictor",
    layout="centered"
)


# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

    /* =====================================================
       MAIN APP BACKGROUND
       ===================================================== */
    body {
        background-color: #87CEFA;
    }

    .stApp {
        background-color: #87CEFA;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */
    section[data-testid="stSidebar"] {
        background-color: #d6ecfa;
    }


    /* Sidebar heading */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #002b5c !important;
        font-weight: 700 !important;
    }


    /* Sidebar labels */
    section[data-testid="stSidebar"] label {
        color: #002b5c !important;
        font-weight: 600 !important;
    }


    /* Sidebar normal text */
    section[data-testid="stSidebar"] p {
        color: #002b5c !important;
    }


    /* =====================================================
       SELECT BOX
       ===================================================== */
    section[data-testid="stSidebar"] div[data-baseweb="select"] {
        background-color: #ffffff !important;
        border-radius: 10px !important;
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"] * {
        color: #002b5c !important;
    }


    /* =====================================================
       NUMBER INPUT
       ===================================================== */
    section[data-testid="stSidebar"] input {
        color: #002b5c !important;
        background-color: #ffffff !important;
    }


    /* =====================================================
       SLIDER
       ===================================================== */

    /* Slider track */
    section[data-testid="stSidebar"] [data-baseweb="slider"] > div > div {
        background-color: #002b5c !important;
    }

    /* Slider handle */
    section[data-testid="stSidebar"] [data-baseweb="slider"] [role="slider"] {
        background-color: #002b5c !important;
        border-color: #002b5c !important;
    }


    /* =====================================================
       PREDICT BUTTON
       ===================================================== */
    .stButton > button {
        background-color: #002b5c !important;
        color: white !important;
        border-radius: 10px !important;
        border: 1px solid white !important;
        font-weight: bold !important;
        width: 100% !important;
        padding: 10px !important;
    }

    .stButton > button:hover {
        background-color: #004080 !important;
        color: white !important;
        border-color: white !important;
    }


    /* =====================================================
       DATAFRAME
       ===================================================== */
    [data-testid="stDataFrame"] {
        border-radius: 10px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================
st.markdown("""
<h1 style="
    color: #002b5c;
    background-color: #e0f0ff;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    font-family: Arial, sans-serif;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
">
    🧑‍💼 Employee Salary Prediction
</h1>
""", unsafe_allow_html=True)


st.markdown(
    "Use this app to predict whether an employee earns "
    "**more than $50K** or not based on their profile."
)


# =========================================================
# SIDEBAR - EMPLOYEE DETAILS
# =========================================================
st.sidebar.header("📋 Enter Employee Details")


# Age
age = st.sidebar.slider(
    "Age",
    18,
    90,
    30
)


# Workclass
workclass = st.sidebar.selectbox(
    "Workclass",
    [
        "Private",
        "Self-emp-not-inc",
        "Self-emp-inc",
        "Federal-gov",
        "Local-gov",
        "State-gov",
        "Without-pay",
        "Never-worked"
    ]
)


# Final Weight
fnlwgt = st.sidebar.number_input(
    "Final Weight (fnlwgt)",
    value=123456
)


# Education
education = st.sidebar.selectbox(
    "Education",
    [
        "Bachelors",
        "HS-grad",
        "11th",
        "Masters",
        "9th",
        "Some-college",
        "Assoc-acdm",
        "Assoc-voc",
        "7th-8th",
        "Doctorate",
        "Prof-school",
        "5th-6th",
        "10th",
        "1st-4th",
        "Preschool",
        "12th"
    ]
)


# Education Number
educational_num = st.sidebar.slider(
    "Education Number",
    1,
    16,
    13
)


# Marital Status
marital_status = st.sidebar.selectbox(
    "Marital Status",
    [
        "Married-civ-spouse",
        "Divorced",
        "Never-married",
        "Separated",
        "Widowed",
        "Married-spouse-absent"
    ]
)


# Occupation
occupation = st.sidebar.selectbox(
    "Occupation",
    [
        "Tech-support",
        "Craft-repair",
        "Other-service",
        "Sales",
        "Exec-managerial",
        "Prof-specialty",
        "Handlers-cleaners",
        "Machine-op-inspct",
        "Adm-clerical",
        "Farming-fishing",
        "Transport-moving",
        "Priv-house-serv",
        "Protective-serv",
        "Armed-Forces"
    ]
)


# Relationship
relationship = st.sidebar.selectbox(
    "Relationship",
    [
        "Wife",
        "Own-child",
        "Husband",
        "Not-in-family",
        "Other-relative",
        "Unmarried"
    ]
)


# Race
race = st.sidebar.selectbox(
    "Race",
    [
        "White",
        "Black",
        "Asian-Pac-Islander",
        "Amer-Indian-Eskimo",
        "Other"
    ]
)


# Gender
gender = st.sidebar.selectbox(
    "Gender",
    [
        "Male",
        "Female"
    ]
)


# Capital Gain
capital_gain = st.sidebar.number_input(
    "Capital Gain",
    value=0
)


# Capital Loss
capital_loss = st.sidebar.number_input(
    "Capital Loss",
    value=0
)


# Hours Per Week
hours_per_week = st.sidebar.slider(
    "Hours per Week",
    1,
    99,
    40
)


# Native Country
native_country = st.sidebar.selectbox(
    "Native Country",
    [
        "United-States",
        "India",
        "Mexico",
        "Philippines",
        "Germany",
        "Canada",
        "Iran",
        "Other"
    ]
)


# Years of Experience
experience = st.sidebar.slider(
    "Years of Experience",
    0,
    40,
    5
)


# =========================================================
# PREPARE INPUT DATA
# =========================================================
input_df = pd.DataFrame({
    "age": [age],
    "workclass": [workclass],
    "fnlwgt": [fnlwgt],
    "education": [education],
    "educational-num": [educational_num],
    "marital-status": [marital_status],
    "occupation": [occupation],
    "relationship": [relationship],
    "race": [race],
    "gender": [gender],
    "capital-gain": [capital_gain],
    "capital-loss": [capital_loss],
    "hours-per-week": [hours_per_week],
    "native-country": [native_country],
    "experience": [experience]
})


# =========================================================
# INPUT SUMMARY
# =========================================================
st.markdown("### 🔍 Input Summary")

st.dataframe(
    input_df.style.set_properties(
        **{"text-align": "left"}
    ),
    use_container_width=True
)


# =========================================================
# PREDICTION
# =========================================================
if st.button("🔮 Predict Salary"):

    with st.spinner("Predicting..."):

        try:

            # Make prediction
            prediction = model.predict(input_df)


            # =================================================
            # MORE THAN $50K
            # =================================================
            if prediction[0] == ">50K":

                st.markdown("""
                <div style="
                    background-color: #002b5c;
                    color: white;
                    padding: 18px;
                    margin-top: 15px;
                    border-radius: 10px;
                    border: 2px solid white;
                    text-align: center;
                    font-size: 18px;
                    font-weight: bold;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                ">
                    ✅ This employee is likely to earn
                    <b>more than $50K</b>.
                </div>
                """, unsafe_allow_html=True)


            # =================================================
            # $50K OR LESS
            # =================================================
            else:

                st.markdown("""
                <div style="
                    background-color: #002b5c;
                    color: white;
                    padding: 18px;
                    margin-top: 15px;
                    border-radius: 10px;
                    border: 2px solid white;
                    text-align: center;
                    font-size: 18px;
                    font-weight: bold;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                ">
                    ℹ️ This employee is likely to earn
                    <b>$50K or less</b>.
                </div>
                """, unsafe_allow_html=True)


        except Exception as e:

            st.error(
                f"❌ Prediction failed: {e}"
            )


# =========================================================
# BATCH PREDICTION
# =========================================================
st.markdown("---")

st.markdown("## 📂 Batch Prediction (Upload CSV)")


uploaded_file = st.file_uploader(
    "Upload CSV file for batch salary prediction",
    type=["csv"]
)


if uploaded_file is not None:

    try:

        # Read uploaded CSV
        batch_df = pd.read_csv(uploaded_file)


        # =================================================
        # UPLOADED DATA PREVIEW
        # =================================================
        st.write("📝 Uploaded Data Preview")

        st.dataframe(
            batch_df.head(),
            use_container_width=True
        )


        # =================================================
        # BATCH PREDICTION
        # =================================================
        batch_preds = model.predict(batch_df)

        batch_df["Predicted Salary Class"] = batch_preds


        # =================================================
        # PREDICTION RESULTS
        # =================================================
        st.write("✅ Prediction Results")

        st.dataframe(
            batch_df.head(),
            use_container_width=True
        )


        # =================================================
        # DOWNLOAD CSV
        # =================================================
        csv_data = batch_df.to_csv(
            index=False
        ).encode("utf-8")


        st.download_button(
            label="⬇️ Download Prediction CSV",
            data=csv_data,
            file_name="salary_predictions.csv",
            mime="text/csv"
        )


    except Exception as e:

        st.error(
            f"❌ Error processing file: {e}"
        )