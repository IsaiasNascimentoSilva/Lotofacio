import requests
import json


result = requests.get('https://loteriascaixa-api.herokuapp.com/api/lotofacil/latest')
db = result.json()
concurso = db['concurso']
dezenas = []
for i in range(1,11):
  con = concurso - i
  result2 = requests.get('https://loteriascaixa-api.herokuapp.com/api/lotofacil/{}'.format(con)).json()
  for j in result2['dezenas']:
    dezenas.append(j)
  
tab = {'01':'','02':'','03':'','04':'','05':'','06':'','07':'','08':'','09':'','10':'','11':'','12':'','13':'','14':'','15':'','16':'','17':'','18':'','19':'','20':'','21':'','22':'','23':'','24':'','25':''}

def count(str):
  global dezenas
  cont = 0
  for i in dezenas:
    if i == str:
      cont+=1
  return cont   
  
for id in list(tab.keys()):
  sum = count(id)
  tab[id] = sum

def menor(lst):
  global tab
  menor = lst[0]
  for g in lst:
      if tab.get(g) < tab.get(menor):
        menor = g
  return menor
  

five = ['']
lst = list(tab.keys())
for x in range(5):
  if five[x] in lst:
    lst.remove(five[x])
  res = menor(lst)
  five.append(res)
  
five.remove('')

print(five)
print(tab)