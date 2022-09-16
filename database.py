import pymongo

def adicionar_player():
    pass

database_client = pymongo.MongoClient("mongodb+srv://LylaZX:Lilinha1702@discord-bot.l1wya.mongodb.net/test")
database = database_client.get_database("PersonagensDB")
fichas = database.personagens

teste = {
    "nome" : "Quinn",
    "raça" : "Espírito",
    "classe" : "Suporte",
    "atributos" : [10, 15, 12, 12, 11, 16],
    "lvl" : 6,
    "pv" : 31,
    "ca" : 17,
    "jp" : 14,
    "movimentacao" : 8,
    "ba_shortrange" : 3,
    "ba_longrange" : 5,
    "po" : 137,
    "xp" : 9.665
}

fichas.insert_one(teste)