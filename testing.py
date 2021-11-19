import numpy as np
from PIL import Image, ImageTk
import PySimpleGUI as sg


def adapta_imagem(img, shape, max_val=1):
    '''
    Função que adapta a imagem para o range e o tipo correto.
    '''
    img = (img - img.min())/(img.max() - img.min())
    
    if max_val > 1:
        img *= max_val
        return img.reshape(shape).astype(np.uint8)
    
    else:
        return img.reshape(shape)


# Carregando a média e os autovalores:
autovetores = np.load('eigenvectors.npy')
mean = np.load('mean.npy')
mean = (mean - mean.mean())/mean.std() # Padronizando a média


# Iniciando montagem da GUI
sg.theme('Dark')

# Coluna com as barras deslizantes dos componentes principais
sliders_column = [
    [sg.Text("Componentes Principais")],
    [sg.Button("Aleatório", button_color='blue', size=(14, 1), key=("Button_Random")), sg.Button("Reset", button_color='green', size=(14, 1), key=("Button_Reset"))],
    [sg.Slider(range=(-255, 255), default_value=0, resolution=5, orientation='h', size=(30, 10), key="PC1")],
    [sg.Slider(range=(-255, 255), default_value=0, resolution=5, orientation='h', size=(30, 10), key="PC2")],
    [sg.Slider(range=(-255, 255), default_value=0, resolution=5, orientation='h', size=(30, 10), key="PC3")],
    [sg.Slider(range=(-255, 255), default_value=0, resolution=5, orientation='h', size=(30, 10), key="PC4")],
    [sg.Slider(range=(-255, 255), default_value=0, resolution=5, orientation='h', size=(30, 10), key="PC5")],
    [sg.Slider(range=(-255, 255), default_value=0, resolution=5, orientation='h', size=(30, 10), key="PC6")],
    [sg.Slider(range=(-255, 255), default_value=0, resolution=5, orientation='h', size=(30, 10), key="PC7")],
    [sg.Slider(range=(-255, 255), default_value=0, resolution=5, orientation='h', size=(30, 10), key="PC8")],
    [sg.Slider(range=(-255, 255), default_value=0, resolution=5, orientation='h', size=(30, 10), key="PC9")],
    [sg.Slider(range=(-255, 255), default_value=0, resolution=5, orientation='h', size=(30, 10), key="PC10")]
]

# Coluna de exibição da imagem
image_column = [
    [sg.Text(text="Media + Componentes*Autovetores")],
    [sg.Image(key="IMAGE")]
]

# Layout completo
layout = [
    [
    sg.Column(sliders_column),
    sg.VSeparator(),
    sg.Column(image_column)
    ]
]

# Definindo janela da GUI
window = sg.Window("EigenFaces - Cats", layout)

last_values = None

# Iniciando loop de leitura da janela
while True:
    
    event, values = window.read(timeout=20)

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if values != last_values:
        
        comps = np.array([[values[f"PC{i}"] for i in range(1,11)]])
        
        img = comps@autovetores + mean
        img = adapta_imagem(img, (64, 64, 3), 255)
        
        img = Image.fromarray(img)
        
        img = img.resize((128, 128))
        
        img = ImageTk.PhotoImage(img)
        
        window["IMAGE"].update(data=img)

        last_values = values
    
    if event == 'Button_Random':
        for i in range(1,11):
            window[f'PC{i}'].update(np.random.randint(-255, 255))

    if event == 'Button_Reset':
        for i in range(1,11):
            window[f'PC{i}'].update(0)