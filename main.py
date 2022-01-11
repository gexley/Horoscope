from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Path = "/Applications/chromedriver"
driver = webdriver.Chrome(Path)
horoscopesList = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius","pisces"]

def getText(sign):
    url = "https://www.elle.com/horoscopes/daily/" + sign + "-daily-horoscope/"
    driver.get(url)
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main"))
        )

        body = main.find_element(By.XPATH, "/ html / body / main / div[6] / div[1] / div[2] / p[1]")
        return body.text
    except:
        print("didnt find")
        driver.quit()

def allHoroscopes():
    for sign in horoscopesList:
        print(sign.capitalize() + ":")
        print(getText(sign))
        print("\r\n")
        driver.quit

def getSign(bday):
    "5/7/2004"
    bday.index("/")


allHoroscopes()




