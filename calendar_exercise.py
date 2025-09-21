import calendar

class ValorIncorrecto(ValueError):
     def __init__(self, message):
         super().__init__(message)

class MiCalendario(calendar.Calendar):
    """Subclase de calendar.Calendar que cuenta cuántas veces ocurre
        un día de la semana en un año específico."""

    def __init__(self):
         super().__init__()

    def count_weekday_in_year(self, year, weekday):
        """Devuelve el número de veces que aparece un día de la semana (0=Lunes..6=Domingo)
            en un año dado. Lanza ValorIncorrecto si el weekday no está en el rango 0–6."""
            
        if weekday < 0 or weekday > 6:
            # Validamos que el día de la semana esté en el rango correcto
            raise ValorIncorrecto("*El valor debe estar entre 0 y 6*")
        
        contador = 0
        for mes in range(1, 13):
            # monthdays2calendar devuelve semanas -> listas de tuplas (día, weekday):
            for semana in self.monthdays2calendar(year, mes):
                #Anidamos bucles que recorrerán cada día de las diferentes semanas
                for dia, wd in semana:
                    if dia != 0 and wd == weekday: # descartamos días de relleno (0)
                        contador += 1
        return contador

if __name__ == "__main__":
    year = int(input("Introduce un año: "))
    weekday = int(input("Introduce un día de la semana en forma de número (donde 0 es Lunes y 6 Domingo): "))
    c = MiCalendario()
    print(c.count_weekday_in_year(year, weekday))
