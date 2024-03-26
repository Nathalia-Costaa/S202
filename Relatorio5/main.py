from LivroModel import LivroModel
from database import Database

print("Seja bem vindo ao cadastro de livros")

db = Database(database="livraria", collection="livros")
db.resetDatabase()
livroModel = LivroModel(db)
while True:
    print("Insira 1 para cadastrar um livro novo") # crud
    print("Insira 2 para buscar um livro")
    print("Insira 3 para atualizar um livro")
    print("Insira 4 para deletar um livro")

    opcao = input()

    if opcao == "1":
        titulo = input("Insira o título do livro")
        autor = input("Insira o autor do livro")
        ano = int(input("Insira o ano do livro"))
        preco = float(input("Insira o preco do livro"))

        livroModel.create_book(titulo, autor, ano, preco)
    elif opcao == "2":
        idLivro = input("Insira o id do livro")

        livroModel.read_book_by_id(idLivro)
    elif opcao == "3":
        idLivro = input("Insira o id do livro")
        titulo = input("Insira o título do livro atualizado")
        autor = input("Insira o autor do livro atualizado")
        ano = int(input("Insira o ano do livro atualizado"))
        preco = float(input("Insira o preco do livro atualizado"))

        livroModel.update_book(idLivro, titulo, autor, ano, preco)
    elif opcao == "4":
        idLivro = input("Insira o id do livro")

        livroModel.delete_book(idLivro)
    else:
        print("Insira uma opção válida")
