import os; os.system('cls' if os.name=='nt' else 'clear'); print('\n'); print("BOT \033[31mtyping-app.fly.dev\033[0m BY \033[36mluxz#8403\033[0m".center(os.get_terminal_size().columns)); print('\n')
from selenium import webdriver
from selenium.webdriver.common.by import By
import time , pyautogui , datetime , pytz
from bs4 import BeautifulSoup

code = input("Input Room code : ")
delay = float(input("Input Delay (default = 0) : ") or 0)
print(f'============================================')

driver = webdriver.Firefox()
driver.set_window_size(900,650)
driver.get('https://typing-app.fly.dev/')

time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="root"]/header/div/div[2]/button[2]').click()
driver.find_element(By.XPATH,'//*[@id="modal"]/div[2]/div[3]/form/div/input').send_keys(code)
driver.find_element(By.XPATH,'//*[@id="modal"]/div[2]/div[3]/form/button').click()

while True:
    try:
        if driver.find_element(By.XPATH,'//*[@id="root"]/main/div/span').text == 'GO!':
            break
    except:
        pass

soup = BeautifulSoup(driver.page_source, 'html.parser')
word_type_list = ''
for i in soup.find_all(class_="_wordWrapper_1ew2v_13"):
    word_type_list += i.get_text()
    word_type_list += ' '

print(f'\033[32mWord :\033[0m {word_type_list}')
print(f'============================================')

time.sleep(0.5)
pyautogui.click(x=170,y=255)

strat_time = datetime.datetime.now(pytz.timezone("Asia/Bangkok")).strftime("%H:%M:%S.%f")[:-3]
print(f'\033[94m[{strat_time}]\033[0m Start typing....')

pyautogui.write(word_type_list,interval=0)

succ_time = datetime.datetime.now(pytz.timezone("Asia/Bangkok")).strftime("%H:%M:%S.%f")[:-3]
print(f'\033[94m[{succ_time}]\033[0m Successfully!')
print(f'============================================')

times = str(datetime.datetime.strptime(succ_time, "%H:%M:%S.%f") - datetime.datetime.strptime(strat_time, "%H:%M:%S.%f"))
print(f'\033[93mTime\033[0m : {times[:-3]}')
print(f'============================================')