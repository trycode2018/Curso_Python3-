import json
import os
from transaction import Transacao

class GerenciadorFinanceiro:
    def __init__(self, arquivo_dados='dados.json'):
        self.transacoes = []
        self.arquivo_dados = arquivo_dados
        self.carregar_dados()

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
        self.salvar_dados()

    def listar_transacoes(self):
        for t in self.transacoes:
            print(f"{t.data} - {t.tipo.upper()} - {t.valor:.2f} Kz - {t.descricao}")

    def calcular_saldo(self):
        saldo = 0
        for t in self.transacoes:
            if t.tipo == 'receita':
                saldo += t.valor
            else:
                saldo -= t.valor
        return saldo

    def filtrar_por_tipo(self, tipo):
        return [t for t in self.transacoes if t.tipo == tipo]

    def salvar_dados(self):
        with open(self.arquivo_dados, 'w') as f:
            json.dump([t.to_dict() for t in self.transacoes], f, indent=4)

    def carregar_dados(self):
        if os.path.exists(self.arquivo_dados):
            with open(self.arquivo_dados, 'r') as f:
                dados = json.load(f)
                self.transacoes = [Transacao.from_dict(t) for t in dados]
