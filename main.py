import matplotlib as plt
import json
import  seaborn as sns

with open("ebadestek.json",encoding="cp437", errors='ignore') as a:
    donusum=json.load(a)



yil=list()
uygulamasayisi=list()


for i in range(0,100):
    yil.append(donusum["records"][i][5])
    uygulamasayisi.append(donusum["records"][i][5])


axes=sns.regplot(x=yil,y=uygulamasayisi)
sns.set_style("whitegrid")

axes.set_title("Yıllara göre ilac uygulama sayısı değişkenliği")
axes.set_ylabel("Uygulama Sayısı")
axes.set_xlabel("Yıllar")

plt.plot(yil,uygulamasayisi,"ro")
plt.show()

