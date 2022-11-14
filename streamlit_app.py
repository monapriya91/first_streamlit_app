import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Favourites')
streamlit.text('Omega 3 & Blueberry')
streamlit.text('Kale, Spinach,Smoothie')
streamlit.text('🐔 Boiled egg')
streamlit.text('🥑 Avacado')
streamlit.header('🍓 Build your own fruit smoothie 🍍')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

