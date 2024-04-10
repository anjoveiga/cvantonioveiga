import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Función para realizar el raspado web y analizar el HTML
def analizar_url(url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    html = driver.page_source
    driver.quit()
    sopa = BeautifulSoup(html, 'html.parser')
    
    resultados = []
    for i in range(1, 7):
        etiquetas_h = sopa.find_all(f'h{i}')
        titulos = [etiqueta.text.strip() for etiqueta in etiquetas_h]
        resultados.append((f'h{i}', len(etiquetas_h), titulos))
    
    return resultados

# Función que crea una ventana para mostrar los resultados
def mostrar_resultados(resultados):
    window = tk.Tk()
    window.title("Resultados del Análisis")
    window.configure(bg='yellow')  # Color de fondo amarillo fosforescente
    
    for nivel, cantidad, titulos in resultados:
        tk.Label(window, text=f"{nivel}: {cantidad}", bg='yellow').pack()
        if titulos:
            lista_titulos = tk.Text(window, height=6, width=50)
            lista_titulos.insert(tk.END, '\n'.join(titulos))
            lista_titulos.pack()
        tk.Label(window, text="", bg='yellow').pack()  # Espaciador
    
    window.mainloop()

# Función que crea una ventana para solicitar la URL
def solicitar_url():
    window = tk.Tk()
    window.title("Análisis Web")
    window.configure(bg='yellow')  # Color de fondo verde fosforescente

    tk.Label(window, text="Introduce la URL de la universidad a analizar:", bg='yellow').pack()
    url_entry = tk.Entry(window, width=50)
    url_entry.pack()

    def on_submit():
        url = url_entry.get()
        window.destroy()  # Cierra la ventana de solicitud
        resultados = analizar_url(url)
        mostrar_resultados(resultados)

    submit_btn = tk.Button(window, text="Analizar", command=on_submit)
    submit_btn.pack()

    window.mainloop()

# Ejecutar la función principal
solicitar_url()
