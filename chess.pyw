#Started to write in Qedit
import tkinter as tk
import tkinter.messagebox as msgbox

pencere=tk.Tk()

class Kare():
  mat_yok=False
  sıradaki_renk="beyaz"
  işaretli_yerler={}
  taşların_yeri={}
  rok={}
  git_işaretli_yerler=[]
  ye_işaretli_yerler=[]
  beyaz_şah_gidilmezler=[]
  siyah_şah_gidilmezler=[]
  tıklandı=False
  tıklanan_kare=None
  check=False
  şah_çeken_taş=[]
  açmaz=[]
  şah_çeken_yol=set()
  gidilmezler=[]
  siyah_gidilenler={}
  beyaz_gidilenler={}
  siyah_taşlar=[]
  beyaz_taşlar=[]
  def __init__(self,renk,ad,*args,**kwargs):
    self.konumun_rengi=renk
    self.taşın_rengi=False
    self.taş=False
    self.taş_label=False
    self.ad=ad
    if(self.konumun_rengi=="beyaz"):
      self.karenin_rengi="#d0f4f1"
    if(self.konumun_rengi=="siyah"):
      self.karenin_rengi="#333131"

  def güncelle(self):
    if(self.taş):
      resim=tk.PhotoImage(file=f"images/{self.taşın_rengi}_{self.taş}.png")
      self.taş_label=tk.Label(pencere,image=resim,bg=self.karenin_rengi)
      self.taş_label.image=resim
      yer=karenin_yeri(self.ad)
      self.taş_label.place(x=yer.split("x")[0],y=yer.split("x")[1])

  @classmethod
  def sırayı_değiştir(cls):
    if(Kare.sıradaki_renk=="beyaz"):
      Kare.sıradaki_renk="siyah"
    else:
      Kare.sıradaki_renk="beyaz"

a1=Kare (renk='beyaz',ad='a1')
a2=Kare (renk='siyah',ad='a2')
a3=Kare (renk='beyaz',ad='a3')
a4=Kare (renk='siyah',ad='a4')
a5=Kare (renk='beyaz',ad='a5')
a6=Kare (renk='siyah',ad='a6')
a7=Kare (renk='beyaz',ad='a7')
a8=Kare (renk='siyah',ad='a8')
b1=Kare (renk='siyah',ad='b1')
b2=Kare (renk='beyaz',ad='b2')
b3=Kare (renk='siyah',ad='b3')
b4=Kare (renk='beyaz',ad='b4')
b5=Kare (renk='siyah',ad='b5')
b6=Kare (renk='beyaz',ad='b6')
b7=Kare (renk='siyah',ad='b7')
b8=Kare (renk='beyaz',ad='b8')
c1=Kare (renk='beyaz',ad='c1')
c2=Kare (renk='siyah',ad='c2')
c3=Kare (renk='beyaz',ad='c3')
c4=Kare (renk='siyah',ad='c4')
c5=Kare (renk='beyaz',ad='c5')
c6=Kare (renk='siyah',ad='c6')
c7=Kare (renk='beyaz',ad='c7')
c8=Kare (renk='siyah',ad='c8')
d1=Kare (renk='siyah',ad='d1')
d2=Kare (renk='beyaz',ad='d2')
d3=Kare (renk='siyah',ad='d3')
d4=Kare (renk='beyaz',ad='d4')
d5=Kare (renk='siyah',ad='d5')
d6=Kare (renk='beyaz',ad='d6')
d7=Kare (renk='siyah',ad='d7')
d8=Kare (renk='beyaz',ad='d8')
e1=Kare (renk='beyaz',ad='e1')
e2=Kare (renk='siyah',ad='e2')
e3=Kare (renk='beyaz',ad='e3')
e4=Kare (renk='siyah',ad='e4')
e5=Kare (renk='beyaz',ad='e5')
e6=Kare (renk='siyah',ad='e6')
e7=Kare (renk='beyaz',ad='e7')
e8=Kare (renk='siyah',ad='e8')
f1=Kare (renk='siyah',ad='f1')
f2=Kare (renk='beyaz',ad='f2')
f3=Kare (renk='siyah',ad='f3')
f4=Kare (renk='beyaz',ad='f4')
f5=Kare (renk='siyah',ad='f5')
f6=Kare (renk='beyaz',ad='f6')
f7=Kare (renk='siyah',ad='f7')
f8=Kare (renk='beyaz',ad='f8')
g1=Kare (renk='beyaz',ad='g1')
g2=Kare (renk='siyah',ad='g2')
g3=Kare (renk='beyaz',ad='g3')
g4=Kare (renk='siyah',ad='g4')
g5=Kare (renk='beyaz',ad='g5')
g6=Kare (renk='siyah',ad='g6')
g7=Kare (renk='beyaz',ad='g7')
g8=Kare (renk='siyah',ad='g8')
h1=Kare (renk='siyah',ad='h1')
h2=Kare (renk='beyaz',ad='h2')
h3=Kare (renk='siyah',ad='h3')
h4=Kare (renk='beyaz',ad='h4')
h5=Kare (renk='siyah',ad='h5')
h6=Kare (renk='beyaz',ad='h6')
h7=Kare (renk='siyah',ad='h7')
h8=Kare (renk='beyaz',ad='h8')

