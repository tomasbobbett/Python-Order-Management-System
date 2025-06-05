import csv
import sys
import os

NOMBRE_ARCHIVO_PEDIDOS = "pedidos.csv"
NOMBRE_ARCHIVO_CLIENTES = "clientes.csv"
NOMBRE_ARCHIVO_AUXILIAR = "aux.csv"

TOMATE = "Tomate"
ZANAHORIA = 'Zanahoria'
LECHUGA = 'Lechuga'

COMANDO_AGREGAR = "agregar"
COMANDO_MODIFICAR = "modificar"
COMANDO_ELIMINAR = "eliminar"
COMANDO_LISTAR = "listar"
COMANDO_HELP = "help"

MODO_LECTURA = 'r'
MODO_APPENDEAR= 'a'
MODO_ESCRITURA = 'w'

VERDURAS_PERMITIDAS = {'T', 'L', 'Z', 'B'}

ID_INICIAL = 0
COMANDO = sys.argv[1]


#PRE: -
#POST: Devuelve true si es que existe el numero del ID que le llega con el nombre de la variable id_pedido en la lista csv de los pedidos. 
#Y devuelve false cuando no lo entuentra.

def existe_pedido(id_pedido):

	try:
		lista_pedidos = open(NOMBRE_ARCHIVO_PEDIDOS, MODO_LECTURA)

	except:
		return

	existe_pedido = False
	lector_pedidos = csv.reader(lista_pedidos, delimiter = ";")

	for linea in lector_pedidos:

		if(int(linea[0]) == id_pedido):

			existe_pedido = True

	lista_pedidos.close()

	return existe_pedido
	




#PRE: -
#POST: Bsuca y devuelve el ultimo numero de id que esta en el archivo de pedidos.csv.
def buscar_ultimo_id():
	ultimo_id = 0
	try:
		lista_pedidos = open(NOMBRE_ARCHIVO_PEDIDOS, MODO_LECTURA)
	except:

		return 0

	lector = csv.reader(lista_pedidos, delimiter = ";")

	for linea in lector:

		ultimo_id = int(linea[0])

	lista_pedidos.close()

	return ultimo_id 




#PRE: -

#POST: Agrega una linea al archivo pedidos si es que existe. Si no existe lo crea. En la linea que agrega estan los datos [ID;INICIAL DE VERDURA;CANTIDAD]
def agregar_pedido(cantidad, verdura):

	try:
		
		lista_pedidos = open(NOMBRE_ARCHIVO_PEDIDOS, MODO_APPENDEAR)
		id_pedido = buscar_ultimo_id() + 1
		
	except:
		 
		lista_pedidos = open(NOMBRE_ARCHIVO_PEDIDOS, MODO_ESCRITURA, newline='')
		id_pedido = ID_INICIAL
		

	escritor_pedidos = csv.writer(lista_pedidos, delimiter=';')

	escritor_pedidos.writerow([id_pedido, verdura[0].capitalize(), cantidad])


	lista_pedidos.close()



#PRE: -
#POST: Agregar  el nombre y el ID del nuevo cliente al archivo csv clientes.csv
def agregar_nombre(nombre_cliente):

	try:
		
		lista_clientes = open(NOMBRE_ARCHIVO_CLIENTES, MODO_APPENDEAR)
		id_pedido = buscar_ultimo_id()
		
	except:

		lista_clientes = open(NOMBRE_ARCHIVO_CLIENTES, MODO_ESCRITURA, newline='')
		id_pedido = ID_INICIAL


	escritor_clientes = csv.writer(lista_clientes, delimiter=';')

	escritor_clientes.writerow([id_pedido, nombre_cliente.capitalize()])

	lista_clientes.close()



#PRE: -
#POST: Agregar un pedido del mismo id ingresado por el usuario con otro tipo de verdura. Agregandolo tambien a pedidos.csv
def agregar_pedido_existente(id_pedido, cant_verdura, tipo_verdura):

	try:
		lista_pedidos = open(NOMBRE_ARCHIVO_PEDIDOS, MODO_LECTURA)

	except:
		print("Debes primero crear ventas para poder modificarlas. Vuelve a intentarlo luego de ingresar alguna.")
		return

	try:
		archivo_aux = open(NOMBRE_ARCHIVO_AUXILIAR, MODO_ESCRITURA)

	except:
		print("Debes primero crear ventas para poder modificarlas. Vuelve a intentarlo luego de ingresar alguna.")
		lista_pedidos.close()
		return

	escritor_aux = csv.writer(archivo_aux, delimiter = ";")

	lector = csv.reader(lista_pedidos, delimiter = ";")

	fila_nueva = [id_pedido, tipo_verdura[0].capitalize(), cant_verdura]
	insertado = False
	
	for linea in lector:
		
		if int(linea[0]) > id_pedido and not insertado:

			escritor_aux.writerow(fila_nueva)
			insertado = True

		escritor_aux.writerow(linea)

	if not insertado :

		escritor_aux.writerow(fila_nueva)

	os.rename(NOMBRE_ARCHIVO_AUXILIAR, NOMBRE_ARCHIVO_PEDIDOS)

	archivo_aux.close()
	lista_pedidos.close()




