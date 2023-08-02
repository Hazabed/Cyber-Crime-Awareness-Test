import streamlit as st
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import pickle
# Define the questions
df = pd.read_csv('Data.csv')
# Create an empty DataFrame to store the responses
# Preprocess the data
categorical_cols = ['Gender', 'Age', 'Education Level']
numerical_cols = ['q' + str(i) for i in range(1, 29)]
preprocessor = ColumnTransformer([
    ('encoder', OneHotEncoder(), categorical_cols),
    ('passthrough', 'passthrough', numerical_cols)
])
a = preprocessor.fit_transform(df)

questions = [
    {
        "id": "Gender",
        "question": "What is your gender?",
        "options": [
            {"option": "Male"},
            {"option": "Female"}
        ]
    },
    {
        "id": "Age",
        "question": "What is your age range?",
        "options": [
            {"option": "20-30"},
            {"option": "30-40"},
            {"option": "40-50"},
            {"option": "+50"}
        ]
    },
    {
        "id": "Education Level",
        "question": "What is your education level?",
        "options": [
            {"option": "Postgraduate"},
            {"option": "Undergraduate"},
            {"option": "High School"},
            {"option": "Middle School"}
        ]
    },
    {
        "id": "q1",
        "question": "Do you share sensitive personal information, such as your address or phone number, on social media platforms?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q2",
        "question": "Do you know how to identify and report online harassment or cyberbullying?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q3",
        "question": "Do you regularly backup important files and data on your devices?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q4",
        "question": "Do you review the privacy settings on your social media accounts?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q5",
        "question": "Do you use different passwords for your online accounts?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q6",
        "question": "Are you familiar with the concept of two-factor authentication and do you use it for your online accounts?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q7",
        "question": "Do you use antivirus software and regularly update it on your devices?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q8",
        "question": "Have you ever fallen for a phishing email or text message?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q9",
        "question": "Do you know what a Trojan is?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q10",
        "question": "Would you connect to a public Wi-Fi network without using a VPN?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q11",
        "question": "Have you ever given out your personal information to an unknown caller?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q12",
        "question": "Do you use a password manager to store and generate strong passwords?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q13",
        "question": "Have you ever fallen for a fake website or advertisement?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q14",
        "question": "Do you use encryption when sending sensitive information online?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q15",
        "question": "Do you use a spam filter on your email account?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q16",
        "question": "Have you ever used a weak or easily guessable password?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q17",
        "question": "Have you ever installed software from an untrusted source?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q18",
        "question": "Do you use a reputable ad-blocker on your browser?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q19",
        "question": "Have you ever fallen for a social media scam?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q20",
        "question": "Do you feel that the risk of online security threats is something that concerns you?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q21",
        "question": "Do you know what social engineering is?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q22",
        "question": "Have you ever fallen for a tech support scam?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q23",
        "question": "Do you use a reputable browser extension to block malicious websites?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q24",
        "question": "Do you feel that the risk of becoming a victim of cybercrime has increased in the past year?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q25",
        "question": "I feel my digital devices (computer, smartphones) have no value to hackers, they do not target me.",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q26",
        "question": "Would you answer a call from an unknown caller?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q27",
        "question": "Do you think social media services protect your personal information?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    },
    {
        "id": "q28",
        "question": "Do you use a firewall on your home network?",
        "options": [
            {"option": "Yes"},
            {"option": "No"}
        ]
    }
]
with open('svm_model.pkl', 'rb') as f:
    clf = pickle.load(f)
# Set page title and description
st.set_page_config(page_title="Cybersecurity test", page_icon="🔒", layout="wide")
st.title("Cybersecurity test")
st.markdown("Please answer the following questions to assess your cybersecurity practices.")

# Create an empty DataFrame to store the responses
df_responses = pd.DataFrame()

# Loop over the questions and display them to the user
for question in questions:
    # Display the question
    st.subheader(question["question"])

    # Display the options
    options = [option["option"] for option in question["options"]]
    answer = st.radio(question["id"], options, key=question['id'])
    df_responses[question["id"]] = [answer]

# Create a submit button
if st.button("Submit"):
    # Display the responses to the user
    df_responses.replace({"Yes": 1, "No": 0}, inplace=True)
    
    X = preprocessor.transform(df_responses)
    preds = clf.predict(X)
    
    result_text = "Based on your responses, the predicted class is: {}".format(preds[0])  # Modify this based on your model output
    
    # Display the result
    st.subheader("Result")
    st.success(result_text)