a=[a1,a2,a3,a4,a5,a6,a7,a8]
b=[b1,b2,b3,b4,b5,b6,b7,b8]
c=[c1,c2,c3,c4,c5,c6,c7,c8]
d=[d1,d2,d3,d4,d5,d6,d7,d8]
e=[e1,e2,e3,e4,e5,e6,e7,e8]
f=[f1,f2,f3,f4,f5,f6,f7,f8]
g=[g1,g2,g3,g4,g5,g6,g7,g8]
h=[h1,h2,h3,h4,h5,h6,h7,h8]

def birleştir(liste,*args):
  for i in args:
    liste.extend(i)

tüm_kareler=[]
birleştir(tüm_kareler,a,b,c,d,e,f,g,h)

dikey1=[a1,b1,c1,d1,e1,f1,g1,h1]
dikey2=[a2,b2,c2,d2,e2,f2,g2,h2]
dikey3=[a3,b3,c3,d3,e3,f3,g3,h3]
dikey4=[a4,b4,c4,d4,e4,f4,g4,h4]
dikey5=[a5,b5,c5,d5,e5,f5,g5,h5]
dikey6=[a6,b6,c6,d6,e6,f6,g6,h6]
dikey7=[a7,b7,c7,d7,e7,f7,g7,h7]
dikey8=[a8,b8,c8,d8,e8,f8,g8,h8]

siyah1=[a8]
siyah2=[a6,b7,c8]
siyah3=[a4,b5,c6,d7,e8]
siyah4=[a2,b3,c4,d5,e6,f7,g8]
siyah5=[b1,c2,d3,e4,f5,g6,h7]
siyah6=[d1,e2,f3,g4,h5]
siyah7=[f1,g2,h3]
siyah8=[h1]

siyaha=[b1,a2]
siyahb=[d1,c2,b3,a4]
siyahc=[f1,e2,d3,c4,b5,a6]
siyahd=[h1,g2,f3,e4,d5,c6,b7,a8]
siyahe=[h3,g4,f5,e6,d7,c8]
siyahf=[h5,g6,f7,e8]
siyahg=[h7,g8]

beyaz1=[a7,b8]
beyaz2=[a5,b6,c7,d8]
beyaz3=[a3,b4,c5,d6,e7,f8]
beyaz4=[a1,b2,c3,d4,e5,f6,g7,h8]
beyaz5=[c1,d2,e3,f4,g5,h6]
beyaz6=[e1,f2,g3,h4]
beyaz7=[g1,h2]

beyaza=[h8]
beyazb=[f8,g7,h6]
beyazc=[d8,e7,f6,g5,h4]
beyazd=[b8,c7,d6,e5,f4,g3,h2]
beyaze=[a7,b6,c5,d4,e3,f2,g1]
beyazf=[a5,b4,c3,d2,e1]
beyazg=[a3,b2,c1]
beyazh=[a1]

yatay=[a,b,c,d,e,f,g,h]
dikey=[dikey1,dikey2,dikey3,dikey4,dikey5,dikey6,dikey7,dikey8]
yatay_ve_dikey=[yatay,dikey]
beyaz_diyagonal1=[beyaz1,beyaz2,beyaz3,beyaz4,beyaz5,beyaz6,beyaz7]
siyah_diyagonal1=[siyah1,siyah2,siyah3,siyah4,siyah5,siyah6,siyah7,siyah8]
beyaz_diyagonal2=[beyaza,beyazb,beyazc,beyazd,beyaze,beyazf,beyazg,beyazh]
siyah_diyagonal2=[siyaha,siyahb,siyahc,siyahd,siyahe,siyahf,siyahg]
siyah_vezir=[yatay,dikey,siyah_diyagonal1,siyah_diyagonal2]
beyaz_vezir=[yatay,dikey,beyaz_diyagonal1,beyaz_diyagonal2]

def taşın_adını_kısalt(taşın_adı):
  sözlük={
    "at":"A",
    "fil":"F",
    "şah":"Ş",
    "vezir":"V",
    "kale":"K",
    "piyon":"P"
  }
  return sözlük[taşın_adı]

def hamleyi_adlandır(gidilen_konum,varılan_konum,taşın_adı,ye=False):
  kısaltma=taşın_adını_kısalt(taşın_adı)
  if(ye):
    return f"{kısaltma}x{gidilen_konum}{varılan_konum}"
  else:
    return f"{kısaltma}{gidilen_konum}{varılan_konum}"