#PRE: -
#POST: Modifica el pedido de id (id_pedido) aumentando solo la cantindad de verdura que lleve. Modificando el archivo pedidos.csv
def modificar_solo_cantidad(id_pedido, cant_verdura, tipo_verdura):

	try:
		lista_pedidos = open(NOMBRE_ARCHIVO_PEDIDOS, MODO_LECTURA)
	except:
		print("Para modificar primero se debe ingresar al menos una compra.")
		return
	try:
		lista_aux = open(NOMBRE_ARCHIVO_AUXILIAR, MODO_ESCRITURA)
	except:
		print("Para modificar primero se debe ingresar al menos una compra.")
		return

	lector_pedidos = csv.reader(lista_pedidos, delimiter = ";")
	escritor_aux = csv.writer(lista_aux, delimiter = ";")
	fila_nueva = [id_pedido, tipo_verdura[0], cant_verdura]
	modificado = False
	for linea in lector_pedidos:

		if int(linea[0]) == id_pedido and modificado == False:
			escritor_aux.writerow(fila_nueva)
			modificado = True
		else:
			escritor_aux.writerow(linea)

	os.rename(NOMBRE_ARCHIVO_AUXILIAR, NOMBRE_ARCHIVO_PEDIDOS)

	lista_pedidos.close()
	lista_aux.close()




#PRE: -
#POST: Modifica un pedido existente en el archivo de pedidos. Si el tipo de verdura es diferente, agrega un nuevo pedido.
def modificar_pedido(id_pedido, cant_verdura, tipo_verdura):
	
	try:
		lista_pedidos = open(NOMBRE_ARCHIVO_PEDIDOS, MODO_LECTURA)

	except:
		print("Debes primero crear ventas para poder modificarlas. Vuelve a intentarlo luego de ingresar alguna.")
		return

	lector = csv.reader(lista_pedidos, delimiter = ";")
	modificado = False

	for linea in lector:

		if int(linea[0]) == id_pedido and modificado == False:

			if linea[1] == tipo_verdura and modificado == False:

				modificar_solo_cantidad(id_pedido, cant_verdura, tipo_verdura)
				modificado = True

			elif modificado == False:
				agregar_pedido_existente(id_pedido, cant_verdura, tipo_verdura)
				modificado = True

	
	lista_pedidos.close()




#PRE: -
#POST: Elimina un pedido específico del archivo de pedidos.
def eliminar_pedido(pedido_a_eliminar):

	try:
		lista_pedidos = open(NOMBRE_ARCHIVO_PEDIDOS, MODO_LECTURA)
	except:
		print("Para eliminar algun pedido primero debes crear alguno. Intente nuevamente luego de haber creado al menos un pedido")

	try:
		archivo_auxiliar = open(NOMBRE_ARCHIVO_AUXILIAR, MODO_ESCRITURA)
	except:
		print("Para eliminar algun pedido primero debes crear alguno. Intente nuevamente luego de haber creado al menos un pedido")
		lista_pedidos.close()
		return

	escritor_aux = csv.writer(archivo_auxiliar, delimiter = ";")
	lector_pedidos_original = csv.reader(lista_pedidos, delimiter = ";")
	eliminado = False

	for fila in lector_pedidos_original:
		if int(fila[0]) != pedido_a_eliminar:
			escritor_aux.writerow(fila)

	os.rename(NOMBRE_ARCHIVO_AUXILIAR, NOMBRE_ARCHIVO_PEDIDOS)

	lista_pedidos.close()
	archivo_auxiliar.close()




#PRE: -
#POST: Elimina al cliente asociado al pedido eliminado.

def eliminar_cliente(pedido_a_eliminar):
	try:
		lista_clientes=open(NOMBRE_ARCHIVO_CLIENTES, MODO_LECTURA)
	except:
		print("Para eliminar algun pedido primero debes crear alguno. Intente nuevamente luego de haber creado al menos un pedido")
	try:
		archivo_auxiliar = open(NOMBRE_ARCHIVO_AUXILIAR, MODO_ESCRITURA)
	except:
		print("Ocurrio un error inesperado. Por favor intente nuevamente.")
		lista_clientes.close()
		return

	escritor_aux = csv.writer(archivo_auxiliar, delimiter = ";")

	lector_clientes_original = csv.reader(lista_clientes, delimiter = ";")


	for linea in lector_clientes_original:

		if int(linea[0]) != pedido_a_eliminar:

			escritor_aux.writerow(linea)

	os.rename(NOMBRE_ARCHIVO_AUXILIAR, NOMBRE_ARCHIVO_CLIENTES)

	lista_clientes.close()
	archivo_auxiliar.close()


