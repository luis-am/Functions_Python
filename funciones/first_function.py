# def multiplicar():
#     result = 10.5 * 4
#     return result
#
# respuesta = multiplicar()
# print(respuesta)

# def multiplicar(x,y):
#     resultado = x * y
#     return resultado
#
# print(multiplicar(10.5,4))
#
# print()
#
# for val in range(1,5):
#     resultado = multiplicar(2, val)
#     print(resultado)

# def is_palindrome(string):
#     # backwards = string[::-1]
#     # return backwards == string
#     return string[::-1] == string


# word = input("Please enter a word: ")
# if is_palindrome(word.casefold()):
#     print(f"{word} is a palindromo.")
# else:
#     print(f"{word} is not a palindromo.")



def is_palindromo(word):
    return word[::-1].casefold() == word.casefold()


def oracion_palindromo(oracion):
    string = ""
    for char in oracion:
        if char.isalnum():
            string += char
        else:
            continue
    return is_palindromo(string)


oracion = input("Ingresa una palabra u oracion: ")
if oracion_palindromo(oracion):
    print("Es palindromo.")
else:
    print("No es palindromo.")

print(oracion_palindromo(oracion))