from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.app import MDApp

from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock
import matplotlib
from matplotlib import pyplot as plt

from math import *




app = MDApp.get_running_app()

txtd = ""
def calcul_1(Qt, L, l, h, tr, comp, prix):
    def calcul_sup(x, y, c=None):
        f1 = -y*sinx-Q
        if c:
            f1 = -y-q
        f2 = x+y*cosx
        return f1, f2

    def calcul_Inf(x, y):
        f1 = -y/sinx
        f2 = x-f1*cosx
        return f1, f2
    Q = Qt*l/L
    q = Q/2
    Ay = Qt/2
    d = sqrt((pow(h, 2)+pow(l, 2)))
    sinx = h/d
    cosx = l/d
    n = 2+2*L/l
    m = 2*n-3
    R = []
    tab = []
    prix_total = 0
    print("Q :",Q)
    print("q : ", q)
    print("noeuds :",n)
    print("barres : ", m)
    for i in range(ceil((n-2)/4)):
        if len(R) < 1:
            f1, f2 = calcul_sup(0, 0, 1)
            f3, f4 = calcul_Inf(0, Ay+f1)
            print(Ay-f1)
            R.append(f1)
            R.append(f2)
            R.append(f3)
            R.append(f4)
        else:
            f1, f2 = calcul_sup(R[-3], R[-2])
            f3, f4 = calcul_Inf(R[-1], f1)
            R.append(f1)
            R.append(f2)
            R.append(f3)
            R.append(f4)
    type = 3
    for i in range(len(R)):
        xtype = h
        if (i+1)%2==0:
            xtype = l
        if type==i+1:
            xtype = d
            type += 4
        if R[i] >= 0:
            print(f"N{i+1} =", R[i], "barre(s)",ceil(R[i]/9), prix*xtype*ceil(R[i]/9))
            if R[i] == 0:
                tab.append((f"N{i+1} ", R[i], "T", xtype, 1, prix*xtype))
                prix_total += prix*xtype
            else:
                tab.append((f"N{i+1} ", R[i], "T", xtype, ceil(R[i]/9), prix*xtype*ceil(R[i]/9)))
                prix_total += prix*xtype*ceil(R[i]/9)
        else:
            print(f"N{i+1} =", R[i], "barre(s)",ceil(abs(R[i]/6)), prix*xtype*ceil(abs(R[i]/6)))
            tab.append([f"N{i+1} ", R[i], "C", xtype,ceil(abs(R[i]/6)), prix*xtype*ceil(abs(R[i]/6))])
            prix_total += prix*xtype*ceil(abs(R[i]/9))
    tab.append((f"N{i+2} ", R[i], "T", xtype, 1, prix*xtype))
    tab.append(("Prix Total", "", "", "", "", prix_total*2+prix*h+n*5))
    return tab

def calcul_2(Qt, L, l, h, tr, comp, prix):
    def calcul_sup(x, y, c=None):
        f1 = (-y-Q)/sinx
        if c:
            f1 = (y-q)/sinx
        f2 = x-f1*cosx

        return f1, f2

    def calcul_Inf(x, y):
        f1 = -y*sinx
        f2 = x+y*cosx

        return f1, f2
    Q = Qt*l/L
    q = Q/2
    Ay = Qt/2
    d = sqrt((pow(h, 2)+pow(l, 2)))
    sinx = h/d
    cosx = l/d
    n = 2*L/l
    m = 2*n-3
    R = []
    tab = []
    prix_total = 0
    print("Q :",Q)
    print("q : ", q)
    print("noeuds :",n)
    print("barres : ", m)
    for i in range(ceil((n-2)/4)):
        if len(R) < 1:
            f1, f2 = calcul_sup(0, Ay, 1)
            f3, f4 = calcul_Inf(0, f1)
            R.append(f1)
            R.append(f2)
            R.append(f3)
            R.append(f4)
        else:
            f1, f2 = calcul_sup(R[-3], R[-2])
            f3, f4 = calcul_Inf(R[-1], f1)
            R.append(f1)
            R.append(f2)
            if i != ceil((n-2)/4) -1:
                R.append(f3)
                R.append(f4)
    type = 3
    for i in range(len(R)):
        xtype = d
        if (i+1)%2==0:
            print("Largeur")
            xtype = l
        if type==i+1:
            #if i == 2:
            print("Hauteur")
            xtype = h
            type += 4
        #else:
        #    pass
        print(xtype)
        if R[i] >= 0:
            print(f"N{i+1} =", R[i], "barre(s)",ceil(R[i]/9), prix*xtype*ceil(R[i]/9))
            if R[i] == 0:
                tab.append((f"N{i+1} ", R[i], "T", xtype, 1, prix*xtype))
                prix_total += prix*xtype
            else:
                tab.append((f"N{i+1} ", R[i], "T", xtype, ceil(R[i]/9), prix*xtype*ceil(R[i]/9)))
                prix_total += prix*xtype*ceil(R[i]/9)
        else:
            print(f"N{i+1} =", R[i], "barre(s)",ceil(abs(R[i]/6)), prix*xtype*ceil(abs(R[i]/6)))
            tab.append([f"N{i+1} ", R[i], "C", xtype,ceil(abs(R[i]/6)), prix*xtype*ceil(abs(R[i]/6))])
            prix_total += prix*xtype*ceil(abs(R[i]/9))

    tab.append((f"N{i+2} ", R[i], "T", xtype, 1, prix*xtype))
    tab.append(("Prix Total", "", "", "", "", prix_total*2+prix*h+n*5))
    return tab


