import difflib
import streamlit as st

# Data: Safe and Unsafe Companies with Arabic and English Translations
arabic_companies = [
    "ليبتون",
    "كارفور", "ستاربكس",
    "نسكافيه",
    "ليز", "دوريتوس", "شيتوس",
    "شيبسي", "صن بايتس", "بيك رولز",
    "ماك","ماكدونالدز", "كنتاكي",
    "بيتزا هت", "دومينوز", "دومينوز بيتزا ",
    "دانون", "نسكويك",
    "بامبرز", "بريل", "فيري",
    "إيريال", "داوني", "تايد", "بونكس",
    "بيبسي", "فانتا", "كوكاكولا",
    "لوكس", "دوف", "لايف بوي"
]
  

english_companies = [
    "lipton",
    "carrefour","starbucks", 
    "nescafe",
    "lay's", "doritos","cheetos",
    "chipsy", "sun bites" , "bic rols",
    "mcdonald's" , "kfc" , 
    "pizza hut" ,"domino's", "domino's pizza",
    "danone","nesquik",
    "pampers","bril", "fairy",
    "ariel", "downy" , "tide", "bonux",
    "pepsi","fanta", "cocacola", 
    "lux" , "dove", "lifeboy"]

# Threshold for matching user input
threshold = 0.8

# Function to find similar company names based on threshold
def find_similar_companies(user_input, companies_list):
    matches = difflib.get_close_matches(str.lower(user_input), companies_list, n=1, cutoff=threshold)
    return matches[0] if matches else None

# Streamlit App
st.markdown("<h1 style='font-size:40px; text-align: center; color: red;'> Boycott Zionist Companies/Products </h1>", unsafe_allow_html=True)
st.markdown("<h1 style='font-size:24px; text-align: left; color: gray;'> Enter a product/company name to check if it supports Israel or not. </h1>", unsafe_allow_html=True)
st.markdown("<h1 style='font-size:25px; text-align: right; color: gray;'> أدخل اسم المنتج/الشركة للتحقق إذا كانت تدعم إسرائيل أم لا </h1>", unsafe_allow_html=True)

# User Input
user_input = st.text_input("Enter Company Name:",placeholder="Arabic/English")

# Check Classification
arabic_match = find_similar_companies(user_input, arabic_companies)
english_match = find_similar_companies(user_input, english_companies)

if user_input:
    if arabic_match:
        st.markdown(f"<h1 style='font-size:30px; text-align: right; color: red;'> ❌{arabic_match}: هذا المنتج صهيوني</h1>", unsafe_allow_html=True)
 
    elif english_match:
        st.markdown(f"<h1 style='font-size:30px; text-align: left; color: red;'> {english_match}: This company supports Israel ❌</h1>", unsafe_allow_html=True)

    else:
        st.markdown(f"<h1 style='font-size:25px; text-align: left; color: gray;'>{user_input} is not available in our database.</h1>", unsafe_allow_html=True)



#########################################################
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.markdown("<h1 style='font-size:20px; text-align: center; color: green; font-family:SansSerif;'>Made with 💖 By Ahmed Hossam</h1>", unsafe_allow_html=True)
    st.markdown("[My Github](https://github.com/Ahmed-Hossam-Aldeen)")


    st.markdown("<h1 style='font-size:40px; text-align: left; color: red; font-family:SansSerif;'>Free<br>Palestine </h1>", unsafe_allow_html=True)
    st.image('https://upload.wikimedia.org/wikipedia/commons/0/00/Flag_of_Palestine.svg', width=50)        