def filvekale_git(konum,listeler):
  gidilebilecekler=[]
  yenecekler=[]
  gidilmezler=[]
  kare=False
  for liste in listeler:
    liste_sıra=sıra_bul(konum,liste)
    sayı=liste_sıra-1
    değer=True
    rakip_taş=False
    while değer:
      if(sayı>=0):
        kare=liste[sayı]
        if(kare.taş):
          değer=False
          if(kare.taşın_rengi!=konum.taşın_rengi):
            if(kare.taş=="şah"):
              Kare.şah_çeken_yol=set(liste[sayı:liste_sıra])
              Kare.check=True 
              Kare.şah_çeken_taş.append(konum)
            else:
              rakip_taş=True
              yenecekler.append(kare)
              while rakip_taş:
                sayı+=1
                try:
                  kare=liste[sayı]
                except IndexError:
                  rakip_taş=False
                if(kare.taş):
                  if((kare.taşın_rengi!=konum.taşın_rengi) and kare.taş=="şah"):
                    Kare.açmaz.append(yenecekler[-1])

          else:
            gidilmezler.append(kare)
        else:
          gidilebilecekler.append(kare)
          gidilmezler.append(kare)
          sayı-=1
      else:
        değer=False

    rakip_taş=False
    sayı=liste_sıra+1
    değer=True
    while değer:
      try:
        kare=liste[sayı]
      except IndexError:
        değer=False
      if(kare.taş):
        if(kare.taşın_rengi!=konum.taşın_rengi):
          if(kare.taş=="şah"):
            Kare.şah_çeken_yol=set(liste[liste_sıra:sayı])
            Kare.check=True 
            Kare.şah_çeken_taş.append(konum)
          else:
            rakip_taş=True
            yenecekler.append(kare)
            while rakip_taş:
              sayı+=1
              try:
                kare=liste[sayı]
              except IndexError:
                rakip_taş=False
              if(kare.taş):
                if((kare.taşın_rengi!=konum.taşın_rengi) and kare.taş=="şah"):
                  Kare.açmaz.append(yenecekler[-1])
        else:
          gidilmezler.append(kare)
        değer=False
      else:
        gidilebilecekler.append(kare)
        gidilmezler.append(kare)
        sayı+=1
  if(konum.taşın_rengi=="siyah"):
    Kare.beyaz_şah_gidilmezler.extend(gidilmezler)
  if(konum.taşın_rengi=="beyaz"):
    Kare.siyah_şah_gidilmezler.extend(gidilmezler)
  
  return([gidilebilecekler,yenecekler])

def terfi_et(tıklanan_kare,konum):
  def buton_komutu():
    sayı=int(str(var.get()))
    if(sayı==1):
      taş="vezir"
    if(sayı==2):
      taş="kale"
    if(sayı==3):
      taş="fil"
    if(sayı==4):
      taş="at"
    taş_kaldır(konum)
    taş_yerleştir(konum,tıklanan_kare.taşın_rengi,taş)
    taş_kaldır(tıklanan_kare)
    tercih_penceresi.destroy()

  tercih_penceresi=tk.Toplevel(pencere)
  var=tk.IntVar()
  vezir_butonu=tk.Radiobutton(tercih_penceresi,variable=var,value=1)
  vezir=tk.PhotoImage(file=f"images/{tıklanan_kare.taşın_rengi}_vezir.png")
  vezir_label=tk.Label(tercih_penceresi,image=vezir)
  vezir_butonu.pack()
  vezir_label.pack()
  kale_butonu=tk.Radiobutton(tercih_penceresi,variable=var,value=2)
  kale=tk.PhotoImage(file=f"images/{tıklanan_kare.taşın_rengi}_kale.png")
  kale_label=tk.Label(tercih_penceresi,image=kale)
  kale_butonu.pack()
  kale_label.pack()
  fil_butonu=tk.Radiobutton(tercih_penceresi,variable=var,value=3)
  fil=tk.PhotoImage(file=f"images/{tıklanan_kare.taşın_rengi}_fil.png")
  fil_label=tk.Label(tercih_penceresi,image=fil)
  fil_butonu.pack()
  fil_label.pack()
  at_butonu=tk.Radiobutton(tercih_penceresi,variable=var,value=4)
  at=tk.PhotoImage(file=f"images/{tıklanan_kare.taşın_rengi}_at.png")
  at_label=tk.Label(tercih_penceresi,image=at)
  at_butonu.pack()
  at_label.pack()
  buton=tk.Button(tercih_penceresi,text="Terfi Et", command=buton_komutu)
  buton.pack()
  tercih_penceresi.mainloop()

