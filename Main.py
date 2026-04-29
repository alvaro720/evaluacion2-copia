import tkinter as tk
from Seguridad import Seguridad
from tkinter import messagebox, simpledialog


from Dao.DAOAdministrador import DAOAdministrador
from Dao.DAORegistro import DAORegistro

from clases.Administrador import Administrador
from clases.Empleado import Empleado
from clases.Registro import Registro


dao_admin = DAOAdministrador()
dao_registro = DAORegistro()

BG = "#2c2f33"
FG = "#ffffff"
BTN = "#7289da"

root = tk.Tk()
root.title("Sistema Empresa")
root.geometry("450x550")
root.configure(bg=BG)

# ---------------- UTIL ----------------
def input_box(v, texto, oculto=False):
    frame = tk.Frame(v, bg=BG)
    frame.pack(pady=5)

    tk.Label(frame, text=texto, bg=BG, fg=FG).pack()
    entry = tk.Entry(frame, show="*" if oculto else "")
    entry.pack()
    return entry


def boton(v, texto, cmd):
    tk.Button(v, text=texto, command=cmd, bg=BTN, fg="white", width=22, height=2).pack(pady=5)


def validar(*campos):
    return all(c.strip() != "" for c in campos)

# ---------------- LOGIN ----------------
def login():
    v = tk.Toplevel(root)
    v.configure(bg=BG)

    tk.Label(v, text="LOGIN", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=10)

    nombre = input_box(v, "Nombre")
    clave = input_box(v, "Contraseña", True)

    def entrar():
        user = dao_admin.validar_login(nombre.get(), clave.get())

        if user:
            v.destroy()
            if user.get_rol() == "admin":
                menu_admin()
            else:
                menu_empleado(user)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    boton(v, "Ingresar", entrar)

# ---------------- ADMIN ----------------
def registrar_admin():
    v = tk.Toplevel(root)
    v.configure(bg=BG)

    nombre = input_box(v, "Nombre")
    clave = input_box(v, "Contraseña", True)

    def guardar():
        admin = Administrador(0, nombre.get(), "", "", clave.get())
        if dao_admin.registrar_admin(admin):
            messagebox.showinfo("OK", "Admin creado")
            v.destroy()

    boton(v, "Guardar", guardar)

# -------- EMPLEADOS --------
def menu_empleados():
    v = tk.Toplevel(root)
    v.configure(bg=BG)

    tk.Label(v, text="EMPLEADOS", bg=BG, fg=FG).pack(pady=10)

    boton(v, "Registrar", registrar_empleado)
    boton(v, "Listar", listar_empleados)
    boton(v, "Eliminar", eliminar_empleado)


def registrar_empleado():
    v = tk.Toplevel(root)
    v.configure(bg=BG)

    nombre = input_box(v, "Nombre")
    correo = input_box(v, "Correo")
    clave = input_box(v, "Contraseña", True)

    def guardar():
        pass_hash = Seguridad.encriptar_clave(clave.get())
        nuevo_emp = Empleado(0, nombre.get(), "", correo.get(), pass_hash)
        if dao_admin.registrar_empleado(nuevo_emp):
            messagebox.showinfo("Éxito", "Empleado registrado correctamente")
            v.destroy()

    boton(v, "Guardar", guardar)


def listar_empleados():
    lista = dao_admin.listar_usuarios()
    texto = "\n".join([f"{u.get_id()} - {u.get_nombre()} - {u.get_rol()}" for u in lista])
    messagebox.showinfo("Usuarios", texto)


def eliminar_empleado():
    id = simpledialog.askinteger("Eliminar", "ID:")
    if dao_admin.eliminar_usuario(id):
        messagebox.showinfo("OK", "Eliminado")

# -------- DEPARTAMENTOS --------
def menu_departamentos():
    nombre = simpledialog.askstring("Departamento", "Nombre:")
    if nombre:
        dao_admin.crear_departamento(nombre)
        messagebox.showinfo("OK", "Creado")

# -------- PROYECTOS --------
def menu_proyectos():
    nombre = simpledialog.askstring("Proyecto", "Nombre:")
    if nombre:
        dao_admin.crear_proyecto(nombre)
        messagebox.showinfo("OK", "Creado")

# -------- MENU ADMIN --------
def menu_admin():
    v = tk.Toplevel(root)
    v.configure(bg=BG)

    tk.Label(v, text="ADMIN", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=10)

    boton(v, "Empleados", menu_empleados)
    boton(v, "Departamentos", menu_departamentos)
    boton(v, "Proyectos", menu_proyectos)

# ---------------- EMPLEADO ----------------
def menu_empleado(user):
    v = tk.Toplevel(root)
    v.configure(bg=BG)

    tk.Label(v, text="EMPLEADO", bg=BG, fg=FG).pack(pady=10)

    boton(v, "Ver datos", lambda: ver_datos(user))
    boton(v, "Registrar tiempo", lambda: registrar_tiempo(user))
    boton(v, "Ver registros", lambda: ver_registros(user))


def ver_datos(user):
    messagebox.showinfo("Datos", f"{user.get_nombre()}")

# -------- REGISTRO --------
def registrar_tiempo(user):
    v = tk.Toplevel(root)
    v.configure(bg=BG)

    fecha = input_box(v, "Fecha")
    hora = input_box(v, "Hora")
    desc = input_box(v, "Descripción")
    proyecto = input_box(v, "ID Proyecto")

    def guardar():
        reg = Registro(0, fecha.get(), hora.get(), desc.get(), user.get_id(), int(proyecto.get()))
        if dao_registro.insertar(reg):
            messagebox.showinfo("OK", "Guardado")
            v.destroy()

    boton(v, "Guardar", guardar)


def ver_registros(user):
    regs = dao_registro.listar_por_empleado(user.get_id())
    texto = "\n".join([f"{r.get_fecha()} - {r.get_hora()}" for r in regs])
    messagebox.showinfo("Registros", texto)

# ---------------- MAIN ----------------
tk.Label(root, text="SISTEMA", bg=BG, fg=FG, font=("Arial", 18)).pack(pady=20)

boton(root, "Registrar Admin", registrar_admin)
boton(root, "Login", login)
boton(root, "Salir", root.quit)

root.mainloop()