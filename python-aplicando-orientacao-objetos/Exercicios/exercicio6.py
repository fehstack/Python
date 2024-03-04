#Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
#Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. 
#Crie duas instâncias da classe e imprima essas instâncias.

class contaBancaria():
    
    contas = []
    
    def __init__(self, titular, saldo):
        self.titular = str(titular)
        self.saldo = int(saldo)
        self.ativo = False
        contaBancaria.contas.append(self)    
    
        
    def __str__(self):
        return f'{self.titular}, {self.saldo}'
    
    
    @classmethod
    def listarContaBancaria(cls):
        for conta in cls.contas:
            print(f'{conta.titular}, {conta.saldo}, {conta.ativo}')
            
    @property
    def ativarConta(self):
        return f'Ativado' if self.ativo else 'Desativado'
    
    def alterarStatus(self):
        self.ativo = not self.ativo
        

contaItau = contaBancaria("Felipe", "250")
contaItau.alterarStatus()  # Altera o status da conta Itaú
contaBancaria.listarContaBancaria()  # Lista as contas bancárias após a alteração do status
