from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")


db = client["restaurante"]
cardapio = db["pratos"]


cardapio.delete_many({})


cardapio.insert_one({"nome": "Pizza Margherita", "preco": 40.0, "categoria": "Pizza"})
cardapio.insert_one({"nome": "Lasanha", "preco": 35.0, "categoria": "Massas"})
cardapio.insert_one({"nome": "Coca-Cola", "preco": 7.0, "categoria": "Bebida"})
print("Pratos adicionados!")


print("\n Cardápio inicial:")
for prato in cardapio.find():
    print(prato)


cardapio.update_one({"nome": "Pizza Margherita"}, {"$set": {"preco": 45.0}})
print("\n Preço da Pizza Margherita atualizado!")


print("\n Cardápio após atualização:")
for prato in cardapio.find():
    print(prato)


cardapio.delete_one({"nome": "Coca-Cola"})
print("\n Coca-Cola removida!")


print("\n Cardápio final:")
for prato in cardapio.find():
    print(prato)
