from functions import *
import os
from dotenv import load_dotenv

load_dotenv()

Q1 = os.getenv("PERSON1")
Q2 = os.getenv("PERSON2")

if Q1 is None:
    raise EnvironmentError("Environment variable PERSON1 is not set.")
if Q2 is None:
    raise EnvironmentError("Environment variable PERSON2 is not set.")

p1 = BankAccount(Q1,5000)
p2 = BankAccount(Q2,3000)
print(p1.retrieveBalance())
print(p1.deposit(500))

print(p1.withdraw(5600))
print(p1.withdraw(300))
print(p1.transact(p2,500))
print(p2.retrieveBalance())
