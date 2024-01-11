import pygame
import sys



pygame.init() # Initialize Pygame
pygame.mixer.init()
pspeed = 6 # Set the player's Speed
pygame.display.set_caption("The Sacrifice") # Set the Window Title
pygame.display.set_icon(pygame.transform.scale(pygame.image.load("Obelisk_Active.png"),(128,128))) # Load the Icon for the Game



def Level1():

    pygame.display.set_caption("The Sacrifice - Level 1")

    SCREEN = pygame.display.set_mode((1280,720))
    SCREEN_RECT = SCREEN.get_rect()

    px = SCREEN_RECT.centerx
    py = SCREEN_RECT.centery

    obeliskActiveImg = pygame.image.load("Obelisk_Active.png")
    obeliskInactiveImg = pygame.image.load("Obelisk.png")

    obeliskInactiveImg = pygame.transform.scale(obeliskInactiveImg,(80,80))
    obeliskActiveImg = pygame.transform.scale(obeliskActiveImg,(80,80))

    obeliskImg = []
    obeliskx = [300,200,700]
    obelisky = [100,600,300]
    obeliskRect = []
    obelisksContacted = [0,0,0] # can be 0 or 1
    num_obelisk = 3

    for i in range(num_obelisk):
        obeliskImg.append(obeliskInactiveImg)
    
    for i in range(len(obeliskImg)):
        obeliskRect.append(obeliskImg[i].get_rect())

    
    def drawPlayer(surface,x,y):
        pygame.draw.circle(surface,('#3880cf'),(x,y),30)


    introAudio = pygame.mixer.Sound("IntroAudio.mp3")
    audioChannel = pygame.mixer.Channel(1)
    
    tutorial = pygame.image.load("Tutorialp1.png")
    

    running = True
    

    Clock = pygame.time.Clock()

    def win():
        Level2()
        sys.exit()
    
    def wincheck():
        if obelisksContacted == [1,1,1]:
            return True
        else:
            return False
    audioChannel.play(introAudio,fade_ms = 5000,)   
    while running:
        SCREEN.fill('#101010')
        drawPlayer(SCREEN,px,py)
        SCREEN.blit(tutorial,(880,0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            py -= pspeed
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            py += pspeed
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            px -= pspeed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            px += pspeed
        
        if px > 1280-30:
            px = 1280-30
        
        if px < 30:
            px = 30
        
        if py > 720-30:
            py = 720-30
        
        if py < 30:
            py = 30
        
        for i in range(len(obeliskImg)): # Draw Multiple Obelisks to the screen
            SCREEN.blit(obeliskImg[i],(obeliskx[i],obelisky[i]))
        

        # Main Game Mechanic
        if px in range(obeliskx[0], obeliskx[0]+64):
            if py in range(obelisky[0], obelisky[0]+64):
                obelisksContacted[0] = 1
                obeliskImg[0] = obeliskActiveImg
        
        
        if px in range(obeliskx[1], obeliskx[1]+64):
            if py in range(obelisky[1], obelisky[1]+64):
                if obelisksContacted == [1,0,0]:
                    obelisksContacted[1] = 1
                    obeliskImg[1] = obeliskActiveImg
            
                
        
        if px in range(obeliskx[2], obeliskx[2]+64):
            if py in range(obelisky[2], obelisky[2]+64):
                if obelisksContacted == [1,1,0]:
                    obelisksContacted[2] = 1
                    obeliskImg[2] = obeliskActiveImg
                
                else:
                    obelisksContacted = [0,0,0]
                    obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
                
              
        

        # ----------------------------------------------------
        
        if wincheck():
            win()
        
        Clock.tick(60)
        pygame.display.flip()

def Level2():

    pygame.display.set_caption("The Sacrifice - Level 2")
    SCREEN = pygame.display.set_mode((1280,720))
    SCREEN_RECT = SCREEN.get_rect()

    pygame.mixer.stop()
    px = SCREEN_RECT.centerx
    py = SCREEN_RECT.centery

    obeliskActiveImg = pygame.image.load("Obelisk_Active.png")
    obeliskInactiveImg = pygame.image.load("Obelisk.png")

    obeliskInactiveImg = pygame.transform.scale(obeliskInactiveImg,(80,80))
    obeliskActiveImg = pygame.transform.scale(obeliskActiveImg,(80,80))

    obeliskImg = []
    obeliskx = [400,300,300,1000]
    obelisky = [500,250,600,100]
    obeliskRect = []
    obelisksContacted = [0,0,0,0] # can be 0 or 1
    num_obelisk = 4

    for i in range(num_obelisk):
        obeliskImg.append(obeliskInactiveImg)
    
    for i in range(len(obeliskImg)):
        obeliskRect.append(obeliskImg[i].get_rect())

    
    def drawPlayer(surface,x,y):
        pygame.draw.circle(surface,('#3880cf'),(x,y),30)


    def drawGunRay(surface,mx,my):
        pygame.draw.line(surface,('#cf5d4622'),(px,py),(mx,my),5)
    
    
    

    running = True
    

    Clock = pygame.time.Clock()


    def win():
        Level3()
        sys.exit()
    
    def wincheck():
        if obelisksContacted == [1,1,1,1]:
            return True
        else:
            return False

    while running:
        SCREEN.fill('#101010')
        drawPlayer(SCREEN,px,py)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            py -= pspeed
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            py += pspeed
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            px -= pspeed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            px += pspeed
        
        if px > 1280-30:
            px = 1280-30
        
        if px < 30:
            px = 30
        
        if py > 720-30:
            py = 720-30
        
        if py < 30:
            py = 30
        
        for i in range(len(obeliskImg)): # Draw Multiple Obelisks to the screen
            SCREEN.blit(obeliskImg[i],(obeliskx[i],obelisky[i]))
        

        # Main Game Mechanic
        if px in range(obeliskx[0], obeliskx[0]+80):
            if py in range(obelisky[0], obelisky[0]+80):
                obelisksContacted = [1,0,0,0]
                obeliskImg[0] = obeliskActiveImg
        
        
        if px in range(obeliskx[1], obeliskx[1]+80):
            if py in range(obelisky[1], obelisky[1]+80):
                if obelisksContacted == [1,0,0,0] or obelisksContacted == [1,1,0,0]:
                    obelisksContacted[1] = 1
                    obeliskImg[1] = obeliskActiveImg
                else:
                    obelisksContacted = [0,0,0,0]
                    obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
            
                
        
        if px in range(obeliskx[2], obeliskx[2]+80):
            if py in range(obelisky[2], obelisky[2]+80):
                if obelisksContacted == [1,1,0,0] or obelisksContacted == [1,1,1,0]:
                    obelisksContacted[2] = 1
                    obeliskImg[2] = obeliskActiveImg
                
                else:
                    obelisksContacted = [0,0,0,0]
                    obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
                
            
        if px in range(obeliskx[3], obeliskx[3]+80):
            if py in range(obelisky[3], obelisky[3]+80):
                if obelisksContacted == [1,1,1,0] or obelisksContacted == [1,1,1,1]:
                    obelisksContacted[3] = 1
                    obeliskImg[3] = obeliskActiveImg
                
                else:
                    obelisksContacted = [0,0,0,0]
                    obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
                
              

        # ----------------------------------------------------
        
        if wincheck():
            win()
        
        Clock.tick(60)
        pygame.display.flip()

def Level3():
    pygame.display.set_caption("The Sacrifice - Level 3")
    SCREEN = pygame.display.set_mode((1280,720))
    SCREEN_RECT = SCREEN.get_rect()

    px = SCREEN_RECT.centerx
    py = SCREEN_RECT.centery

    obeliskActiveImg = pygame.image.load("Obelisk_Active.png")
    obeliskInactiveImg = pygame.image.load("Obelisk.png")

    obeliskInactiveImg = pygame.transform.scale(obeliskInactiveImg,(80,80))
    obeliskActiveImg = pygame.transform.scale(obeliskActiveImg,(80,80))

    obeliskImg = []
    obeliskx = [800,500,200,1000,900]
    obelisky = [100,650,200,500,590]
    obeliskRect = []
    obelisksContacted = [0,0,0,0,0] # can be 0 or 1
    num_obelisk = 5

    for i in range(num_obelisk):
        obeliskImg.append(obeliskInactiveImg)
    
    for i in range(len(obeliskImg)):
        obeliskRect.append(obeliskImg[i].get_rect())

    
    def drawPlayer(surface,x,y):
        pygame.draw.circle(surface,('#3880cf'),(x,y),30)


    def drawGunRay(surface,mx,my):
        pygame.draw.line(surface,('#cf5d4622'),(px,py),(mx,my),5)
    
    
    

    running = True
    

    Clock = pygame.time.Clock()


    def win():
        Level4()
        sys.exit()
    
    def wincheck():
        if obelisksContacted == [1,1,1,1,1]:
            return True
        else:
            return False

    while running:
        SCREEN.fill('#101010')
        drawPlayer(SCREEN,px,py)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            py -= pspeed
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            py += pspeed
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            px -= pspeed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            px += pspeed
        
        if px > 1280-30:
            px = 1280-30
        
        if px < 30:
            px = 30
        
        if py > 720-30:
            py = 720-30
        
        if py < 30:
            py = 30
        
        for i in range(len(obeliskImg)): # Draw Multiple Obelisks to the screen
            SCREEN.blit(obeliskImg[i],(obeliskx[i],obelisky[i]))
        

        # Main Game Mechanic
        if px in range(obeliskx[0], obeliskx[0]+80):
            if py in range(obelisky[0], obelisky[0]+80):
                obelisksContacted = [1,0,0,0,0]
                obeliskImg[0] = obeliskActiveImg
        
        
        if px in range(obeliskx[1], obeliskx[1]+80):
            if py in range(obelisky[1], obelisky[1]+80):
                if obelisksContacted == [1,0,0,0,0] or obelisksContacted == [1,1,0,0,0]:
                    obelisksContacted[1] = 1
                    obeliskImg[1] = obeliskActiveImg
                else:
                    obelisksContacted = [0,0,0,0,0]
                    obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
            
                
        
        if px in range(obeliskx[2], obeliskx[2]+80):
            if py in range(obelisky[2], obelisky[2]+80):
                if obelisksContacted == [1,1,0,0,0] or obelisksContacted == [1,1,1,0,0]:
                    obelisksContacted[2] = 1
                    obeliskImg[2] = obeliskActiveImg
                
                else:
                    obelisksContacted = [0,0,0,0]
                    obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
                
            
        if px in range(obeliskx[3], obeliskx[3]+80):
            if py in range(obelisky[3], obelisky[3]+80):
                if obelisksContacted == [1,1,1,0,0] or obelisksContacted == [1,1,1,1,0]:
                    obelisksContacted[3] = 1
                    obeliskImg[3] = obeliskActiveImg
                
                else:
                    obelisksContacted = [0,0,0,0,0]
                    obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
                
        if px in range(obeliskx[4], obeliskx[4]+80):
            if py in range(obelisky[4], obelisky[4]+80):
                if obelisksContacted == [1,1,1,1,0] or obelisksContacted == [1,1,1,1,1]:
                    obelisksContacted[4] = 1
                    obeliskImg[4] = obeliskActiveImg
                
                else:
                    obelisksContacted = [0,0,0,0,0]
                    obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
                

        # ----------------------------------------------------
        
        if wincheck():
            win()
        
        Clock.tick(60)
        pygame.display.flip()

def Level4():
    pygame.display.set_caption("The Sacrifice - Level 4")
    SCREEN = pygame.display.set_mode((1280,720))
    SCREEN_RECT = SCREEN.get_rect()

    px = SCREEN_RECT.centerx
    py = SCREEN_RECT.centery

    current_time = 0
    static_time = 0

    obeliskActiveImg = pygame.image.load("Obelisk_Active.png")
    obeliskInactiveImg = pygame.image.load("Obelisk.png")

    obeliskInactiveImg = pygame.transform.scale(obeliskInactiveImg,(80,80))
    obeliskActiveImg = pygame.transform.scale(obeliskActiveImg,(80,80))

    PedestalActiveImg = pygame.image.load("Pedestal_Active.png")
    PedestalInactiveImg = pygame.image.load("Pedestal_Deactive.png")

    PedestalActiveImg = pygame.transform.scale(PedestalActiveImg,(80,80))
    PedestalInactiveImg = pygame.transform.scale(PedestalInactiveImg,(80,80))

    PedestalImage = [PedestalActiveImg,PedestalInactiveImg]
    current_pedestal = 0

    Pedestalx = 1280//2 - 40
    Pedestaly = 580

    obeliskImg = []
    obeliskx = [400,300,500,1000,900]
    obelisky = [100,500,300,580,590]
    obeliskRect = []
    obelisksContacted = [0,0,0,0,0] # can be 0 or 1
    num_obelisk = 5

    for i in range(num_obelisk):
        obeliskImg.append(obeliskInactiveImg)
    
    for i in range(len(obeliskImg)):
        obeliskRect.append(obeliskImg[i].get_rect())

    
    def drawPlayer(surface,x,y):
        pygame.draw.circle(surface,('#3880cf'),(x,y),30)


    def drawGunRay(surface,mx,my):
        pygame.draw.line(surface,('#cf5d4622'),(px,py),(mx,my),5)
    
    tutorial = pygame.image.load("Tutorialp2.png")
    
    

    running = True
    

    Clock = pygame.time.Clock()

    timer_font = pygame.font.SysFont("Calibri",20)
    timer_text = timer_font.render("",True,('#ffffff'))
    

    def win():
        Level5()
        sys.exit()
    
    def wincheck():
        if obelisksContacted == [1,1,1,1,1]:
            return True
        else:
            return False
    
    encounterActive = False
    static_time = current_time
    while running:
        if not encounterActive:
            current_time = pygame.time.get_ticks()
            static_time = current_time
        
        else:
            current_time = pygame.time.get_ticks()
            
        
        SCREEN.fill('#101010')
        drawPlayer(SCREEN,px,py)
        SCREEN.blit(tutorial,(880,0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            py -= pspeed
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            py += pspeed
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            px -= pspeed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            px += pspeed
        
        if px > 1280-30:
            px = 1280-30
        
        if px < 30:
            px = 30
        
        if py > 720-30:
            py = 720-30
        
        if py < 30:
            py = 30
        
        for i in range(len(obeliskImg)): # Draw Multiple Obelisks to the screen
            SCREEN.blit(obeliskImg[i],(obeliskx[i],obelisky[i]))
        
        SCREEN.blit(PedestalImage[current_pedestal],(Pedestalx,Pedestaly))

        

        # Main Game Mechanic
        if encounterActive:
            if px in range(obeliskx[0], obeliskx[0]+80):
                if py in range(obelisky[0], obelisky[0]+80):
                    obelisksContacted = [1,0,0,0,0]
                    obeliskImg[0] = obeliskActiveImg
            
            
            if px in range(obeliskx[1], obeliskx[1]+80):
                if py in range(obelisky[1], obelisky[1]+80):
                    if obelisksContacted == [1,0,0,0,0] or obelisksContacted == [1,1,0,0,0]:
                        obelisksContacted[1] = 1
                        obeliskImg[1] = obeliskActiveImg
                    else:
                        obelisksContacted = [0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
                
                    
            
            if px in range(obeliskx[2], obeliskx[2]+80):
                if py in range(obelisky[2], obelisky[2]+80):
                    if obelisksContacted == [1,1,0,0,0] or obelisksContacted == [1,1,1,0,0]:
                        obelisksContacted[2] = 1
                        obeliskImg[2] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
                    
                
            if px in range(obeliskx[3], obeliskx[3]+80):
                if py in range(obelisky[3], obelisky[3]+80):
                    if obelisksContacted == [1,1,1,0,0] or obelisksContacted == [1,1,1,1,0]:
                        obelisksContacted[3] = 1
                        obeliskImg[3] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
                    
            if px in range(obeliskx[4], obeliskx[4]+80):
                if py in range(obelisky[4], obelisky[4]+80):
                    if obelisksContacted == [1,1,1,1,0] or obelisksContacted == [1,1,1,1,1]:
                        obelisksContacted[4] = 1
                        obeliskImg[4] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
                

        # ----------------------------------------------------
        
        if px in range(Pedestalx,Pedestalx+80):
            if py in range(Pedestaly,Pedestaly+80):
                if encounterActive == False:
                    current_pedestal = 1
                    encounterActive = True
                    static_time = pygame.time.get_ticks()
                    timer_text = timer_font.render(str(30-(current_time-static_time)//1000),True,('#ffffff'))
            
        if current_time - static_time > 30000:
            current_pedestal = 0
            obelisksContacted = [0,0,0,0,0]
            obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
            encounterActive = False
        
        timer_text = timer_font.render("Brand of the Sacrifice: "+str(30-(current_time-static_time)//1000),True,('#ffffff'))
        SCREEN.blit(timer_text,(0,720//2-45//2))
        if wincheck():
            win()
        
        Clock.tick(60)
        pygame.display.flip()
    
def Level5():
    pygame.display.set_caption("The Sacrifice - Level 5")
    SCREEN = pygame.display.set_mode((1280,720))
    SCREEN_RECT = SCREEN.get_rect()

    px = SCREEN_RECT.centerx
    py = SCREEN_RECT.centery

    current_time = 0
    static_time = 0

    obeliskActiveImg = pygame.image.load("Obelisk_Active.png")
    obeliskInactiveImg = pygame.image.load("Obelisk.png")

    obeliskInactiveImg = pygame.transform.scale(obeliskInactiveImg,(80,80))
    obeliskActiveImg = pygame.transform.scale(obeliskActiveImg,(80,80))

    PedestalActiveImg = pygame.image.load("Pedestal_Active.png")
    PedestalInactiveImg = pygame.image.load("Pedestal_Deactive.png")

    PedestalActiveImg = pygame.transform.scale(PedestalActiveImg,(80,80))
    PedestalInactiveImg = pygame.transform.scale(PedestalInactiveImg,(80,80))

    PedestalImage = [PedestalActiveImg,PedestalInactiveImg]
    current_pedestal = 0

    Pedestalx = 1280//2 - 40
    Pedestaly = 580

    obeliskImg = []
    obeliskx = [400,300,500,1000,900,100,300,400]
    obelisky = [100,500,300,580,590,200,400,600]
    obeliskRect = []
    obelisksContacted = [0,0,0,0,0,0,0,0] # can be 0 or 1
    num_obelisk = 8

    for i in range(num_obelisk):
        obeliskImg.append(obeliskInactiveImg)
    
    for i in range(len(obeliskImg)):
        obeliskRect.append(obeliskImg[i].get_rect())

    
    def drawPlayer(surface,x,y):
        pygame.draw.circle(surface,('#3880cf'),(x,y),30)


    def drawGunRay(surface,mx,my):
        pygame.draw.line(surface,('#cf5d4622'),(px,py),(mx,my),5)
    
    
    

    running = True
    

    Clock = pygame.time.Clock()

    timer_font = pygame.font.SysFont("Calibri",20)
    timer_text = timer_font.render("",True,('#ffffff'))
    

    def win():
        Level6()
        sys.exit()
    
    def wincheck():
        if obelisksContacted == [1,1,1,1,1,1,1,1]:
            return True
        else:
            return False
    
    encounterActive = False
    static_time = current_time
    while running:
        if not encounterActive:
            current_time = pygame.time.get_ticks()
            static_time = current_time
        
        else:
            current_time = pygame.time.get_ticks()
            
        
        SCREEN.fill('#101010')
        drawPlayer(SCREEN,px,py)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            py -= pspeed
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            py += pspeed
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            px -= pspeed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            px += pspeed
        
        if px > 1280-30:
            px = 1280-30
        
        if px < 30:
            px = 30
        
        if py > 720-30:
            py = 720-30
        
        if py < 30:
            py = 30
        
        for i in range(len(obeliskImg)): # Draw Multiple Obelisks to the screen
            SCREEN.blit(obeliskImg[i],(obeliskx[i],obelisky[i]))
        
        SCREEN.blit(PedestalImage[current_pedestal],(Pedestalx,Pedestaly))

        

        # Main Game Mechanic
        if encounterActive:
            if px in range(obeliskx[0], obeliskx[0]+80):
                if py in range(obelisky[0], obelisky[0]+80):
                    obelisksContacted = [1,0,0,0,0,0,0,0]
                    obeliskImg[0] = obeliskActiveImg
            
            
            if px in range(obeliskx[1], obeliskx[1]+80):
                if py in range(obelisky[1], obelisky[1]+80):
                    if obelisksContacted == [1,0,0,0,0,0,0,0] or obelisksContacted == [1,1,0,0,0,0,0,0]:
                        obelisksContacted[1] = 1
                        obeliskImg[1] = obeliskActiveImg
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]                    
                
                    
            
            if px in range(obeliskx[2], obeliskx[2]+80):
                if py in range(obelisky[2], obelisky[2]+80):
                    if obelisksContacted == [1,1,0,0,0,0,0,0] or obelisksContacted == [1,1,1,0,0,0,0,0]:
                        obelisksContacted[2] = 1
                        obeliskImg[2] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]                    
                    
                
            if px in range(obeliskx[3], obeliskx[3]+80):
                if py in range(obelisky[3], obelisky[3]+80):
                    if obelisksContacted == [1,1,1,0,0,0,0,0] or obelisksContacted == [1,1,1,1,0,0,0,0]:
                        obelisksContacted[3] = 1
                        obeliskImg[3] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]

            if px in range(obeliskx[4], obeliskx[4]+80):
                if py in range(obelisky[4], obelisky[4]+80):
                    if obelisksContacted == [1,1,1,1,0,0,0,0] or obelisksContacted == [1,1,1,1,1,0,0,0]:
                        obelisksContacted[4] = 1
                        obeliskImg[4] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
                    
            if px in range(obeliskx[5], obeliskx[5]+80):
                if py in range(obelisky[5], obelisky[5]+80):
                    if obelisksContacted == [1,1,1,1,1,0,0,0] or obelisksContacted == [1,1,1,1,1,1,0,0]:
                        obelisksContacted[5] = 1
                        obeliskImg[5] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
                    
            if px in range(obeliskx[6], obeliskx[6]+80):
                if py in range(obelisky[6], obelisky[6]+80):
                    if obelisksContacted == [1,1,1,1,1,1,0,0] or obelisksContacted == [1,1,1,1,1,1,1,0]:
                        obelisksContacted[6] = 1
                        obeliskImg[6] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
            
            if px in range(obeliskx[7], obeliskx[7]+80):
                if py in range(obelisky[7], obelisky[7]+80):
                    if obelisksContacted == [1,1,1,1,1,1,1,0] or obelisksContacted == [1,1,1,1,1,1,1,1]:
                        obelisksContacted[7] = 1
                        obeliskImg[7] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
                    

                

        # ----------------------------------------------------
        
        if px in range(Pedestalx,Pedestalx+80):
            if py in range(Pedestaly,Pedestaly+80):
                if encounterActive == False:
                    current_pedestal = 1
                    encounterActive = True
                    static_time = pygame.time.get_ticks()
                    timer_text = timer_font.render(str(30-(current_time-static_time)//1000),True,('#ffffff'))
            
        if current_time - static_time > 30000:
            current_pedestal = 0
            obelisksContacted = [0,0,0,0,0,0,0,0]
            obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
            encounterActive = False
        
        timer_text = timer_font.render("Brand of the Sacrifice: "+str(30-(current_time-static_time)//1000),True,('#ffffff'))
        SCREEN.blit(timer_text,(0,720//2-45//2))
    


        if wincheck():
            win()
        
        Clock.tick(60)
        pygame.display.flip()

def Level6():
    pygame.display.set_caption("The Sacrifice - Level 6")
    SCREEN = pygame.display.set_mode((1280,720))
    SCREEN_RECT = SCREEN.get_rect()

    px = SCREEN_RECT.centerx
    py = SCREEN_RECT.centery

    current_time = 0
    static_time = 0

    obeliskActiveImg = pygame.image.load("Obelisk_Active.png")
    obeliskInactiveImg = pygame.image.load("Obelisk.png")

    obeliskInactiveImg = pygame.transform.scale(obeliskInactiveImg,(80,80))
    obeliskActiveImg = pygame.transform.scale(obeliskActiveImg,(80,80))

    PedestalActiveImg = pygame.image.load("Pedestal_Active.png")
    PedestalInactiveImg = pygame.image.load("Pedestal_Deactive.png")

    PedestalActiveImg = pygame.transform.scale(PedestalActiveImg,(80,80))
    PedestalInactiveImg = pygame.transform.scale(PedestalInactiveImg,(80,80))

    PedestalImage = [PedestalActiveImg,PedestalInactiveImg]
    current_pedestal = 0

    Pedestalx = 1280//2 - 40
    Pedestaly = 580

    obeliskImg = []
    obeliskx = [600,200,400,300,400,200,1100,900,1100,700]
    obelisky = [200,500,300,400,100,100,200,400,400,450]
    obeliskRect = []
    obelisksContacted = [0,0,0,0,0,0,0,0,0,0] # can be 0 or 1
    num_obelisk = 10

    for i in range(num_obelisk):
        obeliskImg.append(obeliskInactiveImg)
    
    for i in range(len(obeliskImg)):
        obeliskRect.append(obeliskImg[i].get_rect())

    
    def drawPlayer(surface,x,y):
        pygame.draw.circle(surface,('#3880cf'),(x,y),30)


    def drawGunRay(surface,mx,my):
        pygame.draw.line(surface,('#cf5d4622'),(px,py),(mx,my),5)
    
    
    

    running = True
    

    Clock = pygame.time.Clock()

    timer_font = pygame.font.SysFont("Calibri",20)
    timer_text = timer_font.render("",True,('#ffffff'))
    

    def win():
        Level7()
        sys.exit()
    
    def wincheck():
        if obelisksContacted == [1,1,1,1,1,1,1,1,1,1]:
            return True
        else:
            return False
    
    encounterActive = False
    static_time = current_time
    while running:
        if not encounterActive:
            current_time = pygame.time.get_ticks()
            static_time = current_time
        
        else:
            current_time = pygame.time.get_ticks()
            
        
        SCREEN.fill('#101010')
        drawPlayer(SCREEN,px,py)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            py -= pspeed
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            py += pspeed
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            px -= pspeed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            px += pspeed
        
        if px > 1280-30:
            px = 1280-30
        
        if px < 30:
            px = 30
        
        if py > 720-30:
            py = 720-30
        
        if py < 30:
            py = 30
        
        for i in range(len(obeliskImg)): # Draw Multiple Obelisks to the screen
            SCREEN.blit(obeliskImg[i],(obeliskx[i],obelisky[i]))
        
        SCREEN.blit(PedestalImage[current_pedestal],(Pedestalx,Pedestaly))

        

        # Main Game Mechanic
        if encounterActive:
            if px in range(obeliskx[0], obeliskx[0]+80):
                if py in range(obelisky[0], obelisky[0]+80):
                    obelisksContacted = [1,0,0,0,0,0,0,0,0,0]
                    obeliskImg[0] = obeliskActiveImg
            
            
            if px in range(obeliskx[1], obeliskx[1]+80):
                if py in range(obelisky[1], obelisky[1]+80):
                    if obelisksContacted == [1,0,0,0,0,0,0,0,0,0] or obelisksContacted == [1,1,0,0,0,0,0,0,0,0]:
                        obelisksContacted[1] = 1
                        obeliskImg[1] = obeliskActiveImg
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]                
                    
            
            if px in range(obeliskx[2], obeliskx[2]+80):
                if py in range(obelisky[2], obelisky[2]+80):
                    if obelisksContacted == [1,1,0,0,0,0,0,0,0,0] or obelisksContacted == [1,1,1,0,0,0,0,0,0,0]:
                        obelisksContacted[2] = 1
                        obeliskImg[2] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]                    
                
            if px in range(obeliskx[3], obeliskx[3]+80):
                if py in range(obelisky[3], obelisky[3]+80):
                    if obelisksContacted == [1,1,1,0,0,0,0,0,0,0] or obelisksContacted == [1,1,1,1,0,0,0,0,0,0]:
                        obelisksContacted[3] = 1
                        obeliskImg[3] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
            if px in range(obeliskx[4], obeliskx[4]+80):
                if py in range(obelisky[4], obelisky[4]+80):
                    if obelisksContacted == [1,1,1,1,0,0,0,0,0,0] or obelisksContacted == [1,1,1,1,1,0,0,0,0,0]:
                        obelisksContacted[4] = 1
                        obeliskImg[4] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]                    
            if px in range(obeliskx[5], obeliskx[5]+80):
                if py in range(obelisky[5], obelisky[5]+80):
                    if obelisksContacted == [1,1,1,1,1,0,0,0,0,0] or obelisksContacted == [1,1,1,1,1,1,0,0,0,0]:
                        obelisksContacted[5] = 1
                        obeliskImg[5] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]

            if px in range(obeliskx[6], obeliskx[6]+80):
                if py in range(obelisky[6], obelisky[6]+80):
                    if obelisksContacted == [1,1,1,1,1,1,0,0,0,0] or obelisksContacted == [1,1,1,1,1,1,1,0,0,0]:
                        obelisksContacted[6] = 1
                        obeliskImg[6] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]

            if px in range(obeliskx[7], obeliskx[7]+80):
                if py in range(obelisky[7], obelisky[7]+80):
                    if obelisksContacted == [1,1,1,1,1,1,1,0,0,0] or obelisksContacted == [1,1,1,1,1,1,1,1,0,0]:
                        obelisksContacted[7] = 1
                        obeliskImg[7] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]

            if px in range(obeliskx[8], obeliskx[8]+80):
                if py in range(obelisky[8], obelisky[8]+80):
                    if obelisksContacted == [1,1,1,1,1,1,1,1,0,0] or obelisksContacted == [1,1,1,1,1,1,1,1,1,0]:
                        obelisksContacted[8] = 1
                        obeliskImg[8] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
            
            if px in range(obeliskx[9], obeliskx[9]+80):
                if py in range(obelisky[9], obelisky[9]+80):
                    if obelisksContacted == [1,1,1,1,1,1,1,1,1,0] or obelisksContacted == [1,1,1,1,1,1,1,1,1,1]:
                        obelisksContacted[9] = 1
                        obeliskImg[9] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
                    

                

        # ----------------------------------------------------
        
        if px in range(Pedestalx,Pedestalx+80):
            if py in range(Pedestaly,Pedestaly+80):
                if encounterActive == False:
                    current_pedestal = 1
                    encounterActive = True
                    static_time = pygame.time.get_ticks()
                    timer_text = timer_font.render(str(30-(current_time-static_time)//1000),True,('#ffffff'))
            
        if current_time - static_time > 30000:
            current_pedestal = 0
            obelisksContacted = [0,0,0,0,0,0,0,0,0,0]
            obeliskImg = [obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg,obeliskInactiveImg]
            encounterActive = False
        
        timer_text = timer_font.render("Brand of the Sacrifice: "+str(30-(current_time-static_time)//1000),True,('#ffffff'))
        SCREEN.blit(timer_text,(0,720//2-45//2))
    



        if wincheck():
            win()
        
        Clock.tick(60)
        pygame.display.flip()

def Level7():
    pygame.display.set_caption("The Sacrifice - Level 7")
    SCREEN = pygame.display.set_mode((1280,720))
    SCREEN_RECT = SCREEN.get_rect()

    px = SCREEN_RECT.centerx
    py = SCREEN_RECT.centery+200

    current_time = 0
    static_time = 0

    obeliskActiveImg = pygame.image.load("Obelisk_Active.png")
    obeliskInactiveImg = pygame.image.load("Obelisk.png")

    obeliskInactiveImg = pygame.transform.scale(obeliskInactiveImg,(80,80))
    obeliskActiveImg = pygame.transform.scale(obeliskActiveImg,(80,80))

    PedestalActiveImg = pygame.image.load("Pedestal_Active.png")
    PedestalInactiveImg = pygame.image.load("Pedestal_Deactive.png")

    PedestalActiveImg = pygame.transform.scale(PedestalActiveImg,(80,80))
    PedestalInactiveImg = pygame.transform.scale(PedestalInactiveImg,(80,80))

    PedestalImage = [PedestalActiveImg,PedestalInactiveImg]
    current_pedestal = 0

    Pedestalx = 1280//2 - 40
    Pedestaly = 720//2 - 40

    obeliskImg = []
    obeliskx = [600,600-300,600-150,600+150,600+300]
    obelisky = [100,290,555,555,290]
    obeliskRect = []
    obelisksContacted = [0,0,0,0,0] # can be 0 or 1
    num_obelisk = 5

    for i in range(num_obelisk):
        obeliskImg.append(obeliskInactiveImg)
    
    for i in range(len(obeliskImg)):
        obeliskRect.append(obeliskImg[i].get_rect())

    
    def drawPlayer(surface,x,y):
        pygame.draw.circle(surface,('#3880cf'),(x,y),30)


    def drawGunRay(surface,mx,my):
        pygame.draw.line(surface,('#cf5d4622'),(px,py),(mx,my),5)
    
    
    

    running = True
    

    Clock = pygame.time.Clock()

    timer_font = pygame.font.SysFont("Calibri",20)
    timer_text = timer_font.render("",True,('#ffffff'))
    

    def win():
        Level8()
        sys.exit()
    
    def wincheck():
        if obelisksContacted == [1,1,1,1,1]:
            return True
        else:
            return False
    
    encounterActive = False
    static_time = current_time
    while running:
        if not encounterActive:
            current_time = pygame.time.get_ticks()
            static_time = current_time
        
        else:
            current_time = pygame.time.get_ticks()
            
        
        SCREEN.fill('#101010')
        drawPlayer(SCREEN,px,py)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            py -= pspeed
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            py += pspeed
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            px -= pspeed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            px += pspeed
        
        if px > 1280-30:
            px = 1280-30
        
        if px < 30:
            px = 30
        
        if py > 720-30:
            py = 720-30
        
        if py < 30:
            py = 30
        
        for i in range(len(obeliskImg)): # Draw Multiple Obelisks to the screen
            SCREEN.blit(obeliskImg[i],(obeliskx[i],obelisky[i]))
        
        SCREEN.blit(PedestalImage[current_pedestal],(Pedestalx,Pedestaly))

        

        # Main Game Mechanic
        if encounterActive:
            if px in range(obeliskx[0], obeliskx[0]+80):
                if py in range(obelisky[0], obelisky[0]+80):
                    obelisksContacted = [1,0,0,0,0]
                    obeliskImg[0] = obeliskActiveImg
            
            
            if px in range(obeliskx[1], obeliskx[1]+80):
                if py in range(obelisky[1], obelisky[1]+80):
                    if obelisksContacted == [1,0,0,0,0] or obelisksContacted == [1,1,0,0,0]:
                        obelisksContacted[1] = 1
                        obeliskImg[1] = obeliskActiveImg
                    else:
                        obelisksContacted = [0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk
                    
            
            if px in range(obeliskx[2], obeliskx[2]+80):
                if py in range(obelisky[2], obelisky[2]+80):
                    if obelisksContacted == [1,1,0,0,0] or obelisksContacted == [1,1,1,0,0]:
                        obelisksContacted[2] = 1
                        obeliskImg[2] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk
         
            if px in range(obeliskx[3], obeliskx[3]+80):
                if py in range(obelisky[3], obelisky[3]+80):
                    if obelisksContacted == [1,1,1,0,0] or obelisksContacted == [1,1,1,1,0]:
                        obelisksContacted[3] = 1
                        obeliskImg[3] = obeliskActiveImg          
                    else:
                        obelisksContacted = [0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk            
                        
            if px in range(obeliskx[4], obeliskx[4]+80):
                if py in range(obelisky[4], obelisky[4]+80):
                    if obelisksContacted == [1,1,1,1,0] or obelisksContacted == [1,1,1,1,1]:
                        obelisksContacted[4] = 1
                        obeliskImg[4] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk                              
               

        # ----------------------------------------------------
        
        if px in range(Pedestalx,Pedestalx+80):
            if py in range(Pedestaly,Pedestaly+80):
                if encounterActive == False:
                    current_pedestal = 1
                    encounterActive = True
                    static_time = pygame.time.get_ticks()
                    timer_text = timer_font.render(str(30-(current_time-static_time)//1000),True,('#ffffff'))
            
        if current_time - static_time > 30000:
            current_pedestal = 0
            obelisksContacted = [0,0,0,0,0]
            obeliskImg = [obeliskInactiveImg] * num_obelisk
            encounterActive = False
        
        timer_text = timer_font.render("Brand of the Sacrifice: "+str(30-(current_time-static_time)//1000),True,('#ffffff'))
        SCREEN.blit(timer_text,(0,720//2-45//2))
    



        if wincheck():
            win()
        
        Clock.tick(60)
        pygame.display.flip()

# Boss Levels
def Level8():
    pygame.display.set_caption("The Sacrifice - Level 8")
    SCREEN = pygame.display.set_mode((1280,720))
    SCREEN_RECT = SCREEN.get_rect()

    px = SCREEN_RECT.centerx
    py = SCREEN_RECT.centery+200

    current_time = 0
    static_time = 0

    obeliskActiveImg = pygame.image.load("Obelisk_Active.png")
    obeliskInactiveImg = pygame.image.load("Obelisk.png")

    obeliskInactiveImg = pygame.transform.scale(obeliskInactiveImg,(80,80))
    obeliskActiveImg = pygame.transform.scale(obeliskActiveImg,(80,80))

    PedestalActiveImg = pygame.image.load("Pedestal_Active.png")
    PedestalInactiveImg = pygame.image.load("Pedestal_Deactive.png")

    PedestalActiveImg = pygame.transform.scale(PedestalActiveImg,(80,80))
    PedestalInactiveImg = pygame.transform.scale(PedestalInactiveImg,(80,80))

    PedestalImage = [PedestalActiveImg,PedestalInactiveImg]
    current_pedestal = 0

    Pedestalx = 1280//2 - 40
    Pedestaly = 720//2 - 40

    obeliskImg = []
    obeliskx = [600-150,600+300,600-200,600+200,600-300,600+150]
    obelisky = [555,290,100,100,290,555]
    obeliskRect = []
    obelisksContacted = [0,0,0,0,0,0] # can be 0 or 1
    num_obelisk = 6

    grandObeliskImg0 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage0.png"),(1024,1024))
    grandObeliskImg1 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage1.png"),(1024,1024))
    grandObeliskImg2 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage2.png"),(1024,1024))
    grandObeliskImg3 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage3.png"),(1024,1024))

    grandObeliskImg = [grandObeliskImg0,grandObeliskImg1,grandObeliskImg2,grandObeliskImg3]


    for i in range(num_obelisk):
        obeliskImg.append(obeliskInactiveImg)
    
    for i in range(len(obeliskImg)):
        obeliskRect.append(obeliskImg[i].get_rect())

    
    def drawPlayer(surface,x,y):
        pygame.draw.circle(surface,('#3880cf'),(x,y),30)


    def drawGunRay(surface,mx,my):
        pygame.draw.line(surface,('#cf5d4622'),(px,py),(mx,my),5)
    
    
    

    running = True
    

    Clock = pygame.time.Clock()

    timer_font = pygame.font.SysFont("Calibri",20)
    timer_text = timer_font.render("",True,('#ffffff'))
    

    def win():
        Level9()
        sys.exit()
    
    def wincheck():
        if obelisksContacted == [1,1,1,1,1,1]:
            return True
        else:
            return False
    
    encounterActive = False
    static_time = current_time
    while running:
        if not encounterActive:
            current_time = pygame.time.get_ticks()
            static_time = current_time
        
        else:
            current_time = pygame.time.get_ticks()
            
        
        SCREEN.fill('#101010')

        SCREEN.blit(grandObeliskImg[0],(SCREEN_RECT.centerx-490,-650)) # Big Obelisk Drawing to Screen

        drawPlayer(SCREEN,px,py)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            py -= pspeed
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            py += pspeed
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            px -= pspeed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            px += pspeed
        
        if px > 1280-30:
            px = 1280-30
        
        if px < 30:
            px = 30
        
        if py > 720-30:
            py = 720-30
        
        if py < 30:
            py = 30
        
        for i in range(len(obeliskImg)): # Draw Multiple Obelisks to the screen
            SCREEN.blit(obeliskImg[i],(obeliskx[i],obelisky[i]))
        
        SCREEN.blit(PedestalImage[current_pedestal],(Pedestalx,Pedestaly))

        

        # Main Game Mechanic
        if encounterActive:
            if px in range(obeliskx[0], obeliskx[0]+80):
                if py in range(obelisky[0], obelisky[0]+80):
                    obelisksContacted = [1,0,0,0,0,0]
                    obeliskImg[0] = obeliskActiveImg
            
            
            if px in range(obeliskx[1], obeliskx[1]+80):
                if py in range(obelisky[1], obelisky[1]+80):
                    if obelisksContacted == [1,0,0,0,0,0] or obelisksContacted == [1,1,0,0,0,0]:
                        obelisksContacted[1] = 1
                        obeliskImg[1] = obeliskActiveImg
                    else:
                        obelisksContacted = [0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk
                    
            
            if px in range(obeliskx[2], obeliskx[2]+80):
                if py in range(obelisky[2], obelisky[2]+80):
                    if obelisksContacted == [1,1,0,0,0,0] or obelisksContacted == [1,1,1,0,0,0]:
                        obelisksContacted[2] = 1
                        obeliskImg[2] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk
         
            if px in range(obeliskx[3], obeliskx[3]+80):
                if py in range(obelisky[3], obelisky[3]+80):
                    if obelisksContacted == [1,1,1,0,0,0] or obelisksContacted == [1,1,1,1,0,0]:
                        obelisksContacted[3] = 1
                        obeliskImg[3] = obeliskActiveImg          
                    else:
                        obelisksContacted = [0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk            
                        
            if px in range(obeliskx[4], obeliskx[4]+80):
                if py in range(obelisky[4], obelisky[4]+80):
                    if obelisksContacted == [1,1,1,1,0,0] or obelisksContacted == [1,1,1,1,1,0]:
                        obelisksContacted[4] = 1
                        obeliskImg[4] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk


            if px in range(obeliskx[5], obeliskx[5]+80):
                if py in range(obelisky[5], obelisky[5]+80):
                    if obelisksContacted == [1,1,1,1,1,0] or obelisksContacted == [1,1,1,1,1,1]:
                        obelisksContacted[5] = 1
                        obeliskImg[5] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk                              
               

        # ----------------------------------------------------
        
        if px in range(Pedestalx,Pedestalx+80):
            if py in range(Pedestaly,Pedestaly+80):
                if encounterActive == False:
                    current_pedestal = 1
                    encounterActive = True
                    static_time = pygame.time.get_ticks()
                    timer_text = timer_font.render(str(30-(current_time-static_time)//1000),True,('#ffffff'))
            
        if current_time - static_time > 30000:
            current_pedestal = 0
            obelisksContacted = [0,0,0,0,0,0]
            obeliskImg = [obeliskInactiveImg] * num_obelisk
            encounterActive = False
        
        timer_text = timer_font.render("Brand of the Sacrifice: "+str(30-(current_time-static_time)//1000),True,('#ffffff'))
        SCREEN.blit(timer_text,(0,720//2-45//2))
    



        if wincheck():
            SCREEN.blit(grandObeliskImg[1],(SCREEN_RECT.centerx-490,-650)) # Big Obelisk Drawing to Screen
            win()
        
        Clock.tick(60)
        pygame.display.flip()

def Level9():
    pygame.display.set_caption("The Sacrifice - Level 9")
    SCREEN = pygame.display.set_mode((1280,720))
    SCREEN_RECT = SCREEN.get_rect()

    px = SCREEN_RECT.centerx
    py = SCREEN_RECT.centery+200

    current_time = 0
    static_time = 0

    obeliskActiveImg = pygame.image.load("Obelisk_Active.png")
    obeliskInactiveImg = pygame.image.load("Obelisk.png")

    obeliskInactiveImg = pygame.transform.scale(obeliskInactiveImg,(80,80))
    obeliskActiveImg = pygame.transform.scale(obeliskActiveImg,(80,80))

    PedestalActiveImg = pygame.image.load("Pedestal_Active.png")
    PedestalInactiveImg = pygame.image.load("Pedestal_Deactive.png")

    PedestalActiveImg = pygame.transform.scale(PedestalActiveImg,(80,80))
    PedestalInactiveImg = pygame.transform.scale(PedestalInactiveImg,(80,80))

    PedestalImage = [PedestalActiveImg,PedestalInactiveImg]
    current_pedestal = 0

    Pedestalx = 1280//2 - 40
    Pedestaly = 720//2 - 40

    obeliskImg = []
    obeliskx = [600-200,600-300,600-150,600+150,600+300,600+200]
    obelisky = [100,290,555,555,290,100]
    obeliskRect = []
    obelisksContacted = [0,0,0,0,0,0] # can be 0 or 1
    num_obelisk = 6

    grandObeliskImg0 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage0.png"),(1024,1024))
    grandObeliskImg1 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage1.png"),(1024,1024))
    grandObeliskImg2 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage2.png"),(1024,1024))
    grandObeliskImg3 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage3.png"),(1024,1024))

    grandObeliskImg = [grandObeliskImg0,grandObeliskImg1,grandObeliskImg2,grandObeliskImg3]


    for i in range(num_obelisk):
        obeliskImg.append(obeliskInactiveImg)
    
    for i in range(len(obeliskImg)):
        obeliskRect.append(obeliskImg[i].get_rect())

    
    def drawPlayer(surface,x,y):
        pygame.draw.circle(surface,('#3880cf'),(x,y),30)


    def drawGunRay(surface,mx,my):
        pygame.draw.line(surface,('#cf5d4622'),(px,py),(mx,my),5)
    
    
    

    running = True
    

    Clock = pygame.time.Clock()

    timer_font = pygame.font.SysFont("Calibri",20)
    timer_text = timer_font.render("",True,('#ffffff'))
    

    def win():
        Level10()
        sys.exit()
    
    def wincheck():
        if obelisksContacted == [1,1,1,1,1,1]:
            return True
        else:
            return False
    
    encounterActive = False
    static_time = current_time
    while running:
        if not encounterActive:
            current_time = pygame.time.get_ticks()
            static_time = current_time
        
        else:
            current_time = pygame.time.get_ticks()
            
        
        SCREEN.fill('#101010')

        SCREEN.blit(grandObeliskImg[1],(SCREEN_RECT.centerx-490,-650)) # Big Obelisk Drawing to Screen

        drawPlayer(SCREEN,px,py)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            py -= pspeed
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            py += pspeed
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            px -= pspeed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            px += pspeed
        
        if px > 1280-30:
            px = 1280-30
        
        if px < 30:
            px = 30
        
        if py > 720-30:
            py = 720-30
        
        if py < 30:
            py = 30
        
        for i in range(len(obeliskImg)): # Draw Multiple Obelisks to the screen
            SCREEN.blit(obeliskImg[i],(obeliskx[i],obelisky[i]))
        
        SCREEN.blit(PedestalImage[current_pedestal],(Pedestalx,Pedestaly))

        

        # Main Game Mechanic
        if encounterActive:
            if px in range(obeliskx[0], obeliskx[0]+80):
                if py in range(obelisky[0], obelisky[0]+80):
                    obelisksContacted = [1,0,0,0,0,0]
                    obeliskImg[0] = obeliskActiveImg
            
            
            if px in range(obeliskx[1], obeliskx[1]+80):
                if py in range(obelisky[1], obelisky[1]+80):
                    if obelisksContacted == [1,0,0,0,0,0] or obelisksContacted == [1,1,0,0,0,0]:
                        obelisksContacted[1] = 1
                        obeliskImg[1] = obeliskActiveImg
                    else:
                        obelisksContacted = [0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk
                    
            
            if px in range(obeliskx[2], obeliskx[2]+80):
                if py in range(obelisky[2], obelisky[2]+80):
                    if obelisksContacted == [1,1,0,0,0,0] or obelisksContacted == [1,1,1,0,0,0]:
                        obelisksContacted[2] = 1
                        obeliskImg[2] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk
         
            if px in range(obeliskx[3], obeliskx[3]+80):
                if py in range(obelisky[3], obelisky[3]+80):
                    if obelisksContacted == [1,1,1,0,0,0] or obelisksContacted == [1,1,1,1,0,0]:
                        obelisksContacted[3] = 1
                        obeliskImg[3] = obeliskActiveImg          
                    else:
                        obelisksContacted = [0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk            
                        
            if px in range(obeliskx[4], obeliskx[4]+80):
                if py in range(obelisky[4], obelisky[4]+80):
                    if obelisksContacted == [1,1,1,1,0,0] or obelisksContacted == [1,1,1,1,1,0]:
                        obelisksContacted[4] = 1
                        obeliskImg[4] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk


            if px in range(obeliskx[5], obeliskx[5]+80):
                if py in range(obelisky[5], obelisky[5]+80):
                    if obelisksContacted == [1,1,1,1,1,0] or obelisksContacted == [1,1,1,1,1,1]:
                        obelisksContacted[5] = 1
                        obeliskImg[5] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk                              
               

        # ----------------------------------------------------
        
        if px in range(Pedestalx,Pedestalx+80):
            if py in range(Pedestaly,Pedestaly+80):
                if encounterActive == False:
                    current_pedestal = 1
                    encounterActive = True
                    static_time = pygame.time.get_ticks()
                    timer_text = timer_font.render(str(30-(current_time-static_time)//1000),True,('#ffffff'))
            
        if current_time - static_time > 30000:
            current_pedestal = 0
            obelisksContacted = [0,0,0,0,0,0]
            obeliskImg = [obeliskInactiveImg] * num_obelisk
            encounterActive = False
        
        timer_text = timer_font.render("Brand of the Sacrifice: "+str(30-(current_time-static_time)//1000),True,('#ffffff'))
        SCREEN.blit(timer_text,(0,720//2-45//2))
    



        if wincheck():
            SCREEN.blit(grandObeliskImg[2],(SCREEN_RECT.centerx-490,-650)) # Big Obelisk Drawing to Screen
            win()
        
        Clock.tick(60)
        pygame.display.flip()

def Level10():
    pygame.display.set_caption("The Sacrifice - Level 10")
    SCREEN = pygame.display.set_mode((1280,720))
    SCREEN_RECT = SCREEN.get_rect()

    px = SCREEN_RECT.centerx
    py = SCREEN_RECT.centery+200

    current_time = 0
    static_time = 0

    obeliskActiveImg = pygame.image.load("Obelisk_Active.png")
    obeliskInactiveImg = pygame.image.load("Obelisk.png")

    obeliskInactiveImg = pygame.transform.scale(obeliskInactiveImg,(80,80))
    obeliskActiveImg = pygame.transform.scale(obeliskActiveImg,(80,80))

    PedestalActiveImg = pygame.image.load("Pedestal_Active.png")
    PedestalInactiveImg = pygame.image.load("Pedestal_Deactive.png")

    PedestalActiveImg = pygame.transform.scale(PedestalActiveImg,(80,80))
    PedestalInactiveImg = pygame.transform.scale(PedestalInactiveImg,(80,80))

    PedestalImage = [PedestalActiveImg,PedestalInactiveImg]
    current_pedestal = 0

    Pedestalx = 1280//2 - 40
    Pedestaly = 720//2 - 40

    obeliskImg = []
    obeliskx = [600+300,600-200,600+200,600-150,600-300,600+150]
    obelisky = [290,100,100,555,290,555]

    obeliskRect = []
    obelisksContacted = [0,0,0,0,0,0] # can be 0 or 1
    num_obelisk = 6

    grandObeliskImg0 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage0.png"),(1024,1024))
    grandObeliskImg1 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage1.png"),(1024,1024))
    grandObeliskImg2 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage2.png"),(1024,1024))
    grandObeliskImg3 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage3.png"),(1024,1024))

    grandObeliskImg = [grandObeliskImg0,grandObeliskImg1,grandObeliskImg2,grandObeliskImg3]


    for i in range(num_obelisk):
        obeliskImg.append(obeliskInactiveImg)
    
    for i in range(len(obeliskImg)):
        obeliskRect.append(obeliskImg[i].get_rect())

    
    def drawPlayer(surface,x,y):
        pygame.draw.circle(surface,('#3880cf'),(x,y),30)


    def drawGunRay(surface,mx,my):
        pygame.draw.line(surface,('#cf5d4622'),(px,py),(mx,my),5)
    
    
    

    running = True
    

    Clock = pygame.time.Clock()

    timer_font = pygame.font.SysFont("Calibri",20)
    timer_text = timer_font.render("",True,('#ffffff'))
    

    def win():
        Level10End()
        sys.exit()
    
    def wincheck():
        if obelisksContacted == [1,1,1,1,1,1]:
            return True
        else:
            return False
    
    encounterActive = False
    static_time = current_time
    while running:
        if not encounterActive:
            current_time = pygame.time.get_ticks()
            static_time = current_time
        
        else:
            current_time = pygame.time.get_ticks()
            
        
        SCREEN.fill('#101010')

        SCREEN.blit(grandObeliskImg[2],(SCREEN_RECT.centerx-490,-650)) # Big Obelisk Drawing to Screen

        drawPlayer(SCREEN,px,py)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            py -= pspeed
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            py += pspeed
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            px -= pspeed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            px += pspeed
        
        if px > 1280-30:
            px = 1280-30
        
        if px < 30:
            px = 30
        
        if py > 720-30:
            py = 720-30
        
        if py < 30:
            py = 30
        
        for i in range(len(obeliskImg)): # Draw Multiple Obelisks to the screen
            SCREEN.blit(obeliskImg[i],(obeliskx[i],obelisky[i]))
        
        SCREEN.blit(PedestalImage[current_pedestal],(Pedestalx,Pedestaly))

        

        # Main Game Mechanic
        if encounterActive:
            if px in range(obeliskx[0], obeliskx[0]+80):
                if py in range(obelisky[0], obelisky[0]+80):
                    obelisksContacted = [1,0,0,0,0,0]
                    obeliskImg[0] = obeliskActiveImg
            
            
            if px in range(obeliskx[1], obeliskx[1]+80):
                if py in range(obelisky[1], obelisky[1]+80):
                    if obelisksContacted == [1,0,0,0,0,0] or obelisksContacted == [1,1,0,0,0,0]:
                        obelisksContacted[1] = 1
                        obeliskImg[1] = obeliskActiveImg
                    else:
                        obelisksContacted = [0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk
                    
            
            if px in range(obeliskx[2], obeliskx[2]+80):
                if py in range(obelisky[2], obelisky[2]+80):
                    if obelisksContacted == [1,1,0,0,0,0] or obelisksContacted == [1,1,1,0,0,0]:
                        obelisksContacted[2] = 1
                        obeliskImg[2] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk
         
            if px in range(obeliskx[3], obeliskx[3]+80):
                if py in range(obelisky[3], obelisky[3]+80):
                    if obelisksContacted == [1,1,1,0,0,0] or obelisksContacted == [1,1,1,1,0,0]:
                        obelisksContacted[3] = 1
                        obeliskImg[3] = obeliskActiveImg          
                    else:
                        obelisksContacted = [0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk            
                        
            if px in range(obeliskx[4], obeliskx[4]+80):
                if py in range(obelisky[4], obelisky[4]+80):
                    if obelisksContacted == [1,1,1,1,0,0] or obelisksContacted == [1,1,1,1,1,0]:
                        obelisksContacted[4] = 1
                        obeliskImg[4] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk


            if px in range(obeliskx[5], obeliskx[5]+80):
                if py in range(obelisky[5], obelisky[5]+80):
                    if obelisksContacted == [1,1,1,1,1,0] or obelisksContacted == [1,1,1,1,1,1]:
                        obelisksContacted[5] = 1
                        obeliskImg[5] = obeliskActiveImg
                    
                    else:
                        obelisksContacted = [0,0,0,0,0,0]
                        obeliskImg = [obeliskInactiveImg] * num_obelisk                              
               

        # ----------------------------------------------------
        
        if px in range(Pedestalx,Pedestalx+80):
            if py in range(Pedestaly,Pedestaly+80):
                if encounterActive == False:
                    current_pedestal = 1
                    encounterActive = True
                    static_time = pygame.time.get_ticks()
                    timer_text = timer_font.render(str(30-(current_time-static_time)//1000),True,('#ffffff'))
            
        if current_time - static_time > 30000:
            current_pedestal = 0
            obelisksContacted = [0,0,0,0,0,0]
            obeliskImg = [obeliskInactiveImg] * num_obelisk
            encounterActive = False
        
        timer_text = timer_font.render("Brand of the Sacrifice: "+str(30-(current_time-static_time)//1000),True,('#ffffff'))
        SCREEN.blit(timer_text,(0,720//2-45//2))


        if wincheck():
            SCREEN.blit(grandObeliskImg[3],(SCREEN_RECT.centerx-490,-650)) # Big Obelisk Drawing to Screen
            win()
        
        Clock.tick(60)
        pygame.display.flip()
   

def Level10End():
    pygame.display.set_caption("The Sacrifice - End Game")
    SCREEN = pygame.display.set_mode((1280,720))
    SCREEN_RECT = SCREEN.get_rect()

    px = SCREEN_RECT.centerx
    py = SCREEN_RECT.centery+200

    current_time = 0
    static_time = 0

    obeliskActiveImg = pygame.image.load("Obelisk_Active.png")
    obeliskInactiveImg = pygame.image.load("Obelisk.png")

    obeliskInactiveImg = pygame.transform.scale(obeliskInactiveImg,(80,80))
    obeliskActiveImg = pygame.transform.scale(obeliskActiveImg,(80,80))

    PedestalActiveImg = pygame.image.load("Pedestal_Active.png")
    PedestalInactiveImg = pygame.image.load("Pedestal_Deactive.png")

    PedestalActiveImg = pygame.transform.scale(PedestalActiveImg,(80,80))
    PedestalInactiveImg = pygame.transform.scale(PedestalInactiveImg,(80,80))

    PedestalImage = [PedestalActiveImg,PedestalInactiveImg]
    current_pedestal = 0

    Pedestalx = 1280//2 - 40
    Pedestaly = 720//2 - 40

    obeliskImg = []
    obeliskx = [600-200,600-300,600-150,600+150,600+300,600+200]
    obelisky = [100,290,555,555,290,100]
    obeliskRect = []
    obelisksContacted = [0,0,0,0,0,0] # can be 0 or 1
    num_obelisk = 6

    grandObeliskImg0 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage0.png"),(1024,1024))
    grandObeliskImg1 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage1.png"),(1024,1024))
    grandObeliskImg2 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage2.png"),(1024,1024))
    grandObeliskImg3 = pygame.transform.scale(pygame.image.load("Grand_Obelisk_Stage3.png"),(1024,1024))

    grandObeliskImg = [grandObeliskImg0,grandObeliskImg1,grandObeliskImg2,grandObeliskImg3]

    EndScreenOverlay = pygame.image.load("EndScreenOverlay.png").convert_alpha()

    HomeButtonImg = pygame.image.load("Home.png")
    HomeButtonRect = HomeButtonImg.get_rect()

    HomeButtonRect.x = SCREEN_RECT.width-HomeButtonRect.width
    HomeButtonRect.y = SCREEN_RECT.height-HomeButtonRect.height

    for i in range(num_obelisk):
        obeliskImg.append(obeliskInactiveImg)
    
    for i in range(len(obeliskImg)):
        obeliskRect.append(obeliskImg[i].get_rect())

    
    def drawPlayer(surface,x,y):
        pygame.draw.circle(surface,('#3880cf'),(x,y),30)


    def drawGunRay(surface,mx,my):
        pygame.draw.line(surface,('#cf5d4622'),(px,py),(mx,my),5)
    

    player_data_file = open("player_data.txt",'w')

    
    

    running = True
    

    Clock = pygame.time.Clock()

    timer_font = pygame.font.SysFont("Calibri",20)
    timer_text = timer_font.render("",True,('#ffffff'))
    

    def win():
        TitleScreen()
        sys.exit()
    
    def wincheck():
        if obelisksContacted == [1,1,1,1,1,1]:
            return True
        else:
            return False
    
    encounterActive = False
    static_time = current_time

    y = 1050
    animationEnd = False
    while running:
        if not encounterActive:
            current_time = pygame.time.get_ticks()
            static_time = current_time
        
        else:
            current_time = pygame.time.get_ticks()
            
        
        SCREEN.fill('#101010') 
        if not animationEnd:           
            SCREEN.blit(grandObeliskImg[3],(SCREEN_RECT.centerx-490,-y)) # Big Obelisk Drawing to Screen
            if y > 200:
                y -= 2
            
            if y == 200:
                SCREEN.blit(EndScreenOverlay,(0,0))

                SCREEN.blit(HomeButtonImg,(HomeButtonRect))
        
       

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                player_data_file.write("True")
                player_data_file.close()
                running = False
                
            
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()

                if HomeButtonRect.collidepoint(mx,my):

                    player_data_file.write("True")
                    player_data_file.close()
                    TitleScreen()
                    sys.exit()
            
                         
               

        # ----------------------------------------------------
        
    


        if wincheck():
            SCREEN.blit(grandObeliskImg[3],(SCREEN_RECT.centerx-490,-650)) # Big Obelisk Drawing to Screen
            win()
        
        Clock.tick(30)
        pygame.display.flip()


def TitleScreen():
    player_data_file = open("player_data.txt", "r")
    player_data = player_data_file.read()
    player_data_file.close()

    SCREEN = pygame.display.set_mode((1280,720))
    SCREEN_RECT = SCREEN.get_rect()

    running = True

    backgroundImg = pygame.image.load("TitleScreenBackground.png")
    backgroundImgRect = backgroundImg.get_rect()

    font = pygame.font.SysFont("Chiller",100)
    text = font.render("Play",True,('#fcd758'))
    text_rect = text.get_rect(center = SCREEN_RECT.center)

    while running:
        SCREEN.blit(backgroundImg,backgroundImgRect)
        SCREEN.blit(text,text_rect)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()

                if text_rect.collidepoint(mx,my):
                    if player_data == "True":
                        LevelSelect()
                        sys.exit()
                    else:
                        Level1()
                        sys.exit()
                    
            
        pygame.display.flip()

def LevelSelect():
    SCREEN = pygame.display.set_mode((1280,720))
    SCREEN_RECT = SCREEN.get_rect()
    running = True

    font = pygame.font.SysFont("Chiller",52)
    selectLevelFont = pygame.font.SysFont("Chiller",80)


    selectLevelText = selectLevelFont.render("Select Level",True,('#ffffff'))
    selectLevelRect = selectLevelText.get_rect()
    selectLevelRect.centerx = SCREEN_RECT.centerx
    selectLevelRect.centery = 720//6


    def playLevel(level:int):
        level_dict = {
            1:Level1,
            2:Level2,
            3:Level3,
            4:Level4,
            5:Level5,
            6:Level6,
            7:Level7,
            8:Level8,
            9:Level9,
            10:Level10,
        }
        level_dict[level]()
        sys.exit()
    
    l1 = font.render("1",True,('#ffffff'))
    l2 = font.render("2",True,('#ffffff'))
    l3 = font.render("3",True,('#ffffff'))
    l4 = font.render("4",True,('#ffffff'))
    l5 = font.render("5",True,('#ffffff'))
    l6 = font.render("6",True,('#ffffff'))
    l7 = font.render("7",True,('#ffffff'))
    l8 = font.render("8",True,('#ffffff'))
    l9 = font.render("9",True,('#ffffff'))
    l10 = font.render("10",True,('#ffffff'))

    l1_RECT = l1.get_rect()
    l2_RECT = l2.get_rect()
    l3_RECT = l3.get_rect()
    l4_RECT = l4.get_rect()
    l5_RECT = l5.get_rect()
    l6_RECT = l6.get_rect()
    l7_RECT = l7.get_rect()
    l8_RECT = l8.get_rect()
    l9_RECT = l9.get_rect()
    l10_RECT = l10.get_rect()
    level_arr = [[l1,l2,l3,l4,l5],[l6,l7,l8,l9,l10]]
    level_rect_arr = [[l1_RECT,l2_RECT,l3_RECT,l4_RECT,l5_RECT],[l6_RECT,l7_RECT,l8_RECT,l9_RECT,l10_RECT]]

    padx = 1280//4 # Change X Padding of Number Select Panel
    pady = 720//4 + 100 # # Change Y Padding of Number Select Panel
    margin = 150 # Change the Distance between Each Number

    HomeButtonImg = pygame.image.load("Home.png")
    HomeButtonRect = HomeButtonImg.get_rect()
    HomeButtonRect.x = SCREEN_RECT.w - 64
    HomeButtonRect.y = SCREEN_RECT.h - 64
    while running:
        SCREEN.fill('#000000')
        SCREEN.blit(HomeButtonImg, HomeButtonRect)
        SCREEN.blit(selectLevelText,selectLevelRect)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()

                if l1_RECT.collidepoint(mx,my):
                    playLevel(1)
                
                if l2_RECT.collidepoint(mx,my):
                    playLevel(2)
                
                if l3_RECT.collidepoint(mx,my):
                    playLevel(3)
                
                if l4_RECT.collidepoint(mx,my):
                    playLevel(4)
                
                if l5_RECT.collidepoint(mx,my):
                    playLevel(5)
                
                if l6_RECT.collidepoint(mx,my):
                    playLevel(6)
                
                if l7_RECT.collidepoint(mx,my):
                    playLevel(7)
                
                if l8_RECT.collidepoint(mx,my):
                    playLevel(8)
                
                if l9_RECT.collidepoint(mx,my):
                    playLevel(9)

                if l10_RECT.collidepoint(mx,my):
                    playLevel(10)
                
                if HomeButtonRect.collidepoint(mx,my):
                    TitleScreen()
                    sys.exit()
        
        posx = 0
        posy = 0
        while posx < len(level_arr):
            posy = 0
            while posy < len(level_arr[posx]):
                SCREEN.blit(level_arr[posx][posy],(posy*margin+padx,posx*margin+pady))
                level_rect_arr[posx][posy].x = posy*margin+padx
                level_rect_arr[posx][posy].y = posx*margin+pady
                posy += 1
            posx += 1                   
            
        pygame.display.flip()


if __name__ == "__main__":
    TitleScreen()