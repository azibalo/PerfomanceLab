def GetNumSystem():
   while True:
      numSystem = input('Выберите систему исчисления: BIN, OCT, DEC, HEX\n')
      if numSystem == 'BIN':
         return 2
      elif numSystem == 'OCT':
         return 8
      elif numSystem == 'DEC':
         return 10
      elif numSystem == 'HEX':
         return 16

# Функция перевода из двоичной системы
def ConvertFromBin(_value, _numSystem):
   if _numSystem == 2:
      return _value
   elif _numSystem == 8:
      return oct(int(_value, 2))
   elif _numSystem == 10:
      return int(_value, 2)
   elif _numSystem == 16:
      return hex(int(_value, 2))


# Функция перевода из восьмеричной системы
def ConvertFromOct(_value, _numSystem):
   if _numSystem == 2:
      return bin(int(_value, 8))
   elif _numSystem == 8:
      return _value
   elif _numSystem == 10:
      return int(_value, 8)
   elif _numSystem == 16:
      return hex(int(_value, 8))


# Функция перевода из десятичной системы
def ConvertFromDec(_value, _numSystem):
   if _numSystem == 2:
      return bin(int(_value))
   elif _numSystem == 8:
      return oct(int(_value))
   elif _numSystem == 10:
      return int(_value)
   elif _numSystem == 16:
      return hex(int(_value))


# Функция перевода из шестнадцатиричной системы
def ConvertFromHex(_value, _numSystem):
   if _numSystem == 2:
      return bin(int(_value, 16))
   elif _numSystem == 8:
      return oct(int(_value, 16))
   elif _numSystem == 10:
      return int(_value, 16)
   elif _numSystem == 16:
      return _value


def main():
   print('Исходная система исчисления:')
   fNumSystem = GetNumSystem()  # Получаем исходную систему исчисления
   value = input('Введите значение: ')  # Получаем исходное число
   print('Система исчисления в которую необходимо перевести число:')
   sNumSystem = GetNumSystem()  # Получаем систему исчисления в которую необходимо перевести
   if fNumSystem == 2:
      print(ConvertFromBin(value, sNumSystem))
   elif fNumSystem == 8:
      print(ConvertFromOct(value, sNumSystem))
   elif fNumSystem == 10:
      print(ConvertFromDec(value, sNumSystem))
   elif fNumSystem == 16:
      print(ConvertFromHex(value, sNumSystem))
   elif fNumSystem == "":
      print(ConvertFromDec(value, sNumSystem))

main()