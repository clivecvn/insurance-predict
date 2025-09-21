import streamlit as st
import joblib

st.title("U.S. Health insurance predictor")

model = joblib.load("forest.pkl")

st.header("Input Features")
with st.form("form"):
    age = st.slider("Age", 0, 125, 50)
    children = st.slider("Children", 0, 30, 0)
    bmi = st.slider("Bmi", 9.0, 65.0, 25.0)
    sex = st.selectbox("Gender", ("-", "Male", "Female"))
    region = st.selectbox(
        "Region", ("-", "Northwest", "Northeast", "Southwest", "Southeast")
    )
    smoker = st.checkbox("Smoker")
    submit_form = st.form_submit_button("Submit")
    if submit_form:
        errors = []
        if sex == "-":
            errors.append("Gender is required")
        if region == "-":
            errors.append("Region is required.")
        if errors:
            for error in errors:
                st.error(error)
        else:
            if sex == "Male":
                sex_male = True
                sex_female = False
            else:
                sex_male = False
                sex_female = True
            if smoker == True:
                smoker_no = False
                smoker_yes = True
            else:
                smoker_no = True
                smoker_yes = False
            if region == "Northeast":
                region_northeast = True
                region_northwest = False
                region_southeast = False
                region_southwest = False
            elif region == "Northwest":
                region_northeast = False
                region_northwest = True
                region_southeast = False
                region_southwest = False
            elif region == "Southeast":
                region_northeast = False
                region_northwest = False
                region_southeast = True
                region_southwest = False
            else:
                region_northeast = False
                region_northwest = False
                region_southeast = False
                region_southwest = True
            prediction = model.predict(
                [
                    [
                        age,
                        bmi,
                        children,
                        sex_female,
                        sex_male,
                        smoker_no,
                        smoker_yes,
                        region_northeast,
                        region_northwest,
                        region_southeast,
                        region_southwest,
                    ]
                ]
            )
            print(age, children, bmi, sex, region, smoker)
            print(
                age,
                bmi,
                children,
                sex_female,
                sex_male,
                smoker_no,
                smoker_yes,
                region_northeast,
                region_northwest,
                region_southeast,
                region_southwest,
            )
try:
    st.header(f"${round(float(prediction),2)}")
except:
    pass
