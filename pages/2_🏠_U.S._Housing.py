import streamlit as st

# Diccionario para almacenar los datos de los usuarios registrados
user_database = {}

def main():
    st.title("Aplicación de Registro e Inicio de Sesión")

    menu = ["Inicio", "Registro", "Inicio de Sesión"]
    choice = st.sidebar.selectbox("Menú", menu)

    if choice == "Inicio":
        st.subheader("Inicio")
        st.write("Bienvenido a nuestra aplicación web. Por favor, regístrese o inicie sesión.")

    elif choice == "Registro":
        st.subheader("Registro")
        username = st.text_input("Nombre de usuario")
        password = st.text_input("Contraseña", type="password")

        if st.button("Registrarse"):
            if username and password:
                if username in user_database:
                    st.error("El nombre de usuario ya existe. Por favor, elija otro.")
                else:
                    user_database[username] = password
                    st.success("Registro exitoso. Ahora puede iniciar sesión.")
            else:
                st.warning("Por favor, ingrese un nombre de usuario y una contraseña.")

    elif choice == "Inicio de Sesión":
        st.subheader("Inicio de Sesión")
        username = st.text_input("Nombre de usuario")
        password = st.text_input("Contraseña", type="password")

        if st.button("Iniciar Sesión"):
            if username in user_database and user_database[username] == password:
                st.success(f"Bienvenido, {username}! Sesión iniciada correctamente.")
            else:
                st.error("Nombre de usuario o contraseña incorrectos.")

if __name__ == '__main__':
    main()
