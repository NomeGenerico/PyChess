def GerarTabuleiro():
	temp = []
	Tabuleiro = []
	for i in range(8):
		temp.append(0)
	for i in range(8):
		Tabuleiro.append(temp[:])
	return Tabuleiro

def GerarTabuleiroPecas():
    Tabuleiro = GerarTabuleiro()
    i = 0
    while i < 8:
        if i == 0 or i == 1 or i == 6 or i == 7:
            j = 0
            while j < 8:
                Tabuleiro[i][j] = 1
                j = j+1
        i = i + 1

    return Tabuleiro

def GerarTabuleiroPeao():
    Tabuleiro = GerarTabuleiro()
    i = 0
    while i < 8:
        if i == 1 or i == 6:
            j = 0
            while j < 8:
                Tabuleiro[i][j] = 1
                j = j+1
        i = i + 1

    return Tabuleiro

def GerarTabuleiroCor():
    Tabuleiro = GerarTabuleiro()
    i = 0
    while i < 8:
        if i == 0 or i == 1:
            j = 0
            while j < 8:
                Tabuleiro[i][j] = -1
                j = j+1
        i = i + 1
    i = 0
    while i < 8:
        if i == 6 or i == 7:
            j = 0
            while j < 8:
                Tabuleiro[i][j] = 1
                j = j+1
        i = i + 1
    return Tabuleiro

def GerarTabuleiroBispo():
    Tabuleiro = GerarTabuleiro()
    Tabuleiro[0][2] = 1
    Tabuleiro[0][5] = 1
    Tabuleiro[7][2] = 1
    Tabuleiro[7][5] = 1
    return Tabuleiro

def GerarTabuleiroCavalo():
    Tabuleiro = GerarTabuleiro()
    Tabuleiro[0][1] = 1
    Tabuleiro[0][6] = 1
    Tabuleiro[7][1] = 1
    Tabuleiro[7][6] = 1
    return Tabuleiro

def GerarTabuleiroTorre():
    Tabuleiro = GerarTabuleiro()
    Tabuleiro[0][0] = 1
    Tabuleiro[0][7] = 1
    Tabuleiro[7][0] = 1
    Tabuleiro[7][7] = 1
    return Tabuleiro

def GerarTabuleiroRainha():
    Tabuleiro = GerarTabuleiro()
    Tabuleiro[0][3] = 1
    Tabuleiro[7][3] = 1
    return Tabuleiro

def GerarTabuleiroRei():
    Tabuleiro = GerarTabuleiro()
    Tabuleiro[0][4] = 1
    Tabuleiro[7][4] = 1
    return Tabuleiro

def AllBoard():
    Tabuleiro = GerarTabuleiro()
    return Tabuleiro

#Todo:
def FenBoardUpdater(rank,i):
    return 

def FenNotationReader(Fen, Key):
    global TabuleiroPecas, TabuleiroCor, TabuleiroPeao, TabuleiroBispo, TabuleiroCavalo, TabuleiroTorre, TabuleiroRainha, TabuleiroRei, Activecolor
    Fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    Rank8,Rank7,Rank6,Rank5,Rank4,Rank3,Rank2,Rank1andStuf = Fen.split("/")
    Rank1, ActiveColor, CastelingRights, EnPeaseantTarget, HalfMoves, FullMoves = Rank1andStuf.split(" ")
    d = dict([(1, Rank8),(2, Rank7),(3, Rank6),(4, Rank5),(5, Rank4),(6, Rank3),(7, Rank2),(8, Rank1),("A", ActiveColor),("C", CastelingRights),("E", EnPeaseantTarget),("H", HalfMoves),("F", FullMoves)])
    return d[Key]

#Todo:
def FenNotationGenerate():
    Fen = "a"
    return Fen

ActiveColor = "w"
TabuleiroPecas = GerarTabuleiroPecas()
TabuleiroCor = GerarTabuleiroCor()
TabuleiroPeao = GerarTabuleiroPeao()
TabuleiroBispo = GerarTabuleiroBispo()
TabuleiroCavalo = GerarTabuleiroCavalo()
TabuleiroTorre = GerarTabuleiroTorre()
TabuleiroRainha = GerarTabuleiroRainha()
TabuleiroRei = GerarTabuleiroRei()