#PRE: -
#POST:Devuelve el nombre del cliente correspondiente al ID proporcionado.

def buscar_cliente_correspondiente(id_cliente):
	try:
		lista_clientes = open(NOMBRE_ARCHIVO_CLIENTES, MODO_LECTURA)
	except:
		print("Ocurrio un error inesperado. Por favor intente nuevamente")
		return

	lector_clientes = csv.reader(lista_clientes, delimiter = ";")

	nombre_cliente = "nombre"
	
	for linea in lector_clientes:

		if int(linea[0]) == id_cliente:

			nombre_cliente = str(linea[1])

	lista_clientes.close()
	return str(nombre_cliente)




#PRE: --
#POST: Muestra información sobre todos los pedidos y clientes presentes en los archivos de pedidos y clientes.

def mostrar_pedidos_totales():

	try:
		lista_pedidos = open(NOMBRE_ARCHIVO_PEDIDOS, MODO_LECTURA)

	except:
		print("No tenes pedidos cargados para mostrar")
		return
	try:
		lista_clientes = open(NOMBRE_ARCHIVO_CLIENTES, MODO_LECTURA)
	except:
		print("Ocurrio un error inesperado. Por favor intente nuevamente.")
		lista_pedidos.close()
		return


	lector_pedidos = csv.reader(lista_pedidos, delimiter = ";")
	lector_clientes = csv.reader(lista_clientes, delimiter = ";")

	cliente = "nombre"
	verdura = "verdura"
	for linea_pedidos in lector_pedidos:

		if linea_pedidos[1] == TOMATE[0]:
			verdura = TOMATE
		elif linea_pedidos[1] == ZANAHORIA[0]:
			verdura = ZANAHORIA
		elif linea_pedidos[1] == LECHUGA[0]:
			verdura = LECHUGA
		else:
			verdura="Brocoli"

		cliente = str(buscar_cliente_correspondiente(int(linea_pedidos[0])))

		print(f"\nID: {linea_pedidos[0]}\nNombre: {cliente} \nVerdura: {verdura}\nCantidad: {linea_pedidos[2]}\n")

	lista_pedidos.close()
	lista_clientes.close()



#PRE: 
#POST: Muestra información sobre un pedido específico con el ID proporcionado.

def mostrar_pedido_especifico(pedido_a_mostrar):

	try:
		lista_pedidos = open(NOMBRE_ARCHIVO_PEDIDOS, MODO_LECTURA)

	except:
		print("No tenes pedidos cargados para mostrar")
		return

	try:
		lista_clientes = open(NOMBRE_ARCHIVO_CLIENTES, MODO_LECTURA)
	except:
		print("No tenes pedidos cargados para mostrar")
		lista_pedidos.close()
		return


	lector_pedidos = csv.reader(lista_pedidos, delimiter = ";")
	lector_clientes = csv.reader(lista_clientes, delimiter = ";")

	print(f"El pedido de ID [{pedido_a_mostrar}] tiene los siguientes datos cargados:\n")

	verdura = "verdura"

	for linea_pedidos in lector_pedidos:

		if linea_pedidos[1] == TOMATE[0]:
			verdura = TOMATE
		elif linea_pedidos[1] == ZANAHORIA[0]:
			verdura = ZANAHORIA
		elif linea_pedidos[1] == LECHUGA[0]:
			verdura = LECHUGA
		else:
			verdura="Brocoli"

		if int(linea_pedidos[0]) == pedido_a_mostrar:

			cliente = str(buscar_cliente_correspondiente(int(linea_pedidos[0])))

			print(f"\nID: {linea_pedidos[0]}\nNombre: {cliente}\nVerdura: {verdura}\nCantidad: {linea_pedidos[2]}\n")

	lista_pedidos.close()
	lista_clientes.close()



