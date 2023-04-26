##5) Escreva um programa que inverta os caracteres de um string.

##IMPORTANTE:
##a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente 
##definida no código;
##b) Evite usar funções prontas, como, por exemplo, reverse;

string = 'SANDRO'
new_string = ""

for x in string.split():
    new_string = x[::-1]

print(new_string)