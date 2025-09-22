import streamlit as st
import option_menu
from streamlit_option_menu 


# variables
page_title = "App Barberia"
page_icon = ":barber:"
layout = "centered"

# configuracion de la pagina
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

st.image("assets/Banner.jpg")
st.title("Bienvenido a la App de la Barberia ")


selected = option_menu(menu_title=None, options=["Reservar", "Ver Citas", "Servicios", "Contacto"],
                       icons=["calendar-plus", "calendar-check",
                              "scissors", "envelope"],
                       orientation="horizontal")

# RESERVAR CITAS
if selected == "Reservar":

    st.subheader("Reserva tu cita de manera facil y rapida")

    C1, C2 = st.columns(2)

    with C1:
        nombre = st.text_input("Nombre")
        fecha = st.date_input("Fecha")
        hora = st.time_input("Hora")
        servicio = st.selectbox(
            "Servicio", ["Corte de pelo", "Afeitado", "Corte de barba", "Corte de pelo y barba", "Peinados", "Tratamientos capilares", "Coloracion", "Masajes"])
        
    with C2:
        telefono = st.text_input("Telefono")
        mail = st.text_input("Email")
        comentarios = st.text_area("Comentarios")

    
    enviar = st.button("Reservar Cita")
    
    if enviar:

        if nombre == "":
                st.warning("Por favor ingresa tu nombre")
        elif telefono == "":
                st.warning("Por favor ingresa tu telefono")
        else:
                st.success("Su reserva ha sido correctamente enviada")


# VER CITAS
if selected == "Ver Citas":
    st.subheader("Citas Reservadas")
    try:
        with open("citas.txt", "r") as f:
            citas = f.readlines()
            for cita in citas:
                st.text(cita)
    except FileNotFoundError:
        st.warning("No hay citas reservadas")
    except Exception as e:
        st.error(f"Error al leer las citas: {e}")
    st.info("Si deseas eliminar una cita, por favor contacta con la barberia")


# CONTACTO
if selected == "Contacto":

    st.image("assets/map.jpg")
    st.markdown(
        "Pulsa [aqui](https://goo.gl/maps/1mX4b3r1H2z5cU5K8) para ver la ubicacion en Google Maps")

    st.subheader("Horarios")
    dia, hora = st.columns(2)
    dia.text("Lunes")
    hora.text("10:00 a 19:00")
    dia.text("Martes")
    hora.text("10:00 a 19:00")
    dia.text("Miercoles")
    hora.text("10:00 a 19:00")
    dia.text("Jueves")
    hora.text("10:00 a 19:00")
    dia.text("Viernes")
    hora.text("10:00 a 19:00")
    dia.text("Sabado")
    hora.text("10:00 a 14:00")

    st.subheader("Redes Sociales")
    st.text("Instagram: @barberia")
    st.text("Facebook: Barberia")

    st.subheader("Contacto")
    st.text("Telefono: 123-456-7890")
    st.text("Email: contacto@barberia.com")


# SERVICIOS
if selected == "Servicios":
    col1, col2, col3 = st.columns(3)

    with col1:
        servicios = st.container()
    servicios.subheader("Servicios")
    servicios.text("Corte de pelo - ")
    servicios.text("Afeitado - ")
    servicios.text("Corte de barba - ")
    servicios.text("Corte de pelo y barba - ")
    servicios.text("Peinados - ")
    servicios.text("Tratamientos capilares - ")
    servicios.text("Coloracion - ")
    servicios.text("Masajes - ")
     
    with col2:
         precios = st.container()
    precios.subheader("Precios")
    precios.text("$15")
    precios.text("$10")
    precios.text("$12")
    precios.text("$25")
    precios.text("$20")
    precios.text("$30")
    precios.text("$40")
    precios.text("$50")

    
    with col3:
        imagen = st.container() 
    imagen.subheader("Galeria de Servicios")

    imagen.image("assets/barba.jpg")
    imagen.image("assets/corte.jpg")
    imagen.image("assets/corte maquina.jpg")

    servicios.text("Consulta con nuestro equipo para servicios personalizados")

# backend

