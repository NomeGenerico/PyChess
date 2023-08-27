def GerarTabuleiro():
         temp = []
         Tabuleiro = []
         for i in range(8):
                 temp.append(0)
         for i in range(8):
                 Tabuleiro.append(temp[:])
         return Tabuleiro 
     
def AllBoard():
     Tabuleiro = GerarTabuleiro()
     return Tabuleiro 
  
#Todo: 
def FenBoardUpdater(FenDict):
  	global TabuleiroPecas, TabuleiroCor, TabuleiroPeao, TabuleiroBispo, TabuleiroCavalo, TabuleiroTorre, TabuleiroRainha, TabuleiroRei, Activecolor
  	k = 1
  	while k < 9:
  	    i = 0
  	    while i < 8:
  	        l = []
  	        x = FenDict[k]
  	        l = [*x]
  	        taml = len(l)
  	        j = 0
  	        while j < taml:
  	            match l[i]:
  	                case "1":
  	                    i = i + 1
  	                case "2":
  	                    i = i + 2
  	                case "3":
  	                    i = i + 3
  	                case "4":
  	                    i = i + 4
  	                case "5":
  	                    i = i + 5
  	                case "6":
  	                    i = i + 6
  	                case "7":
  	                    i = i + 7
  	                case "8":
  	                    i = i + 8
  	                case "p":
  	                    TabuleiroPecas[k-1][i] = 1
  	                    TabuleiroCor[k-1][i] = -1
  	                    TabuleiroPeao[k-1][i] =1
  	                    i = i + 1
  	                case "r":
  	                    TabuleiroPecas[k-1][i] = 1
  	                    TabuleiroCor[k-1][i] = -1
  	                    TabuleiroTorre[k-1][i] =1
  	                    i = i + 1
  	                case "n":
  	                    TabuleiroPecas[k-1][i] = 1
  	                    TabuleiroCor[k-1][i] = -1
  	                    TabuleiroCavalo[k-1][i] =1
  	                    i = i + 1
  	                case "b":
  	                    TabuleiroPecas[k-1][i] = 1
  	                    TabuleiroCor[k-1][i] = -1
  	                    TabuleiroBispo[k-1][i] =1
  	                    i = i +1
  	                case "q":
  	                    TabuleiroPecas[k-1][i] = 1
  	                    TabuleiroCor[k-1][i] = -1
  	                    TabuleiroRainha[k-1][i] =1
  	                    i = i +1
  	                case "k":
  	                    TabuleiroPecas[k-1][i] = 1
  	                    TabuleiroCor[k-1][i] = -1
  	                    TabuleiroRei[k-1][i] =1
  	                    i = i +1
  	                case "P":
  	                    TabuleiroPecas[k-1][i] = 1
  	                    TabuleiroCor[k-1][i] = 1
  	                    TabuleiroPeao[k-1][i] =1
  	                    i = i + 1
  	                case "R":
  	                    TabuleiroPecas[k-1][i] = 1
  	                    TabuleiroCor[k-1][i] = 1
  	                    TabuleiroTorre[k-1][i] =1
  	                    i = i + 1
  	                case "N":
  	                    TabuleiroPecas[k-1][i] = 1
  	                    TabuleiroCor[k-1][i] = 1
  	                    TabuleiroCavalo[k-1][i] =1
  	                    i = i + 1
  	                case "B":
  	                    TabuleiroPecas[k-1][i] = 1
  	                    TabuleiroCor[k-1][i] = 1
  	                    TabuleiroBispo[k-1][i] =1
  	                    i = i + 1
  	                case "Q":
  	                    TabuleiroPecas[k-1][i] = 1
  	                    TabuleiroCor[k-1][i] = 1
  	                    TabuleiroRainha[k-1][i] =1
  	                    i = i +1
  	                case "K":
  	                    TabuleiroPecas[k-1][i] = 1
  	                    TabuleiroCor[k-1][i] = 1
  	                    TabuleiroRei[k-1][i] =1
  	                    i = i +1
  	            j = j + 1
  	    k = k + 1
  	return  


def FenNotationReader(Fen):
     global TabuleiroPecas, TabuleiroCor, TabuleiroPeao, TabuleiroBispo, TabuleiroCavalo, TabuleiroTorre, TabuleiroRainha, TabuleiroRei, Activecolor, FenDict
     if Fen == 1:
         Fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
     Rank8,Rank7,Rank6,Rank5,Rank4,Rank3,Rank2,Rank1andStuf = Fen.split("/")
     Rank1, ActiveColor, CastelingRights, EnPeaseantTarget, HalfMoves, FullMoves = Rank1andStuf.split(" ")
     FenDict = dict([(1, Rank8),(2, Rank7),(3, Rank6),(4, Rank5),(5, Rank4),(6, Rank3),(7, Rank2),(8, Rank1),("A", ActiveColor),("C", CastelingRights),("E", EnPeaseantTarget),("H", HalfMoves),("F", FullMoves)])
     FenBoardUpdater(FenDict)
     
#Todo: 
def FenNotationGenerate():
     Fen = "a"
     return Fen

def GerarGameState():
    global FullMoves, HalfMoves, EnPeaseantTarget, ActiveColor, CastelingRights, TabuleiroPecas, TabuleiroCor, TabuleiroPeao, TabuleiroBispo, TabuleiroCavalo, TabuleiroTorre, TabuleiroRainha, TabuleiroRei, Activecolor, FenDict
    TabuleiroPecas = GerarTabuleiro()
    TabuleiroCor = GerarTabuleiro()
    TabuleiroPeao = GerarTabuleiro()
    TabuleiroBispo = GerarTabuleiro()
    TabuleiroCavalo = GerarTabuleiro()
    TabuleiroTorre = GerarTabuleiro()
    TabuleiroRainha = GerarTabuleiro()
    TabuleiroRei = GerarTabuleiro()
    FenNotationReader(1)
    CastelingRights = FenDict["C"]
    ActiveColor = FenDict["A"]
    EnPeaseantTarget = FenDict["E"]
    HalfMoves = FenDict["H"]
    FullMoves = FenDict["F"]
    

GerarGameState()
