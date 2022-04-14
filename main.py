import numpy as np
import threading
import time

def tempatual(nome, temp):
    auxprint = f"--------Temperatura atual--------\n" + \
               f"Sensor {nome} está em {temp}°C\n" + \
               f"----------------------------------\n"
    print(auxprint)

def umidificador(nome, temp, intervalo):
    tempatual(nome, temp)
    print(f"Sensor {nome} requisitou a ligação do umidificador")
    while temp > 28:
        temp -= round(np.random.uniform(1.25, 2.3), 2)
        auxprint = f"-----------------------Umidificador e Ventoinha-------------------------\n" + \
        f"Temperatura no sensor {nome} diminuindo. T = {temp}ºC\n" + \
        f"Ambiente mais úmido\n" + \
        f"-----------------------------------------------------------------------------------\n"
        print(auxprint)
        time.sleep(intervalo)
    return temp

def aquecedor(nome, temp, intervalo):
    tempatual(nome, temp)
    print(f"Sensor {nome} requisitou a ligação do aquecedor")
    while temp < 18:
        temp += round(np.random.uniform(0.6, 1.5), 2)
        auxprint = f"--------------------Aquecedor---------------------\n" + \
                   f"Temperatura no sensor {nome} aumentando. T = {temp}ºC\n" + \
                   f"--------------------------------------------------\n"
        print(auxprint)
        time.sleep(intervalo)
    return temp

def ventoinha(nome, temp, intervalo):
    tempatual(nome, temp)
    print(f"Sensor {nome} requisitou a ligação da ventoinha")
    while temp > 24:
        temp -= round(np.random.uniform(0.6, 1.5), 2)
        if bool(np.random.randint(0, 1)):
            temp += round(np.random.uniform(0.6, 0.9), 2)
            auxprint = "--------------------Ventoinha---------------------\n" + \
                       f"Temperatura no sensor {nome} baixando. T = {temp}ºC\n" + \
                       f"--------------------------------------------------\n"
            print(auxprint)
            break

        auxprint = "--------------------Ventoinha---------------------\n" + \
                   f"Temperatura no sensor {nome} baixando. T = {temp}ºC\n" + \
                   f"--------------------------------------------------\n"
        print(auxprint)
        time.sleep(intervalo)
    return temp

#Sensor virtual
def SensorTemp(nome, intervalo):
    temp = round(np.random.uniform(16, 25), 2)
    while True:
        min, max = temp*0.8, temp*1.2
        temp = round(np.random.uniform(min, max), 2)
        if temp > 28:
            temp = umidificador(nome, temp, intervalo)
        elif temp >= 25:
            temp = ventoinha(nome, temp, intervalo)
        elif 18 <= temp < 24:
            auxprint = f"-------Temperatura ambiente-------\n" + \
                       f"Sensor {nome} está em {temp}°C\n" + \
                       f"----------------------------------\n"
            print(auxprint)
        else:
            temp = aquecedor(nome, temp, intervalo)
        time.sleep(intervalo)


#Gerando os sensores virtuiais
aux1 = ["Inatel", "Casa Camila", "Casa Matheus"]
for i in range(3):
    nome = aux1[i]
    x = threading.Thread(target=SensorTemp, args=(nome, 4))
    x.start()