def piyon_git(konum):
  gidilebilecekler=[]
  yenecekler=[]
  liste_sıra=liste_sıra_bul(konum,yatay)
  sayı=sıra_bul(konum,yatay[liste_sıra])

  if(konum.taşın_rengi=="beyaz" ):
    if(sayı+1<8 ):
      if((not(yatay[liste_sıra][sayı+1].taş))and sayı+2<8):
        if(konum in dikey2):
          if(not(yatay[liste_sıra][sayı+2].taş)):
            gidilebilecekler.append(yatay[liste_sıra][sayı+2])
        gidilebilecekler.append(yatay[liste_sıra][sayı+1])
      if(liste_sıra+1<8):
        if(yatay[liste_sıra+1][sayı+1].taş and yatay[liste_sıra+1][sayı+1].taşın_rengi=="siyah"):
          if(yatay[liste_sıra+1][sayı+1].taş=="şah"):
            Kare.check=True
            Kare.şah_çeken_taş.append(yatay[liste_sıra+1][sayı+1])
          else:
            yenecekler.append(yatay[liste_sıra+1][sayı+1])
      if(sayı-1>=0):
        if(yatay[liste_sıra-1][sayı+1].taş and yatay[liste_sıra-1][sayı+1].taşın_rengi=="siyah"):
          if(yatay[liste_sıra-1][sayı+1]).taş=="şah":
            Kare.check=True
            Kare.şah_çeken_taş.append(yatay[liste_sıra-1][sayı+1])
          else:
            yenecekler.append(yatay[liste_sıra-1][sayı+1])
  if(konum.taşın_rengi=="siyah" ):
    if(sayı-1>=0):
      if(not(yatay[liste_sıra][sayı-1].taş)):
        if(konum in dikey7):
          if(not(yatay[liste_sıra][sayı-2].taş)):
            gidilebilecekler.append(yatay[liste_sıra][sayı-2])
        gidilebilecekler.append(yatay[liste_sıra][sayı-1])
      if(liste_sıra+1<8):
        if(yatay[liste_sıra+1][sayı-1].taş and yatay[liste_sıra+1][sayı-1].taşın_rengi=="beyaz"):
          if(yatay[liste_sıra+1][sayı-1].taş=="şah"):
            Kare.check=True
            Kare.şah_çeken_taş.append(yatay[liste_sıra+1][sayı-1])
          else:
            yenecekler.append(yatay[liste_sıra+1][sayı-1])
      if(sayı-1>=0):
        if(yatay[liste_sıra-1][sayı-1].taş and yatay[liste_sıra-1][sayı-1].taşın_rengi=="beyaz"):
          if(yatay[liste_sıra-1][sayı-1].taş=="şah"):
            Kare.check=True
            Kare.şah_çeken_taş.append(yatay[liste_sıra-1][sayı-1])
          else:
            yenecekler.append(yatay[liste_sıra-1][sayı-1])
  if(konum.taşın_rengi=="siyah"):
    Kare.beyaz_şah_gidilmezler.extend(yenecekler)
  if(konum.taşın_rengi=="beyaz"):
    Kare.siyah_şah_gidilmezler.extend(yenecekler)
  return (gidilebilecekler,yenecekler)

def vezir_git(konum,listeler):
  gidilebilecekler=[]
  yenecekler=[]
  sonuç=filvekale_git(konum,listeler)
  gidilebilecekler.extend(sonuç[0])
  yenecekler.extend(sonuç[1])
  return([gidilebilecekler,yenecekler])

def şah_kontrol(liste_sıra,sıra):
  kareler=[]
  try:
    if(liste_sıra>=0 and sıra>=0):
      kareler.append(dikey[liste_sıra][sıra])
  except IndexError:
    pass
  return kareler

def şah_git(konum):
  if(konum.taşın_rengi=="siyah"):
    gidilemeyenler=Kare.siyah_şah_gidilmezler
  if(konum.taşın_rengi=="beyaz"):
    gidilemeyenler=Kare.beyaz_şah_gidilmezler
  liste_sıra=liste_sıra_bul(konum,dikey)
  sıra=sıra_bul(konum,dikey[liste_sıra])
  kareler=[]
  gidilmezler=[]
  gidilebilecekler=[]
  yenecekler=[]
  kareler.extend(şah_kontrol(liste_sıra-1,sıra+1))
  kareler.extend(şah_kontrol(liste_sıra-1,sıra))
  kareler.extend(şah_kontrol(liste_sıra-1,sıra-1))
  kareler.extend(şah_kontrol(liste_sıra+1,sıra-1))
  kareler.extend(şah_kontrol(liste_sıra+1,sıra))
  kareler.extend(şah_kontrol(liste_sıra+1,sıra+1))
  kareler.extend(şah_kontrol(liste_sıra,sıra-1))
  kareler.extend(şah_kontrol(liste_sıra,sıra+1))

  for i in kareler:
    if(i in gidilemeyenler):
      pass
    elif(i.taş):
      if(i.taşın_rengi!=konum.taşın_rengi):
        yenecekler.append(i)
      else:
        gidilmezler.append(i)
    else:
      gidilebilecekler.append(i)
      gidilmezler.append(i)
  if(konum.taşın_rengi=="siyah"):
    Kare.beyaz_şah_gidilmezler.extend(gidilmezler)
  if(konum.taşın_rengi=="beyaz"):
    Kare.siyah_şah_gidilmezler.extend(gidilmezler)
  return([gidilebilecekler,yenecekler])

