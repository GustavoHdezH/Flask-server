from app import app
# De la carpeta app importa todo    
if __name__ == "__main__":
    app.run(debug=True,port=8046)
    # Para producción se quita el debug
    # host= IP sobre la que se desea montar o pude ser 127.0.0.1
    # port= Por defecto es el puerto 5000, de lo contrario se puede poner
    # cualquier puerto que no este en uso.
