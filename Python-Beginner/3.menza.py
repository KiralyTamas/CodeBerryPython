count=0
k1=["Pálfi Aranka I","Gál Asztik I","Földes Nóra N","Mondi Zita I","Király Tamás I","Bendegúz I","Csigridí I","Szuri I","Uhu I"]
while count<len(k1):
  if k1[count][-1]=="I":
    print(k1[count]+" betűvel lett jelezve, kér uzsonnát")
  else:
    print(k1[count]+" betűvel lett jelezve, nem kér uzsonnát")
  count+=1