class JogoBatalhaNaval:
    def __init__(self):
        # Inicialização do jogo
        pass

    def jogar(self, arquivo_jogador1, arquivo_jogador2):
        instrucoes_j1 = self.ler_instrucoes(arquivo_jogador1)
        instrucoes_j2 = self.ler_instrucoes(arquivo_jogador2)

        # Verificação de quantidade de peças e tiros
        if not (self.validar_instrucoes(instrucoes_j1) and self.validar_instrucoes(instrucoes_j2)):
            print("Erro: Formato inválido nas instruções dos jogadores.")
            return False

        # Continuação do jogo...
        return True

    def ler_instrucoes(self, arquivo):
        with open(arquivo, 'r') as f:
            instrucoes = f.readlines()
        # Remover quebras de linha e espaços extras
        instrucoes = [linha.strip() for linha in instrucoes]
        return instrucoes

    def validar_instrucoes(self, instrucoes):
        for instrucao in instrucoes:
            partes = instrucao.split(';')
            if len(partes) != 2:
                return False
            movimentos = partes[1].split('|')
            for movimento in movimentos:
                if not self.validar_movimento(movimento):
                    return False
        return True

    def validar_movimento(self, movimento):
        if len(movimento) < 2:
            return False
        if len(movimento) == 2:
            if not (movimento[0].isalpha() and movimento[1].isdigit()):
                return False
        elif len(movimento) == 3:
            if not (movimento[0].isalpha() and movimento[1].isdigit() and movimento[2] in ['V', 'H']):
                return False
        return True


# Inicialização e execução do jogo
if __name__ == "__main__":
    jogo = JogoBatalhaNaval()
    resultado = jogo.jogar('jogador1.txt', 'jogador2.txt')
    if resultado:
        print("Jogo concluído com sucesso.")
    else:
        print("Ocorreu um erro no jogo.")
