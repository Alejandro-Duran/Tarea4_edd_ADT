class Trabajadores:
    def __init__( self, numero_trabajador, nombre, paterno, materno, h_extra, s_base, año_ingreso):
        self.__numero_trabajador = numero_trabajador
        self.__nombre = nombre
        self.__paterno = paterno
        self.__materno = materno
        self.__h_extra = h_extra
        self.__s_base = s_base
        self.__año_ingreso = año_ingreso

    def set_numero_trabajador(self,numero_trabajador):
        self.__numero_trabajador = numero_trabajador
    def get_numero_tabajador(self):
        return self.__numero_trabajador

    def set_nombre(self,nombre):
        self.__nombre = nombre
    def get_nombre(self):
        return self.__nombre

    def set_paterno(self,paterno):
        self.__paterno = paterno
    def get_paterno(self):
        return self.__paterno

    def set_materno(self,materno):
        self.__materno = materno
    def get_materno(self):
        return self.__materno

    def set_h_extra(self,h_extra):
        self.__h_extra = h_extra
    def get_h_extra(self):
        return self.__h_extra

    def set_s_base(self,s_base):
        self.__s_base = s_base
    def get_s_base(self):
        return self.__s_base

    def set_año_ingreso(self,año_ingreso):
        self.__año_ingreso = año_ingreso
    def get_año_ingreso(self):
        return self.__año_ingreso

    def to_string(self):
        return "Numero: "+self.__numero_trabajador+", Nombre: "+self.__nombre+", Paterno: "+self.__paterno+", Matreno: "+self.__materno+", Horas Extra: "+self.__h_extra+", Sueldo Base: "+self.__s_base+", Año ingreso: "+self.__año_ingreso
