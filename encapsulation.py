class bank_account:
  __password = "" #private attribute
  def __init__(self, password):
    self.__password = password

obj = bank_account(23416)
print(obj.__password)
