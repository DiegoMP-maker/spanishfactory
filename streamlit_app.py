import streamlit as st
import openai

st.set_page_config(page_title="SpanishFactory", layout="centered")

st.title("🇪🇸 SpanishFactory – Generador de ejercicios ELE con IA")
st.markdown("Crea ejercicios personalizados para tus clases de español en segundos.")

# Campo para la API key
api_key = st.text_input("🔑 Introduce tu clave de OpenAI", type="password")

if not api_key:
    st.warning("Por favor, introduce tu clave API de OpenAI para continuar.")
    st.stop()

openai.api_key = api_key

# Inputs del usuario
nivel = st.selectbox("🧭 Nivel", ["A1", "A2", "B1", "B2", "C1"])
tema = st.text_input("🧠 Tema léxico (ej. turismo, trabajo, salud...)")
gramatica = st.text_input("⚙️ Punto gramatical (ej. pretérito indefinido, subjuntivo...)")
tipo = st.selectbox("📄 Tipo de ejercicio", ["Rellenar huecos", "QCM", "Matching", "Transformar frases"])
boton = st.button("✨ Generar ejercicio")

if boton:
    with st.spinner("Generando ejercicio..."):
        prompt = f"""
Eres un generador de ejercicios para clases de español como lengua extranjera. 
Crea un ejercicio para el nivel {nivel} sobre el tema "{tema}", trabajando el punto gramatical "{gramatica}", 
en formato "{tipo}". Incluye instrucciones claras y de 3 a 5 ítems, adecuados al nivel.

Formato de salida: solo el ejercicio, bien presentado.
"""

        try:
            respuesta = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=800
            )
            ejercicio = respuesta['choices'][0]['message']['content']
            st.markdown("### 📝 Ejercicio generado:")
            st.write(ejercicio)
        except Exception as e:
            st.error(f"❌ Error al generar el ejercicio: {e}")