import random; import tkinter as tk
Okno=tk.Tk()
Okno.geometry("400x200")
Okno.title("události")
LVystup=tk.Label()
LVystup.pack()


Okno.bind("<a>",lambda aevent:print("zmackl jsi acko"))
Okno.bind("<Key>",lambda aevent:print("zmackl jsi cokoliv krome acka"))
Okno.bind("<Return>",lambda aevent:print("zmackl jsi enter"))
Okno.bind("<Escape>",lambda aevent:print("zmackl jsi esc"))
Okno.bind("<Down>",lambda aevent:print("zmackl jsi sipku dolu"))
Okno.bind("<Shift-Down>",lambda aevent:print("zmackl jsi shift+sipku dolu"))


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

def cesta():
    amoznost=singlecube()
    if   amoznost<=4: print("byl jsi zasazen")
    elif amoznost>=6: print("uhnul jsi")
    else:
        print("jsi mrtev")           

cesta()
"""
def pohyb():
    nahoru=
    vpravo
    dolu
    vlevo
"""
class Menu: #hlavni obrazovka, loop nez tlacitka
    def __init__(self):
        self.mainsc=["Play","Settings","Quit"]
        self.zvolen_moznost=0
    
    def zobraz_menu(self):
        print("\n"*50) #clean screen
        for index, option in enumerate(self.options):
            if index==self.selected.option:
                print(f">{option}<")
            else:
                print(f"{option}")
"""    
    def spust(self):
        while True:
            self.zobraz_menu()
            command=input("W nahoru, S dolů, Enter pro potvrzení: ").strip().lower()
            if command=="w":
                self.selected_option=(self.selected_option - 1)% len(self.selected)
            elif command=="s":
                self.selected_option=(self.selected_option + 1)% len(self.selected)
            elif==
 """               
 #   def prubeh(self):


    
