import pygame
import sys
import random

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

isJumping = False #Αν γινει True το ορθογωνιο θα πηδηξει
jumpCount = 10 #Υψος πηδηματος



snow_list = [] #Λιστα για τις νιφάδες χιονιού

for i in range(50): #Δημιουργια 50 νιφαδων χιονιου
    x_snow = random.randrange(0, screen_width) #Τυχαια θεση Χ για τη χιονονιφαδα
    y_snow = random.randrange(0, screen_height) #Τυχαια θεση Υ για τη χιονονιφαδα
    snow_list.append([x_snow, y_snow]) #Προσθηκη της νιφάδας στη λιστα


click_sound = pygame.mixer.Sound("gunshot.wav") #Φορτωνει το ηχητικο αρχειο
pygame.mixer.music.load("bgmusic.wav") #Φορτωνει το μουσικο αρχειο
pygame.mixer.music.play(-1) #Παραμενει σε λουπα (-1)


background_image = pygame.image.load("space.jpg") #Φορτωνει την εικονα φοντου
background_image = pygame.transform.scale(background_image, (screen_width, screen_height)) #Αλλαζει το μεγεθος της εικονας στο μεγεθος της οθονης
player_image = pygame.image.load("player.png") #Φορτωνει την εικονα του παικτη
player_image = pygame.transform.scale(player_image, (50, 50)) #Αλλαζει το μεγεθος της εικονας του παικτη στο μεγεθος του ορθογωνιου
player_image.set_colorkey(WHITE) #Κανει διαφανες το μαυρο χρωμα στην εικονα του παικτη


done = False #Οταν θα θελω να βγω απο το παιχνιδι θα γινει True
clock = pygame.time.Clock() #Οριζει το ρολοι για να κλειδωσουμε τα fps του παιχνιδιου

while not done: #Οσο το done ειναι False συνεχιζουμε το παιχνιδι
    for event in pygame.event.get(): #Καλουμε απο την pygame.get 
        if event.type == pygame.QUIT: #Αν πατησουμε το Χ για να κλεισουμε το παραθυρο
            done = True #Βγαζουμε απο την λουπα
   
        elif event.type==pygame.MOUSEBUTTONDOWN: #Αν πατησουμε το ποντικι
            click_sound.play() #Παραγουμε τον ηχο
            mouse_x, mouse_y=pygame.mouse.get_pos() #Παιρνουμε τις συντεταγμενες του ποντικιου
            print("Mouse clicked at:", mouse_x, mouse_y) #Εμφανιζουμε τις συντεταγμενες στην κονσολα

    keys = pygame.key.get_pressed() #Δεχομαστε ολες τις πληκτρολογησεις του παικτη

    if keys[pygame.K_LEFT]: #Αν πατησουμε το αριστερο βελακι
        x -= vel #Μετακινηση αριστερα

    if keys[pygame.K_RIGHT]: #Αν πατησουμε το δεξι βελακι
        x += vel #Μετακινηση δεξια

    if keys[pygame.K_UP]: #Αν πατησουμε το πανω βελακι
        y -= vel #Μετακινηση πανω οταν δεν πηδαει

    if keys[pygame.K_DOWN]: #Αν πατησουμε το κατω βελακι
        y += vel #Μετακινηση κατω οταν δεν πηδαει

    if keys[pygame.K_PLUS]: #Αν πατησουμε το +
        vel += 1 #Αυξηση ταχυτητας

    if keys[pygame.K_MINUS]: #Αν πατησουμε το -
        vel -= 1 #Μειωση ταχυτητας
        if vel < 1:
                vel = 1 #Ελαχιστη ταχυτητα 1

    if keys[pygame.K_q]: #Αν πατησουμε το q
       x-=vel #μετακινιση πανω αριστερα (διαγωνια)
       y-=vel 

    if keys[pygame.K_SPACE]: #Αν πατησουμε το space
        if not isJumping: #Αν δεν ειναι ηδη σε πηδημα
            isJumping = True #Ξεκιναει το πηδημα

    if isJumping: #Αν ειναι σε πηδημα
        if jumpCount >= -10: #Οσο το jumpCount ειναι μεγαλυτερο ή ισο με -10
            neg = 1 #Θετικος αριθμος
            if jumpCount < 0: 
                neg = -1 #Αν το jumpCount ειναι αρνητικο το κανουμε αρνητικο για να κατεβαινει
            y -= (jumpCount ** 2) * 0.5 * neg #Τετραγωνικη κινηση για πιο φυσικο πηδημα
            jumpCount -= 1 #Μειωνουμε το jumpCount
        else: 
            isJumping = False #Τελειωσε το πηδημα
            jumpCount = 10 #Επαναφορα του jumpCount για την επομενη φορα

    #βαζουμε ορια για να μη βγαινει το ορθογωνιο εξω απο την οθονη
    if x < 0: #Αν βγει εξω αριστερα
       x = 0
    
    if x > screen_width - 20: #20 το πλάτος του ορθογωνίου #Αν βγει εξω δεξια
       x = screen_width - 20 
    
    if y < 0: #Αν βγει εξω πανω
       y = 0
    
    if y > screen_height - 20: #20 το ύψος του ορθογωνίου #Αν βγει εξω κατω
       y = screen_height - 20

    screen.fill(BLACK) #Γεμιζει τον καμβα με μαυρο χρωμα
    
    screen.blit(background_image, (0, 0)) #Ζωγραφιζει την εικονα φοντου στον καμβα

    for i in range(len(snow_list)): #Για καθε νιφαδα στη λιστα
        pygame.draw.circle(screen, WHITE, snow_list[i], 2) #Σχεδιαζει τη νιφαδα ως κυκλο με ακτινα 2
        snow_list[i][1] += 1 #Κινει τη νιφαδα κατω
        snow_list[i][0] += random.randrange(-1, 3) #Τυχαια μικρη κινηση αριστερα ή δεξια για πιο φυσικο αποτελεσμα

        #if snow_list[i][1] > screen_height: #Αν η νιφαδα βγει εξω απο την κατω μερια της οθονης
        #  snow_list[i][1] = random.randrange(-50, -10) #Την ξαναβαζουμε τυχαια πανω απο την οθονη
        #  snow_list[i][0] = random.randrange(0, screen_width) #Τυχαια θεση Χ
        
        if snow_list[i][1]>screen_height: #Αν βγει εξω απο κατω
            a=random.randrange(0,3) #Τυχαιος αριθμος απο 0 εως 2
            if (a==0 or a==1): #Πιθανοτητα 2 στα 3 να ξαναμπει απο πανω
                snow_list[i][1]=0 #Ξαναμπαινει απο πανω
                snow_list[i][0]=random.randrange(0, screen_width) #Τυχαια θεση Χ
            else:
                snow_list[i][0]=0 #Ξαναμπαινει απο αριστερα
                snow_list[i][1]=random.randrange(0, screen_height) #Τυχαια θεση Υ
    
    


    
    
    #pygame.draw.rect(screen, RED, [x, y, 50, 50]) #Σχεδιαζει ενα κοκκινο ορθογωνιο
    
    screen.blit(player_image, (x, y)) #Ζωγραφιζει την εικονα του παικτη στον καμβα

    pygame.display.flip() #Ενημερωνει την οθονη
    clock.tick(60) #Κλειδωνει τα fps στα 60, παντα βαζουμε ενα οριο για να μη ξεφυγει η χρηση της cpu
