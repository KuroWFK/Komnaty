import tkinter as tk; from tkinter import messagebox; import random


class Hra:
    def __init__(self,anastaveni):
        self.nastaveni= anastaveni
        self.nastaveni.title("Komnaty")
        
        self.platno= tk.Canvas(nastaveni, width=400, height=400, bg="brown") #nastaveni platna
        self.platno.pack()
        
        self.mistnosti=  [self.platno.create_rectangle(0,0,150,150, outline="black",fill="green"),#mistnosti
                          self.platno.create_rectangle(250,0,400,150, outline="black",fill="red"),
                          self.platno.create_rectangle(0,250,150,400, outline="black",fill="purple"),
                          self.platno.create_rectangle(250,250,400,400, outline="black",fill="gray")]
        
        self.chodba= self.platno.create_rectangle(150,0,250,50, outline="black",fill="black") #chodba
        
        self.postava=  self.platno.create_rectangle(60,60,60,60, outline="blue",fill="blue") #hráč
        
        self.pozice_postavy= (190,390) #nastaveni počáteční pozice
        
        self.nastaveni.bind("<Key>", self.pohyb_hrace) #nastavovani klaves
        
        self.mas_klic= False #dulezita promenna pro vyhru, z prvotni inicializace nastavena na false, jakoze klic hrac nema
        self.nepritel_porazen= [False,False] #nepratele vysledek boje, seznam nepratel kde kazdy je neporazen v prvotni inicializaci
        
    def pohyb_hrace(self,aevent): #nastaveni ovladani
        x,y= self.pozice_postavy
        if   aevent.keysym== "Up": y-=20 #o kolik se postava pohne stisk klavesy
        elif aevent.keysym== "Right": x+=20
        elif aevent.keysym== "Down": y+=20
        elif aevent.keysym== "Left": x-=20
        
        if 0<= x <=380 and 0<= y <= 380:
            self.pozice_postavy= (x,y)
            self.platno.coords(self.postava, x, y, x+20, y+20) #posunuti objektu
            self.kontrola_pozice()
            
    def kontrola_pozice(self):
        x,y= self.pozice_postavy
        #y= self.pozice_postavy
        
        if    50 <= x <=100 and 50<= y <=100 and not self.nepritel_porazen[0]: #mistnost1 a stav 1 nepritele
            self.boj(0)
        elif 300 <= x <=350 and 50<= y <=100 and not self.nepritel_porazen[1]: #mistnost2 a stav druheho nepritele
            self.boj(1)
        elif  80 <= x <=120 and 290<= y <=320:
            self.zobraz_zpravu("???","Hmmmm copak to tu máme...\n hele to je poklad") #poklad
        elif 330 <= x <=380 and 370<= y <=380: #mistnost4 s klicem
            if not self.mas_klic: #pouziti zaporu
                self.mas_klic = True
                self.zobraz_zpravu("KLÍČ","No sakra to je klíč....\n  Našel jsem klíč")
            else:
                self.zobraz_zpravu("DALŠÍ KLÍČ", "Tenhle už mám, další nepotřebuju")
        elif 150 <= x <=250 and 0<= y <=10: #chodba vyhra
            if self.mas_klic==True:
                self.gratulacka() #slo by to i bez, aaaale....
            else:
                self.zobraz_zpravu("HAHAHA","bez klíče to nepůjde")
                
    def zobraz_zpravu(self, titulek, zprava): #metoda ktera mi zajisti automaticke zaktivneni hlavního okna
        messagebox.showinfo(titulek, zprava)
        self.nastaveni.focus_force()
                
    def gratulacka(self):#.... ale udelal jsem funkci na stejnem principu jako preskakovaniz uvodniho menu, ze se do nej po skonceni vratim
        self.zobraz_zpravu("OK","tak jo vyhrál jsi tuhle triviální hru")
        self.nastaveni.withdraw()
        uvodni_obrazovka.deiconify()
                
    def boj(self,anepritel_stav): #musim dosadit argument aby mohl byt dle pozice postavy doplnen na prislusny prvek seznamu
        kostka1=random.randint(1,6)
        kostka2=random.randint(1,6)
        vysledek= kostka1 + kostka2
        if vysledek> 2:
            self.nepritel_porazen[anepritel_stav] = True
            self.zobraz_zpravu(f"TVŮJ BOJOVÝ VÝSLEDEK JE {vysledek}",f"Padlo ti {kostka1} a {kostka2}\n PORAZIL JSI TOHO NEŘÁDA")
        else:
            self.zobraz_zpravu(f"TVŮJ BOJOVÝ VÝSLEDEK JE {vysledek}",f"Padlo ti {kostka1} a {kostka2}\n DOSTAL JSI KLEPEC!!! \n Tak tohle mě fáááákt moc mrzí, chichichiiii")
            self.platno.coords(self.postava,10,10,10,10)
            self.pozice_postavy=(190,390)
            
