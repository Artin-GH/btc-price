from selenium import webdriver
from selenium.webdriver.common.by import By
import pygame
from threading import Thread


def set_price_thread():
    global price
    driver.get(url)
    while True:
        price = driver.find_element(By.XPATH, xpath).text


def label(text: str):
    return font.render(text, True, "red")


xpath = "//*[@id=\"anchor-page-1\"]/div/div[3]/div[1]/div/div/div/div[1]/div[1]"
url = "https://www.tradingview.com/symbols/BTCUSD/"
price = "Opening website..."

driver_options = webdriver.ChromeOptions()
driver_options.headless = True
driver = webdriver.Chrome(options=driver_options)

pygame.init()
window_caption = "BTC Price (Project - X)"
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption(window_caption)

running = True
font = pygame.font.SysFont("Helvetica", 50, True)
price_label = label(price)

Thread(target=set_price_thread).start()


while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    price_label = label(price)
    screen.blit(price_label, (screen.get_width() / 2 - price_label.get_width() / 2,
                              screen.get_height() / 2 - price_label.get_height() / 2))

    pygame.display.update()

pygame.quit()
driver.quit()
