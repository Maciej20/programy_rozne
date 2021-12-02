#Prosta gra

import math
import pygame
from pygame.locals import ( 
    KEYDOWN,
    K_SPACE,
    MOUSEBUTTONDOWN,
)
import time

pygame.init()
screen = pygame.display.set_mode([500, 600])
running = True
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(str(0), True, (0,0,0), (0,255,0))
textRect = text.get_rect()


class Game:
    def __init__(self, radius, colours, position):
        self.radius = radius
        self.colours = colours
        self.position = position

    def getposition(self):
        return self.position
    
    def rotate(self, speed):
        self.position = self.position + speed
        if self.position >= 2*math.pi*self.radius:
            self.position = self.position - 2*math.pi*self.radius
        #print(self.position)
    
    def drawcircle(self):
        pygame.draw.circle(screen, a.colours, (250,250), a.radius)
        #pygame.draw.line(screen, (0,0,0), (250, 250),(250,325), width=3)

    def drawlines(self, line_position):
        pygame.draw.line(screen, (0,255,0), (250, 250),(250+2*self.radius*math.sin(line_position/self.radius), 
                        250+2*self.radius*math.cos(line_position/self.radius)), width=3)
    
    def drawnewline(self):
        pygame.draw.line(screen, (0,255,0), (250, 250),(250+2*self.radius*math.sin(0/self.radius), 
                                250+2*self.radius*math.cos(0/self.radius)), width=3)
    

class Arrow:
    def __init__(self, length, linepos):
        self.linepos = linepos
        self.length = length
    
    def drawnewarrow(self):
        pygame.draw.line(screen, (0,255,0), (250, 250),(250+2*self.length*math.sin(self.linepos/self.length), 
                        250+2*self.length*math.cos(self.linepos/self.length)), width=3)
        pygame.draw.circle(screen, (0,255,00), (250+2*self.length*math.sin(self.linepos/self.length), 
                        250+2*self.length*math.cos(self.linepos/self.length)), 10)
    
    def rotation(self, speed):
        self.linepos = self.linepos + speed
        if self.linepos >= 2*math.pi*self.length:
            self.linepos = self.linepos - 2*math.pi*self.length


def downarrow():
    pygame.draw.line(screen, (0,255,0), (250,425), (250,525),width=3)
    pygame.draw.circle(screen, (0,255,0),(250,525), 10)

def newgame():
    global lost, lines, arrows, score, position
    lost = False
    lines = [0]
    lines.sort()
    arrows = []
    for line in lines:
        arrows.append(Arrow(75,line))
    score = 0
    a.position = 0
    
a = Game(75, (0,255,0), 0)
newgame()

while running:
    while lost == False:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                lost = True

            if event.type == KEYDOWN:
                lines.append(a.getposition())
                arrows.append(Arrow(75,0))
                score   += 1

            if event.type == MOUSEBUTTONDOWN:
                lines.append(a.getposition())
                arrows.append(Arrow(75,0))
                score += 1

            try:
                for line in lines[:-1]:
                    if abs(lines[-1] - line) <= 10:
                        lost = True
                    
                lines.sort()

                if 2*math.pi*a.radius - lines[-1] + lines[0]  <= 10 and 2*math.pi*a.radius - lines[-1] <= 10 and lines[0] < 10:
                    lost = True
            except IndexError:
                pass
            
        screen.fill((50,50,50))
        if lost:
            pygame.draw.circle(screen, (255,0,0), (100,100), a.radius)
            score -= 1
        a.drawcircle()
        for arrow in arrows:
            arrow.drawnewarrow()
            arrow.rotation(1)
        
        downarrow()
        text = font.render(str(score), True, (0,0,0), (0,255,0))
        screen.blit(text, (250,250))
        
        pygame.display.flip()
        a.rotate(1)
        time.sleep(0.01)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_SPACE:
            newgame()

pygame.quit()