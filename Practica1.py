class Engine:
  """
  Definicion de la clase Engine que representa el motor de un vehículo
  """
  def __init__ (self, _type, potency, weight): # El constructor de la clase Engine, que inicializa los atributos del motor.
    self._type = _type     # Tipo de motor, es un atributo protegido.
    self.potency = potency # Potencia del motor en caballos de fuerza.
    self.weight = weight   # Peso del motor en kilogramos.

class Vehicle:
  """
  Definición de la clase base Vehicle, que inicializa los atributos comunes de todos los vehiculos.
  """
def __init__(self, engine, chassis, model, year): # El constructor de la clase Vehicle que inicializa los atributos comunes de todos los Vehiculos.
        self.engine = engine    # Instancia de Engine que representa el motor de vehiculo.
        self.chassis = chassis  # Tipo de chasis del vehiculo.
        self.model = model      # Modelo del vehiculo.
        self.year = year        # Año de fabricación del vehículo.
        self.gas_consumption = self.calculate_gas_consumption()    #llamada al método para calcular el consumo de gasolina al crear el objeto.

def calculate_gas_consumption(self):      # Método para calcular el consumo de gasolina del vehiculo.
        chassis_factor = 0.3 if self.chassis == 'A' else 0.5      # Factor de ajuste basado en el tipo de chasis.
        return 1.1 * self.engine.potency + 0.2 * self.engine.weight - chassis_factor    # Fórmula para calcular el consumo de gasolina.

class Car(Vehicle):      # Clase Car que hereda Vehicle y representa un automovil.
    def __init__(self, engine, chassis, model, year, doors):   # Constructor de la clase Carm que añade el atributo especifico 'doors'.
        super().__init__(engine, chassis, model, year)         # Llamada al constructor de la superclase.
        self.doors = doors          # Número de puertas del automovil.

class Truck(Vehicle):      # Clase Truck que hereda de Vehicle y representa un camión.
    def __init__(self, engine, chassis, model, year, cargo_capacity):        # Constructor de la clase Truck, que añade el atributo específico 'cargo_capacity'.
        super().__init__(engine, chassis, model, year)  # Llamada al constructor de la superclase.
        self.cargo_capacity = cargo_capacity        # Capacidad de carga del camión en kilogramos.

class Yacht(Vehicle):     # Clase Truck que hereda de Vehicle y representa un Yate.
  def __init__(self, engine, chassis, model, year, lenght):     # Constructor de la clase Yatch, que añade el atributo específico 'lenght'.
    super().__init__(engine, chassis, model, year)              # Llamada al constructor de la superclase.
    self.lenght = lenght      # Longitud del Yate en metros.

class Motorcycle(Vehicle):  # Clase Motorcycle que hereda de Vehicle y representa un motocicleta.
  def __init__(self, engine, chassis, model, year, has_sidecar):     # Constructor de la clase Motorcycle, que añade el atributo específico 'has_sidecar'.
    super().__init__(engine, chassis, model, year)          # Llamada al constructor de la superclase.
    self.has_sidecar = has_sidecar      # Booleano que indica si la motocicleta tiene sidecar.

def create_vehicle():     # Función para crear un vehículo basado en la entrada del usuario.
    vehicle_type = input("Ingrese el tipo de vehículo (Car, Truck, Yacht, Motorcycle): ")       # Se le solicita al usuario el tipo de vehículo y los detalles del motor y chasis.
    engine_type = input("Ingrese el tipo de motor: ")
    potency = float(input("Ingrese la potencia del motor: "))
    weight = float(input("Ingrese el peso del motor: "))
    chassis = input("Ingrese el chasis (A o B): ")
    model = input("Ingrese el modelo: ")
    year = int(input("Ingrese el año: "))

    engine = Engine(engine_type, potency, weight)     # Crea una instancia de Engine con los datos proporcionados. 

    if vehicle_type.lower() == 'car':
        doors = int(input("Ingrese el número de puertas: "))
        return Car(engine, chassis, model, year, doors)

    elif vehicle_type.lower() == 'truck':
        cargo_capacity = float(input("Ingrese la capacidad de carga: "))
        return Truck(engine, chassis, model, year, cargo_capacity)

    elif vehicle_type.lower() == 'yacht':
        length = float(input("Ingrese la longitud: "))
        return Yacht(engine, chassis, model, year, length)

    elif vehicle_type.lower() == 'motorcycle':
        has_sidecar = input("¿Tiene sidecar? (Sí/No): ").lower() == 'sí'
        return Motorcycle(engine, chassis, model, year, has_sidecar)
    else:
        print("Tipo de vehículo no reconocido.")
        return None

def main_menu():        # Función principal que muestra el menú y permite al usuario interactuar con el programa.
    vehicles = []       # Lista para almacenar los vehículos creados.

    while True:         # Bucle principal del menú.
        print("Menú principal:")
        print("1. Crear un nuevo vehículo")
        print("2. Ver todos los vehículos")
        print("3. Salir")
        option = input("Seleccione una opción: ")

        if option == '1':    # Opciones del menú para crear vehículos, ver la lista de vehículos o salir del programa.
            vehicle = create_vehicle()
            if vehicle:
                vehicles.append(vehicle)
                print("Vehículo creado exitosamente.")
        elif option == '2':
            for vehicle in vehicles:
                print(f"{vehicle.__class__.__name__} - Modelo: {vehicle.model}, Año: {vehicle.year}, Consumo de gasolina: {vehicle.gas_consumption}L")
        elif option == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":        # Punto de entrada del programa.
    main_menu()