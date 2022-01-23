class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__maim__':
        p = Pessoa('Rogerio')
        print(Pessoa.cumprimentar(p))
        print(id(p))
        print(p.cumprimentar())
        print(p.nome)
        p.nome = 'Renato'
        print(p.nome)
        print(p.idade)
