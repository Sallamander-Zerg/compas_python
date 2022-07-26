from dadata import Dadata
import sqlite3
con = sqlite3.connect('local.db')
print("введите ваш token для доступа к Dadata")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS DadataUsers (Dadata_URL_servis,programming_language,token)''')
print("выберете язык введите влучаи неверного выбора програма закроеться")
print("ru для исползования Русского")
print("en to use Еnglish")
def compas(dadata):    
    print("введите нужное вам место положение")
    zapros = dadata.suggest(name="address", query=input(),language=lang)
    for i in range(len(zapros)):
        print(i,zapros[i]['value'])
    print("уточните ваш адрес")
    result=dadata.clean(name="address", source=input())
    print(result[0]["geo_lat"]["geo_lon"])

lang =  input()
token = input() 
def database(lang,token):
    if lang=="en" or lang=="ru":
        cur.execute("INSERT INTO DadataUsers (Dadata_URL_servis,programming_language,token) VALUES ('https://dadata.ru',?,?)",(lang,token))
        con.commit()
        while True: 
            dadata = Dadata(token) 
            compas(dadata)     
            continue
    else:
        print("ошибка языка")    
database(lang,token) 
    