from PIL import Image
from customtkinter import *

set_appearance_mode("light")

# Listar de IP que posso adcionar dentro dicionario
data = {
    
    'AVIAO': '10.0.1.254',
    'PARA': '10.0.1.253',   
    'CASAMAE ': '10.0.1.252',
    'NEGOLISO': '10.0.1.251',
    'MUSEU MAC': '10.0.1.250',
    'NEGODOIDO ': '10.0.1.249',
    'LEO': '10.0.1.248',
    'Nado': '10.0.1.247',
    'Erick': '10.0.1.246',
    'Marcelo': '10.0.1.245',    
}


janela = CTk()
janela.title('Acesso facilitado')


janela.geometry('300x250')

image_path = os.path.join(os.path.dirname(__file__), 'logo.png')

image = CTkImage(light_image = Image.open(image_path), size=(100, 100))

image_label = CTkLabel(janela, image=image, text='')



def clique():
    nome = checkbox.get()
    ip = ( data.get(nome))
    os.popen(f'explorer http://{ip}')


image_label.pack()

label = CTkLabel(janela,text="Endereços: ", font=('arial bold',12))
label.pack()

#Lista de acesso para ser utilizado no ComboBox

acessos = [ 'AVIAO',
    'PARA',
    'CASAMAE' ,
    'NEGOLISO',
    'MUSEU MAC',
    'NEGODOIDO',
    'LEO',
    'Nado',
    'Erick',
    'Marcelo',]

checkbox = CTkComboBox(janela,values=(acessos))
checkbox.pack(padx=10,pady=10)

botao = CTkButton(janela,text='Acessar',command=clique)
botao.pack(padx=10,pady=10)


nome = CTkLabel(janela,text="Desenvolvido por LSRAMOS", font=('arial',9))
nome.pack()

janela.mainloop()