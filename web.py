import streamlit as st
from streamlit import session_state

import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo  App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{i}")
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        st.rerun()


st.text_input(label='', placeholder='Add a new todo...', on_change=add_todo, key='new_todo')
