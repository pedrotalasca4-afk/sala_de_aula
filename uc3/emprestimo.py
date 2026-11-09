class Cliente:
    def __init__(self, nome, emprestimos_anteriores=0):
        self.nome = nome
        self.emprestimos_anteriores = emprestimos_anteriores


class Emprestimo:
    def __init__(self, cliente):
        self.cliente = cliente
        self.jogos = []

    def limite_emprestimo(self):
        if self.cliente.emprestimos_anteriores > 10:
            return 4
        return 3

    def adicionar(self, titulo):
        if not titulo:
            raise ValueError("Sem titulo, não pode estar vazip")
        if titulo in self.jogos:
            raise ValueError("Não pode jogo repetido")
        if len(self.jogos) >= self.limite_emprestimo():
            raise ValueError("Limite de jogso foi atingido para este cliente")

        self.jogos.append(titulo)