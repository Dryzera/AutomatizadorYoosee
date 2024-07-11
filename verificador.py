import psutil
import pyautogui as pa
import time

pa.PAUSE = 5
pa.FAILSAFE = False
time.sleep(15)


while True:
    flag_not_open = None
    
    def verifica_aberto():
        while True:
            time.sleep(10)
            if not "Yoosee.exe" in (i.name() for i in psutil.process_iter()):
                flag_not_open = True
                return flag_not_open
        
    verificando = False
    verificando = verifica_aberto

    if verificando() is True:
        pa.hotkey('win', 'r')
        pa.write('E:\\Yoosee')
        pa.press('enter')
        pa.hotkey('win', 'up')


    