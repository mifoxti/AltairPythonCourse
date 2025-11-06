class BankAccount:
    """Класс банковского счета - пример абстракции и инкапсуляции"""

    def __init__(self, account_holder, initial_balance=0):
        # Публичный атрибут - доступны извне
        self.account_holder = account_holder

        # Защищенные атрибуты (одно подчеркивание) - внутренняя реализация
        self._balance = initial_balance
        self._transaction_history = []

        # Приватный атрибут
        self.__account_id = self.__generate_account_id()

    def __generate_account_id(self):
        """Приватный метод - генерирует id счета"""
        return f"ACC{id(self) % 10000:04d}"

    def deposit(self, amount):
        """Публичный метод - пополнение счета"""
        if amount > 0:
            self._balance += amount
            self._add_transaction(f"Deposit: +{amount}")
            return True
        return False

    def withdraw(self, amount):
        """Публичная функция для снятия средств"""
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._add_transaction(f"Withdraw: -{amount}")
            return True
        return False

    def _add_transaction(self, message):
        """Защищенная функция - внутренняя логика"""
        self._transaction_history.append(message)

    def get_balance(self):
        """Публичный метод - контролируемый доступ к балансу"""
        return self._balance

    def get_account_info(self):
        """Публичный метод - безопасный доступ к информации"""
        return {
            'holder': self.account_holder,
            'balance': self._balance,
            'account': self.__account_id # Доступ изнутри класса разрешен
        }


# Использование
account = BankAccount("Ученик Альтаира", 1000)

# Публичные методы - работаем с ними
account.deposit(1000)
account.withdraw(200)

# Публичные атрибуты - доступны
print(f"Владелец: {account.account_holder}")

# Защищенный атрибуты - технически доступны, но использоваться не должны
print(f"Баланс (через _balance): {account._balance}") # Так делать не стоит

# Приватные атрибуты - доступ запрещен
# print(account.__account_id)
print(f"Информация: {account.get_account_info()}")