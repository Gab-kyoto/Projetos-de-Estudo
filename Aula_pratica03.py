nomes = []
idades = []
sexos = []
dados = []
cadastros = 0
media = 0
encerrar = 'não definido ainda'
mulher_menos_30 = 0
homem_acima_media = 0
while encerrar != "n":
    nome = input("Qual seu nome? ")
    nomes.append(nome)
    idade = 2024 - int(input("Qual seu ano de nascimento? "))
    idades.append(idade)
    print("Qual seu sexo?")
    sexo = input("homem/mulher ").lower()
    sexos.append(sexo)
    dados.append([nomes, idades, sexos])
    print(dados , end= " ")
    print("Deseja cadastrar mais alguém? ")
    if sexo == "mulher" and idade <=30:
        mulher_menos_30 += 1
    elif sexo == "homem" and idade > media:
        homem_acima_media += 1
    cadastros += 1
    encerrar = input("s/n")
media = sum(idades) / len(idades)
print(f"Total de cadastros: {cadastros}")
print(f"Media das idades: {media}")
print(f"Mulheres abaixo dos 30 anos: {mulher_menos_30}")
print(f"Homens acima da media: {homem_acima_media}")