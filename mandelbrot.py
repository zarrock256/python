import pygame
import math

#Podstawowe parametry programu
width = 800
height = 600
leftBorder = -2
rightBorder = 1
topBorder = 1
bottomBorder = -1
cycles = 100    #Określa z jaką dokładnością badamy granicę ciagu dla danej liczby zespolonej

#Zainicjowanie okienka programu
pygame.init()

#Ustawienie parametrów okna
screen = pygame.display.set_mode((800,600))

#Tytuł okna
pygame.display.set_caption("Fraktal Mandelbrota")

#Pętla działania programu
running = True

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

for i in range(1,width+1):
        for j in range(1,height+1):

            complex0 = complex(leftBorder + ((rightBorder - leftBorder) / width) * i,   #Podzielenie liczb zespolonych
                               bottomBorder + ((topBorder - bottomBorder)/height) * j)  #na odpowiedniki waględem
                                                                                        ##wyświetlanych pikseli
            complex1 = 0
            n = 0
            while abs(complex1) < 2 and n < cycles:         #Sprawdzanie warunku dla liczb ze zbioru Mandelbrota
                complex1 = complex1 * complex1 + complex0
                n += 1

            color = int(n * 255 / cycles)                   #Nadanie koloru konkretnym pikselom
            color1 = int(n*150/cycles)
            color2 = int(n*100/cycles)
            pygame.draw.rect(screen,(color,color1,color2), (i+1,j+1, 1, 1)) #Rysowanie pikseli

pygame.display.update()     
while running:
    if event.type == pygame.QUIT:
        running = False