def at_kontrol(liste_sıra,sayı):
  kareler=[]
  try:
    if(liste_sıra>=0 and sayı>=0):
      kareler.append(dikey[liste_sıra][sayı])
  except IndexError :
    pass
  return kareler

def at_git(konum):
  yenecekler=[]
  gidilebilecekler=[]
  liste_sıra=liste_sıra_bul(konum,dikey)
  sayı=sıra_bul(konum,dikey[liste_sıra])
  kareler=[]
  kareler.extend(at_kontrol(liste_sıra-1,sayı+2))
  kareler.extend(at_kontrol(liste_sıra-1,sayı-2))
  kareler.extend(at_kontrol(liste_sıra+1,sayı+2))
  kareler.extend(at_kontrol(liste_sıra+1,sayı-2))
  kareler.extend(at_kontrol(liste_sıra+2,sayı-1))
  kareler.extend(at_kontrol(liste_sıra+2,sayı+1))
  kareler.extend(at_kontrol(liste_sıra-2,sayı-1))
  kareler.extend(at_kontrol(liste_sıra-2,sayı+1))
  for kare in kareler:
    if(kare.taş):
      if(kare.taşın_rengi!=konum.taşın_rengi):
        if(kare.taş=="şah"):
          Kare.check=True 
          Kare.şah_çeken_taş.append(konum)
        else:
          yenecekler.append(kare)
    else:
      gidilebilecekler.append(kare)
  return([gidilebilecekler,yenecekler])

def sıra_bul(konum,liste):
  return liste.index(konum)

def liste_bul(konum,listeler):
  for liste in listeler:
    if(konum in liste):
      return liste

def liste_sıra_bul(konum,listeler):
  liste=liste_bul(konum,listeler)
  return listeler.index(liste)

def taşa_göre_konum(konum):
  liste=[]
  if(konum.taş=="fil"):
    if(konum.konumun_rengi=="siyah"):
      liste.append(liste_bul(konum,siyah_diyagonal1))
      liste.append(liste_bul(konum,siyah_diyagonal2))
    if(konum.konumun_rengi=="beyaz"):
      liste.append(liste_bul(konum,beyaz_diyagonal1))
      liste.append(liste_bul(konum,beyaz_diyagonal2))
    return filvekale_git(konum,liste)
  if(konum.taş=="at"):
    return at_git(konum)
  if(konum.taş=="kale"):
    liste.append(liste_bul(konum,yatay))
    liste.append(liste_bul(konum,dikey))
    return filvekale_git(konum,liste)
  if(konum.taş=="vezir"):
    if(konum.konumun_rengi=="siyah"):
      for i in siyah_vezir:
        liste.append(liste_bul(konum,i))
      return vezir_git(konum,liste)
    if(konum.konumun_rengi=="beyaz"):
      for i in beyaz_vezir:
        liste.append(liste_bul(konum,i))
      return vezir_git(konum,liste)
  if(konum.taş=="piyon"):
    return piyon_git(konum)


def bul(taşların_konumu,şahlar):
  sözlük={}
  for i in taşların_konumu:
    if(i.taş=="şah"):
      şahlar.append(i)
    else:
      sonuç=taşa_göre_konum(i)
      sözlük[i]=tuple(sonuç)
  return sözlük

def taşları_sırala():
  Kare.siyah_taşlar=[]
  Kare.beyaz_taşlar=[]
  for i in tüm_kareler:
    if(i.taş):
      Kare.taşların_yeri[i.taş_label]=i
      if(i.taşın_rengi=="siyah"):
        Kare.siyah_taşlar.append(i)
      if(i.taşın_rengi=="beyaz"):
        Kare.beyaz_taşlar.append(i)

def rok_kontrol():
  if(not(e1.taş)):
    Kare.rok["beyaz_uzun_rok"]=False
    Kare.rok["beyaz_kısa_rok"]=False
  if(not(e8.taş)):
    Kare.rok["siyah_uzun_rok"]=False
    Kare.rok["siyah_kısa_rok"]=False
  if(a1.taşın_rengi!="beyaz"):
    Kare.rok["beyaz_uzun_rok"]=False
  if(h1.taşın_rengi!="beyaz"):
    Kare.rok["beyaz_kısa_rok"]=False
  if(a8.taşın_rengi!="siyah"):
    Kare.rok["siyah_uzun_rok"]=False
  if(h8.taşın_rengi!="siyah"):
    Kare.rok["siyah_uzun_rok"]=False

