class NoArvore:
    def __init__(self, nome, filhos=None):
        self.nome = nome
        self.filhos = []

    def add_filho(self, filho):
        self.filhos.append(filho)

    def encontrar(self, filo, classe, caracteristica):
        filho = self.verifica_filhos(filo)
        filho = filho.verifica_filhos(classe)
        filho = filho.verifica_filhos(caracteristica)

        return filho.filhos[0].nome

    def __repr__(self, posicaoNo=0):
        retorno = '     ' * posicaoNo + repr(self.nome) + "\n"
        for filho in self.filhos:
            retorno += filho.__repr__(posicaoNo + 1)

        return retorno
    
    def verifica_filhos(self, definicao):
        for filho in self.filhos:
            if filho.nome == definicao:
                return filho


class Arvore:
    def __init__(self, noPai):
        self.noPai = noPai

    def __repr__(self):
        return repr(self.noPai)

    def encontrar(self, filo, classe, caracteristica):
        return self.noPai.encontrar(filo, classe, caracteristica)


if __name__ == "__main__":
    animal = NoArvore("animal")

    ###############################################

    '''VERTEBRADO'''
    vertebrado = NoArvore("vertebrado")

    '''AVE'''
    ave = NoArvore("ave")

    ave_carnivoro = NoArvore("carnivoro")
    aguia = NoArvore("aguia")

    ave_onivoro = NoArvore("onivoro")
    pomba = NoArvore("pomba")

    '''MAMIFERO'''
    mamifero = NoArvore("mamifero")

    mamifero_onivoro = NoArvore("onivoro")
    homem = NoArvore("homem")

    mamifero_herbivoro = NoArvore("herbivoro")
    vaca = NoArvore("vaca")

    ###############################################

    '''INVERTEBRADO'''
    invertebrado = NoArvore("invertebrado")

    '''INSETO'''
    inseto = NoArvore("inseto")

    inseto_hematofago = NoArvore("hematofago")
    pulga = NoArvore("pulga")

    inseto_herbivoro = NoArvore("herbivoro")
    lagarta = NoArvore("lagarta")

    '''ANELIDEO'''
    anelideo = NoArvore("anelideo")

    anelideo_hematofago = NoArvore("hematofago")
    sanguessuga = NoArvore("sanguessuga")

    anelideo_onivoro = NoArvore("onivoro")
    minhoca = NoArvore("minhoca")

    ###############################################

    animal.add_filho(vertebrado)
    animal.add_filho(invertebrado)

    vertebrado.add_filho(ave)
    vertebrado.add_filho(mamifero)

    ave.add_filho(ave_carnivoro)
    ave.add_filho(ave_onivoro)

    ave_carnivoro.add_filho(aguia)
    ave_onivoro.add_filho(pomba)

    mamifero.add_filho(mamifero_onivoro)
    mamifero.add_filho(mamifero_herbivoro)

    mamifero_onivoro.add_filho(homem)
    mamifero_herbivoro.add_filho(vaca)

    invertebrado.add_filho(inseto)
    invertebrado.add_filho(anelideo)

    inseto.add_filho(inseto_hematofago)
    inseto.add_filho(inseto_herbivoro)

    inseto_hematofago.add_filho(pulga)
    inseto_herbivoro.add_filho(lagarta)

    anelideo.add_filho(anelideo_hematofago)
    anelideo.add_filho(anelideo_onivoro)

    anelideo_hematofago.add_filho(sanguessuga)
    anelideo_onivoro.add_filho(minhoca)

    arvore = Arvore(animal)

    filo = str(input())
    classe = str(input())
    caracteristica = str(input())
    print(arvore.encontrar(filo, classe, caracteristica))
