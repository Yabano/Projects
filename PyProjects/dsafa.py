
# num_tita, altura_muro = map(int, input().split())
# ordem_tita = input()
# altura_tita_p, altura_tita_m, altura_tita_g = map(int, input().split())

# muros_construidos = 1
# altura_atual = altura_muro

# for tita in ordem_tita:
#     if tita == "P":
#         dano_muro = altura_tita_p
#     elif tita == "M":
#         dano_muro = altura_tita_m
#     else:
#         dano_muro = altura_tita_g

#     if dano_muro <= altura_atual:
#         altura_atual = altura_atual - dano_muro
        
#     else:
#         altura_atual = altura_muro - dano_muro
#         muros_construidos+=1

# print(muros_construidos)


# num_tita, x = map(int, input().split())
# titan_sizes = input()
# p, num_muros, g = map(int, input().split())

# walls_built = 1
# current_wall_height=x

# for titan_size in titan_sizes:
#     if titan_size == 'P':
#         if current_wall_height >= p:
#             current_wall_height -= p
#         else:
#             walls_built += 1
#             current_wall_height = (current_wall_height+x) - p
#     elif titan_size == 'M':
#         if current_wall_height >= num_muros:
#             current_wall_height -= num_muros
#         else:
#             walls_built += 1
#             current_wall_height = (current_wall_height+x) - num_muros
#     elif titan_size == 'G':
#         if current_wall_height >= g:
#             current_wall_height -= g
#         else:
#             walls_built += 1
#             current_wall_height = (current_wall_height+x) - g

# print(walls_built)



# num_tita, num_muros = map(int, input().split())
# tita_string = input()
# tita_p, tita_m, tita_g = map(int, input().split())

# v = [num_muros]
# tl = 1
# x = 0

# while num_tita > 0:
#     if tita_string[x] == 'P':
#         q = tita_p
#     elif tita_string[x] == 'M':
#         q = tita_m
#     else:
#         q = tita_g

#     v.sort()
#     meio = (tl - 1) // 2
#     i = 0

#     while i <= tl - 1 and v[meio] < q:
#         i = meio + 1
#         meio = (i + tl - 1) // 2

#     if i > tl - 1:
#         v.append(num_muros - q)
#         tl += 1
#     else:
#         v[meio] -= q

#     x += 1
#     num_tita -= 1

# print(tl)

num_tita, vida_muro = map(int, input().split())
titan_string = input()
tita_p, tita_m, tita_g = map(int, input().split())

lista_muros = [vida_muro]

i = 0

for titan in titan_string:

    if titan == "P":
        dano = tita_p
    

    elif titan == "M":
        dano = tita_m
    
    else: 
        dano = tita_g

    if dano > lista_muros[i]:
        lista_muros.append(vida_muro - dano)
        lista_muros.sort()
        i+=1

    else:
        x = 0
        while x <= len(lista_muros)-1:
            if lista_muros[x] >= dano:
                lista_muros[x] -= dano
            x+=1


print(len(lista_muros))