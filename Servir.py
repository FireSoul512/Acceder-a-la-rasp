import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect( ('raspy2412.ddns.net',7080) )
    print("Empesando proceso de servir el alimento")
    mensaje = "SERVO"
    s.send(bytes(mensaje, "utf-8"))
    msg = s.recv(1024)
    print("El peso actual de del dispensador es de: ",msg.decode("utf-8"),"g")
    #print(msg.decode("utf-8")) # Obtener solo la cantidad el numero lo regresa como String
    s.close()
    print()
    print("ADIOS")

except:
    print("No se pudo establecer conexion ;v")