import os; os.system('cls' if os.name=='nt' else 'clear'); print('\n'); print("BOT \033[31mtyping-app.fly.dev\033[0m BY \033[36mluxz#8403\033[0m".center(os.get_terminal_size().columns)); print('\n')
from selenium import webdriver
from selenium.webdriver.common.by import By
import time , pyautogui , datetime , pytz

driver = webdriver.Firefox()
driver.set_window_size(900,650)
driver.get('https://typing-app.fly.dev/')
time.sleep(2)
elements = driver.find_elements(By.CLASS_NAME, "_wordWrapper_1ew2v_13")
word_type_list = ''
for element in elements:
    text_value = element.text
    word_type_list += text_value
    word_type_list += ' '

print(f'\033[32mWord :\033[0m {word_type_list}')
print(f'============================================')
time.sleep(1)
pyautogui.click(x=170,y=255)
wordnumbercheck = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/div[1]/p').text.split("/")
delay = None
if int(wordnumbercheck[1]) <= 12:
    delay = 0.03
else:
    delay = 0.001

print(f'\033[94m[{datetime.datetime.now(pytz.timezone("Asia/Bangkok")).strftime("%H:%M:%S.%f")[:-3]}]\033[0m Start typing.... (Delay {delay})')
pyautogui.write(word_type_list,interval=delay)


print(f'\033[94m[{datetime.datetime.now(pytz.timezone("Asia/Bangkok")).strftime("%H:%M:%S.%f")[:-3]}]\033[0m Successfully!')
print(f'============================================')

wpm = driver.find_element(By.XPATH , '/html/body/div/main/div/div/div[1]/div[1]/div[1]/p[2]')
accuracy = driver.find_element(By.XPATH , '/html/body/div/main/div/div/div[1]/div[1]/div[2]/div/div[3]/p')
times = driver.find_element(By.XPATH , '/html/body/div/main/div/div/div[2]/div[1]/div[4]/p[2]')
error = driver.find_element(By.XPATH , '/html/body/div/main/div/div/div[2]/div[1]/div[3]/p[2]')

print(f'\033[93mWPM\033[0m : {wpm.text}')
print(f'\033[93mAccuracy\033[0m : {accuracy.text}')
print(f'\033[93mError\033[0m : {error.text}')
print(f'\033[93mTime\033[0m : {times.text}')
print(f'============================================')

driver.close()