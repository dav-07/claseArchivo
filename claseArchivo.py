import shutil, os

from sys import exit
class Archivo:
    def __init__(self, nombre):
        try:
            self.f = open(nombre, 'r')
            self.nombre = nombre
        except:
            print("No se puede abrir el archivo", nombre)
            exit()
        
    def muestra(self):
        i=1
        for linea in self.f:
            print(  "{:3}{}".format(i,linea), end="")
            i+=1
        self.f.seek(0)
        
    def cuentaVocales(self):
        def vocales(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set("aeiouáéíóúAEIOU"):
                    contador +=1
            return contador

        contador = 0
        for linea in self.f:
            contador +=vocales(linea)
        self.f.seek(0)
        return contador
    
    def cuentaConsonantes(self):
        def consonantes(s):
            contador = 0
            for i in range(len(s)):
                if s[i].lower() in set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"):
                    contador += 1
            return contador
        
        contador = 0
        for linea in self.f:
            contador +=consonantes(linea)
        self.f.seek(0)
        return contador

    def cuentasigpuntuacion(self):
        def signos(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set(",;.:...¿?¡!()*/-_"""):
                    contador += 1
            return contador
        
        contador = 0
        for linea in self.f:
            contador +=signos(linea)
        self.f.seek(0)
        return contador

    def cuentaespacio(self):
        def espacio(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set(" "):
                    contador += 1
            return contador
        
        contador = 0
        for linea in self.f:
            contador +=espacio(linea)
        self.f.seek(0)
        return contador

    def cuentapalabras(self):
        def palabra(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set(" \n"):
                    contador += 1
            return contador 
        
        contador = 0
        for linea in self.f:
            contador +=palabra(linea)
        self.f.seek(0)
        return contador + 1

    def cuentaslinea(self):
        def lineas(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set("\n"):
                    contador += 1
            return contador
        
        contador = 1
        for linea in self.f:
            contador +=lineas(linea)
        self.f.seek(0)
        return contador
    
    def cuentamayusculas(self):
        def mayusculas(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set("AÁBCDEÉFGHIÍJKLMNOÓPQRSTUÚVWXYZ"):
                    contador += 1
            return contador

        contador = 0
        for linea in self.f:
            contador +=mayusculas(linea)
        self.f.seek(0)
        return contador     
    
    def cuentaminusculas(self):
        def minusculas(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set("aeiouáéíóúbcdfghjklmnpqrstvwxyz"):
                    contador += 1
            return contador

        contador = 0
        for linea in self.f:
            contador +=minusculas(linea)
        self.f.seek(0)
        return contador

    def copiarch(self, copia):
        shutil.copy(self.f.name, copia)
        print("\n9._ El archivo se a copiado con el nombre de copia")
         

    def convmayusculas(self):
        contador = ""
        for linea in self.f:
            contador +=linea.upper()
        self.f.seek(0)
        return contador
    
    def convminusculas(self):
        contador = ""
        for linea in self.f:
            contador += linea.lower()
        self.f.seek(0)
        return contador

    def hexadecimal(self):
        h = []
        def d(s):
            for i in range(len(s)):
                h.append(hex(ord(s[i])))

        for linea in self.f:
            d(linea)
        print(h)
        self.f.seek(0)

                

    
