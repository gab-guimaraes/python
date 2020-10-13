from SpotifyExample.Artist import Artist


class Music:
    def __init__(self, nome, artist, duracao):
        self.nome = nome
        self.artist = artist
        self.duracao = duracao

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def getArtist(self):
        return self.artist

    def setArtist(self):
        return self.artist

    def getDuracao(self):
        return self.duracao

    def setDuracao(self):
        return self.duracao

    def imprimeTudo(self):
        print("Nome da Banda: ", self.artist.nome)
        print("País: ", self.artist.pais)
        print("Música: ", self.getNome())
        print("Duração: ", self.getDuracao())
        return ""


