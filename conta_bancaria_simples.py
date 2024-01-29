# sacar, adicionar, que os atibutos são nome, cpf e saldo e os metodos serão adicionar e sacar saldo

class ContaBancaria:
    def __init__(self, saldo, cpf):
        self._saldo = saldo
        self._cpf = cpf  

    def depositar(self, valor, cpf_digitado):
        if self._verificar_cpf(cpf_digitado):
            if valor > 0:
                self._saldo += valor
                return f'Depósito de {valor} realizado. Novo saldo: {self._saldo}'
            else:
                return 'Valor de depósito inválido.'
        else:
            return 'CPF inválido. Operação não autorizada.'

    def sacar(self, valor, cpf_digitado):
        if self._verificar_cpf(cpf_digitado):
            if valor > 0 and valor <= self._saldo:
                self._saldo -= valor
                return f'Saque de {valor} realizado! seu Novo saldo: {self._saldo}'
            else:
                return 'Valor de saque inválido.'
        else:
            return 'O conta CPF como  inválido. Operação não autorizada.'

    def _verificar_cpf(self, cpf_digitado):  
        return cpf_digitado == self._cpf

    def _verificar_saldo(self):  
        return f'Saldo atual: {self._saldo}'

 
conta1 = ContaBancaria(1000, "123.456.789-00")

conta1.depositar(100, "123.456.789-00")
conta1.sacar(100, "123.456.789-00")
print(conta1.sacar)
print(conta1._saldo)