def mat():
  if(Kare.sıradaki_renk=="beyaz"):
    kazanan_renk="Siyah"
  if(Kare.sıradaki_renk=="siyah"):
    kazanan_renk="Beyaz"
  Kare.sıradaki_renk=None
  def boş(event):
    pass
  tahta.bind("<1>",boş)
  msgbox.showinfo(title="Bitti!", message=f"{kazanan_renk} kazandı.")

def mat_kontrol():
  Kare.mat_yok=False
  if(Kare.sıradaki_renk=="siyah"):
    kontrol=Kare.siyah_gidilenler
  if(Kare.sıradaki_renk=="beyaz"):
    kontrol=Kare.beyaz_gidilenler
  for i in kontrol.values():
    if(i==([], []) or i==[[],[]]):
      pass
    else:
      Kare.mat_yok=True
  if(not(Kare.mat_yok)):
    mat()

def hamle_başı():
  Kare.beyaz_taşlar=[]
  Kare.siyah_taşlar=[]
  Kare.açmaz=[]
  şahlar=[]
  taşları_sırala()
  rok_kontrol()
  if(Kare.sıradaki_renk=="beyaz"):
    Kare.siyah_gidilenler=bul(Kare.siyah_taşlar,şahlar)
  if(Kare.sıradaki_renk=="siyah"):
    Kare.beyaz_gidilenler=bul(Kare.beyaz_taşlar,şahlar)
  if(Kare.check):
    if(len(Kare.şah_çeken_taş)==1):
      sözlük={}
      Kare.beyaz_gidilenler=bul(Kare.beyaz_taşlar,şahlar)
      Kare.siyah_gidilenler=bul(Kare.siyah_taşlar,şahlar)
      if(Kare.sıradaki_renk=="siyah"):
        sözlük=bul(Kare.siyah_taşlar,şahlar)
        for a in sözlük.keys():
          gidilenler=[]
          yenecekler=[]
          if(Kare.şah_çeken_taş[0] in sözlük[a][1]):
            yenecekler.append(Kare.şah_çeken_taş[0])
          for i in Kare.şah_çeken_yol:
            if(i in sözlük[a][0]):
              gidilenler.append(i)
          Kare.siyah_gidilenler[a]=(gidilenler,yenecekler)
      if(Kare.sıradaki_renk=="beyaz"):
        sözlük=bul(Kare.beyaz_taşlar,şahlar)
        for a in sözlük.keys():
          gidilenler=[]
          yenecekler=[]
          if(Kare.şah_çeken_taş in sözlük[a][1]):
            yenecekler.append(Kare.şah_çeken_taş)
          for i in Kare.şah_çeken_yol:
            if(i in sözlük[a][0]):
              gidilenler.append(i)
          Kare.beyaz_gidilenler[a]=(gidilenler,yenecekler)
  else:
    if(Kare.sıradaki_renk=="siyah"):
      Kare.siyah_gidilenler=bul(Kare.siyah_taşlar,şahlar)
    if(Kare.sıradaki_renk=="beyaz"):
      Kare.beyaz_gidilenler=bul(Kare.beyaz_taşlar,şahlar)
  Kare.şah_çeken_taş=[]
  şahlar=list(set(şahlar))
  şah_git(şahlar[1])
  for i in şahlar:
    if(i.taşın_rengi=="siyah"):
      Kare.siyah_gidilenler[i]=şah_git(i)
    if(i.taşın_rengi=="beyaz"):
      Kare.beyaz_gidilenler[i]=şah_git(i)
  mat_kontrol()

def label_dan_kare(label):
  return Kare.işaretli_yerler[label]

def taştan_kare(label):
  return Kare.taşların_yeri[label]

def ye(event):
  Kare.tıklandı=False
  Kare.sırayı_değiştir()
  konum=label_dan_kare(event.widget)
  işaretleri_kaldır()
  ye_fonksiyonu(konum,Kare.tıklanan_kare)

def ye_fonksiyonu(konum,gidilen_konum):
  if(gidilen_konum.taş=="piyon" and (konum in dikey1 or konum in dikey8)):
    if((gidilen_konum.taşın_rengi=="siyah") and (konum in dikey1)):
      terfi_et(gidilen_konum,konum)
    if((gidilen_konum.taşın_rengi=="beyaz") and (konum in dikey8)):
      terfi_et(gidilen_konum,konum)
  else:
    konum.taş=gidilen_konum.taş
    konum.taşın_rengi=gidilen_konum.taşın_rengi
    konum.taş_label.destroy()
    konum.taş_label=gidilen_konum.taş_label
    gidilen_konum.taş=False
    gidilen_konum.taşın_rengi=False
    konum.taş_label["bg"]=konum.karenin_rengi
    konum.taş_label.bind("<Button-1>",taşkonum)
    yer=karenin_yeri(konum)
    gidilen_konum.taş_label.place(x=yer.split("x")[0],y=yer.split("x")[1])
    if(Kare.check):
      Kare.check=False
  hamle_başı()


