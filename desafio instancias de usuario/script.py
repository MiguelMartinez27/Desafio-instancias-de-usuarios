from usuario import Usuario

def leer_usuarios(archivo_usuarios, archivo_errores):
    usuarios = []
    with open(archivo_usuarios, 'r') as f:
        for linea in f:
            try:
                datos_usuario = eval(linea.strip())
                nombre = datos_usuario.get('nombre')
                apellido = datos_usuario.get('apellido')
                email = datos_usuario.get('email')
                genero = datos_usuario.get('genero')
                usuario = Usuario(nombre, apellido, email, genero)
                usuarios.append(usuario)
            except Exception as e:
                with open(archivo_errores, 'a') as error_log:
                    error_log.write(f"Error al procesar la linea: {linea}\n")
                    error_log.write(f"Excepcion: {e}\n")
    return usuarios

if __name__ == "__main__":
    archivo_usuarios = 'usuarios.txt'
    archivo_errores = 'error.log'
    usuarios = leer_usuarios(archivo_usuarios, archivo_errores)
    for usuario in usuarios:
        print(f"Usuario: {usuario.nombre} {usuario.apellido}, Email: {usuario.email}, Género: {usuario.genero}")