def draw_1(j):
    global txtd
    def draw_ob1(x, end=False):
        global txtd
        m = n
        if not end:
            m = n-1
        for y in range(0,m):
            if (x==0 or y==0 or x==y or x%n==0 or x==n-1 or y==n-1):
                if x==0 or x==n-1:
                    print("*", end="")
                    txtd += "*. "
                else:
                    print("*", end="")
                    txtd += "*     "
            else:
                print(" ", end="")
                txtd += "  "
        if end:
            print()
            txtd += "\n"
    def draw_ob2(x, end=False):
        global txtd
        for y in range(0,n-1):
            if (x==0 or y==0 or x%n==0 or x==n-1 or x+y==n-1):
                if x==0 or x==n-1:
                    print("*", end="")
                    txtd += "*  "
                else:
                    print("*", end="")
                    txtd += "*    "
            else:
                print(" ", end="")
                txtd += "  "
        if end:
            print()
            txtd += "\n"
    n = 7
    txtd = ""
    for i in range (n):
        for _ in range (j):
            draw_ob2(i)
        for _ in range (j-1):
            draw_ob1(i)
        draw_ob1(i, 1)
    print(txtd)
    return txtd

def calcul_prix_2(h=1, l=1):
    def calcul_sup(x, y, c=None):
        f1 = (-y-Q)/sinx
        if c:
            f1 = (y-q)/sinx
        f2 = x-f1*cosx

        return f1, f2

    def calcul_Inf(x, y):
        f1 = -y*sinx
        f2 = x+y*cosx

        return f1, f2
    longueur = float(app.modelscreen.ids.long.text)
    hauteur = h
    largeur = l
    diagonal = sqrt((pow(hauteur, 2)+pow(largeur, 2)))
    sinx = hauteur/diagonal
    cosx = largeur/diagonal
    R = []
    Qt = float(app.modelscreen.ids.charge.text)
    Q = Qt*largeur/longueur
    q = Q/2
    Ay = Qt/2
    noeuds = 2*longueur/largeur
    barres = 2*noeuds-3
    prix = 15
    prix_total = 0
    tab = []
    for i in range(ceil((noeuds-2)/4)):
        if len(R) < 1:
            f1, f2 = calcul_sup(0, Ay, 1)
            f3, f4 = calcul_Inf(0, f1)
            R.append(f1)
            R.append(f2)
            R.append(f3)
            R.append(f4)
        else:
            f1, f2 = calcul_sup(R[-3], R[-2])
            f3, f4 = calcul_Inf(R[-1], f1)
            R.append(f1)
            R.append(f2)
            if i != ceil((noeuds-2)/4) -1:
                R.append(f3)
                R.append(f4)
    type = 3
    for i in range(len(R)):
        xtype = diagonal
        if (i+1)%2==0:
            print("Largeur")
            xtype = largeur
        if type==i+1:
            #if i == 2:
            print("Hauteur")
            xtype = hauteur
            type += 4
        #else:
        #    pass
        print(xtype)
        if R[i] >= 0:
            prix_total += prix*xtype*ceil(R[i]/9)
        else:
            prix_total += prix*xtype*ceil(abs(R[i]/9))
    return prix_total*2+15*hauteur+noeuds*5

