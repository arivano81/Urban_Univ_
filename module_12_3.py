import threading
import random
from time import sleep


class Bank(threading.Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.tarnsaction_count = 100
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(self.tarnsaction_count):
            if self.balance < 500:
                try:
                    self.lock.release()
                except Exception:
                    pass
                finally:
                    amount = random.randint(50, 100)
                    self.balance += amount
                    print(f'Пополнение: {amount}. Баланс: {self.balance}')
                    sleep(0.001)

    def take(self):
        for i in range(self.tarnsaction_count):
            amout = random.randint(50, 100)
            print(f'Запрос на {amout}.')
            if amout < self.balance:
                self.balance -= amout
                print(f'Снятие: {amout}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
