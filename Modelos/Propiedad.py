class Propiedad:
    Nombre = ""
    Direccion = ""
    Contacto = ""
  
    def __init__(self, nombre, direccion, contacto):
        self.Nombre = nombre
        self.Direccion = direccion
        self.Contacto = contacto

    def get_Nombre(self):
        return self.Nombre

    def getDireccion(self):
        return self.Direccion

    def getContacto(self):
        return self.Contacto

    def setNombre(self,nombre):
        self.Nombre = nombre
    
    def setDireccion(self,direccion):
        self.Direccion = direccion
    
    def setContacto(self,contacto):
        self.Contacto = contacto
    
    def _str(self):
        print("Nombre Propiedad: "+self.Nombre)
        print("\nDireccion Propiedad: "+self.Direccion)
        print("Contacto Propiedad: "+self.Contacto)

    