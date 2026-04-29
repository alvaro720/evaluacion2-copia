import tkinter as tk
from tkinter import messagebox, simpledialog

BG = "#2c2f33"
FG = "#ffffff"
BTN = "#7289da"


def input_box(parent, label_text, hidden=False):
    frame = tk.Frame(parent, bg=BG)
    frame.pack(pady=6, padx=12, fill="x")

    tk.Label(frame, text=label_text, bg=BG, fg=FG).pack(anchor="w")
    entry = tk.Entry(frame, show="*" if hidden else "")
    entry.pack(fill="x")
    return entry


def create_button(parent, text, command):
    tk.Button(parent, text=text, command=command, bg=BTN, fg="white", width=24, height=2).pack(pady=6)


def validar(*fields):
    return all(field and field.strip() != "" for field in fields)


def mostrar_lista(title, lines):
    if not lines:
        messagebox.showinfo(title, "No hay registros para mostrar.")
        return
    messagebox.showinfo(title, "\n".join(lines))


def login():
    window = tk.Toplevel(root)
    window.configure(bg=BG)
    window.title("Iniciar sesión")
    window.geometry("420x320")
    window.resizable(False, False)

    tk.Label(window, text="INICIAR SESIÓN", bg=BG, fg=FG, font=("Arial", 18)).pack(pady=20)

    cuenta_input = input_box(window, "Correo electrónico o nombre")
    contrasena_input = input_box(window, "Contraseña", hidden=True)

    def entrar():
        cuenta = cuenta_input.get().strip()
        contrasena = contrasena_input.get()
        if not validar(cuenta, contrasena):
            messagebox.showwarning("Aviso", "Completa todos los campos.")
            return

        window.destroy()
        if "admin" in cuenta.lower():
            menu_admin()
        else:
            menu_empleado(cuenta or "Empleado Demo")

    create_button(window, "Ingresar", entrar)


def registrar_admin():
    window = tk.Toplevel(root)
    window.configure(bg=BG)
    window.title("Registrar administrador")
    window.geometry("420x460")
    window.resizable(False, False)

    tk.Label(window, text="REGISTRAR ADMINISTRADOR", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=12)

    nombre = input_box(window, "Nombre completo")
    rut = input_box(window, "RUT")
    correo = input_box(window, "Correo electrónico")
    clave = input_box(window, "Contraseña", hidden=True)

    def guardar():
        if not validar(nombre.get(), rut.get(), correo.get(), clave.get()):
            messagebox.showwarning("Aviso", "Completa todos los campos.")
            return

        messagebox.showinfo("Demo", "Administrador registrado en la interfaz demo.")
        window.destroy()
        menu_admin()

    create_button(window, "Guardar administrador", guardar)


def registrar_empleado():
    window = tk.Toplevel(root)
    window.configure(bg=BG)
    window.title("Registrar empleado")
    window.geometry("420x620")
    window.resizable(False, False)

    tk.Label(window, text="REGISTRAR EMPLEADO", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=12)

    input_box(window, "Nombre completo")
    input_box(window, "RUT")
    input_box(window, "Correo electrónico")
    input_box(window, "Contraseña", hidden=True)
    input_box(window, "Rol")
    input_box(window, "Teléfono")
    input_box(window, "Salario")
    input_box(window, "Fecha de inicio")
    input_box(window, "ID Departamento")

    def guardar():
        messagebox.showinfo("Demo", "Empleado registrado en la interfaz demo.")
        window.destroy()

    create_button(window, "Guardar empleado", guardar)


def listar_empleados():
    lines = [
        "1 | Juan Pérez | juan@demo.com | 555-1234 | 1200 | 2026-01-01 | Dept Demo",
        "2 | María Gómez | maria@demo.com | 555-5678 | 1300 | 2026-02-01 | Dept Demo"
    ]
    mostrar_lista("Empleados", lines)


def eliminar_empleado():
    rut = simpledialog.askstring("Eliminar empleado", "RUT del empleado:")
    if rut:
        messagebox.showinfo("Demo", "En esta demo no se elimina nada. Solo se muestra la interfaz.")


def registrar_departamento():
    window = tk.Toplevel(root)
    window.configure(bg=BG)
    window.title("Registrar departamento")
    window.geometry("420x360")
    window.resizable(False, False)

    tk.Label(window, text="REGISTRAR DEPARTAMENTO", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=12)

    input_box(window, "Nombre del departamento")
    input_box(window, "Gerente")

    def guardar():
        messagebox.showinfo("Demo", "Departamento registrado en la interfaz demo.")
        window.destroy()

    create_button(window, "Guardar departamento", guardar)


