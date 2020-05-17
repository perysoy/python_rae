import requests
from bs4 import BeautifulSoup

from verbos.conjugacion import _conjugacion

def _comprobar_si_verbo(sopa):
    ''' Comprueba si la palabra de la rae es un verbo (Retorna True sino False).
    '''
    verbo = sopa.find('a', attrs={'class': 'e2'})
    if verbo is not None:
        return True
    else:
        return False

def _comprobar_si_existe(palabra):
    ''' Funcion que comprueba si la palabra existe en la RAE: Si existe devuelve la sopa
        si no existe devuelve False
    '''
    url = 'https://dle.rae.es/'
    response = requests.get(url+palabra)#, headers=headers)

    if response.status_code == 200: # todo ok
        sopa = BeautifulSoup(response.text, 'html.parser')

        resultados = sopa.find('div', attrs={'id': 'resultados'})

        aviso_relacionadas = 'Aviso: La palabra ' + palabra + ' no está en el Diccionario. La'
        aviso_relacionada2 = 'Entradas que contienen la forma'    # Para palabras como 'coletas' que devuelve esa cadena
        aviso_no_existe = 'Aviso: La palabra ' + palabra + ' no está en el Diccionario.'

        if resultados.text.startswith(aviso_relacionadas):   # no ha introducido bien la palabra y le da posibles
            lista = sopa.find('div', attrs={'class': 'item-list'})
            relacionadas = lista.select('div[class^=n1]')
            print(f'La palabra no existe tal vez queria decir: {relacionadas[0].text}')
            return False
        elif resultados.text.startswith(aviso_no_existe):
            print(f'No existe la palabra {palabra} en el diccionario')
            return False
        elif resultados.text.startswith(aviso_relacionada2) == True:   # cuando por ejemplo envias coletas esto muestra la web: Entradas que contienen la forma «coletas»:
            lista = resultados.find('div', attrs={'class': 'otras'})
            relacionadas = lista.select('div[class^=n1]')
            print(f'La palabra no existe tal vez queria decir: {relacionadas[0].text[:-1]}')
            return False
        else: return resultados # devuelve la sopa para encontrar la definicion


    else:
        return f'Error al cargar la pagina {response.status_code}'

def conjugar(verbo):
    ''' Funcion conjugar que devuelve una lista de diccionarios con el indicativo, subjuntivo, imperativo y formas no personales
        lo primero que tiene que hacer es comprobar si la palabra que va en el argumento existe (devuelve True comprobar_si_existe)
        segundo: si existe, comprobar que sea verbo
        tercero: si es verbo entonces ya devolver la lista de diccionarios
        Retorna False si no es un verbo la palabra
        Retorna lista de diccionarios con Indicativo, Subjuntivo, Imperativo y las formas no personales.
    '''
    url = 'https://dle.rae.es/'
    response = requests.get(url+verbo)#, headers=headers)
    if response.status_code == 200: # todo ok
        sopa = BeautifulSoup(response.text, 'html.parser')
        # if _comprobar_si_existe(verbo):
        if _comprobar_si_existe(verbo) is not False:
            if _comprobar_si_verbo(sopa):
                lista = _conjugacion(sopa)
                return lista
            else:
                return False
        else:
            # print(f'no existe')
            return False
    else:
        return f'error en cargar la pagina {response.status_code}'
    



def busqueda_rae(busqueda):
    ''' Función que devuelve una lista con las definiciones de la RAE
        Primero comprueba si la palabra existe (True si si, False si no)
        Segundo: Si es True devuelve una lista con las definiciones, si es False devuelve None
    '''
    comprobar = _comprobar_si_existe(busqueda)
    if comprobar is not False:
            articulo = comprobar.find('article')
            # cabecera = articulo.find('header')['title']  # Muestra: Definición de {busqueda}
            # latin = articulo.find('p', attrs={'class': 'n2'})   # proviene de:
            defins = articulo.select("p[class^=j]")   # ^es que empieza, si es * es que contiene
            definiciones = []
            for defin in defins:
                definiciones.append(defin.text)
            contiene_busqueda = articulo.select("p[class^=k]")  # Por ejemplo si buscamos árbol veremos lo que hace lo siguiente, y son las los parrafos k su clase empieza por k
            for opcion in contiene_busqueda:
                print(f'\n{opcion.text}:')
                print(opcion.find_next_sibling().text)  # muestra el siguiente elemento (find_next_sibling()) en este caso <p class='m' que es la definicion de opcion
            print(f'{definiciones}')
            return definiciones
    else: # Devuelve None
        return None

if __name__ == "__main__":
    busqueda_rae('amor')
    # print(conjugar('amar'))
