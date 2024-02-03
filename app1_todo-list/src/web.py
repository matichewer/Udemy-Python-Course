# web.py
import streamlit as st
import functions


all_todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    all_todos.append(todo)
    functions.write_todos(all_todos)
    st.session_state["new_todo"] = ""


st.title("My ToDo app")
st.subheader("This is a simple ToDo app")
st.write("Built with Streamlit")

for index, todo in enumerate(all_todos):
    if todo != "\n":  # para evitar un checkbox en el ultimo renglon blanco
        checkbox = st.checkbox(todo, key=todo) # crea checkbox para cada ToDo item
        if checkbox: # si el checkbox esta marcado, elimina el ToDo item
            all_todos.pop(index)
            functions.write_todos(all_todos)
            del st.session_state[todo]
            st.rerun()

# fmt: off
st.text_input(
    label=" ", # para q no tenga titulo el input
    placeholder="Add a new todo", # titulo dentro del input
    on_change=add_todo, # ejecuta la funcion cuando el usuario presiona ENTER
    key="new_todo"
)
# fmt: on


# Para ver el estado de la app
#st.session_state

