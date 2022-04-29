import pyautogui
import time
 
def click(): 
    #time.sleep(0.1)     
    pyautogui.click()
 
def main():
    for i in range(500): 
        click()
 
main()
#Test