def calcul_prix_1(h=1, l=1):
    def calcul_sup(x, y, c=None):
        f1 = -y*sinx-Q
        if c:
            f1 = -y-q
        f2 = x+y*cosx
        return f1, f2

    def calcul_Inf(x, y):
        f1 = -y/sinx
        f2 = x-f1*cosx
        return f1, f2

    longueur = float(app.modelscreen.ids.long.text)
    hauteur = h
    largeur = l
    diagonal = sqrt((pow(hauteur, 2)+pow(largeur, 2)))
    sinx = hauteur/diagonal
    cosx = largeur/diagonal
    R = []
    Qt = float(app.modelscreen.ids.charge.text)
    Q = Qt*largeur/longueur
    q = Q/2
    Ay = Qt/2
    noeuds = 2+2*longueur/largeur
    barres = 2*noeuds-3
    prix = 15
    prix_total = 0
    tab = []
    for i in range(ceil((noeuds-2)/4)):
        if len(R) < 1:
            f1, f2 = calcul_sup(0, 0, 1)
            f3, f4 = calcul_Inf(0, Ay+f1)
            print(Ay-f1)
            R.append(f1)
            R.append(f2)
            R.append(f3)
            R.append(f4)
        else:
            f1, f2 = calcul_sup(R[-3], R[-2])
            f3, f4 = calcul_Inf(R[-1], f1)
            R.append(f1)
            R.append(f2)
            R.append(f3)
            R.append(f4)
    type = 3
    for i in range(len(R)):
        xtype = h
        if (i+1)%2==0:
            xtype = l
        if type==i+1:
            xtype = diagonal
            type += 4
        if R[i] >= 0:
            if R[i] == 0:
                prix_total += prix*xtype
            else:
                prix_total += prix*xtype*ceil(R[i]/9)
        else:
            prix_total += prix*xtype*ceil(abs(R[i]/9))
    return prix_total*2+15*hauteur+noeuds*5

class ResultScreen(MDScreen):
    def on_enter(self):
        pass
    def calcul(self, Qt, L, l, h, tr, comp, prix):
        layout = AnchorLayout()
        data = []
        if Qt and L and l and h and tr and comp and prix:
            Qt, L, l, h, tr, comp, prix = float(Qt), float(L), float(l), float(h), float(tr), float(comp), float(prix)
            Clock.schedule_once(lambda x:app.switch_screen("resultscreen"))
            if app.model == 1:
                data = calcul_1(Qt, L, l, h, tr, comp, prix)
                H = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]
                y = [calcul_prix_1(i, l) for i in H]
                L = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]
                y2 = [calcul_prix_1(h, i) for i in L]
                d = [calcul_prix_1(i, i) for i in L]
                fig, ax = plt.subplots()

                fig.set_size_inches((15, 6))

                ax.scatter(h, calcul_prix_1(h, l), c="red")
                ax.plot(H, y)
                fig.tight_layout()
                ax.scatter(H[y.index(min(y))], min(y))
                ax.plot(L, y2)
                ax.scatter(L[y2.index(min(y2))], min(y2))
                ax.plot(L, d)
                ax.scatter(L[d.index(min(d))], min(d))
                ax.legend([f"prix h = {h}, dist = {l}",f"prix  f(h) et dist = {l}", f"prix minimum h = {H[y.index(min(y))]} et dist = {l}", f"prix  f(dist), h={h}", f"prix minimum h = {h} et dist = {L[y2.index(min(y2))]}", f"prix diagonal f(h) et f(dist)", f"prix minimal f(diag) h= {L[d.index(min(d))]}, dist = {L[d.index(min(d))]}"])
                fig.savefig("graph.png", dpi=150)
                self.ids.graph.reload()
            else:
                data = calcul_2(Qt, L, l, h, tr, comp, prix)
                H = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]
                y = [calcul_prix_2(i, l) for i in H]
                L = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]
                y2 = [calcul_prix_2(h, i) for i in L]
                d = [calcul_prix_2(i, i) for i in L]
                fig, ax = plt.subplots()

                fig.set_size_inches((15, 6))

                ax.scatter(h, calcul_prix_2(h, l), c='red')
                ax.plot(H, y)
                fig.tight_layout()
                ax.scatter(H[y.index(min(y))], min(y))
                ax.plot(L, y2)
                ax.scatter(L[y2.index(min(y2))], min(y2))
                ax.plot(L, d)
                ax.scatter(L[d.index(min(d))], min(d))
                ax.legend([f"prix h = {h}, dist = {l}",f"prix  f(h) et dist = {l}", f"prix minimum h = {H[y.index(min(y))]} et dist = {l}",f"prix  f(dist), h={h}", f"prix minimum h = {h} et dist = {L[y2.index(min(y2))]}", f"prix diagonal f(h) et f(dist)", f"prix minimal f(diag) h= {L[d.index(min(d))]}, dist = {L[d.index(min(d))]}"])
                fig.savefig("graph.png", dpi=150)
                self.ids.graph.reload()



            app.dessin = draw_1(6)
        self.data_tables = MDDataTable(
            size_hint=(.9, 1),
            use_pagination=True,
            column_data = [
                ("N° ", dp(15)),
                ("Force", dp(35)),
                ("Type de force", dp(30)),
                ("L d'une barre", dp(35)),
                ("Nbre barres", dp(30)),
                ("Prix", dp(35)),
            ],
            row_data = data
        )
        layout.add_widget(self.data_tables)
        self.ids.calc.clear_widgets()
        self.ids.calc.add_widget(layout)


Builder.load_file('resultscreen.kv')
