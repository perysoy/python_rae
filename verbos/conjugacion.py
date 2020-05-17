from verbos.diccionarios import indicativo, subjuntivo, imperativo

def _conjugacion(sopa):
    ''' Requiere que comprobar_si_verbo devuelva True
        retorna una lista con 3 diccionarios: [indicativo, subjuntivo, imperativo]

    '''
    conjugacion = sopa.find('div', attrs={'id': 'conjugacion'})
    articulo = sopa.find('article')
    # cabecera = articulo.find('header')['title']  # Muestra: Conjugación de {busqueda}
    tabla = sopa.find('table')
    infinitivo = tabla.find(text='Infinitivo')  # infinitivo esta en la 4º columna de de la siguiente <tr> donde encontramos 'Infinitivo'
    cabecera_inf_ger = infinitivo.parent.parent  # la fila de Infinitivo  Gerundio (label)
    inf_ger = cabecera_inf_ger.find_next_sibling()
    dic_formas_no_personales = {}
    for celda in inf_ger:
        if celda.text=='':
            continue
        dic_formas_no_personales['infinitivo'] = celda.text
        dic_formas_no_personales['gerundio'] = celda.text
    # print(dic_formas_no_personales)
    participio = inf_ger.find_next_sibling().find_next_sibling()   # 2 <tr> (find_next_sibling()) para encontrar el participio
    dic_formas_no_personales['participio'] = participio.text
    # print(dic_formas_no_personales)
    
    fila_singular_primera_yo = participio.find_next_sibling().find_next_sibling().find_next_sibling()
    # print(fila_singular_primera_yo.find_all('td')[-2].text)
    
    indicativo['Presente']['Singular']['Primera']['yo'] = fila_singular_primera_yo.find_all('td')[-2].text
    indicativo['Copretérito']['Singular']['Primera']['yo'] = fila_singular_primera_yo.find_all('td')[-1].text
    fila_singular_primera_tu = fila_singular_primera_yo.find_next_sibling()
    indicativo['Presente']['Singular']['Segunda']['tú/vos'] = fila_singular_primera_tu.find_all('td')[-2].text
    indicativo['Copretérito']['Singular']['Segunda']['tú/vos'] = fila_singular_primera_tu.find_all('td')[-1].text
    fila_singular_primera_usted = fila_singular_primera_tu.find_next_sibling()
    indicativo['Presente']['Singular']['Segunda']['usted'] = fila_singular_primera_usted.find_all('td')[-2].text
    indicativo['Copretérito']['Singular']['Segunda']['usted'] = fila_singular_primera_usted.find_all('td')[-1].text
    fila_singular_tercera_el = fila_singular_primera_usted.find_next_sibling()
    indicativo['Presente']['Singular']['Tercera']['él, ella'] = fila_singular_tercera_el.find_all('td')[-2].text
    indicativo['Copretérito']['Singular']['Tercera']['él, ella'] = fila_singular_tercera_el.find_all('td')[-1].text
    fila_plural_primera_nosotros = fila_singular_tercera_el.find_next_sibling()
    indicativo['Presente']['Plural']['Primera']['nosotros, nosotras'] = fila_plural_primera_nosotros.find_all('td')[-2].text
    indicativo['Copretérito']['Plural']['Primera']['nosotros, nosotras'] = fila_plural_primera_nosotros.find_all('td')[-1].text
    fila_plural_segunda_vosotros = fila_plural_primera_nosotros.find_next_sibling()
    indicativo['Presente']['Plural']['Segunda']['vosotros, vosotras'] = fila_plural_segunda_vosotros.find_all('td')[-2].text
    indicativo['Copretérito']['Plural']['Segunda']['vosotros, vosotras'] = fila_plural_segunda_vosotros.find_all('td')[-1].text
    fila_plural_segunda_ustedes = fila_plural_segunda_vosotros.find_next_sibling()
    indicativo['Presente']['Plural']['Segunda']['ustedes'] = fila_plural_segunda_ustedes.find_all('td')[-2].text
    indicativo['Copretérito']['Plural']['Segunda']['ustedes'] = fila_plural_segunda_ustedes.find_all('td')[-1].text
    fila_plural_tercera_ellos = fila_plural_segunda_ustedes.find_next_sibling()
    indicativo['Presente']['Plural']['Tercera']['ellos, ellas'] = fila_plural_tercera_ellos.find_all('td')[-2].text
    indicativo['Copretérito']['Plural']['Tercera']['ellos, ellas'] = fila_plural_tercera_ellos.find_all('td')[-1].text
    # con esto hemos terminado el Indicativo presente y copreterito ahora tenemos que hacer 2 saltos de linea para hacver preterito y futuro simple
    # cabecera = articulo.find('header')['title']  # Muestra: Conjugación de {busqueda}
    # print(fila_singular_primera_yo)
    # for celda in fila_singular_primera_yo:
    #     try: 
    #         print(celda['data-g'])
    #     except KeyError:
    #         pass
    
    fila_singular_primera_yo = fila_plural_tercera_ellos.find_next_sibling().find_next_sibling()
    indicativo['Pretérito']['Singular']['Primera']['yo'] = fila_singular_primera_yo.find_all('td')[-2].text
    indicativo['Futuro']['Singular']['Primera']['yo'] = fila_singular_primera_yo.find_all('td')[-1].text
    fila_singular_primera_tu = fila_singular_primera_yo.find_next_sibling()
    indicativo['Pretérito']['Singular']['Segunda']['tú/vos'] = fila_singular_primera_tu.find_all('td')[-2].text
    indicativo['Futuro']['Singular']['Segunda']['tú/vos'] = fila_singular_primera_tu.find_all('td')[-1].text
    fila_singular_primera_usted = fila_singular_primera_tu.find_next_sibling()
    indicativo['Pretérito']['Singular']['Segunda']['usted'] = fila_singular_primera_usted.find_all('td')[-2].text
    indicativo['Futuro']['Singular']['Segunda']['usted'] = fila_singular_primera_usted.find_all('td')[-1].text
    fila_singular_tercera_el = fila_singular_primera_usted.find_next_sibling()
    indicativo['Pretérito']['Singular']['Tercera']['él, ella'] = fila_singular_tercera_el.find_all('td')[-2].text
    indicativo['Futuro']['Singular']['Tercera']['él, ella'] = fila_singular_tercera_el.find_all('td')[-1].text
    fila_plural_primera_nosotros = fila_singular_tercera_el.find_next_sibling()
    indicativo['Pretérito']['Plural']['Primera']['nosotros, nosotras'] = fila_plural_primera_nosotros.find_all('td')[-2].text
    indicativo['Futuro']['Plural']['Primera']['nosotros, nosotras'] = fila_plural_primera_nosotros.find_all('td')[-1].text
    fila_plural_segunda_vosotros = fila_plural_primera_nosotros.find_next_sibling()
    indicativo['Pretérito']['Plural']['Segunda']['vosotros, vosotras'] = fila_plural_segunda_vosotros.find_all('td')[-2].text
    indicativo['Futuro']['Plural']['Segunda']['vosotros, vosotras'] = fila_plural_segunda_vosotros.find_all('td')[-1].text
    fila_plural_segunda_ustedes = fila_plural_segunda_vosotros.find_next_sibling()
    indicativo['Pretérito']['Plural']['Segunda']['ustedes'] = fila_plural_segunda_ustedes.find_all('td')[-2].text
    indicativo['Futuro']['Plural']['Segunda']['ustedes'] = fila_plural_segunda_ustedes.find_all('td')[-1].text
    fila_plural_tercera_ellos = fila_plural_segunda_ustedes.find_next_sibling()
    indicativo['Pretérito']['Plural']['Tercera']['ellos, ellas'] = fila_plural_tercera_ellos.find_all('td')[-2].text
    indicativo['Futuro']['Plural']['Tercera']['ellos, ellas'] = fila_plural_tercera_ellos.find_all('td')[-1].text
    # con esto hemos terminado el Indicativo preterito y futuro ahora tenemos que hacer 2 saltos de linea para el ultimo dei ndicativo: postpreterito
    fila_singular_primera_yo = fila_plural_tercera_ellos.find_next_sibling().find_next_sibling()
    indicativo['PostPretérito']['Singular']['Primera']['yo'] = fila_singular_primera_yo.find_all('td')[-1].text
    fila_singular_primera_tu = fila_singular_primera_yo.find_next_sibling()
    indicativo['PostPretérito']['Singular']['Segunda']['tú/vos'] = fila_singular_primera_tu.find_all('td')[-1].text
    fila_singular_primera_usted = fila_singular_primera_tu.find_next_sibling()
    indicativo['PostPretérito']['Singular']['Segunda']['usted'] = fila_singular_primera_usted.find_all('td')[-1].text
    fila_singular_tercera_el = fila_singular_primera_usted.find_next_sibling()
    indicativo['PostPretérito']['Singular']['Tercera']['él, ella'] = fila_singular_tercera_el.find_all('td')[-1].text
    fila_plural_primera_nosotros = fila_singular_tercera_el.find_next_sibling()
    indicativo['PostPretérito']['Plural']['Primera']['nosotros, nosotras'] = fila_plural_primera_nosotros.find_all('td')[-1].text
    fila_plural_segunda_vosotros = fila_plural_primera_nosotros.find_next_sibling()
    indicativo['PostPretérito']['Plural']['Segunda']['vosotros, vosotras'] = fila_plural_segunda_vosotros.find_all('td')[-1].text
    fila_plural_segunda_ustedes = fila_plural_segunda_vosotros.find_next_sibling()
    indicativo['PostPretérito']['Plural']['Segunda']['ustedes'] = fila_plural_segunda_ustedes.find_all('td')[-1].text
    fila_plural_tercera_ellos = fila_plural_segunda_ustedes.find_next_sibling()
    indicativo['PostPretérito']['Plural']['Tercera']['ellos, ellas'] = fila_plural_tercera_ellos.find_all('td')[-1].text
    
    # ahora subjuntivo
    fila_singular_primera_yo = fila_plural_tercera_ellos.find_next_sibling().find_next_sibling().find_next_sibling()
    subjuntivo['Presente']['Singular']['Primera']['yo'] = fila_singular_primera_yo.find_all('td')[-2].text
    subjuntivo['Futuro']['Singular']['Primera']['yo'] = fila_singular_primera_yo.find_all('td')[-1].text
    fila_singular_primera_tu = fila_singular_primera_yo.find_next_sibling()
    subjuntivo['Presente']['Singular']['Segunda']['tú/vos'] = fila_singular_primera_tu.find_all('td')[-2].text
    subjuntivo['Futuro']['Singular']['Segunda']['tú/vos'] = fila_singular_primera_tu.find_all('td')[-1].text
    fila_singular_primera_usted = fila_singular_primera_tu.find_next_sibling()
    subjuntivo['Presente']['Singular']['Segunda']['usted'] = fila_singular_primera_usted.find_all('td')[-2].text
    subjuntivo['Futuro']['Singular']['Segunda']['usted'] = fila_singular_primera_usted.find_all('td')[-1].text
    fila_singular_tercera_el = fila_singular_primera_usted.find_next_sibling()
    subjuntivo['Presente']['Singular']['Tercera']['él, ella'] = fila_singular_tercera_el.find_all('td')[-2].text
    subjuntivo['Futuro']['Singular']['Tercera']['él, ella'] = fila_singular_tercera_el.find_all('td')[-1].text
    fila_plural_primera_nosotros = fila_singular_tercera_el.find_next_sibling()
    subjuntivo['Presente']['Plural']['Primera']['nosotros, nosotras'] = fila_plural_primera_nosotros.find_all('td')[-2].text
    subjuntivo['Futuro']['Plural']['Primera']['nosotros, nosotras'] = fila_plural_primera_nosotros.find_all('td')[-1].text
    fila_plural_segunda_vosotros = fila_plural_primera_nosotros.find_next_sibling()
    subjuntivo['Presente']['Plural']['Segunda']['vosotros, vosotras'] = fila_plural_segunda_vosotros.find_all('td')[-2].text
    subjuntivo['Futuro']['Plural']['Segunda']['vosotros, vosotras'] = fila_plural_segunda_vosotros.find_all('td')[-1].text
    fila_plural_segunda_ustedes = fila_plural_segunda_vosotros.find_next_sibling()
    subjuntivo['Presente']['Plural']['Segunda']['ustedes'] = fila_plural_segunda_ustedes.find_all('td')[-2].text
    subjuntivo['Futuro']['Plural']['Segunda']['ustedes'] = fila_plural_segunda_ustedes.find_all('td')[-1].text
    fila_plural_tercera_ellos = fila_plural_segunda_ustedes.find_next_sibling()
    subjuntivo['Presente']['Plural']['Tercera']['ellos, ellas'] = fila_plural_tercera_ellos.find_all('td')[-2].text
    subjuntivo['Futuro']['Plural']['Tercera']['ellos, ellas'] = fila_plural_tercera_ellos.find_all('td')[-1].text    
    # acabamos con presente y futuro del subjuntivo ahora vamos con el ultimo tiempo del subjuntivo: preterito

    fila_singular_primera_yo = fila_plural_tercera_ellos.find_next_sibling().find_next_sibling()
    # print(fila_singular_primera_yo)

    subjuntivo['Pretérito']['Singular']['Primera']['yo'] = fila_singular_primera_yo.find_all('td')[-1].text
    fila_singular_primera_tu = fila_singular_primera_yo.find_next_sibling()
    subjuntivo['Pretérito']['Singular']['Segunda']['tú/vos'] = fila_singular_primera_tu.find_all('td')[-1].text
    fila_singular_primera_usted = fila_singular_primera_tu.find_next_sibling()
    subjuntivo['Pretérito']['Singular']['Segunda']['usted'] = fila_singular_primera_usted.find_all('td')[-1].text
    fila_singular_tercera_el = fila_singular_primera_usted.find_next_sibling()
    subjuntivo['Pretérito']['Singular']['Tercera']['él, ella'] = fila_singular_tercera_el.find_all('td')[-1].text
    fila_plural_primera_nosotros = fila_singular_tercera_el.find_next_sibling()
    subjuntivo['Pretérito']['Plural']['Primera']['nosotros, nosotras'] = fila_plural_primera_nosotros.find_all('td')[-1].text
    fila_plural_segunda_vosotros = fila_plural_primera_nosotros.find_next_sibling()
    subjuntivo['Pretérito']['Plural']['Segunda']['vosotros, vosotras'] = fila_plural_segunda_vosotros.find_all('td')[-1].text
    fila_plural_segunda_ustedes = fila_plural_segunda_vosotros.find_next_sibling()
    subjuntivo['Pretérito']['Plural']['Segunda']['ustedes'] = fila_plural_segunda_ustedes.find_all('td')[-1].text
    fila_plural_tercera_ellos = fila_plural_segunda_ustedes.find_next_sibling()
    subjuntivo['Pretérito']['Plural']['Tercera']['ellos, ellas'] = fila_plural_tercera_ellos.find_all('td')[-1].text
    # con esto se acabo del subjuntivo ahora falta el imperativo

    fila_singular_segunda_tu = fila_plural_tercera_ellos.find_next_sibling().find_next_sibling().find_next_sibling()
    imperativo['Singular']['Segunda']['tú/vos']  = fila_singular_segunda_tu.find_all('td')[-1].text
    fila_singular_segunda_usted = fila_singular_segunda_tu.find_next_sibling()
    imperativo['Singular']['Segunda']['usted'] = fila_singular_segunda_usted.find_all('td')[-1].text
    fila_plural_segunda_vosotros = fila_singular_segunda_usted.find_next_sibling()
    imperativo['Plural']['Segunda']['vosotros, vosotras'] = fila_plural_segunda_vosotros.find_all('td')[-1].text
    fila_plural_segunda_ustedes = fila_plural_segunda_vosotros.find_next_sibling()
    imperativo['Plural']['Segunda']['ustedes'] = fila_plural_segunda_ustedes.find_all('td')[-1].text

    
    return [ {'indicativo': indicativo}, {'subjuntivo': subjuntivo} , {'imperativo': imperativo}, {'formas_no_personales': dic_formas_no_personales} ]