def git(event,):
  Kare.tıklandı=False
  gidilen_konum=Kare.tıklanan_kare
  konum=label_dan_kare(event.widget)
  # hamleyi_adlandır(gidilen_konum,konum,gidilen_konum)
  işaretleri_kaldır()
  if(gidilen_konum.taş=="piyon"):
    if((gidilen_konum.taşın_rengi=="siyah") and (konum in dikey1)):
      terfi_et(gidilen_konum,konum)
    if((gidilen_konum.taşın_rengi=="beyaz") and (konum in dikey8)):
      terfi_et(gidilen_konum,konum)
  konum.taş=gidilen_konum.taş
  konum.taşın_rengi=gidilen_konum.taşın_rengi
  konum.taş_label=gidilen_konum.taş_label
  gidilen_konum.taş=False
  gidilen_konum.taşın_rengi=False
  konum.taş_label["bg"]=konum.karenin_rengi
  konum.taş_label.bind("<Button-1>",taşkonum)
  yer=karenin_yeri(konum)
  gidilen_konum.taş_label.place(x=yer.split("x")[0],y=yer.split("x")[1])
  Kare.sırayı_değiştir()
  if(Kare.check):
    Kare.check=False
  hamle_başı()


def karenin_yeri(konum):
  if(type(konum)==str):
    isim=konum
  else:
    isim=konum.ad
  sayı=0
  while True:
    if(isim[0]=="abcdefgh"[sayı]):
      break
    else:
      sayı+=1
      continue
  return str(sayı*64)+"x"+str((int(isim[1])-1)*64)

def işaretleri_kaldır():
  for i in Kare.git_işaretli_yerler:
    i.destroy()
  for i in Kare.ye_işaretli_yerler:
    i.destroy()
  Kare.git_işaretli_yerler=[]
  Kare.ye_işaretli_yerler=[]

def rok_türünü_bul(label):
  konum=label_dan_kare(label)
  if(konum.ad=="c8"):
    return "siyah_uzun_rok"
  if(konum.ad=="g8"):
    return "siyah_kısa_rok"
  if(konum.ad=="c1"):
    return "beyaz_uzun_rok"
  if(konum.ad=="g1"):
    return "beyaz_kısa_rok"

def rok_at(event):
  boyut=rok_türünü_bul(event.widget)
  if(boyut=="siyah_uzun_rok"):
    taş_yerleştir(c8,Kare.tıklanan_kare.taşın_rengi,Kare.tıklanan_kare.taş)
    taş_kaldır(e8)
    taş_yerleştir(d8,"siyah","kale")
    taş_kaldır(a8)
  if(boyut=="siyah_kısa_rok"):
    taş_yerleştir(g8,Kare.tıklanan_kare.taşın_rengi,Kare.tıklanan_kare.taş)
    taş_kaldır(e8)
    taş_yerleştir(f8,"siyah","kale")
    taş_kaldır(h8)
  if(boyut=="beyaz_uzun_rok"):
    taş_yerleştir(c1,Kare.tıklanan_kare.taşın_rengi,Kare.tıklanan_kare.taş)
    taş_kaldır(e1)
    taş_yerleştir(d1,"beyaz","kale")
    taş_kaldır(a1)
  if(boyut=="beyaz_kısa_rok"):
    taş_yerleştir(g1,Kare.tıklanan_kare.taşın_rengi,Kare.tıklanan_kare.taş)
    taş_kaldır(e1)
    taş_yerleştir(f1,"beyaz","kale")
    taş_kaldır(h1)
  işaretleri_kaldır()
  Kare.sırayı_değiştir()

def rok_işaret_koy(konum):
  gidilen_foto=tk.PhotoImage(file="images/gidilenler.png")
  işaretlenecekler=[]
  if(not(Kare.check)):
    if(konum.taşın_rengi=="siyah"):
      if(Kare.rok["siyah_uzun_rok"] and not(b8.taş) and not(c8.taş) and not(d8.taş)):
        işaretlenecekler.append(c8)
      if(Kare.rok["siyah_kısa_rok"] and not(f8.taş) and not(g8.taş)):
        işaretlenecekler.append(g8)
    if(konum.taşın_rengi=="beyaz"):
      if(Kare.rok["beyaz_uzun_rok"] and not(b1.taş) and not(c1.taş) and not(d1.taş)):
        işaretlenecekler.append(c1)
      if(Kare.rok["beyaz_kısa_rok"] and not(f1.taş) and not(g1.taş)):
        işaretlenecekler.append(g1)
    for i in işaretlenecekler:
      label=tk.Label(pencere,image=gidilen_foto,bg=i.karenin_rengi)
      label.image=gidilen_foto
      yer=karenin_yeri(i)
      label.place(x=yer.split("x")[0],y=yer.split("x")[1])
      label.bind("<1>",rok_at)
      Kare.git_işaretli_yerler.append(label)
      Kare.işaretli_yerler[label]=i

