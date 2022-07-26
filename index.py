from dadata import Dadata
import sqlite3
con = sqlite3.connect('local.db')
print("введите ваш token для доступа к Dadata")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS DadataUsers (programming_language,token)''')
pl =  input()
token = input()
cur.execute("INSERT INTO DadataUsers (programming_language,token) VALUES (?,?)",(pl,token))
con.commit()
dadata = Dadata(token)
print("введите нужное вам место положение")
zapros = dadata.suggest(name="address", query=input())
for i in range(len(zapros)):
    print(i,zapros[i]['value'])
print("уточните ваш адрес")
result=dadata.clean(name="address", source=input())
print(result)
    