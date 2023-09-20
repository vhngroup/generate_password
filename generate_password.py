# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:02:27 2023

@author: @Victor
"""

import secrets
import string

def crear_password(longitud):
  todo_caracteres = string.ascii_letters + string.digits + string.punctuation
  password =""
  print(longitud)
  for _ in range (longitud):
    password += secrets.choice(todo_caracteres)
  return password

try:
    longitud = int(input("Por favor ingrese la logitud de la contraseña: "))
except ValueError:
    print("Por favor solo ingrese numeros enteros....")

def main():
    nuevo_pass = crear_password(longitud)
    print("Se ha generado la contraseña: ", nuevo_pass)
    
if __name__ == "__main__":
    main()