def spustit_hru(): #spusteni tlacitkem
    uvodni_obrazovka.withdraw()  # Skryje úvodní obrazovku
    nastaveni.deiconify()  # Zobrazí hlavní okno, zobrazuje predtim skryta okna na pozadi
    
def ukonci_hru(): #zavrit hru s popupem
    if messagebox.askyesno("Potvrzení", "Opravdu chcete ukončit program?"):
        uvodni_obrazovka.destroy()
        nastaveni.destroy()

#vytvoreni uvodni obrazovky s vlastnim obrazkem, aktivnimi tlacitky a nadpisem
uvodni_obrazovka= tk.Tk()
uvodni_obrazovka.title("Úvodní obrazovka")
uvodni_obrazovka.geometry("400x360")
obrazek_uvod= tk.PhotoImage(file="komnata_png.png")
LObrazek= tk.Label(uvodni_obrazovka, image=obrazek_uvod)
LObrazek.pack()

tlacitko_start= tk.Button(uvodni_obrazovka, text="Start", command=spustit_hru, width=12,)#nastavovani a polohovani tlacitek
tlacitko_start.place(x=100, y=330)
tlacitko_konec= tk.Button(uvodni_obrazovka, text="Šlus", command=ukonci_hru, width=12,)
tlacitko_konec.place(x=200, y=330)
LNazev = tk.Label(uvodni_obrazovka, text="Komnaty", font=("Rockwell Nova Extra Bold", 32), bg="#A9A9A9", fg="#8B0000")
LNazev.place(relx=0.5, rely=0.7, anchor="center")#vkladani napisu a editace

nastaveni = tk.Toplevel(uvodni_obrazovka)#vytvoreni noveho okna ktere neni to hlavni okno
nastaveni.withdraw()  # Skryje hlavní okno při spuštění ale stale bezi na pozadi

hra= Hra(nastaveni) #bez toho to neslo, protoze promenna hra propojuje tridu hra s oknem nastaveni
uvodni_obrazovka.mainloop()
#nastaveni=tk.Tk()
#nastaveni.mainloop()
#Hra()
#tridu nemusim volat, jelikožjsem v ni zahrnul vse potrebne pro beh programu
#taktéž jsem vytvoril instanci tridy "hra" a tkinter vse spusti, volat muzu ale je to
#zbytecne a python pak drzkuje

"""
def singlecube():
    kostka1=random.randint(1,6)
    print(f"padlo {kostka1}")
    return kostka1 #nahodny hod 1 kostkou
singlecube()

def doublecube():
    kostka1=random.randint(1,6)
    kostka2=random.randint(1,6)
    print(f"na prvni kostce padlo {kostka1} a na druhé {kostka2}")
    return kostka1, kostka2  #nahodny hod 2 kostkami
doublecube()

def doublesoucet():
    kostka1=random.randint(1,6)
    kostka2=random.randint(1,6)
    akcnicislo=kostka1+kostka2
    print(f"padlo {kostka1} a {kostka2} celkove tedy {akcnicislo}")
    return akcnicislo #nahodny hod 2 kostkami secteno
doublesoucet()
"""


"""
Okno=tk.Tk()
Okno.geometry("800x600")
Okno.title("Zkouska")
platno_sirka=1000
platno_vyska=600
sirka=30; vyska=30
x=platno_sirka/2-sirka/2 ; y=platno_vyska/2-vyska/2
Platno=tk.Canvas() 
Platno.config(width=platno_sirka, height=platno_vyska)
RCtverec=Platno.create_rectangle(x,y, x+sirka,y+vyska,fill="red")

class mapa:
    RCtverec=Platno.create_rectangle(x,y, x+sirka,y+vyska,fill="red")
    RCtverec=Platno.create_rectangle(x,y, x+sirka,y+vyska,fill="red")
    RCtverec=Platno.create_rectangle(x,y, x+sirka,y+vyska,fill="red")
    RCtverec=Platno.create_rectangle(x,y, x+sirka,y+vyska,fill="red")
    RCtverec=Platno.create_rectangle(x,y, x+sirka,y+vyska,fill="red")
    RCtverec=Platno.create_rectangle(x,y, x+sirka,y+vyska,fill="red")
 """   


#Okno.mainloop()


