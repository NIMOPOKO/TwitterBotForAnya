from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
import time
import urllib
import cv2
# seleniumを起動
ChromeOptions = webdriver.ChromeOptions()
#ChromeOptions.add_argument('--headless')
ChromeOptions.add_argument('--no-sandbox')
ChromeOptions.add_argument('--disable-dev-shm-usage')
ChromeOptions.add_argument('window-size=1440,990')
ChromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])

CHROMEDRIVER = "..\driver\chromedriver"
chrome_service = fs.Service(executable_path=CHROMEDRIVER)

driver = webdriver.Chrome(service=chrome_service,options=ChromeOptions)
upload_username = ""
def login_twitter(account, password):
    # ログインページを開く
    driver.get('https://twitter.com/login/')
    time.sleep(3)

    # account入力
    element_account = driver.find_element(By.NAME,'text')
    element_account.send_keys(account)
    time.sleep(3)
    element_login = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
    element_login.click()
    time.sleep(3)
    element_pass = driver.find_element(By.NAME,"password")
    element_pass.send_keys(password)
    time.sleep(3)
    element_login = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
    element_login.click()
    time.sleep(3) 
def send_tweet(text):
    driver.get('https://twitter.com/home')
    time.sleep(3)
    # テキスト入力
    element_text = driver.find_element(By.CLASS_NAME,"notranslate")
    element_text.click()
    element_text.send_keys(text)
    time.sleep(3)
    # ツイートボタン
    tweet_button = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
    driver.execute_script("arguments[0].click();", tweet_button)
    time.sleep(3)

def jump_my():
    driver.get('https://twitter.com/home')
    time.sleep(3)
    profile_button = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div')
    driver.execute_script("arguments[0].click();", profile_button)
    time.sleep(3)
def click_kotei():
    settei_button = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div/div/div')
    driver.execute_script("arguments[0].click();", settei_button)
    time.sleep(3)
    kotei_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div[2]/div[2]/div')
    driver.execute_script("arguments[0].click();", kotei_button)
    time.sleep(3)
    kettei_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span/span')
    driver.execute_script("arguments[0].click();", kettei_button)
    time.sleep(3)

def jump_kotei():
    jump_my()
    kotei_tweet = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/div/article/div')
    driver.execute_script("arguments[0].click();", kotei_tweet)
    time.sleep(3)

def init():
    str_textname = "写真リプライで画像処理するます！起きた時間：" + str(time.time())
    send_tweet(str_textname)
    jump_my()
    click_kotei()
    jump_my()
    click_kotei()
    jump_kotei()



login_twitter("Anya_Image","suzuki")
init()

def picture_import():
    tweet_user = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[3]/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/a/div/span')
    picture_tweet = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[3]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div/div/div/div/a/div/div[2]/div/img')
    src = picture_tweet.get_attribute('src')
    with urllib.request.urlopen(src)as rf:
        data = rf.read()
    # with open()構文を使ってバイナリデータをpng形式で書き出す
    with open(".\\picture\\import.png", mode="wb")as wf:
        wf.write(data)
    time.sleep(3)
    return tweet_user.text

def picture_rapu():
    img = cv2.imread(".\\picture\\import.png")
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    dst = cv2.Laplacian(gray, cv2.CV_32F, ksize=3)
    cv2.imwrite(".\\result\\result.png", dst)

def picture_tweet(name):
    driver.get('https://twitter.com/home')
    time.sleep(3)
    # テキスト入力
    str_text = name
    element_text = driver.find_element(By.CLASS_NAME,"notranslate")
    element_text.click()
    element_text.send_keys(str_text)

    image_file_path = "C:\\Users\\nimon\\3D Objects\\python\\twitter\\testvenv\\Scripts\\result\\result.png"
    driver.find_element(By.XPATH,'//input[@type="file"]').send_keys(image_file_path)

    tweet_button = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
    driver.execute_script("arguments[0].click();", tweet_button)
    time.sleep(5)

def tweet_delete():
    settei_button = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[3]/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div/div/div')
    driver.execute_script("arguments[0].click();", settei_button)
    time.sleep(3)
    hihyouji_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div[6]/div[2]/div/span')
    driver.execute_script("arguments[0].click();", hihyouji_button)
    time.sleep(3)
    hihyouji_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div/span/span')
    driver.execute_script("arguments[0].click();", hihyouji_button)
    time.sleep(3)
    

while True:
    jump_kotei()
    try:
        upload_username = picture_import()
        tweet_delete()
        picture_rapu()
        picture_tweet(upload_username)
    except:
        time.sleep(10)