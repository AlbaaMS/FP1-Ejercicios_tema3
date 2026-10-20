from datetime import date, timedelta

def es_dia_festivo(fecha: date) -> bool:
    """
    Verifica si una fecha corresponde a un día festivo recurrente (ignora el año).
    
    Parámetros:
        fecha (date): La fecha a verificar.
        
    Devuelve:
        bool: True si el mes y día coinciden con un festivo, False en caso contrario.
    """    
    dias_festivos = {
        (1, 1),    # Año Nuevo
        (1, 6),    # Día de Reyes
        (3, 19),   # San José
        (5, 1),    # Día del Trabajo
        (8, 15),   # Asunción de la Virgen
        (10, 12),  # Fiesta Nacional de España
        (11, 1),   # Todos los Santos
        (12, 6),   # Día de la Constitución
        (12, 8),   # Inmaculada Concepción
        (12, 25)   # Navidad
    }
    
    return (fecha.month, fecha.day) in dias_festivos

def es_dia_no_laborable(fecha:date) -> bool:
    '''
    Devuelve True si la fecha es fin de semana o festivo
    '''
    dia_semana= fecha.weekday()
    return (dia_semana == 5 or dia_semana == 6) or es_dia_festivo(fecha) 

def calcular_siguiente_valida(fecha, dias):
    '''
    Recibe la fecha de la última ocurrencia  y un intervalo en días. 
    Calcula la próxima fecha sumando el intervalo. 
    Si la fecha resultante cae en un día no laborable, la función debe avanzar día a día hasta encontrar el siguiente día laborable, devolviendo esta fecha.
    '''
    fecha = fecha + timedelta(days = dias)
    while es_dia_no_laborable(fecha):
        fecha = fecha + timedelta(days=1)
    return fecha


def planificar_eventos(inicio: date, intervalo_dias: int, num_eventos: int) -> tuple[int, date]:
    '''
    Recibe una fecha_inicio para los eventos, un intervalo_dias (días entre cada dos eventos) y el número de eventos en total a planificar (número entero num_eventos). 
    Genera y muestra por pantalla las fechas para cada uno de los eventos.
    '''
    print(f"--- Planificación de {num_eventos} eventos recurrentes (Intervalo: {intervalo_dias} días) ---")
    
    if es_dia_no_laborable(inicio):
        inicio = calcular_siguiente_valida(inicio,dias=10)
        
    num_evento = 1
    
    while num_eventos > 0:
        inicio = calcular_siguiente_valida(inicio, dias=10)
        print(f"Evento {num_evento}: {inicio}")
        
        inicio += timedelta(days=intervalo_dias)
        num_evento += 1
        num_eventos -= 1
        
    return num_eventos, inicio
planificar_eventos(date(2026, 1, 1), timedelta(10),5)
