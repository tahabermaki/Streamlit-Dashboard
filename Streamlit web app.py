# Web app with streamlit

import streamlit as st
import pandas as pd

st.title('Library database')
st.markdown("""---""")
st.subheader('Overview of the database')
# show_button = st.button('Show tables')

# Sidebar

col1, col2 = st.sidebar.columns(2)
books_show = col1.checkbox('books')
authors_show = col1.checkbox('authors')
countries_show = col1.checkbox('countries')
publishers_show = col2.checkbox('publishers')
publishing_show = col2.checkbox('publishing')

st.sidebar.markdown("""---""")

st.sidebar.header('User Input Features')

selected_period1 = st.sidebar.slider('Select the birth year span', 1700, 2020, (1700, 2020), 20)
selected_period2 = st.sidebar.slider('Select the release year span', 1700, 2020, (1700, 2020), 20)

person_or_item = st.sidebar.text_input("Select an author/book")

# Main

## Showing the tables

# books table
df_books = get_table('books', connection1, ['book_id', 'book_name', 'author', 'release_year', 'author_id'])
books = LibraryTable('books', df_books)
df_selected1 = books.span(selected_period2, 'release_year')
df_selected1 = books.name_check(['book_name', 'author'], person_or_item)

# authors table
df_authors = get_table('authors', connection1, ['author_id', 'author', 'birth_year', 'country_id'])
authors = LibraryTable('authors', df_authors)
df_selected2 = authors.span(selected_period1, 'birth_year')
df_selected2 = authors.name_check(['author'], person_or_item)

# countries table
df_countries = get_table('countries', connection1, ['country_id', 'country', 'last_release_id', 'last_release_year'])
countries = LibraryTable('countries', df_countries)

# publishers table
df_publishers = get_table('publishers', connection1, ['publisher_id', 'publisher_name'])
publishers = LibraryTable('publishers', df_publishers)

# publishing table
df_publishing = get_table('publishing', connection1, ['publisher_id', 'author_id', 'total_sales'])
publishing = LibraryTable('publishing', df_publishing)

if books_show:
    st.subheader('Table of books')
    st.dataframe(df_selected1)
if authors_show:
    st.subheader('Table of authors')
    st.dataframe(df_selected2)
if countries_show:
    st.subheader('Table of countries')
    st.dataframe(countries.df)
if publishers_show:
    st.subheader('Table of publishers')
    st.dataframe(publishers.df)
if publishing_show:
    st.subheader('Table of publishing')
    st.dataframe(publishing.df)

# Query stuff

the_query = st.sidebar.text_area("Input query")

st.markdown("""---""")

if the_query != "":
    st.subheader("Custom query result")
    st.dataframe(pd.DataFrame(execute_query(connection1, the_query)))

# Plot stuff

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

query1 = """
SELECT countries.country_name, COUNT(countries.country_name) 
FROM authors 
JOIN books ON books.author_id=authors.author_id 
JOIN countries ON countries.country_id=authors.country_id 
GROUP BY country_name;
"""

temp_tab = pd.DataFrame(execute_query(connection1, query1), columns=['country', 'occurrence'])
labels = temp_tab.country
sizes = temp_tab.occurrence
explode = (0.1, 0, 0, 0, 0)

plot_button = st.sidebar.button('Show plot')
if plot_button:
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
           startangle=90)
    ax.set_title('Country representation')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.markdown("""---""")
    st.pyplot(fig)
