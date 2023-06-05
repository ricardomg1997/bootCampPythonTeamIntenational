
class BankAccount:
   
    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositing(self, valor):
        self.saldo = self.saldo + valor
        print(f"Operación exitosa, el valor del depósito fue: ${valor}. Tu nuevo saldo es $ {self.saldo}")
    
    def withdrawing(self, valor):
        self.saldo = self.saldo - valor
        print(f"Operación exitosa, el valor del retiro fue: ${valor}. Tu nuevo saldo es $ {self.saldo}, ")
       
    
    def account_balance(self):
        print(f"su saldo es: $ {self.saldo}")
      
    
client = BankAccount(20)
client.depositing(20)
client.withdrawing(5)
client.account_balance()