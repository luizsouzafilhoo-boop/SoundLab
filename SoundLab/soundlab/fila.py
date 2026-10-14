"""
TAD Fila de Execução — Módulo 3 (Semana 1)
Implementação de Fila (FIFO) e Fila Circular para repetição.
"""

class No:
    """Elo da fila: guarda a faixa e o ponteiro para o próximo."""
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class FilaExecucao:
    """Fila de reprodução (FIFO): a primeira faixa a entrar é a primeira a sair."""
    def __init__(self):
        self._frente = None
        self._tras = None
        self._tamanho = 0

    def enfileirar(self, faixa):
        """Insere um novo nó no FIM da fila (_tras)."""
        novo = No(faixa)
        if self._tras is None:
            self._frente = novo
            self._tras = novo
        else:
            self._tras.proximo = novo
            self._tras = novo
        self._tamanho += 1

    def desenfileirar(self):
        """Remove e devolve o valor do nó na FRENTE da fila."""
        if self.vazia():
            raise IndexError("fila de execucao vazia")
        no = self._frente
        self._frente = no.proximo
        if self._frente is None:
            self._tras = None
        self._tamanho -= 1
        return no.valor

    def vazia(self):
        return self._tamanho == 0

    def __len__(self):
        return self._tamanho


class FilaCircular(FilaExecucao):
    """Fila circular para o modo de repetição automática."""
    def desenfileirar_com_repeticao(self):
        """Remove a faixa da frente, executa e joga ela de volta para o fim da fila."""
        if self.vazia():
            raise IndexError("fila vazia")
        faixa = self.desenfileirar()
        self.enfileirar(faixa)
        return faixa