if __name__ == "__main__":


	#AGREGAR-----------------

	if sys.argv[1] == COMANDO_AGREGAR:

		cant_verdura_a_agregar = int(sys.argv[2])
		verdura_a_agregar  = sys.argv[3]
		nombre_cliente = sys.argv[4]

		if int(cant_verdura_a_agregar) < 0:
			print("La cantidad a agregar no puede ser negativa.")
			exit()
		if len(sys.argv) == 5:

			if verdura_a_agregar.upper() in VERDURAS_PERMITIDAS:

				agregar_pedido(cant_verdura_a_agregar, verdura_a_agregar)
				agregar_nombre(nombre_cliente)
				print("¡Se añadio tu compra exitosamente!")

			else:
				print("Estas ingresando una verdura que no tenemos. Las opciones validas son:\n(LECHUGA)\t(TOMATE)\t(ZANAHORIA)\t(BROCOLI)\n")

		else:
			print("Estas ingresando el comando de manera erronea. El formato para usar el comando AGREGAR es:\n agregar [cantidad de verduras] [inicial de la verdura] [nombre del comprador]")		
	


	#MODIFICAR---------------

	elif COMANDO == COMANDO_MODIFICAR:

		if buscar_ultimo_id() == 0:
			print("No hay datos en el archivo para modificar. Agrega alguno con la funcion *agregar* para luego poder modificarlo")
			exit()

		pedido_a_modificar = int(sys.argv[2])
		verdura_a_modificar = sys.argv[4].upper().capitalize()
		cant_verdura_a_modificar = int(sys.argv[3])

		if int(cant_verdura_a_modificar) < 0:
			print("La cantidad a modificar no puede ser negativa.")
			exit()

		if len(sys.argv) == 5:

			if verdura_a_modificar.upper() in VERDURAS_PERMITIDAS:

				if existe_pedido(pedido_a_modificar) == True:
	
					modificar_pedido(pedido_a_modificar, cant_verdura_a_modificar, verdura_a_modificar)
					print("¡Se modifico el pedido correctamente!")

				else:

					print("No hay un pedido registrado con ese ID.")

			else:

				print("Estas ingresando una verdura que no tenemos. Las opciones validas son:\n(LECHUGA)\t(TOMATE)\t(ZANAHORIA)\t(BROCOLI)\n")
	
		else:
			print("Estas ingresando mal el comando modificar. Para mas informacion sobre su formato, ingrese [help].")
	#ELIMINAR----------------

	elif COMANDO == COMANDO_ELIMINAR:
		if buscar_ultimo_id() == 0:
			print("No hay datos en el archivo para eliminar")
			exit()

		pedido_a_eliminar = int(sys.argv[2])
		if int(pedido_a_eliminar) < 0:
			print("No existe un pedido con ID negativo.")
			exit()

		if len(sys.argv) == 3:

			if existe_pedido(pedido_a_eliminar) == True:

				eliminar_pedido(pedido_a_eliminar)
				eliminar_cliente(pedido_a_eliminar)

				print(f"Pedido numero {pedido_a_eliminar} eliminado correctamente.")

			else:
				print(f"No existe tal pedido de ID numero {pedido_a_eliminar}")

		else:
			print("El formato del comando ELIMINAR es de la manera *eliminar [ID del pedido]*.")

	#LISTAR-------------------

	elif COMANDO == COMANDO_LISTAR:
		if buscar_ultimo_id() == 0:
			print("No hay datos en el archivo para mostrar")
			exit()

		accion = sys.argv

		if len(accion) == 2:

			mostrar_pedidos_totales()

		elif len(accion) == 3:

			pedido_a_mostrar = int(sys.argv[2])

			if int(pedido_a_mostrar) < 0:
				print("La cantidad a mostrar no puede ser negativa.")
				exit()
			elif existe_pedido(pedido_a_mostrar) == False:
				print("No existe ningun pedido con ese ID")
				exit()

			mostrar_pedido_especifico(pedido_a_mostrar)

		else:
			print("El formato del comando ingresado es erroneo. Para mas informacion de cada comando ingrese *help*.")


	#HELP-----------

	elif COMANDO == COMANDO_HELP:
		print("El programa cuenta con 4 comandos:\n\n\t1) Agregar: Su funcion es agregar una compra con los datos del comprador.\n")
		print("\t   FORMATO: *agregar [cantidad de verduras] [inicial de la verdura] [nombre del comprador]*\n\n")
		print("\t2) Modificar: Su funcion es modificar un pedido. Ya sea agregando otro tipo de verdura o aumentar la cantidad de verdura que iba a llevar en primer lugar")
		print("\n\t   FORMATO: *modificar [ID del pedido que se desea modificar] [cantidad de verdura] [inicial de la verdura]")
		print("\n\n\t3) Eliminar: Se utiliza para eliminar un pedido especifico\n")
		print("\t   FORMATO: *eliminar [ID del pedido a eliminar]*\n\n")
		print("\t4) Listar: Se puede utilizar para mostrar todos los pedidos con sus respectivos datos. Pero tambien se puede utilizar para mostar un solo pedido\n")
		print("\t   FORMATO: *listar*")
		print("\t   Para listar un pedido en especifico se le debe agregar al lado el numero de ID del pedido que ser quiera mostrar")
	else:

		print("Comando invalido. Por favor intente nuevamente. Si desea informacion a cerca de los comandos ingrese [help]")