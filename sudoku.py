from random import randrange
import time


sudoku = [3, 0, 6, 5, 0, 8, 4, 0, 0,
          5, 2, 0, 0, 0, 0, 0, 0, 0,
          0, 8, 7, 0, 0, 0, 0, 3, 1,
          0, 0, 3, 0, 1, 0, 0, 8, 0,
          9, 0, 0, 8, 6, 3, 0, 0, 5,
          0, 5, 0, 0, 9, 0, 6, 0, 0,
          1, 3, 0, 0, 0, 0, 2, 5, 0,
          0, 0, 0, 0, 0, 0, 0, 7, 4,
          0, 0, 5, 2, 0, 6, 3, 0, 0]

vaikein_sudoku = [0, 0, 5, 3, 0, 0, 0, 0, 0,
                  8, 0, 0, 0, 0, 0, 0, 2, 0,
                  0, 7, 0, 0, 1, 0, 5, 0, 0,
                  4, 0, 0, 0, 0, 5, 3, 0, 0,
                  0, 1, 0, 0, 7, 0, 0, 0, 6,
                  0, 0, 3, 2, 0, 0, 0, 8, 0,
                  0, 6, 0, 5, 0, 0, 0, 0, 9,
                  0, 0, 4, 0, 0, 0, 0, 3, 0,
                  0, 0, 0, 0, 0, 9, 7, 0, 0]

koneelle_vaikea_sudoku = [0,0,0,0,0,0,0,0,0,
                          0,0,0,0,0,3,0,8,5,
                          0,0,1,0,2,0,0,0,0,
                          0,0,0,5,0,7,0,0,0,
                          0,0,4,0,0,0,1,0,0,
                          0,9,0,0,0,0,0,0,0,
                          5,0,0,0,0,0,0,7,3,
                          0,0,2,0,1,0,0,0,0,
                          0,0,0,0,4,0,0,0,9]                  


koko = 9
aputaulukko = []
taulukko = []




##luodaan ensin syötteestä sudoku taulukko jota voidaan käyttää ratkaisemiseen
def muotoile(sudo):
    taulukko.clear()
    apurivi = []
    i = 0

    for number in sudo:
        apurivi.append(number)
        i = i + 1
        
        if i == 9:
            taulukko.append(apurivi)
            apurivi = []
            i = 0



def piirrä(a):
    #rivin i sarake j tulostetaan 
    for i in range(koko):
        for j in range(koko):
            print(a[i][j],end = " ")
        print()    


def tarkistaja(taulukko, rivi, sarake):

    #katsotaan ollaanko rivissä 8 ja viimeisessä sarakkeessa jos ollaan palauttaa True ja sen jälkeen ratkaistaan viimeinen rivi

    if (rivi == koko -1 and sarake == koko):
        return True

    #katsotaan ollaanko viimeisessä sarakkeessa riviltä

    if (sarake == koko):
        rivi += 1
        sarake = 0
    
    #tarkastetaan onko jo valitussa kohdassa luku valmiiksi ja jos on niin mennään seuraavaan kohtaan

    if (taulukko[rivi][sarake] > 0):                                            
        return tarkistaja (taulukko, rivi, sarake +1)


    #annetaan kohdalle numero ja tarkastetaan se, mikäli se on oikein lisätään se

    for numero in range(1,koko+1,1):

        if ratkaisija(taulukko,rivi,sarake,numero):
            taulukko[rivi][sarake] = numero
            if tarkistaja(taulukko,rivi,sarake+1):
                return True
        taulukko[rivi][sarake] = 0

    return False            





def ratkaisija(taulukko, rivi, sarake, numero):

    #tarkistetaan onko rivillä jo annettu numero 
    for x in range(koko):
        if taulukko[rivi][x] == numero:
            return False

    #tarkistetaan onko sarakkeessa jo annettu numero
    for x in range(koko):
        if taulukko[x][sarake] == numero:
            return False

    #sudoku lauta on jaettu 9 pienenempään neliöön jotka koostuvat 9 kohdasta. Oikea neliö saadaan ottamalla jakojäännös rivinumerosta ja miinustamalla se rivinumerosta.

    aloitusRivi = rivi - rivi % 3
    aloitusSarake = sarake - sarake % 3

    #tarkistetaan onko 3x3 neliössä jo annettu numero

    for r in range(3):
        if taulukko[aloitusRivi + r][aloitusSarake] == numero:
            return False
        for s in range(3):
            if taulukko[aloitusRivi + r][aloitusSarake + s] == numero:
                return False


    #jos kaikki edelliset meni läpi palautetaan true ja annettu numero on oikein

    return True

