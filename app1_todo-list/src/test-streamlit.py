import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Mi titulo")
st.subheader("Mi subtitulo")
st.write("Mi texto")

st.checkbox("Checkbox")
st.radio("Radio", ["A", "B", "C"])
st.balloons()
st.button("Boton")
st.text_input("Texto")
st.number_input("Numero")
st.text_area("Area de texto")
st.selectbox("Selectbox", ["A", "B", "C"])
st.multiselect("Multiselect", ["A", "B", "C"])
st.slider("Slider")
st.select_slider("Select slider", ["A", "B", "C"])
st.text("Texto")
st.json({"key": "value"})
st.code("print('Hola mundo')")
st.file_uploader("File uploader")
st.color_picker("Color picker")
st.date_input("Date input")
st.time_input("Time input")
st.progress(50)
st.spinner("Spinner")
st.error("Error")
st.warning("Warning")
st.info("Info")
st.success("Success")
data = {"key": "value"}  # Define the 

fig = plt.figure()  # Define the variable `fig` with a matplotlib figure object
st.pyplot(fig)

st.pyplot()  # Equivalent to st.pyplot(fig) where fig is the last figure that you plotted
st.pyplot(fig, clear_figure=True)  # Equivalent to st.pyplot() followed by st.pyplot(fig)


data_activar = {
    'codigo ztv': ['001', '002', '003', '004'],
    'dispositivo': ['Dispositivo A', 'Dispositivo B', 'Dispositivo C', 'Dispositivo D'],
    'activo': [True, False, True, False]
}

# Crea un DataFrame con los datos
df_activar = pd.DataFrame(data_activar)

# Agrega la tabla a la aplicación Streamlit
st.write("Tabla con botones de activación")
for i, row in df_activar.iterrows():
    cols = st.columns([1, 2, 1, 1])
    cols[0].write(row['codigo ztv'])
    cols[1].write(row['dispositivo'])
    cols[2].write(row['activo'])
    # Aquí agregamos el botón en la columna "activar"
    if cols[3].button("Activar", key=f"button{i}"):
        # Aquí puedes definir lo que sucede cuando se hace clic en el botón
        st.write(f"Dispositivo {row['codigo ztv']} activado")