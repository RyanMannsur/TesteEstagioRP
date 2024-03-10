def inverter_string(texto):
    texto_invertido = ''
    for caractere in texto:
        texto_invertido = caractere + texto_invertido
    return texto_invertido

texto_original = input("Digite uma string: ")
texto_invertido = inverter_string(texto_original)
print('String invertida: {}' .format(texto_invertido))
