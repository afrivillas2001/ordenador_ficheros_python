import os, shutil

extenciones = {
    "Fotos": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tif'],
    "Word": ['.doc', '.docm', '.docx', '.dot', '.dotm', '.dotx', '.odt', '.rtf', '.wps'],
    "Excel": ['.csv', '.dbf', '.dif', '.ods', '.prn', '.slk', '.xla', '.xlam', '.xls', '.xlsb', '.xlsm', '.xlsx', '.xlt', '.xltm', '.xltx', '.xlw', '.xps'],
    "Pdf": ['.pdf'],
    "Powerpoint": ['.emf', '.odp', '.pot', '.potm', '.potx', '.ppa', '.ppam', '.pps', '.ppsm', '.ppsx', '.ppt', '.pptm', '.pptx'],
    "Ejecutables": ['.exe', '.dll', '.pif', '.cmd', '.wsf', '.air', '.vb', '.bat', '.gadget', '.app', '.ds', '.dsa'],
    "videos": ['.mp4', '.mpeg', '.mov', '.wmv', '.avi', '.avchd']
}

def crearCarpetas(path):
    xts = obtenerExtenciones(path)
    for i in extenciones.keys():
        for k in xts:
            if k in extenciones[i] and not os.path.exists(path+i):
               os.mkdir(path+i)

def ordenar(path, archivo, ext):
    for i in extenciones.keys():
        if ext in extenciones[i]:
            try:
                 shutil.move(path+archivo, path+i)
            except:
                print(f"Ocurrio un erro {archivo}") 

def obtenerExtenciones(path):
    xts = []
    for i in os.listdir(path):
        ext = os.path.splitext(i)[1]
        if ext not in extenciones and ext != "":
            xts.append(ext)
    return xts

def process(path):
    crearCarpetas(path)
    for archivo in os.listdir(path):
        ext  = os.path.splitext(archivo)[1]
        ordenar(path, archivo, ext)

while True:    
    path = input("Ingrese la direccion de la carpeta a ordenar: ")
    if os.path.exists(path):
        path += "/"
        break
    else:
        print("error, el path ingresado no existe")

process(path)
print("Proceso finalizado!!!")
    
