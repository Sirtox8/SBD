from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()
libreriaBD = cliente["libreria"]
librosColeccion = libreriaBD["libros"]

miquery = { "precio": 19.99 } 

libros = librosColeccion.find(miquery)  # Busca los que tienen precio igual a 19.99

miquery = { "precio":  { "$gt": 19 } }
 
libros = librosColeccion.find(miquery) # Busca los que tienen el precio mayor que 19 

miquery = { "titulo":  { "$regex": "^D" } }

libros = librosColeccion.find(miquery) # Busca a toso los que tengan un título que empieza por D