def listar_departamentos():
    lines = [
        "1 | Sistemas | Ana Demo",
        "2 | Ventas | Carlos Demo"
    ]
    mostrar_lista("Departamentos", lines)


def registrar_proyecto():
    window = tk.Toplevel(root)
    window.configure(bg=BG)
    window.title("Registrar proyecto")
    window.geometry("420x380")
    window.resizable(False, False)

    tk.Label(window, text="REGISTRAR PROYECTO", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=12)

    input_box(window, "Nombre del proyecto")
    input_box(window, "Descripción")
    input_box(window, "Fecha de inicio")

    def guardar():
        messagebox.showinfo("Demo", "Proyecto registrado en la interfaz demo.")
        window.destroy()

    create_button(window, "Guardar proyecto", guardar)


def listar_proyectos():
    lines = [
        "1 | Proyecto A | Demo de interfaz",
        "2 | Proyecto B | Demo de interfaz"
    ]
    mostrar_lista("Proyectos", lines)


def menu_admin():
    window = tk.Toplevel(root)
    window.configure(bg=BG)
    window.title("Panel administrador")
    window.geometry("420x520")
    window.resizable(False, False)

    tk.Label(window, text="PANEL ADMINISTRADOR", bg=BG, fg=FG, font=("Arial", 18)).pack(pady=16)

    create_button(window, "Registrar empleado", registrar_empleado)
    create_button(window, "Listar empleados", listar_empleados)
    create_button(window, "Eliminar empleado", eliminar_empleado)
    create_button(window, "Registrar departamento", registrar_departamento)
    create_button(window, "Listar departamentos", listar_departamentos)
    create_button(window, "Registrar proyecto", registrar_proyecto)
    create_button(window, "Listar proyectos", listar_proyectos)


def menu_empleado(name):
    window = tk.Toplevel(root)
    window.configure(bg=BG)
    window.title("Panel empleado")
    window.geometry("420x420")
    window.resizable(False, False)

    tk.Label(window, text=f"BIENVENIDO {name}", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=16)

    create_button(window, "Ver mis datos", lambda: ver_datos(name))
    create_button(window, "Registrar tiempo", lambda: registrar_tiempo(name))
    create_button(window, "Ver mis registros", lambda: ver_registros(name))


def ver_datos(name):
    info = (
        f"Nombre: {name}\n"
        f"Correo: {name.lower().replace(' ', '.')}@demo.com\n"
        f"Rol: empleado\n"
        f"RUT: 11.111.111-1"
    )
    messagebox.showinfo("Mis datos", info)


def registrar_tiempo(name):
    window = tk.Toplevel(root)
    window.configure(bg=BG)
    window.title("Registrar tiempo")
    window.geometry("420x420")
    window.resizable(False, False)

    tk.Label(window, text="REGISTRAR TIEMPO", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=12)

    input_box(window, "Fecha")
    input_box(window, "Hora")
    input_box(window, "Descripción")
    input_box(window, "ID de proyecto")

    def guardar():
        messagebox.showinfo("Demo", "Registro de tiempo guardado en la interfaz demo.")
        window.destroy()

    create_button(window, "Guardar registro", guardar)


def ver_registros(name):
    lines = [
        "1 | 2026-04-29 09:00 | Tarea demo | Proyecto A",
        "2 | 2026-04-29 14:00 | Otra tarea demo | Proyecto B"
    ]
    mostrar_lista("Mis registros", lines)


def actualizar_estado_inicio():
    status_label.config(text="Demo de interfaz: interactúa con las ventanas para ver el diseño.", fg="#99aab5")


root = tk.Tk()
root.title("Sistema Empresarial")
root.geometry("520x580")
root.configure(bg=BG)
root.resizable(False, False)

root_frame = tk.Frame(root, bg=BG)
root_frame.pack(pady=25)

logo_label = tk.Label(root_frame, text="SISTEMA EMPRESARIAL", bg=BG, fg=FG, font=("Arial", 22, "bold"))
logo_label.pack(pady=10)

subtitle_label = tk.Label(
    root_frame,
    text="Administra usuarios, departamentos, proyectos y tiempos desde una sola ventana.",
    bg=BG,
    fg="#b9bbbe",
    wraplength=460,
    justify="center"
)
subtitle_label.pack(pady=6)

buttons_frame = tk.Frame(root, bg=BG)
buttons_frame.pack(pady=12)

create_button(buttons_frame, "Registrar administrador", registrar_admin)
create_button(buttons_frame, "Iniciar sesión", login)
create_button(buttons_frame, "Salir", root.quit)

status_label = tk.Label(root, text="", bg=BG, fg="#99aab5", font=("Arial", 11))
status_label.pack(pady=12)

actualizar_estado_inicio()

root.mainloop()
