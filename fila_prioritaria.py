
# Cria a classe e defini seus atributos
class FilaPrioritaria:
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""

# Defini o método responsável por gerar as senhas, lembrando que o código da fila é inserido nesse método.

    def gera_senha_atual(self)->None:
        self.senha_atual = f"PR{self.codigo}"

# definir o método que verifica qual a posição atual da fila e caso ela seja maior ou igual a 100 a posição da fila deve ser resetada.

    def reseta_fila(self)->None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

# chamar esses métodos e inserir a senha atual na fila.

    def atualiza_fila(self)->None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

# Com as senhas geradas e a fila sendo alimentada já podemos nos preocupar em chamar os clientes que devem ser atendidos!

    def chama_cliente(self,caixa:int)->str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f"Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}")  
    
# Por fim vamos criar o método responsável por gerar as estatisticas esse método deve retornar uma estatística detalhada ou resumida de acordo com um argumento recebido.

    def estastistica(self, dia: str, agencia: int, flag: str)-> dict:
        if flag!="detail":
            estastistica = {f"{agencia}-{dia}": len(self.clientes_atendidos)}
        else:
            estastistica = {}
            estastistica ["dia"] = dia
            estastistica ["agencia"] = agencia
            estastistica ["clientes atendidos"] = self.clientes_atendidos
            estastistica ["quantidade de clientes atendidos"] = len(self.clientes_atendidos)

        return estastistica
