medias = []
qtd = 3
for i in range(qtd):
    temperaturas = list(map(int, input(f"Digite as temperaturas da Cidade {i+1}: ").split()))
    medias.append(sum(temperaturas)/len(temperaturas))

for i, media in enumerate(medias, 1):
    if media >=25:
        print(f"Cidade {i} possui um clima quente, com temperaturas média de: {media:.1f}°C. Utilizar roupas mais leves e refrescantes.")
    elif 16 <= media < 25:
        print(f"Cidade {i} possui um clima ameno, com temperaturas média de: {media:.1f}°C. O meio-termo é recomendado para a escolha de vestimenta.")
    else:
        print(f"Cidade {i} possui um clima frio, com temperaturas média de: {media:.1f}°C. Utilizar roupas mais quentes e que impeçam a entrada de brisa fria.")