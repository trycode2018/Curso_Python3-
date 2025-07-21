from datetime import datetime

class Transacao:
    def __init__(self, tipo, valor, descricao, data=None):
        if tipo not in ['receita', 'despesa']:
            raise ValueError("Tipo deve ser 'receita' ou 'despesa'.")

        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao
        self.data = data if data else datetime.now().strftime('%Y-%m-%d')

    def to_dict(self):
        return {
            'tipo': self.tipo,
            'valor': self.valor,
            'descricao': self.descricao,
            'data': self.data
        }

    @staticmethod
    def from_dict(dados):
        return Transacao(
            tipo=dados['tipo'],
            valor=dados['valor'],
            descricao=dados['descricao'],
            data=dados['data']
        )
