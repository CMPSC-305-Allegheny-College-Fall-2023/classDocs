#!/usr/bin/env python3

import streamlit as st
import pandas as pd
import numpy as np
import sqlite3

# global variables

myData = pd.read_csv('emissions.csv')
chart_data = pd.DataFrame(myData)
myDBFile = "outDatabase.sqlite3"

def makeDB():
    """function to make a database"""
    # connect the SQLite library to the data
    conn = sqlite3.connect(myDBFile)

    # write the csv data to the base
    myData.to_sql('myData', conn, if_exists='replace', index=False)

    # create cursor object
    cur = conn.cursor()

    # return the cur object to main()
    return cur
    
    # end of makeDB()

def prettyTabler(myResults):
    """ table formatter"""
    with st.expander("Pretty Table"):
        query_df = pd.DataFrame(myResults)
        st.dataframe(query_df)

    # end of prettyTabler()
def main():
    """driver function of the program"""
    st.title('My Database App')
    # end of main()

    menu = ["Make chart", "Balloons", "Snow", "Show tables", "Make database", "Interact"]
    choice = st.sidebar.selectbox("What do you want to do?",menu)

    if choice == "Make chart":
        st.area_chart(chart_data, x ="Year", y = "emissions")
    
    if choice == "Balloons":
        st.balloons()

    if choice == "Snow":
        st.snow()

    if choice == "Make database":
        st.write("making a database from csv")        
        cur = makeDB() # make the db from csv


    if choice == "Show tables":
        cur = makeDB() # make the db from csv
        st.write("Showing tables")        
        DB_table_str = "SELECT name FROM sqlite_master WHERE type ='table'; "

        myQuery = st.text_input('Edit your query here', DB_table_str)
        cur.execute(myQuery)
        results = cur.fetchall()
        st.write(results)

        prettyTabler(results)


    if choice == "Interact":
        cur = makeDB() # make the db from csv
        st.write("Showing tables")        
        DB_table_str = "SELECT * FROM myData; "

        myQuery = st.text_input('Edit your query here', DB_table_str)
        cur.execute(myQuery)
        results = cur.fetchall()
        st.write(results)

        prettyTabler(results)


    # end of main()

main()




