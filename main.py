import pygame
import random

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
szerokosc = 640
wysokosc = 480
ekran = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("Ping Pong")

# Kolory
czarny = (0, 0, 0)
bialy = (255, 255, 255)

# Inicjalizacja paletki
paletka_szerokosc = 10
paletka_wysokosc = 80
paletka1_x = 30
paletka2_x = szerokosc - 30 - paletka_szerokosc
paletka1_y = wysokosc // 2 - paletka_wysokosc // 2
paletka2_y = wysokosc // 2 - paletka_wysokosc // 2
paletka1_predkosc = 0
paletka2_predkosc = 0

# Inicjalizacja piłki
pilka_szerokosc = 10
pilka_predkosc_x = 0.1
pilka_predkosc_y = 0.1
pilka_x = szerokosc // 2 - pilka_szerokosc // 2
pilka_y = wysokosc // 2 - pilka_szerokosc // 2

# Główna pętla gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Obsługa klawiatury
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paletka1_predkosc = -0.2
            if event.key == pygame.K_s:
                paletka1_predkosc = 0.2
            if event.key == pygame.K_UP:
                paletka2_predkosc = -0.2
            if event.key == pygame.K_DOWN:
                paletka2_predkosc = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paletka1_predkosc = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paletka2_predkosc = 0

    # Aktualizacja pozycji paletek i piłki
    paletka1_y += paletka1_predkosc
    paletka2_y += paletka2_predkosc
    pilka_x += pilka_predkosc_x
    pilka_y += pilka_predkosc_y

    # Odbicie piłki od górnej i dolnej ściany
    if pilka_y <= 0 or pilka_y >= wysokosc - pilka_szerokosc:
        pilka_predkosc_y *= -1

    # Odbicie piłki od paletki
    if pilka_x <= paletka1_x + paletka_szerokosc and \
            paletka1_y <= pilka_y <= paletka1_y + paletka_wysokosc:
        pilka_predkosc_x *= -1
    elif pilka_x >= paletka2_x - pilka_szerokosc and \
            paletka2_y <= pilka_y <= paletka2_y + paletka_wysokosc:
        pilka_predkosc_x *= -1

    # Piłka przekroczyła linię bramki
    if pilka_x <= 0 or pilka_x >= szerokosc - pilka_szerokosc:
        pilka_x = szerokosc // 2 - pilka_szerokosc // 2
        pilka_y = wysokosc // 2 - pilka_szerokosc // 2
        pilka_predkosc_x = 0.1
        pilka_predkosc_y = 0.1

    # Wyczyszczenie ekranu
    ekran.fill(czarny)

    # Rysowanie paletek i piłki
    pygame.draw.rect(ekran, bialy, (paletka1_x, paletka1_y, paletka_szerokosc, paletka_wysokosc))
    pygame.draw.rect(ekran, bialy, (paletka2_x, paletka2_y, paletka_szerokosc, paletka_wysokosc))
    pygame.draw.ellipse(ekran, bialy, (pilka_x, pilka_y, pilka_szerokosc, pilka_szerokosc))

    # Aktualizacja pozycji paletki gracza 1
    paletka1_y += paletka1_predkosc

    # Sprawdź, czy paletka gracza 1 nie wychodzi poza górny i dolny kraniec ekranu
    if paletka1_y < 0:
        paletka1_y = 0
    elif paletka1_y > wysokosc - paletka_wysokosc:
        paletka1_y = wysokosc - paletka_wysokosc

    # Aktualizacja pozycji paletki gracza 2
    paletka2_y += paletka2_predkosc

    # Sprawdź, czy paletka gracza 2 nie wychodzi poza górny i dolny kraniec ekranu
    if paletka2_y < 0:
        paletka2_y = 0
    elif paletka2_y > wysokosc - paletka_wysokosc:
        paletka2_y = wysokosc - paletka_wysokosc

    # Aktualizacja ekranu
    pygame.display.update()


