import keyboard
import time
from rich.console import Console
import pickle
import os

console = Console()
seleccion = 0
menu_principal = ["Ver inventario", "Modificar inventario", "Crear un inventario", "Eliminar un inventario", "Salir"]
menu_modificar = ["Agregar o modificar un elemento", "Eliminar un elemento"]

def guardarInventarios():
    with open('inventarios.pkl', 'wb') as file:
        pickle.dump(listaInventarios, file)

def cargarInventarios():
    try:
        with open('inventarios.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
    
listaInventarios = cargarInventarios()

def limpiar():
    sistema_operativo = os.name

    if sistema_operativo == 'posix':
        os.system('clear')
    elif sistema_operativo == 'nt':  # Windows
        os.system('cls')
    else:
        os.system('clear')

def timer():
    time.sleep(0.15)

def titulo():
    console.print(f"""[yellow]
.______     ______   ___   ___ ___   ___  _______  _______  
|   _  \   /  __  \  \  \ /  / \  \ /  / |   ____||       \ 
|  |_)  | |  |  |  |  \  V  /   \  V  /  |  |__   |  .--.  |
|   _  <  |  |  |  |   >   <     >   <   |   __|  |  |  |  |
|  |_)  | |  `--'  |  /  .  \   /  .  \  |  |____ |  '--'  |
|______/   \______/  /__/ \__\ /__/ \__\ |_______||_______/   

|-------------------------- V.1.0 -------------------------|
    [/yellow]""")

def salir():
    titulo()
    console.print(f"[yellow]¡Nos vemos! Gracias por usar Boxxed[/yellow]", style = "bold")
    time.sleep(3)
    exit()

def menu(opciones, seleccion):
    titulo()
    for x, opcion in enumerate(opciones):
        if x == seleccion:
            console.print(f"[yellow]◆ {opcion}[/yellow]", style = "bold")
        else:
            console.print(f"[white]{opcion}[/white]")
    
    console.print(f"\n[yellow][🡱][/yellow][white] subir selección[/white]    [yellow][🡳][/yellow][white] bajar seleccion[/white]    [yellow][ENTER][/yellow][white] seleccionar[/white]")

def navegador():
    global seleccion
    seleccion = 0
    
    limpiar()
    menu(menu_principal, seleccion)
    
    while True:
        tecla = keyboard.read_key(suppress=True)

        if tecla == "flecha arriba":
            seleccion = (seleccion - 1) % len(menu_principal)
        elif tecla == "flecha abajo":
            seleccion = (seleccion + 1) % len(menu_principal)

        elif tecla == "enter":
            if seleccion == 0:
                limpiar()
                verInventario()
                break
            elif seleccion == 1:
                limpiar()
                modificarInventario()
                break
            elif seleccion == 2:
                limpiar()
                crearInventario()
                break
            elif seleccion == 3:
                limpiar()
                eliminarInventario()
                break
            elif seleccion == 4:
                limpiar()
                salir()

        timer()
        limpiar()
        menu(menu_principal, seleccion)

def verInventario():
    titulo()
    console.print(f"[yellow]Lista de inventarios guardados[/yellow]\n", style="bold")

    if len(listaInventarios) == 0:
        console.print(f"[red]No tienes ningun inventario[/red]")
        time.sleep(2)
        navegador()
    else:
        for inv, _ in listaInventarios:
            console.print(f"[white]{inv}[/white]", style="bold")
        console.print(f"\n[yellow]Escriba el nombre del inventario que desea revisar o escriba[/yellow] [red]'cancelar'[/red] [yellow]para regresar al menu.[/yellow]\n")
        nombreInventario = input("")

        if nombreInventario == "cancelar":
            timer()
            limpiar()
            navegador()
        else:
            inventarioEncontrado = False

            for nombre, inventario in listaInventarios:
                if nombre == nombreInventario:
                    inventarioEncontrado = True
                    limpiar()
                    titulo()
                    console.print(f"[yellow]Inventario '{nombreInventario}'[/yellow]\n", style="bold")
                    for item, cantidad in inventario.items():
                        console.print(f"[cyan]{item}[/cyan]: {cantidad}")

                    console.print(f"\n[yellow][ESC][/yellow][white] regresar al menu[/white]")

                    keyboard.wait("esc")
                    timer()
                    navegador()
                    
                    if not inventarioEncontrado:
                        limpiar()
                        titulo()
                        console.print(f"[red]No se encontro ningun inventario con el nombre '{nombreInventario}'[/red]")
                        time.sleep(2)
                        guardarInventarios()
                        limpiar()
                        verInventario()

def modificarInventario():
    titulo()
    console.print(f"[yellow]Lista de inventarios guardados[/yellow]\n", style="bold")

    if len(listaInventarios) == 0:
        console.print(f"[red]No tienes ningun inventario[/red]")
        time.sleep(2)
        navegador()
    else:
        for inv, _ in listaInventarios:
            console.print(f"[white]{inv}[/white]", style="bold")

        console.print(f"\n[yellow]Escriba el nombre del inventario que desea modificar o escriba[/yellow] [red]'cancelar'[/red] [yellow]para regresar al menu.[/yellow]\n")
        nombreInventario = input("")

        if nombreInventario == "cancelar":
            timer()
            limpiar()
            navegador()
        
        else:
            inventarioEncontrado = False

            for nombre, inventario in listaInventarios:
                if nombre == nombreInventario:
                    inventarioEncontrado = True
                    limpiar()
                    titulo()
                    console.print(f"[yellow]Inventario '{nombreInventario}'[/yellow]\n", style="bold")
                    for item, cantidad in inventario.items():
                        console.print(f"[cyan]{item}[/cyan]: {cantidad}")
                        
                    console.print(f"\n[yellow][A][/yellow][white] añadir o modificar un item[/white]    [yellow][E][/yellow][white] eliminar un item[/white]    [yellow][ESC][/yellow][white] regresar al menu[/white]")

                    if not inventarioEncontrado:
                        limpiar()
                        titulo()
                        console.print(f"[red]No se encontro ningun inventario con el nombre '{nombreInventario}'[/red]")
                        time.sleep(2)
                        navegador()

                    while True:
                        tecla = keyboard.read_key(suppress=True)

                        if tecla == "a":
                            limpiar()
                            titulo()
                            console.print(f"[yellow]Agregando/modificando un item en el inventario '{nombreInventario}'[/yellow]\n", style="bold")
                            console.print(f"[yellow]Escriba el nombre del item que desea agregar/modificar o escriba[/yellow][red] 'cancelar'[/red][yellow] para volver al menu[/yellow]\n")
                            nombreItem = input("")

                            if nombreItem == "cancelar":
                                limpiar()
                                titulo()
                                console.print(f"[red]Operacion cancelada con exito[/red]")
                                time.sleep(2)
                                limpiar()
                                modificarInventario()
                            elif nombreItem == "":
                                limpiar()
                                titulo()
                                console.print(f"[red]Debes ingresar un nombre valido[/red]")
                                time.sleep(2)
                                limpiar()
                                modificarInventario()
                            else:
                                limpiar()
                                titulo()
                                console.print(f"[yellow]Agregando un nuevo item en el inventario '{nombreInventario}'[/yellow]\n", style="bold")
                                console.print(f"[yellow]Escriba la cantidad del item que desea agregar/modificar o escriba[/yellow][red] 'cancelar'[/red][yellow] para volver al menu[/yellow]\n")
                                cantidadItem = input("")

                                if cantidadItem == "cancelar":
                                    limpiar()
                                    titulo()
                                    console.print(f"[red]Operacion cancelada con exito[/red]")
                                    time.sleep(2)
                                    limpiar()
                                    modificarInventario()
                                elif cantidadItem == "":
                                    limpiar()
                                    titulo()
                                    console.print(f"[red]Debes ingresar una cantidad valida[/red]")
                                    time.sleep(2)
                                    limpiar()
                                    modificarInventario()
                                else:
                                    inventario[nombreItem] = [cantidadItem]
                                    limpiar()
                                    titulo()
                                    console.print(f"[yellow]Item agregado/modificado con exito[/yellow]")
                                    time.sleep(2)
                                    limpiar()
                                    guardarInventarios()
                                    modificarInventario()
                        
                        if tecla == "e":
                            limpiar()
                            titulo()
                            console.print(f"[yellow]Eliminando un item en el inventario '{nombreInventario}'[/yellow]\n", style="bold")
                            console.print(f"[yellow]Escriba el nombre del item que desea eliminar o escriba[/yellow][red] 'cancelar'[/red][yellow] para volver al menu[/yellow]\n")
                            nombreItem = input("")

                            if nombreItem == "cancelar":
                                limpiar()
                                titulo()
                                console.print(f"[red]Operacion cancelada con exito[/red]")
                                time.sleep(2)
                                limpiar()
                                modificarInventario()
                            elif nombreItem == "":
                                limpiar()
                                titulo()
                                console.print(f"[red]¡Ingrese un nombre valido![/red]")
                                time.sleep(2)
                                limpiar()
                                modificarInventario()
                            else:
                                for nombre, inventario in listaInventarios:
                                    if nombre == nombreInventario:

                                        if nombreItem in inventario:
                                            del inventario[nombreItem]
                                            limpiar()
                                            titulo()
                                            console.print(f"[yellow]¡El item '{nombreItem}' se ha eliminado del inventario '{nombreInventario}'[/yellow]")
                                            time.sleep(2)
                                            guardarInventarios()
                                            limpiar()
                                            modificarInventario()
                                        else:
                                            limpiar()
                                            titulo()
                                            console.print(f"[red]¡El item '{nombreItem}' no existe en el inventario '{nombreInventario}'![/red]")
                                            time.sleep(2)
                                            limpiar()
                                            modificarInventario()
                        
                        if tecla == "esc":
                            modificarInventario()


def crearInventario():
    titulo()
    console.print(f"[yellow]Creando un inventario[/yellow]", style="bold")
    console.print(f"[yellow]Ingrese el nombre de su inventario o escriba[/yellow] [red]'cancelar'[/red] [yellow]para regresar al menu.[/yellow]\n")
    timer()
    nombreInventario = console.input("")

    if nombreInventario == "cancelar":
        timer()
        limpiar()
        navegador()
    else:
        inventario_existente = any(nombre == nombreInventario for nombre, _ in listaInventarios)

        if inventario_existente:
            limpiar()
            titulo()
            console.print(f"[red]El inventario '{nombreInventario}' ya existe.[/red]")
            time.sleep(2)
            navegador()
        else:
            nuevoInventario = dict()
            listaInventarios.append((nombreInventario, nuevoInventario))
            limpiar()
            titulo()
            console.print(f"[yellow]¡Inventario '{nombreInventario}' creado con éxito![/yellow]")
            time.sleep(2)
            guardarInventarios()
            navegador()

def eliminarInventario():

    titulo()
    console.print(f"[yellow]Lista de inventarios guardados[/yellow]\n", style="bold")

    if len(listaInventarios) == 0:
        console.print(f"[red]No tienes ningun inventario[/red]")
        time.sleep(2)
        navegador()
    else:
        for inv, _ in listaInventarios:
            console.print(f"[white]{inv}[/white]", style="bold")
        console.print(f"[yellow]\nEliminando un inventario[/yellow]", style="bold")
        console.print(f"[yellow]Ingrese el nombre de su inventario o escriba[/yellow] [red]'cancelar'[/red] [yellow]para regresar al menu.[/yellow]\n")
        timer()
        nombreInventario = console.input("")

        if nombreInventario == "cancelar":
            timer()
            limpiar()
            navegador()
        else:

            inventarioEncontrado = False

            for i, (inv, cont) in enumerate(listaInventarios):
                if inv == nombreInventario:
                    inventarioEncontrado = True
                    del listaInventarios[i]
                    limpiar()
                    titulo()
                    console.print(f"[yellow]¡Inventario '{nombreInventario}' eliminado con exito![/yellow]")
                    time.sleep(2)
                    guardarInventarios()
                    limpiar()
                    navegador()
                    break
            if not inventarioEncontrado:
                limpiar()
                titulo()
                console.print(f"[red]No se encontro un inventario con el nombre '{nombreInventario}'[/red]")
                time.sleep(2)
                limpiar()
                navegador()

navegador()
