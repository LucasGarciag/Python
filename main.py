import pyautogui

##Cria pasta numa tela com resolução de 1280x1024
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.hotkey('win', 'm')
pyautogui.moveTo(640, 512, duration=1)
pyautogui.rightClick()
pyautogui.moveTo(650, 745, duration=1)
pyautogui.click()
pyautogui.moveTo(1000, 745, duration=1)
pyautogui.moveTo(1000, 450, duration=1)
pyautogui.click()
pyautogui.write('Pasta do cabrito', interval=0.25)
pyautogui.press('enter')
