import main

# Aqui vamos a demostrar  lo que pasa cuando llamamos con un import a nuestros modulos 
#print('example => ', main.data)
# -----output------
# Hola
# ['mex', 'Pe'] [400, 300]
# Que pais quieres ver => Mexico
# [{'Country': 'Mexico', 'Population': 600}]
# example =>  [{'Country': 'Mexico', 'Population': 600}, {'Country': 'Colombia', 'Population': 500}]

#arriba podemos   ver que basicamente estamos importando otros modulos aparte del que importamos y estamos activando todo el script cuando solo queremos una sola cosa 

print(main.data)
#aqui imprimimos la variable data, por lo que queriamos ir
main.run()
#aqui hacemos un print de la funcion que mueve todo el modulo 