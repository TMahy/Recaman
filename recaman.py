import pygame
import time
import colorsys
import math
pygame.init()

"""
Recaman Sequence Visualiser using the pygame library
"""

def recaman(sequence, counter):
    """
    Generates the next recaman number in the sequence, with a counter on number of iterations
    """
    next = sequence[counter-1] - counter
    if (next < 0 or next in sequence):
        next = sequence[counter-1] + counter
    sequence.append(next)
    counter += 1
    return sequence, counter

def draw(screen, sequence, counter):
    """
    Draws the sequence of numbers using alternating arcs.
    Scaling the size of the arcs based on the largest number reached in the sequence
    """
    screen.fill((0,0,0))
    Max = max(sequence)
    scaled_sequence = [sequence[i]*(980/Max) for i in range(len(sequence))]

    for i in range(len(sequence)-1):
        center = (scaled_sequence[i]+scaled_sequence[i+1])/2
        radius = round(abs(center - scaled_sequence[i]))
        thickness = 2
        color = rainbow(i)
        if i % 2 != 0:
            pygame.draw.circle(screen, color, (center, 400), radius, thickness, True, True, False, False)
        else:
            pygame.draw.circle(screen, color, (center, 400), radius, thickness, False, False, True, True)

def rainbow(num):
    """
    Scales the number of iterations to a colour, cycles on a rainbow scale.
    """
    color = colorsys.hsv_to_rgb((num/2)%360./360., 1., 1.)
    return tuple(round(i*255) for i in color)

def draw_screen(screen, sequence, counter):
    """
    Draws the screen and all accompanying info
    """
    font = pygame.font.SysFont("helvetica", 30)
    text_iter = font.render("Iteration: " + str(counter), True, (255,255,255))
    text_value = font.render("Value: "+ str(sequence[-1]), True, (255,255,255))
    screen.blit(text_iter, (20, 20))
    screen.blit(text_value, (20, 50))

def main():
    screen = pygame.display.set_mode((1000,800))
    pygame.display.set_caption('Recaman Sequence Visualised - Space to Start/Stop')
    
    sequence = [0]
    counter = 1 

    Run = True
    Step = False
    key = None
    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
            #Sequence visualiser starts and pauses on space press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Step = not Step
        if Step == True:
            sequence, counter = recaman(sequence, counter)
            draw(screen, sequence, counter)
            pygame.time.delay(50)
        draw_screen(screen, sequence, counter)
        pygame.display.update()

main()
pygame.quit()