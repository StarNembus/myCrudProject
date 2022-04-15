# Создайте класс банковского счета, который имеет 2 атрибута:
# owner - владелец
# balance - баланс

# и два метода:
#  deposit - депозит
# withdraw - снять средства

# Сумма снятия не должна превышать доступный баланс
# Создайте инстанс класса, сделайте несколько внесений и снятий средств,
# а также проверьте, что баланс счета не должен уходить в минус при снятии средств

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Владелец счета: {self.owner}\nБаланс счета: ${self.balance}'

    def deposit(self, amt):
        self.amt = amt
        # прибавляем к текущему значению указанную сумму
        self.balance += amt
        print(f'Внесение выполнено, внесено {self.amt}')

    def withdraw(self, wd_amt):
        self.wd_amt = wd_amt
        if self.balance >= wd_amt:
            self. balance -= wd_amt
            print(f'Снятие выполнено {self.wd_amt}')
        else:
            print(f'Недостаточно средств')



# Создаем инстанс класса
acct = Account('Влад', 100)

# Выводим информацию об объекте
print(acct)

# Отображаем атрибут объекта владельца
print(acct.owner)

# Отображаем атрибут баланса счета
print(acct.balance)

# Выполняем несколько внесений и снятий средств
print(acct.deposit(50))


print(acct.withdraw(75))

# Пытаемся выполнить снятие, которое превышает баланс
print(acct.withdraw(500))

