import pygame
import sys

pygame.init()

BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen_width = 700
screen_height = 500
size = (screen_width, screen_height) #Οριζουμε το μεγεθος του παραθυρου
screen = pygame.display.set_mode(size) #Οριζει τον καμβα σχεδιασης με το μεγεθος που του δωσαμε

pygame.display.set_caption("My First Game") #Οριζει τον τιτλο του παραθυρου   


x=screen_width / 2
y=screen_height / 2
vel=5 #pixel μετακινησης

done = False #Οταν θα θελω να βγω απο το παιχνιδι θα γινει True
clock = pygame.time.Clock() #Οριζει το ρολοι για να κλειδωσουμε τα fps του παιχνιδιου

while not done: #Οσο το done ειναι False συνεχιζουμε το παιχνιδι
    for event in pygame.event.get(): #Καλουμε απο την pygame.get 
        if event.type == pygame.QUIT: #Αν πατησουμε το Χ για να κλεισουμε το παραθυρο
            done = True #Βγαζουμε απο την λουπα
   
    keys = pygame.key.get_pressed() #Δεχομαστε ολες τις πληκτρολογησεις του παικτη

    if keys[pygame.K_LEFT]: #Αν πατησουμε το αριστερο βελακι
        x -= vel #Μετακινηση αριστερα

    if keys[pygame.K_RIGHT]: #Αν πατησουμε το δεξι βελακι
        x += vel #Μετακινηση δεξια

    if keys[pygame.K_UP]: #Αν πατησουμε το πανω βελακι
        y -= vel #Μετακινηση πανω

    if keys[pygame.K_DOWN]: #Αν πατησουμε το κατω βελακι
        y += vel #Μετακινηση κατω

    if keys[pygame.K_PLUS]: #Αν πατησουμε το +
        vel += 1 #Αυξηση ταχυτητας

    if keys[pygame.K_MINUS]: #Αν πατησουμε το -
        vel -= 1 #Μειωση ταχυτητας
        if vel < 1:
                vel = 1 #Ελαχιστη ταχυτητα 1

    if keys[pygame.K_q]: #Αν πατησουμε το q
       x-=vel #μετακινιση πανω αριστερα (διαγωνια)
       y-=vel 

    #βαζουμε ορια για να μη βγαινει το ορθογωνιο εξω απο την οθονη
    if x < 0: #Αν βγει εξω αριστερα
       x = 0
    
    if x > screen_width - 20: #20 το πλάτος του ορθογωνίου #Αν βγει εξω δεξια
       x = screen_width - 20 
    
    if y < 0: #Αν βγει εξω πανω
       y = 0
    
    if y > screen_height - 20: #20 το ύψος του ορθογωνίου #Αν βγει εξω κατω
       y = screen_height - 20

    screen.fill(WHITE) #Γεμιζει τον καμβα με λευκο χρωμα

    pygame.draw.rect(screen, RED, [x, y, 20, 20]) #Σχεδιαζει ενα κοκκινο ορθογωνιο

    pygame.display.flip() #Ενημερωνει την οθονη
    clock.tick(60) #Κλειδωνει τα fps στα 60, παντα βαζουμε ενα οριο για να μη ξεφυγει η χρηση της cpu
