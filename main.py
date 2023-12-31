
import requests

# Configura as requisicoes
result = requests.get('https://loteriascaixa-api.herokuapp.com/api/lotofacil/latest')
db = result.json()
concurso = db['concurso']
dezenas = []
for i in range(1,11):
  con = concurso - i
  result2 = requests.get('https://loteriascaixa-api.herokuapp.com/api/lotofacil/{}'.format(con)).json()
  for j in result2['dezenas']:
    dezenas.append(j)

# base de dados
tab = {'01':'','02':'','03':'','04':'','05':'','06':'','07':'','08':'','09':'','10':'','11':'','12':'','13':'','14':'','15':'','16':'','17':'','18':'','19':'','20':'','21':'','22':'','23':'','24':'','25':''}

# Contador de repeticao
def count(str):
  global dezenas
  cont = 0
  for i in dezenas:
    if i == str:
      cont+=1
  return cont   


# Adiciona a soma de repeticao da dezena na base de dados
for id in list(tab.keys()):
  sum = count(id)
  tab[id] = sum

# Econtra a dezena que menos se repete na base de dados
def menor(lst):
  global tab
  menor = lst[0]
  for g in lst:
      if tab.get(g) < tab.get(menor):
        menor = g
  return menor
  
# Armazena as cincos dezenas menos repetidas
dez = ['']
lst = list(tab.keys())
for x in range(10):
  if dez[x] in lst:
    lst.remove(dez[x])
  res = menor(lst)
  dez.append(res)
  
dez.remove('')

# Criar jogos
game1 = []
for i in tab.keys():
  if not(i in dez):
    game1.append(i)

# Exibi o resultado ao usuario
print(dez)
print(game1)