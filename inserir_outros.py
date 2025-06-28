from pymongo import MongoClient

def conectar_mongo():
    # Conexão usando a mesma URI que você já usa no app
    client = MongoClient("mongodb+srv://ryant3525:talpo100@meucluster.yyky9es.mongodb.net/?retryWrites=true&w=majority&appName=meucluster")
    db = client["eshop_brasil"]
    return db

def inserir_outros_dados(db):
    outros = db["outros_dados"]
    
    # Dados de exemplo (poderiam ser pedidos antigos, visitas, etc.)
    dados = [
        {"nome": "Cliente X", "email": "x@teste.com", "cidade": "Recife", "produto": "Livro", "valor": 49.90},
        {"nome": "Cliente Y", "email": "y@teste.com", "cidade": "Salvador", "produto": "Fone", "valor": 99.90},
        {"nome": "Cliente Z", "email": "z@teste.com", "cidade": "Curitiba", "produto": "Tênis", "valor": 189.90},
    ]
    
    result = outros.insert_many(dados)
    print(f"✅ Inseridos {len(result.inserted_ids)} documentos na coleção 'outros_dados'.")

if __name__ == "__main__":
    db = conectar_mongo()
    inserir_outros_dados(db)
