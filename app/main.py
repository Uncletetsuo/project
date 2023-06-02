import utils
import random  #modulo que esta dentro de
#Cualquier archivo en python se considera un modulo, tambien hay modulos dentro del lenguaje de programacion instalado en los binarios de la computadora
import read_csv
import charts
import pandas as pd 

def run():
#new structure with pandas
    data = pd.read_csv('/app/data.csv')
    data = data[data['Continent'] == 'Asia']
    countries = data['Country/Territory'].values
    percentages = data['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentages)
    
    #data2 = pd.read_csv('/home/fercs/Documents/Project/app/data.csv')
    data2 = read_csv.read_csv('/app/data.csv')
    country = str(input('Que pais quieres ver => '))
    result = utils.population_by_country(data2, country)
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)
    #old structure without pandas
    # data = read_csv.read_csv('/home/fercs/Documents/Project/app/data.csv')
    # countries = list(map(lambda x: x['Country/Territory'], data))
    # percentages = list(map(lambda x: x['World Population Percentage'], data))
    # charts.generate_pie_chart(countries, percentages)

# tambien podemos acceder a un metodo o funcion especifica con:Cambo
# from human import man

if __name__ == '__main__':
    run()

#gracias a este entry point, este modulo sigue sirviendo por separado, a que me refiero, no necesitas de example para poder correr el modulo, la misma terminal
# puede activar la funcion