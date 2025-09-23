import calendar

class DiaIncorrecto(ValueError):
    def __init__(self, message):
        super().__init__(message)

class MiCalendario(calendar.Calendar):
    """Subclase de calendar.Calendar que cuenta cuántas veces ocurre
        un día de la semana en un año específico."""

    def __init__(self):
         super().__init__()

    def count_weekday_in_year(self, year, weekday):
        """Devuelve el número de veces que aparece un día de la semana (Lunes, Domingo, etc.)
            en un año dado. Lanza ValorIncorrecto si el weekday no es un día de la semana válido."""
        
        contador = 0
        for mes in range(1, 13):
            for semana in self.monthdays2calendar(year, mes):
                for dia, wd in semana:
                    if dia != 0 and wd == weekday:
                        contador += 1
        return contador
    
def testeador_dias_semana(dia_semana):
    if dia_semana not in dias_semana:
        raise DiaIncorrecto("Error. introduce un día de la semana válido.")
    
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

if __name__ == "__main__":
    year = int(input("Introduce un año: "))

    # Validación del input con while
    while True:
            try:
                dia_semana = input("Introduce el nombre de un día de la semana: ")
                dia_semana = dia_semana.strip().lower().capitalize()
                testeador_dias_semana(dia_semana)
                weekday = dias_semana.index(dia_semana)
                break
            except DiaIncorrecto as e:
                print(e)
                   
    c = MiCalendario()
    resultado = c.count_weekday_in_year(year, weekday)
    print(resultado)

