import pygame
import sys

# Initialize Pygame
pygame.init()

# Οριζουμε τα χρωματα που θα χρησιμοποιησουμε

BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

size = (700, 500) #Οριζουμε το μεγεθος του παραθυρου
screen = pygame.display.set_mode(size) #Οριζει τον καμβα σχεδιασης με το μεγεθος που του δωσαμε
pygame.display.set_caption("My First Pygame Program") #Οριζει τον τιτλο του παραθυρου   

done = False #Οταν θα θελω να βγω απο το παιχνιδι θα γινει True
clock = pygame.time.Clock() #Οριζει το ρολοι για να κλειδωσουμε τα fps του παιχνιδιου

while not done: #Οσο το done ειναι False συνεχιζουμε το παιχνιδι
    for event in pygame.event.get(): #Καλουμε απο την pygame.get 
        if event.type == pygame.QUIT: #Αν πατησουμε το Χ για να κλεισουμε το παραθυρο
            done = True #Βγαζουμε απο την λουπα

    screen.fill(WHITE) #Γεμιζει τον καμβα με λευκο χρωμα

    # Σχεδιασμος σχηματων
    pygame.draw.line(screen, BLACK, [50,0], [100,100],5 ) #Σχεδιαζει μια μαυρη γραμμη
    pygame.draw.rect(screen, RED, [20,20,250,100], 2) #Σχεδιαζει ενα κοκκινο ορθογωνιο
    pygame.draw.ellipse(screen, GREEN, [300, 200, 200, 100], 0) #Σχεδιαζει μια πρασινη ελλειψη
    pygame.draw.polygon(screen, BLUE, [[100, 100], [0, 200], [200, 200]], 5) #Σχεδιαζει ενα μπλε πολυγωνο
    pygame.draw.circle(screen, BLACK, [400, 400], 50, 0) #Σχεδιαζει ενα μαυρο κυκλο

    pygame.display.flip() #Ενημερωνει την οθονη

    clock.tick(60) #Κλειδωνει τα fps στα 60, παντα βαζουμε ενα οριο για να μη ξεφυγει η χρηση της cpu
