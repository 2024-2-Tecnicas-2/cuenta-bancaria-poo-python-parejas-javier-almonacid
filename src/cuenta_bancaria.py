class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo):
        self._titular = titular
        self._numero_cuenta = numero_cuenta
        self._saldo = saldo
        self._tipo_interes = 0  # Tipo de interés en porcentaje
 
    def get_titular(self):
        return self._titular
 
    def set_titular(self, titular):
        self._titular = titular
 
    def get_numero_cuenta(self):
        return self._numero_cuenta
 
    def get_saldo(self):
        return self._saldo
 
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
 
    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
 
    def set_tipo_interes(self, tipo_interes):
        if tipo_interes >= 0:
            self._tipo_interes = tipo_interes
 
    def calcular_interes(self):
        return self._saldo * self._tipo_interes / 100