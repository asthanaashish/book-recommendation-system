import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

book_pivot = pickle.load(open('book_pivot.pkl', 'rb'))
book_sparse = pickle.load(open('book_sparse.pkl','rb'))

model = NearestNeighbors(algorithm='brute')
model.fit(book_sparse)


def recommend(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    book_list = distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1),
                                                          n_neighbors=6)

    recommended_books = []
    # Looping over suggestions
    for i in range(len(book_list)):
        # if i!=0:
        #     print("The suggestions for",book_name,"are: ")
        if not i:
            recommended_books.append(book_pivot.index[suggestions[i]])
            return recommended_books




##DISPLAYS BOOK LIST##
book_dict = pickle.load(open('book_dict.pkl', 'rb'))
book_lis = pd.DataFrame(book_dict)       ##DO NOT TOUCH##                                                                  #book_list['title'].values


#TITLE
st.title("BOOK RECOMMENDER SYSTEM")

#selected_book = st.selectbox(book_list)
options = st.selectbox('ENTER A BOOK NAME', book_lis['title'].values)

if st.button('Recommend'):

    recommendations = recommend(options)
    for i in recommendations:
        st.table(i)
