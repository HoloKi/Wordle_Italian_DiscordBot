import os
import json


def Aggiorna_punti(user_id,nickname, points):
    # Controllo se l'utente è nel database
    presente = Check(user_id)
    # Se non è presente sul database
    if presente is not True:
        Aggiungi_utente(user_id,nickname,points)
    # Se è presente sul database
    else:
        Modifica_punti(user_id, points)





def test(user_id,nickname,point):
    print(f'{user_id},{nickname},{point}')
    data = {
        "wordle": [
            {
            "id": user_id,
            "nickname": nickname,
            "punti": point
            }
        ]
    }
    with open("data.json", "w") as write_file:
        json.dump(data, write_file,indent=4)


def Check(user_id):
    f = open("data.json", "r")
    data = json.loads(f.read())
    for i in data['wordle']:
        print(i)
        id = int(data['wordle'][0]['id'])
        print(id)
        if id == user_id:
            print("trovato")
            return True
    print("nulla")
    return False

def Aggiungi_utente(user_id,nickname,points, filename='data.json'):
    new_data = {
        "id": user_id,
        "nickname": nickname,
        "punti": points
    }
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["wordle"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)


def Modifica_punti(user_id, points):
    with open("data.json", "r") as file_json:
        data = json.loads(file_json.read())
        for i in data['wordle']:
            print(i)
            #id = int(data['wordle'][0]['id'])
            #Trovo utente con quell'id
            if i['id'] == user_id:
                punti = int(i['punti'])
                print(punti)
                punti_agg = punti + int(points)
                print(punti_agg)
                i['punti'] = punti_agg
                with open("data.json","w") as f:
                    json.dump(data,f,indent=4)
                return
            else:
                print("c'è stato un problema con l'aggiornamento dei punti")
                return

def sortMethod(e):
  return e['punti']

def Lista():
    with open("data.json", "r") as file_json:
        lista = []
        data = json.loads(file_json.read())
        print(data)
        data['wordle'].sort(key=sortMethod, reverse=True)
        for i in data['wordle']:
            lista.append(i)
            print(i)

        return lista



