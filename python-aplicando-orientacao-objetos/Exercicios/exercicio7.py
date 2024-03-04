class ClienteBanco():
    """
    Classe para representar um cliente bancário.

    Attributes:
        cliente (list): Uma lista de todos os clientes bancários criados.
    """
    
    cliente = []
    
    def __init__(self, nome, idade, renda, endereco, telefone):
        """
        Inicializa um objeto ClienteBanco.

        Args:
            nome (str): O nome do cliente.
            idade (int): A idade do cliente.
            renda (float): A renda do cliente.
            endereco (str): O endereço do cliente.
            telefone (str): O número de telefone do cliente.
        """
        self._nome = nome.title()
        self._idade = idade
        self._renda = renda
        self._endereco = endereco.title()
        self._telefone = telefone
        self._ativo = True
        ClienteBanco.cliente.append(self)
        
    def __str__(self):
        """
        Retorna uma representação em string do objeto ClienteBanco.

        Returns:
            str: O nome e a idade do cliente.
        """
        return f'{self._nome},{self._idade}'
    
    
    @classmethod
    def listarCliente(cls):
        """
        Lista todos os clientes bancários.

        Atributos listados: nome, idade, renda, endereço, telefone e estado ativo.

        """
        print(f'{"Nome".ljust(20)} | {"Idade".ljust(20)} | {"Renda".ljust(20)} | {"Endereço".ljust(20)} | {"Telefone".ljust(20)} | {"Ativo".ljust(20)}')
        
        for cliente in cls.cliente:
            print(f'{cliente._nome.ljust(20)} | {cliente._idade.ljust(20)} | {cliente._renda.ljust(20)} | {cliente._endereco.ljust(20)} | {cliente._telefone.ljust(20)} | {cliente.ativarCliente.ljust(20)}')
    
    @property
    def ativarCliente(self):
        """
        Retorna o status de ativação do cliente.

        Returns:
            str: 'Ativado' se o cliente estiver ativo, 'Desativado' caso contrário.
        """
        return 'Ativado' if self._ativo else 'Desativado'
    
    def alterarStatus(self):
        """
        Altera o status do cliente entre ativo e inativo.

        Se o cliente estiver ativo,  este método o tornará inativo e vice-versa.
        """
        self._ativo = not self._ativo


bancoSantander = ClienteBanco("felipe", "17", "2500", "leonardo da Vinci", "1123592077")
bancoSantander.alterarStatus()
ClienteBanco.listarCliente()