def işaret_koy(konum):
  gidilen_foto=tk.PhotoImage(file="images/gidilenler.png")
  yenen_foto=tk.PhotoImage(file="images/yenen.png")
  if(not(konum in Kare.açmaz)):
    if(konum.taş=="şah"):
      rok_işaret_koy(konum)
    if(konum.taşın_rengi=="siyah"):
      gidilenler=Kare.siyah_gidilenler[konum]
    if(konum.taşın_rengi=="beyaz"):
      gidilenler=Kare.beyaz_gidilenler[konum]
    for i in gidilenler[0]:
      renk=i.karenin_rengi
      label=tk.Label(pencere,image=gidilen_foto,bg=renk)
      label.image=gidilen_foto
      yer=karenin_yeri(i)
      label.place(x=yer.split("x")[0],y=yer.split("x")[1])
      label.bind("<1>",git)
      Kare.git_işaretli_yerler.append(label)
      Kare.işaretli_yerler[label]=i
    for i in gidilenler[1]:
      renk=i.karenin_rengi
      label=tk.Label(pencere,image=yenen_foto,bg=renk)
      label.image=yenen_foto
      yer=karenin_yeri(i)
      label.place(x=yer.split("x")[0],y=yer.split("x")[1])
      label.bind("<1>",ye)
      Kare.ye_işaretli_yerler.append(label)
      Kare.işaretli_yerler[label]=i

def boşkonum(event):
  xi=int(event.x/(tahta["width"]/8))
  yi=int(event.y/(tahta["height"]/8))
  konum=yatay[xi][yi]
  tıkla(konum)

def taşkonum(event):
  konum=taştan_kare(event.widget)
  if(konum.taşın_rengi==Kare.sıradaki_renk):
    tıkla(konum)
  else:
    hamle_başı()

def tıkla(konum):
  hamle_başı()
  if(Kare.tıklandı):
    Kare.tıklandı=False
    işaretleri_kaldır()
    Kare.tıklanan_kare=None
  else:
    if(konum.taş):
      Kare.tıklandı=True
      Kare.tıklanan_kare=konum
      işaret_koy(konum)


def taş_yerleştir(konum,renk,taşın_adı):
  if(renk=="beyaz"):
    Kare.beyaz_taşlar.append(konum)
  if(renk=="siyah"):
    Kare.siyah_taşlar.append(konum)
  konum.taş=taşın_adı
  konum.taşın_rengi=renk
  konum.güncelle()
  konum.taş_label.bind("<Button-1>",taşkonum)

def taş_kaldır(konum):
  if(konum.taşın_rengi=="beyaz"):
    Kare.beyaz_taşlar.remove(konum)
  if(konum.taşın_rengi=="siyah"):
    Kare.siyah_taşlar.remove(konum)
  konum.taş=False
  konum.taşın_rengi=False
  konum.taş_label.destroy()
  konum.taş_label=False

def başlangıç():
  Kare.rok["beyaz_uzun_rok"]=True
  Kare.rok["beyaz_kısa_rok"]=True
  Kare.rok["siyah_kısa_rok"]=True
  Kare.rok["siyah_uzun_rok"]=True
  sıralama=["kale","at","fil","vezir","şah","fil","at","kale"]
  for i in range(8):
    taş_yerleştir(dikey1[i],"beyaz",sıralama[i])
  for i in dikey2:
    taş_yerleştir(i,"beyaz","piyon")

  for i in range(8):
    taş_yerleştir(dikey8[i],"siyah",sıralama[i])
  for i in dikey7:
    taş_yerleştir(i,"siyah","piyon")
  
  hamle_başı()


resim=tk.PhotoImage(file="images/tahta.png")
tahta=tk.Label(pencere,image=resim,width=512,height=512)
pencere.geometry("512x512")
def maç(tahta=tahta,pencere=pencere):
  tahta.place(x=0,y=0)
  başlangıç()
  tahta.bind("<Button-1>",boşkonum)
def ana_ekran(pencere=pencere):
  def yapanlar():
    root=tk.Toplevel(tahta)
    tk.Label(root,text="Hasan Serdal Köksal", font=("Helvetica", 45)).pack()
    root.mainloop()
  def oyun_aç():
    oyun_aç.destroy()
    yapımcılar.destroy()
    maç()
  oyun_aç=tk.Button(pencere,width=15,height=2,text="Oyuna Başla",command=oyun_aç)
  yapımcılar=tk.Button(pencere,width=15,height=2,text="Yapımcılar",command=yapanlar)
  oyun_aç.place(x=233,y=210)
  yapımcılar.place(x=233,y=250)

ana_ekran()
pencere.mainloop()
pencere.title("Satranç")