def generoi_sudoku(vaikeusaste,kerrat):
    

    tyhjä_sudoku = [0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    muotoile(tyhjä_sudoku)
    

    for rivit in range(koko):
        taulukko[rivit][randrange(9)] = randrange(10)
        
    #käytetään ratkaisijaa tarkistamaan virheet taulukon generoinnissa eli sama numero useammin samassa rivissä yms.

    for rivit in range(koko):
        for numerot in range(1,10):
            if duplikaattien_tarkistaja(taulukko,rivit,sarake=rivit,numero=numerot) == False:              
                taulukko.clear()
                
                generoi_sudoku(vaikeusaste,kerrat+1)
                
            else:
                pass

    return tarkistaja(taulukko,0,0),(sudokun_tyhjentäjä(taulukko,vaikeusaste,0))                        ###########palauttaa generatorin tuloksen
        
        


def duplikaattien_tarkistaja(taulukko, rivi, sarake, numero):

    määrä = 0

    #tarkistetaan onko rivillä jo annettu numero 
    for x in range(koko):
        if taulukko[rivi][x] == numero:
            määrä += 1
            
            if määrä > 1:
                return False

            
    määrä = 0
    #tarkistetaan onko sarakkeessa jo annettu numero
    for x in range(koko):
        if taulukko[x][sarake] == numero:
            määrä += 1

            if määrä > 1:
                return False

    #sudoku lauta on jaettu 9 pienenempään neliöön jotka koostuvat 9 kohdasta. Oikea neliö saadaan ottamalla jakojäännös rivinumerosta ja miinustamalla se rivinumerosta.

    aloitusRivi = rivi - rivi % 3
    aloitusSarake = sarake - sarake % 3

    #tarkistetaan onko 3x3 neliössä jo annettu numero
    määrä = 0
    for oma_numero in range(1,10):
        määrä=0
        for r in range(3):
            if taulukko[aloitusRivi + r][aloitusSarake] == oma_numero:
                määrä += 1
            if määrä > 1:
                
                return False
            for s in range(3):
                if taulukko[aloitusRivi + r][aloitusSarake + s] == oma_numero:
                    määrä += 1
                if määrä > 1:
                    
                    return False

    if määrä > 1:
         
        return False

    #jos kaikki edelliset meni läpi palautetaan true ja annettu numero on oikein

    return True


def sudokun_tyhjentäjä(taulukko,vaikeusaste,poistetut):
    #1 helppo  20 - 30
    #2 keski  30-50
    #3 vaikea   50-64
    
    if vaikeusaste == 1:
        for r in range(koko):
            for s in range(koko):
                if randrange(2) == 1 and taulukko[r][s] != 0 and poistetut <45:
                    taulukko[r][s] = 0
                    poistetut = poistetut +1
                if poistetut < 30 and poistetut >45:
                    return False    
                
        if poistetut < 30:
            sudokun_tyhjentäjä(taulukko,vaikeusaste,poistetut)
        else:
            return piirrä(taulukko),print(poistetut)   

    if vaikeusaste == 2:  
        for r in range(koko):
            for s in range(koko):
                if randrange(2) == 1 and taulukko[r][s] != 0 and poistetut <55:
                    taulukko[r][s] = 0
                    poistetut = poistetut +1
                if poistetut < 45 and poistetut >55:
                    return False    
                
        if poistetut < 45:
            sudokun_tyhjentäjä(taulukko,vaikeusaste,poistetut)
        else:
            return piirrä(taulukko),print(poistetut)
        
    if vaikeusaste == 3:
       
        for r in range(koko):
            for s in range(koko):
                if randrange(2) == 1 and taulukko[r][s] != 0 and poistetut <64:
                    taulukko[r][s] = 0
                    poistetut = poistetut +1
                if poistetut < 60 and poistetut >64:
                    return False    
                
        if poistetut < 60:
            sudokun_tyhjentäjä(taulukko,vaikeusaste,poistetut)
        else:
            return piirrä(taulukko),print(poistetut)




def sudoku_ohjelma():
    print('Haluatko ratkaista sudokun vai generoida sudokun')
    value = int(input('1: Ratkaise 2: generoi'))
    if value == 1:
        muotoile(sudoku)
        print('1: ')
        piirrä(taulukko)

        muotoile(vaikein_sudoku)
        print('2: ')
        piirrä(taulukko)

        muotoile(koneelle_vaikea_sudoku)
        print('3: ')
        piirrä(taulukko)

        value = int(input('Kumman haluat ratkaista 1, 2 vai 3?'))

        if (value == 1):
            muotoile(sudoku)
            tarkistaja(taulukko,0,0)
            piirrä(taulukko)
            exit()

        if value == 2:
            muotoile(vaikein_sudoku)
            tarkistaja(taulukko,0,0)
            piirrä(taulukko)
            exit()

        if value == 3:
            muotoile(koneelle_vaikea_sudoku)
            tic = time.perf_counter()
            tarkistaja(taulukko,0,0)
            toc = time.perf_counter()
            piirrä(taulukko)
            print(f'Ratkaisuun meni {toc - tic:0.4f} seconds')
            exit()        




    if value == 2:    
        value = int(input('1: Helppo , 2: Keskivaikea, 3: Vaikea'))
        if value ==1:
            generoi_sudoku(1,0)
        if value == 2:
            generoi_sudoku(2,0)
        if value == 3:
            generoi_sudoku(3,0)
            
            value = int(input('1: Näytä ratkaisu')) 
            if value == 1:
                ratkaisija(taulukko,0,0)
                piirrä(taulukko)

        else:
            print('Väärä numero')
            sudoku_ohjelma()

        value = int(input('1: Näytä ratkaisu')) 
        if value == 1:
            ratkaisija(taulukko,0,0)
            piirrä(taulukko)

    else:
        print('väärä numero')
        sudoku_ohjelma()    

sudoku_ohjelma()