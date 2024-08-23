from constante import *
from porta import *
from UI import *
from display import *


#colocar porta que voce está usando no arduino
Arduino = serial.Serial("COM3" ,9600, timeout=1)

y = [30]*NUM
count = NUM-1

pygame.font.init()
my_font = pygame.font.SysFont('arial', 20)
text_surface = my_font.render('P - pause / unpause       A - acelera       D - desacelera', False, (0, 0, 0))
text_surface2 = my_font.render('5V', False, (0, 0, 0))
text_surface2 = my_font.render('5V', False, (0, 0, 0))


#controle variaveis
passar = 3
pause = False
running = True

for i in range(NUM):
    y[i] = 300*i/NUM

r = getData(Arduino)
print(r)

#cria janela
screen = pygame.display.set_mode((WIDTH, HIGH)) 
pygame.display.set_caption('Ociloscopio') 
screen.fill(COR_BACKGROUND)


def AtualizaPontos():
    global count
    global passar
    for i in range(passar):
        getData(Arduino)
    r = getData(Arduino)*(400/1024)
    y[count] = r
    count+=1
    if count >= NUM:
        count = 0



def textoTempo():
    global my_font
    global passar
    x = (passar + 1)*5
    s = str(x)+'s'
    ts = my_font.render(s, False, (0, 0, 0))
    screen.blit(ts, (WIDTH-BORDA,TAMYDISP+BORDA))




while running:
    screen.blit(text_surface, (BORDA,TAMYDISP+2*BORDA))
    screen.blit(text_surface2, (BORDA-30,BORDA-20))
    textoTempo()
    
    t1 = threading.Thread(target=DrawGrafico, args=(screen,y,count,))
    t2 = threading.Thread(target=UpdateUI, args=(screen,))
    t1.start()
    t2.start()
    #DrawGrafico(screen,y,count)
    #UpdateUI(screen)
    if not pause:
        AtualizaPontos()
    t2.join()
    t1.join()
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause = not pause
            if event.key == pygame.K_d:
                passar += 1
            if event.key == pygame.K_a:
                if passar > 0:
                    passar -= 1          



pygame.quit()

















