from livro.livro_fisico import LivroFisico


class Membro:
    def __init__(self, membro_id, nome, endereco, telefone):
        self.__membro_id = membro_id
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__livro_emprestados = []

    def emprestarlivro(self, livro: LivroFisico):
        if livro.estaDisponivel():
            self.__livro_emprestados.append(livro)
            livro.emprestar()
        else:
            print("livro indiponivel")

    def devolverlivors(self, livro: LivroFisico):
        if livro in self.__livro_emprestados:
            self.__livro_emprestados.remove(livro)
            livro.devolve()
        else:
            print("livro não encontrado!")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, value):
        self.__telefone = value

    @property
    def membro_id(self):
        return self.__membro_id

    @membro_id.setter
    def membro_id(self, value):
        self.__membro_id = value

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, value):
        self.__endereco = value


if __name__ == "__main__":
    membroBiblioteca = Membro(1, "luana", "rua a", "888888888")

    livro2 = LivroFisico(2, "hp", "fulana", "1990", 100)
    membroBiblioteca.emprestarlivro(livro1)
    membroBiblioteca.emprestarlivro(livro2)
    membroBiblioteca.devolverlivors(livro2)
