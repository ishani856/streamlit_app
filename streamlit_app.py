import streamlit

streamlit.title('I am getting better version of myself every day')

streamlit.header('I have started my journey and in the middle of it to  being an data scientist 😍 ')
streamlit.text(' 😁 I fulfill the requirements and skillsets of above headline :-) hehehe')
streamlit.text('Like data analysis of the streaming data, python as a communicator in the ground of world, visualisation as an reporting , algorithms to train and deploy the model')
streamlit.text('I have some experience in data engineering tools like ssis,ssms,ssas,ssrs,databricks pipeline')
streamlit.text('Yeaahhhh 😉.....cool so for these  sql is must and ETL related practices as well')
streamlit.text('Also completed the Full Stack Analyst Certification')
streamlit.text('A good practice of On Cloud Practices in Azure is been added inspite of all above ...... sounds good yeaahhhhh 💖👌🤞.......... lets keep going this journey')


streamlit.header(' 😋  Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥫  Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🥚 Hard-Boiled Free-Range Egg')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
