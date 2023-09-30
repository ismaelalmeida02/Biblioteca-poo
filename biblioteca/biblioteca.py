from livro.livro_fisico import LivroFisico
from membro.membro import Membro

class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__membros = []

    def cadastrarMembro(self,membro: Membro):
        self.__membros.append(membro)
        print("novo membro adicionado a biblioteca!")

    def deletarMembro(self, membro_id):
        for membro in self.__membros:
            if membro.membro_id == membro_id:
                self.__membros.remove(membro)
                print("membro deletado com sucesso!")

    def cadastrarLivro(self, livro: LivroFisico):
        self.__livros.append(livro)
        print("novo livro adicionados a bibliteoca")

    def deletarLivro(self, id):
        for livro in self.__livros:
            if livro.livro_id == id:
                self.__livros.remove(livro)
                print("Livro deletado com sucesso!")

    def listarLivros(self):
        for livro in self.__livros:
            print(f"id: {livro.livro_id}")
            print(f"titulo: {livro.titulo}")
            print(f"autor: {livro.autor}")
            print(f"ano: {livro.ano_publi}")
            print(f"n° de páginas: {livro.numero_paginas} \n")

    def listarMembros(self):
        print("... Membros Cadastrados ...")
        for membro in self.__membros:
            print(f"id: {membro.membro_id}")
            print(f"nome: {membro.nome}")
            print(f"endereço: {membro.endereco}")
            print(f"telefone: {membro.telefone}")

if __name__ == "__main__":
    biblioteca = Biblioteca()
    m1 = Membro(1,"luis" , "rua e","987354876")
    m2 = Membro(2,"cabral" , "rua c","3487354876")
    liv1 = LivroFisico(1,"tolkien" , "lor" , 1970 ,700)
    biblioteca.cadastrarMembro(m1)
    biblioteca.cadastrarMembro(m2)
    biblioteca.cadastrarLivro(liv1)
    biblioteca.listarMembros()
    biblioteca.listarLivros()

