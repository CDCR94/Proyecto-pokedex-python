import requests

def obtener_clima(ciudad, api_key):
    """
    Función para obtener el clima actual de una ciudad usando OpenWeatherMap.
    Parámetros:
        ciudad (str): Nombre de la ciudad, ej. "Cancún,mx"
        api_key (str): Tu API Key de OpenWeather
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es&units=metric"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        nombre = datos['name']
        temp = datos['main']['temp']
        sensacion = datos['main']['feels_like']
        clima = datos['weather'][0]['description']

        print(f"📍 Ciudad: {nombre}")
        print(f"🌡️ Temperatura: {temp} °C")
        print(f"🤔 Sensación térmica: {sensacion} °C")
        print(f"☁️ Clima: {clima}")

    else:
        print(f"❌ Error {respuesta.status_code}: {respuesta.text}")


# -----------------------
# EJEMPLO DE USO:
# -----------------------

API_KEY = "0eff9765ba0aa9db7c88d5c4c947f325"   # 
ciudad = "Villahermosa,mx"          # 

obtener_clima(ciudad, API_KEY)