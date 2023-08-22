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
    
TabuleiroPecas = GerarTabuleiroPecas()
TabuleiroCor = GerarTabuleiroCor()
TabuleiroPeao = GerarTabuleiroPeao()
TabuleiroBispo = GerarTabuleiroBispo()
TabuleiroCavalo = GerarTabuleiroCavalo()
TabuleiroTorre = GerarTabuleiroTorre()
TabuleiroRainha = GerarTabuleiroRainha()
TabuleiroRei = GerarTabuleiroRei()	

print(TabuleiroPecas)


