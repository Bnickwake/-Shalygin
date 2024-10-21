# Шалыгин Никита ФПэ-01-22

import numpy as np
import matplotlib.pyplot as plt
import iapws
from iapws import IAPWS97 as gas
import os

MPa = 10 ** 6
kPa = 10 ** 3
unit = 1 / MPa
grad_Cels = 1
                  #Задача 1
#Построить график зависимости термического КПД паротурбинного цикла без промежуточного перегрева пара при следующих параметрах пара:
# 𝑃0 = 5, 10, 15, 20 МПа. Для каждого значения взять следующие значения температуры
# 𝑡0= 300, 350, 400, 450, 500 градусов Цельсия,
# 𝑃𝑘= 5 кПа. Принять давление за последней ступенью паровой турбины
# 𝑃2=𝑃𝑘. Термический КПД цикла оценивать без учета подогрева воды в питательном насосе и регенеративной системе.

# масивы значений давления и темпратуры



def kpd(PO,TO,PK):
        point_0 = gas(P = PO * unit, T = (TO + 273.15))
        point_condenser_inlet = gas(P = (PK * unit) , s = point_0.s)
        point_pump_outlet = gas(P = (PK * unit), x = 0)
        useful_energy = point_0.h - point_condenser_inlet.h
        full_energy = point_0.h - point_pump_outlet.h
        kpd_value = (useful_energy / full_energy) * 100
        return kpd_value
# функция kpd вычисляет значение термического кпд используя параметры p0, t0 и pk


p0 = np.array([5 * MPa, 10 * MPa, 15 * MPa, 20 * MPa]) # Мега Паскаль
t0 = np.array([300, 350, 400, 450 ,500]) # Градус Цельсия
pk = 5 * kPa


for P0 in p0:
    KPD = []
    for T0 in t0:
        kpd_value = kpd(P0, T0, pk)
        KPD.append(kpd_value)
    plt.xlabel("t0, градусы Цельсия")
    plt.ylabel("Термический КПД, %")
    plt.title("График зависимости термического КПД от to")
    plt.plot(t0,KPD, label = f"При P0 = {P0 * unit} МПа")
plt.grid()
plt.legend()
# Определяем путь к рабочему столу
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Определяем путь к папке "в гитхаб", так называется моя папка с графиками
folder_name = "в гитхаб"
folder_path = os.path.join(desktop_path, folder_name)

# Проверяем, существует ли папка "в гитхаб"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Форматируем путь к файлу
file_path = os.path.join(folder_path, 'dz1graf1.png')

# Сохраняем график в указанной папке (это перезапишет файл, если он существует)
plt.savefig(file_path)
plt.show()





                # Задача 2
# Построить график зависимости термического КПД паротурбинного цикла без промежуточного перегрева пара при следующих параметрах пара:
# 𝑃0= 5 МПа,
# 𝑡0= 450 градусов Цельсия,
# 𝑃𝑘= 5, 10, 15, 20, 50 кПа. Принять давление за последней ступенью паровой турбины
# 𝑃2= 𝑃𝑘. Термический КПД цикла оценивать без учета подогрева воды в питательном насосе и регенеративной системе.


# Значение давления и темпратуры
p0 = 5 * MPa  #мега паскаль
t0 = 450 #градусы цельсия
pk = np.array([5 * kPa, 10 * kPa, 15 * kPa, 20 * kPa, 50 * kPa]) # Кило Паскаль
# 1) KPD- массив КПД
KPD = []
for Pk in pk:
    kpd_value = kpd(p0, t0, Pk)
    KPD.append(kpd_value)
plt.xlabel("Pk, Па")
plt.ylabel("Термический КПД, %")
plt.title("График зависимости термического КПД от Pk")
plt.plot(pk,KPD, label = f"При P0 = {p0 * unit} (МПа) и температуре t0= {t0} (градус Цельсия)")
plt.grid()
plt.legend( loc='upper left')

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

folder_name = "в гитхаб"
folder_path = os.path.join(desktop_path, folder_name)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_path = os.path.join(folder_path, 'dz1graf2.png')

plt.savefig(file_path)
plt.show()

