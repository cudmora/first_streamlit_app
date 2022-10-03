import streamlit
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.header('🥣Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text(':chicken Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Strawberries','Avocado'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruitvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    # write your own comment -what does the next line do? 
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("please select a fruit to get more info")
  else:
    back_from_function = get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()
    


def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
     my_cur.execute("SELECT * from fruit_load_list")
     return my_cur.fetchall()

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
     my_cur.execute("insert into fruit_load_list values ('from streamlit')")
      return "Thanks for adding " + new_fruit


if streamlit.button('get fruit load'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.header("the fruit load list contains:")
  streamlit.dataframe(my_data_rows)


add_my_fruit = streamlit.text_input('What fruit would you like to add')
if streamlit.button('add a fruit to the list):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
streamlit.write('Thanks for adding ', add_my_fruit)

#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
