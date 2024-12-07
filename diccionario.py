meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD":"Una expresion que utilza la gente para explicar algo gracioso",
            "TQM":"Te Quiero Mucho",
            "SHEESH":"ligera desaprobación"
            }
word=input("escribe una palabra que no entiendas")

if word in meme_dict.keys():
    print(meme_dict[word])
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print("la palabra no esta en el diccionario")
    # ¿Qué hacer si no se encuentra la palabra?
