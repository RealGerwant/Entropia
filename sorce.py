import atom
import pygame
import math
import matplotlib.pyplot as plt

def main():
    r = int(input("Podaj r:"))
    ScreenHeight = int(input("Podaj wysokość okna:"))
    advanceMode = int(input("Run in advance mode? (0 or 1):"))
    ScreenWidth  = int(ScreenHeight * 16/9)


    #### PĘDY
    P = r+(1-r%2)
    qP = 2*P+1

    ####PRZESTRZEN
    R = 2*r+1
    qR=2*R+1

    r= 2**r

    deltaT = 1/(2*P)
    Atoms =[]
    Velocities = []

    BoxSize = ScreenHeight/qR

    Radius =int(BoxSize/2)

    RozmiarTextu = int(ScreenHeight/45)

    IleWBoxie =[]

    for i in range(qR):
        IleWBoxie.append([])

    for i in range(qR):
        for j in range(qR):
            IleWBoxie[i].append([])

    for i in range(qR):
            for j in range(qR):
                for k in range(5):
                    IleWBoxie[i][j].append(0)

    for i in range(r):
        x= atom.Atom()
        x.RandomVelocity(P)
        Atoms.append(x)


    for i in  range(r):
        Atoms[i].SetPosition(10, Radius + i * (ScreenHeight/ r))


    pygame.init()

    font= pygame.font.SysFont("monospace", RozmiarTextu)


    ColorRed = (255,0,0)
    ColorBlue = (0,0,255)
    ColorBlack = (0,0,0)

    resolution = (ScreenHeight *2,ScreenHeight)
    window = pygame.display.set_mode(resolution,pygame.DOUBLEBUF)
    surface = pygame.display.get_surface()
    clock = pygame.time.Clock()

    WartoscPedow =[]

    for i in range(qP):
        WartoscPedow.append([])

    for i in range(qP):
        Velocities.append([])
        for j in range(qP):
            Velocities[i].append(0)

    Entropia =[]
    tj =0


    while True:
        pygame.event.get()

        for i in range(qR):
            for j in range(qR):
                for k in range (5):
                    IleWBoxie[j][i][k] =0

# 1 -dx +dy| 2 +dx +dy
# 3 -dx -dy| 3 +dx -dy

        for i in range(r):
            IleWBoxie[math.floor(Atoms[i].y / BoxSize)-1][math.floor(Atoms[i].x / BoxSize)-1][0] +=1
            if (Atoms[i].dx < 0 and Atoms[i].dy > 0):
                IleWBoxie[math.floor(Atoms[i].y / BoxSize) - 1][math.floor(Atoms[i].x / BoxSize) - 1][1] += 1
            if (Atoms[i].dx > 0 and Atoms[i].dy > 0):
                IleWBoxie[math.floor(Atoms[i].y / BoxSize) - 1][math.floor(Atoms[i].x / BoxSize) - 1][2] += 1
            if (Atoms[i].dx < 0 and Atoms[i].dy < 0):
                IleWBoxie[math.floor(Atoms[i].y / BoxSize) - 1][math.floor(Atoms[i].x / BoxSize) - 1][3] += 1
            if (Atoms[i].dx > 0 and Atoms[i].dy < 0):
                IleWBoxie[math.floor(Atoms[i].y / BoxSize) - 1][math.floor(Atoms[i].x / BoxSize) - 1][4] += 1


        #########################

        mianownik =1
        licznik = math.factorial(r)

        if (advanceMode == 0):
            print("nAD")
            for i in range(qR):
                for j in range(qR):
                    mianownik *= math.factorial(IleWBoxie[j][i][0])
        else:
            print("AD")
            for i in range(qR):
                for j in range(qR):
                    for k in range(1,5):
                        mianownik *= math.factorial(IleWBoxie[j][i][k])

        PT = licznik//mianownik

        entropia = math.log(PT,2)
        print(entropia)
        Entropia.append(entropia)
        if tj % 2 == 0:
            plt.plot(Entropia)
        else:
            plt.close()

        plt.show()
        ##############

        if tj%100 == 0 and tj != 0:
            x= str(input("Go for more?: "))
            if x != "y":
                break;

        for i in range(qP):
            for j in range(qP):
                Velocities[i][j] = 0

        for i in range(r):
            Velocities[Atoms[i].dy + P][Atoms[i].dx + P] +=1

        for i in range(qP):
            text = ""
            for j in range(qP):
                text += str(Velocities[i][j]) + "  "
            WartoscPedow[i] = text

        for i in range(qP):
            WartoscPedow[i] = font.render(WartoscPedow[i],1,ColorRed)



        for i in range(qR):
            pygame.draw.lines(window, ColorRed, False, [((i+1) * BoxSize, 0), ((i+1) * BoxSize, ScreenHeight)], 1)
            pygame.draw.lines(window, ColorRed, False, [(0, i * BoxSize), (ScreenHeight, i * BoxSize)], 1)


        window.fill(ColorBlack)

        for i in range(qR):
            pygame.draw.lines(window, ColorRed, False, [((i + 1) * BoxSize, 0), ((i + 1) * BoxSize, ScreenHeight)], 1)
            pygame.draw.lines(window, ColorRed, False, [(0, i * BoxSize), (ScreenHeight, i * BoxSize)], 1)

        for i in range(qP):
            window.blit(WartoscPedow[i],(ScreenHeight +50,(i+1)* RozmiarTextu * 2))

        pygame.display.update()

        for i in range(r):
            pygame.draw.circle(window,ColorBlue,(int(Atoms[i].x),int(Atoms[i].y)),Radius)

        pygame.display.update()

        for i in range(r):
            Atoms[i].MakeMove(deltaT,ScreenHeight,Radius)

        tj+=1

main()