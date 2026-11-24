import streamlit as st
import requests

st.set_page_config(page_title="Eventia", page_icon="🎉", layout="wide")
st.title("Eventia")
st.caption("Gestión inteligente de eventos y reservaciones")

st.subheader("Asistente de Eventia")
st.info("La interfaz de chat se conectará con el backend, el cliente MCP y el proveedor de IA.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("¿Qué deseas consultar?")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        st.write("La conexión con el asistente de IA está pendiente de implementación.")
    st.session_state.messages.append({
        "role": "assistant",
        "content": "La conexión con el asistente de IA está pendiente de implementación."
    })
