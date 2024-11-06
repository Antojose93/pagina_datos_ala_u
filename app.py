import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Análisis Predictivo de Seguridad y Alertas Preventivas",
    page_icon="🔒",  # Puedes reemplazarlo con otro emoji o URL de imagen
)
# Función para cargar la animación de Lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Cargar animación de Lottie
lottie_security = load_lottieurl("https://lottie.host/7d628140-f5b2-4078-833b-f837838405ef/Qplees0EVA.json")  # URL ejemplo para animación de seguridad


# Contenedor de bienvenida y descripción
with st.container():
    st.subheader("Datos para la paz")
    st.title("Análisis Predictivo de Seguridad y Alertas Preventivas")
   

# Sección: Problema y Contexto
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Problema y Contexto")
        st.markdown(
            """
            <div style="text-align: justify;">
                La seguridad ciudadana es fundamental en el contrato social. En Colombia, los ciudadanos enfrentan retos en su vida diaria que requieren una respuesta proactiva y tecnológica.
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("Nuestra propuesta es analizar datos públicos para identificar tendencias temporales en delitos como homicidios, secuestros y extorsiones. Gracias al análisis de datos y machine learning, generamos predicciones que permiten alertar en lenguaje natural a los ciudadanos sobre riesgos específicos.")
        st.write("[Ejemplo de un analisis sobre homicidios en el departamento de Bolivar ](https://bootcampia-ioykyyxbgy7yjetkhm8pew.streamlit.app/)")

    with right_column:
        st_lottie(lottie_security, height=300, key="security")
        
# Seccion propuesta de valor
with st.container():
    st.write("---")
    st.header("¿Cómo lo vamos a hacer?")
    st.markdown(
        """
        <div style="text-align: justify;">
            La aplicación permite a los ciudadanos reportar incidentes en tiempo real, como robos, acosos, agresiones o procedimientos ilegales de parte de autoridades. La plataforma facilita que estos reportes lleguen directamente a los servicios de emergencia pertinentes: la policía para incidentes de seguridad, los bomberos para situaciones de incendio, y las ambulancias para accidentes y personas heridas. Además, los usuarios pueden registrar a miembros de su familia para que también reciban notificaciones en tiempo real sobre estos incidentes, ayudando a proteger a sus seres queridos.
            <br><br>
            Los datos de estos reportes ciudadanos sirven como insumo de información para el componente de análisis predictivo, proporcionando datos actuales y enriqueciendo la base de conocimiento del sistema para mejorar las alertas preventivas.
        </div>
        """,
        unsafe_allow_html=True
    )
st.write('''
<div style="width: 100%;"><div style="position: relative; padding-bottom: 56.25%; padding-top: 0; height: 0;"><iframe title="Pitch Genial" frameborder="0" width="1200" height="675" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genially.com/672814d2f2b9eaa6686f0e67" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

''',unsafe_allow_html=True)