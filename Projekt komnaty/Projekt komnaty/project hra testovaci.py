import tkinter as tk; from tkinter import messagebox; import random


def spustit_hru():
    uvodni_obrazovka.withdraw()  # Skryjeme úvodní obrazovku
    nastaveni.deiconify()  # Zobrazíme hlavní okno



class Hra:
    def __init__(self,anastaveni):
        self.nastaveni= anastaveni
        """
        self.mistnosti= amistnosti
        self.postava= apostava
        self.pozice_postavy= apozice_postavy        
        self.nepritel_porazen= anepritel_porazen
        """
        
        self.nastaveni.title("Komnaty")
        
        self.platno= tk.Canvas(nastaveni, width=400, height=400, bg="brown") #nastaveni platna
        self.platno.pack()
        
        self.mistnosti=  [self.platno.create_rectangle(0,0,150,150, outline="black"),#mistnosti
                          self.platno.create_rectangle(250,0,400,150, outline="black"),
                          self.platno.create_rectangle(0,250,150,400, outline="black"),
                          self.platno.create_rectangle(250,250,400,400, outline="black")]
        
        self.chodba= self.platno.create_rectangle(150,0,250,50, outline="black") #chodba
        
        self.postava=  self.platno.create_rectangle(60,60,60,60, outline="blue") #hráč
        
        self.pozice_postavy= (190,390) #nastaveni počáteční pozice
        
        self.nastaveni.bind("<Key>", self.pohyb_hrace) #nastavovani klaves
        
        self.mas_klic= False #dulezita promenna pro vyhru
        self.nepritel_porazen= [False,False] #nepratele vysledek boje
        
    def pohyb_hrace(self,event):
        x,y= self.pozice_postavy
        if   event.keysym== "Up": y-=20
        elif event.keysym== "Right": x+=20
        elif event.keysym== "Down": y+=20
        elif event.keysym== "Left": x-=20
        
        if 0<= x <=380 and 0<= y <= 380:
            self.pozice_postavy= (x,y)
            self.platno.coords(self.postava, x, y, x+20, y+20)
            self.kontrola_pozice()
            
    def kontrola_pozice(self):
        x,y= self.pozice_postavy
        
        if    50 <= x <=150 and 50<= y <=150 and not self.nepritel_porazen[0]: #mistnost1
            self.boj(0)
        elif 250 <= x <=350 and 50<= y <=150 and not self.nepritel_porazen[1]: #mistnost2
            self.boj(1)
        elif  50 <= x <=150 and 250<= y <=350: messagebox.showinfo("","Hmmmm copak to tu máme, hele to je poklad") #poklad
        elif 250 <= x <=350 and 250<= y <=350: #mistnost4 s klicem
            if not self.mas_klic:
                self.mas_klic = True
                messagebox.showinfo("No sakra to je klíč","našel jsem klíč")
            else:
                messagebox.showinfo("další klíč", "tenhle už mám, další nepotřebuju")
        elif 150 <= x <=250 and 175<= y <=225: #chodba vyhra
            if self.mas_klic:
                messagebox.showinfo("ok","tak jo vyhrál jsi tuhle triviální hru")
            else:
                messagebox.showinfo("hahaha","bez klíče to nepůjde")
                
    def boj(self,nepritel_stav):
        vysledek= random.randint(1,6) + random.randint(1,6)
        if vysledek> 6:
            self.nepritel_porazen= True
            messagebox.showinfo("","porazil jsi toho neřáda")
        else:
            messagebox.showinfo("","Tak tohle mě fáááákt moc mrzí,chichichiiii")
            self.platno.coords(self.postava,60,60,80,80)
            self.pozice_postavy=(190,390)


uvodni_obrazovka= tk.Tk()
uvodni_obrazovka.title("Úvodní obrazovka")
uvodni_obrazovka.geometry("400x360")
obrazek_uvod= tk.PhotoImage(file="komnata_png.png")  # Upravte cestu k vašemu obrázku
LObrazek= tk.Label(uvodni_obrazovka, image=obrazek_uvod)
LObrazek.pack()

LNazev = tk.Label(uvodni_obrazovka, text="Komnaty", font=("Rockwell Nova Extra Bold", 32), bg="#A9A9A9", fg="#8B0000")
LNazev.place(relx=0.5, rely=0.7, anchor="center")

tlacitko_start= tk.Button(uvodni_obrazovka, text="Start", command=spustit_hru, width=12,)
tlacitko_start.place(x=150, y=330)


nastaveni = tk.Toplevel(uvodni_obrazovka)
nastaveni.withdraw()  # Skryjeme hlavní okno při spuštění



hra = Hra(nastaveni)
uvodni_obrazovka.mainloop()
nastaveni=tk.Tk()
hra=Hra(nastaveni)
nastaveni.mainloop()
            
        
        
        
Hra()

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


