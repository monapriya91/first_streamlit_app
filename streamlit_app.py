import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Favourites')
streamlit.text('Omega 3 & Blueberry')
streamlit.text('Kale, Spinach,Smoothie')
streamlit.text('🐔 Boiled egg')
streamlit.text('🥑 Avacado')
streamlit.header('🍓 Build your own furit smoothie 🍍')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
