# Funcion para obtener una Ferrari por su ID
def filtrar_por_id(data, id):
   
    # Asignamos el valor de id y lo convertimos a string para la comparación
    auto_id_param = id

    # Recorro el JSON
    for ferrari in data:
        
        # Obtenemos el id de la Ferrari de turno
        current_id = ferrari['id']

        # Validamos si coincide con la ID buscada
        if current_id == auto_id_param:
            return ferrari # Si es asi devuelvo la Ferrari encontrada

    # Si el bucle termina sin encontrar una coincidencia, devolvemos None
    return None
  
# Funcion para obtener una Ferrari por su modelo
def filtrar_por_modelo(data, model):
    
    modelo_param = f"Ferrari {model}".lower()

    # Recorremos el JSON 
    for ferrari in data:
     
     # Por cada ferrari obtenemos el 'modelo' de la Ferrari de turno
     modelo_auto = ferrari['modelo'].lower()

     # Validamos si la Ferrari de turno coincide con el modelo buscado
     if modelo_param == modelo_auto:
      return ferrari # Si es asi devolvemos la Ferrari encontrada

    # Si el bucle termina sin encontrar una coincidencia, devolvemos None
    return None 

# Funcion para obtener una Ferrari por su año de creación
def filtrar_por_anio(data, year):
    
    anio_param = year

     # Recorremos el JSON 
    for ferrari in data:
     
     # Por cada ferrari obtenemos el 'modelo' de la Ferrari de turno
     anio_auto = ferrari['anio']

     # Validamos si la Ferrari de turno coincide con el modelo buscado
     if anio_param == anio_auto:
      return ferrari # Si es asi devolvemos la Ferrari encontrada

    # Si el bucle termina sin encontrar una coincidencia, devolvemos None
    return None 

# Funcion para filtrar por tipos
def filtrar_por_tipo(data, tipo):
    
    tipo_param = tipo.lower()

    # Se crea una lista filtrada de Ferraris
    ferraris_filtradas = []

    # Recorremos el JSON 
    for ferrari in data:
    
     # Validamos si la Ferrari de turno tiene el mismo valor de tipo de auto que el buscado
     if ferrari['tipo_de_automovil'].lower() == tipo_param:
      ferraris_filtradas.append(ferrari)

    return ferraris_filtradas

# Funcion para filtrar por caballos de fuerza
def filtrar_por_caballos(data, caballos):
    
    caballos_param = caballos

    # Se crea una lista filtrada de Ferraris
    ferraris_filtradas = []

    # Recorremos el JSON 
    for ferrari in data:
    
     # Validamos si la Ferrari de turno tiene el mismo valor de caballos de fuerza que el buscado
     if ferrari['caballos_de_fuerza'] == caballos_param:
      ferraris_filtradas.append(ferrari)

    return ferraris_filtradas

# Funcion para filtrar por velocidad
def filtrar_por_velocidad(data, velocidad):
    
    velocidad_param = velocidad

    # Se crea una lista filtrada de Ferraris
    ferraris_filtradas = []

    # Recorremos el JSON 
    for ferrari in data:
    
     # Validamos si la Ferrari de turno tiene el mismo valor de velocidad que el buscado
     if ferrari['velocidad_maxima'] == velocidad_param:
      ferraris_filtradas.append(ferrari)

    return ferraris_filtradas

# Funcion para filtrar por aceleración
def filtrar_por_aceleracion(data, aceleracion):
    
    aceleracion_param = aceleracion

    # Se crea una lista filtrada de Ferraris
    ferraris_filtradas = []

    # Recorremos el JSON 
    for ferrari in data:
    
     # Validamos si la Ferrari de turno tiene el mismo valor de aceleración que el buscado
     if ferrari['aceleracion'] == aceleracion_param:
      ferraris_filtradas.append(ferrari)

    return ferraris_filtradas

# Función para filtrar por un rango de años
def filtra_por_rango_anios(data, min_year, max_year):
    
    min_year_param = min_year
    max_year_param = max_year
    
    # Lista donde almacenaremos los Ferraris filtrados
    ferraris_filtradas = []

    # Recorremos el JSON de Ferraris
    for ferrari in data:
        # Validamos si el año del Ferrari está dentro del rango
        if min_year_param <= ferrari['anio'] <= max_year_param:
            ferraris_filtradas.append(ferrari)

    # Retornamos la lista filtrada después de recorrer todos los elementos
    return ferraris_filtradas

# Función para filtrar por un rango de velocidad
def filtra_por_rango_velocidad(data, min_velocidad, max_velocidad):
    # Se crea una lista filtrada de Ferraris
    ferraris_filtradas = []

    # Recorremos el JSON
    for ferrari in data:
        # Validamos si la velocidad del auto está entre el rango
        if min_velocidad <= ferrari['velocidad_maxima'] <= max_velocidad:
            ferraris_filtradas.append(ferrari)

    # Retornamos la lista completa filtrada
    return ferraris_filtradas
  
# Función para filtrar por un rango de caballos de fuerza
def filtra_por_rango_caballos(data, min_hp, max_hp):
  
  #Asignamos los valores de caballos de fuerza
  hp_max_param = max_hp
  hp_min_param = min_hp

  # Se crea una lista filtrada de Ferraris
  ferraris_filtradas = []

  # Recorremos el JSON
  for ferrari in data:
    # Validamos si los caballos de fuerza del auto esta entre el rango
    if hp_min_param <= ferrari['caballos_de_fuerza'] and ferrari['caballos_de_fuerza'] <= hp_max_param:
        ferraris_filtradas.append(ferrari)

  # Retornamos la lista completa filtrada      
  return ferraris_filtradas
  
# Función para filtrar por un rango de aceleracion
def filtra_por_rango_aceleracion(data, min_aceleracion, max_aceleracion):
  
  #Asignamos los valores 
  aceleracion_max_param = max_aceleracion
  aceleracion_min_param = min_aceleracion

  # Se crea una lista filtrada de Ferraris
  ferraris_filtradas = []

  # Recorremos el JSON
  for ferrari in data:
    # Validamos si la aeleracion del auto esta entre el rango
    if aceleracion_min_param <= ferrari['aceleracion'] and ferrari['aceleracion'] <= aceleracion_max_param:
        ferraris_filtradas.append(ferrari)

  # Retornamos la lista completa filtrada       
  return ferraris_filtradas
    