import cv2
import numpy as np
import time
import pyautogui

ekran_boyutu = (1920,1080)
cc = cv2.VideoWriter_fourcc(*"XVID")
veri =  cv2.VideoWriter("cıkıs.avi",cc,20.0,(ekran_boyutu))

fps = 30
prev = 0

while True:
    zamancekildi = time.time() - prev
    foto = pyautogui.screenshot()
    if zamancekildi> 1.0/fps:
        prev = time.time()
        frame = np.array(foto)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        veri.write(frame)

    cv2.waitKey(100)


cv2.destroyAllWindows()
veri.release()