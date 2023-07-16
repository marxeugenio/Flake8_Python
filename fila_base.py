import abc


class FilaBase(metaclass=abc.ABCMeta):
    codigo = 0
    fila = []
    clientes_atendidos = []
    senha_atual = None

    @abc.abstractmethod
    def chama_cliente(self, caixa):
        ...

    @abc.abstractmethod
    def estatistica(self, dia, agencia, flag_detail):
        ...

    @abc.abstractmethod
    def atualiza_fila(self):
        ...