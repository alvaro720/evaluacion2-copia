import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog

from Seguridad import Seguridad
from credenciales import llaves
from clases.Administrador import Administrador
from clases.Empleado import Empleado

BG = "#2c2f33"
FG = "#ffffff"
BTN = "#7289da"

root = tk.Tk()
root.title("Sistema Empresa")
root.geometry("520x580")
root.configure(bg=BG)
root.resizable(False, False)

# ---------------- UTIL ----------------

def conectar_db():
    return mysql.connector.connect(
        host=llaves["host"],
        user=llaves["usuario"],
        password=llaves["contrasena"],
        database=llaves["db"]
    )


def ejecutar_query(sql, params=None, commit=False, fetch_all=False, fetch_one=False):
    conn = None
    cursor = None
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute(sql, params or ())

        if commit:
            conn.commit()
            return True

        if fetch_one:
            return cursor.fetchone()

        if fetch_all:
            return cursor.fetchall()

        return True
    except Exception as e:
        messagebox.showerror("Error de base de datos", str(e))
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def input_box(v, texto, oculto=False):
    frame = tk.Frame(v, bg=BG)
    frame.pack(pady=6, padx=12, fill="x")

    tk.Label(frame, text=texto, bg=BG, fg=FG).pack(anchor="w")
    entry = tk.Entry(frame, show="*" if oculto else "")
    entry.pack(fill="x")
    return entry


def boton(v, texto, cmd):
    tk.Button(v, text=texto, command=cmd, bg=BTN, fg="white", width=24, height=2).pack(pady=6)


def validar(*campos):
    return all(c and c.strip() != "" for c in campos)


def mostrar_lista(titulo, lineas):
    if not lineas:
        messagebox.showinfo(titulo, "No hay registros para mostrar.")
        return
    texto = "\n".join(lineas)
    messagebox.showinfo(titulo, texto)


def existe_admin():
    fila = ejecutar_query(
        "SELECT idAdministrador FROM Administrador LIMIT 1",
        fetch_one=True
    )
    return bool(fila)

# ---------------- LOGIN ----------------

def obtener_usuario_por_cuenta(cuenta, password):
    sql_admin = (
        "SELECT idAdministrador, nombre, rut, correo, contrasena, rol "
        "FROM Administrador WHERE correo = %s OR nombre = %s"
    )
    admin = ejecutar_query(sql_admin, (cuenta, cuenta), fetch_one=True)
    if admin and Seguridad.validar_clave(password, admin[4]):
        return Administrador(admin[0], admin[1], admin[2], admin[3], admin[4], admin[5])

    sql_empleado = (
        "SELECT idEmpleado, nombre, rut, correo, contrasena, rol, telefono, salario, inicio_contrato, Departamento_idDepartamento "
        "FROM Empleado WHERE correo = %s OR nombre = %s"
    )
    empleado = ejecutar_query(sql_empleado, (cuenta, cuenta), fetch_one=True)
    if empleado and Seguridad.validar_clave(password, empleado[4]):
        return Empleado(
            empleado[0], empleado[1], empleado[2], empleado[3], empleado[4], empleado[5],
            empleado[6], empleado[7], empleado[8], empleado[9]
        )

    return None


def login():
    v = tk.Toplevel(root)
    v.configure(bg=BG)
    v.title("Iniciar sesión")
    v.geometry("420x320")
    v.resizable(False, False)

    tk.Label(v, text="INICIAR SESIÓN", bg=BG, fg=FG, font=("Arial", 18)).pack(pady=20)

    cuenta_input = input_box(v, "Correo electrónico o nombre")
    contrasena_input = input_box(v, "Contraseña", True)

    def entrar():
        usuario = obtener_usuario_por_cuenta(cuenta_input.get(), contrasena_input.get())
        if usuario:
            v.destroy()
            if usuario.get_rol() == "admin":
                menu_admin()
            else:
                menu_empleado(usuario)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    boton(v, "Ingresar", entrar)

# ---------------- ADMIN ----------------

def registrar_admin():
    v = tk.Toplevel(root)
    v.configure(bg=BG)
    v.title("Registrar administrador")
    v.geometry("420x420")
    v.resizable(False, False)

    tk.Label(v, text="REGISTRAR ADMIN", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=12)

    nombre = input_box(v, "Nombre completo")
    rut = input_box(v, "RUT")
    correo = input_box(v, "Correo electrónico")
    clave = input_box(v, "Contraseña", True)

    def guardar():
        if not validar(nombre.get(), rut.get(), correo.get(), clave.get()):
            messagebox.showwarning("Aviso", "Completa todos los campos.")
            return

        contrasena_hash = Seguridad.encriptar_clave(clave.get())
        sql = (
            "INSERT INTO Administrador (nombre, rut, correo, contrasena, rol) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        if ejecutar_query(sql, (nombre.get(), rut.get(), correo.get(), contrasena_hash, "admin"), commit=True):
            messagebox.showinfo("Éxito", "Administrador registrado correctamente.")
            v.destroy()
            actualizar_estado_inicio()

    boton(v, "Guardar administrador", guardar)

# -------- EMPLEADOS --------

def menu_empleados():
    v = tk.Toplevel(root)
    v.configure(bg=BG)
    v.title("Administrar empleados")
    v.geometry("420x420")
    v.resizable(False, False)

    tk.Label(v, text="GESTIÓN DE EMPLEADOS", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=12)

    boton(v, "Registrar empleado", registrar_empleado)
    boton(v, "Listar empleados", listar_empleados)
    boton(v, "Eliminar empleado", eliminar_empleado)


def registrar_empleado():
    v = tk.Toplevel(root)
    v.configure(bg=BG)
    v.title("Registrar empleado")
    v.geometry("420x620")
    v.resizable(False, False)

    tk.Label(v, text="REGISTRAR EMPLEADO", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=12)

    nombre = input_box(v, "Nombre completo")
    rut = input_box(v, "RUT")
    correo = input_box(v, "Correo electrónico")
    clave = input_box(v, "Contraseña", True)
    rol = input_box(v, "Rol")
    telefono = input_box(v, "Teléfono")
    salario = input_box(v, "Salario")
    inicio = input_box(v, "Fecha de inicio")
    departamento = input_box(v, "ID Departamento")

    def guardar():
        if not validar(nombre.get(), rut.get(), correo.get(), clave.get(), rol.get(), departamento.get()):
            messagebox.showwarning("Aviso", "Completa al menos los campos requeridos.")
            return

        contrasena_hash = Seguridad.encriptar_clave(clave.get())
        sql = (
            "INSERT INTO Empleado (nombre, rut, correo, contrasena, rol, telefono, salario, inicio_contrato, Departamento_idDepartamento) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        if ejecutar_query(
            sql,
            (
                nombre.get(), rut.get(), correo.get(), contrasena_hash,
                rol.get(), telefono.get(), salario.get() or None,
                inicio.get(), departamento.get()
            ),
            commit=True
        ):
            messagebox.showinfo("Éxito", "Empleado registrado correctamente.")
            v.destroy()

    boton(v, "Guardar empleado", guardar)


def listar_empleados():
    filas = ejecutar_query(
        "SELECT idEmpleado, nombre, correo, rol, Departamento_idDepartamento FROM Empleado",
        fetch_all=True
    )
    lineas = [f"{f[0]} | {f[1]} | {f[2]} | {f[3]} | Dept {f[4]}" for f in filas] if filas else []
    mostrar_lista("Empleados", lineas)


def eliminar_empleado():
    rut = simpledialog.askstring("Eliminar empleado", "RUT del empleado:")
    if rut:
        if ejecutar_query("DELETE FROM Empleado WHERE rut = %s", (rut,), commit=True):
            messagebox.showinfo("OK", "Empleado eliminado.")

# -------- DEPARTAMENTOS --------

def registrar_departamento():
    v = tk.Toplevel(root)
    v.configure(bg=BG)
    v.title("Registrar departamento")
    v.geometry("420x360")
    v.resizable(False, False)

    tk.Label(v, text="REGISTRAR DEPARTAMENTO", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=12)

    nombre = input_box(v, "Nombre del departamento")
    gerente = input_box(v, "Gerente")

    def guardar():
        if not validar(nombre.get(), gerente.get()):
            messagebox.showwarning("Aviso", "Completa todos los campos.")
            return

        sql = "INSERT INTO Departamento (nombre, gerente) VALUES (%s, %s)"
        if ejecutar_query(sql, (nombre.get(), gerente.get()), commit=True):
            messagebox.showinfo("Éxito", "Departamento registrado correctamente.")
            v.destroy()

    boton(v, "Guardar departamento", guardar)


def listar_departamentos():
    filas = ejecutar_query("SELECT idDepartamento, nombre, gerente FROM Departamento", fetch_all=True)
    lineas = [f"{f[0]} | {f[1]} | {f[2]}" for f in filas] if filas else []
    mostrar_lista("Departamentos", lineas)

# -------- PROYECTOS --------

def registrar_proyecto():
    v = tk.Toplevel(root)
    v.configure(bg=BG)
    v.title("Registrar proyecto")
    v.geometry("420x380")
    v.resizable(False, False)

    tk.Label(v, text="REGISTRAR PROYECTO", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=12)

    nombre = input_box(v, "Nombre del proyecto")
    descripcion = input_box(v, "Descripción")
    fecha_inicio = input_box(v, "Fecha de inicio")

    def guardar():
        if not validar(nombre.get(), descripcion.get(), fecha_inicio.get()):
            messagebox.showwarning("Aviso", "Completa todos los campos.")
            return

        sql = "INSERT INTO Proyecto (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
        if ejecutar_query(sql, (nombre.get(), descripcion.get(), fecha_inicio.get()), commit=True):
            messagebox.showinfo("Éxito", "Proyecto registrado correctamente.")
            v.destroy()

    boton(v, "Guardar proyecto", guardar)


def listar_proyectos():
    filas = ejecutar_query("SELECT idProyecto, nombre, descripcion FROM Proyecto", fetch_all=True)
    lineas = [f"{f[0]} | {f[1]} | {f[2]}" for f in filas] if filas else []
    mostrar_lista("Proyectos", lineas)

# -------- MENU ADMIN --------

def menu_admin():
    v = tk.Toplevel(root)
    v.configure(bg=BG)
    v.title("Panel administrador")
    v.geometry("420x520")
    v.resizable(False, False)

    tk.Label(v, text="PANEL ADMINISTRADOR", bg=BG, fg=FG, font=("Arial", 18)).pack(pady=16)

    boton(v, "Registrar empleado", registrar_empleado)
    boton(v, "Listar empleados", listar_empleados)
    boton(v, "Eliminar empleado", eliminar_empleado)
    boton(v, "Registrar departamento", registrar_departamento)
    boton(v, "Listar departamentos", listar_departamentos)
    boton(v, "Registrar proyecto", registrar_proyecto)
    boton(v, "Listar proyectos", listar_proyectos)

# ---------------- EMPLEADO ----------------

def menu_empleado(user):
    v = tk.Toplevel(root)
    v.configure(bg=BG)
    v.title("Panel empleado")
    v.geometry("420x420")
    v.resizable(False, False)

    tk.Label(v, text=f"BIENVENIDO {user.get_nombre()}", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=16)

    boton(v, "Ver mis datos", lambda: ver_datos(user))
    boton(v, "Registrar tiempo", lambda: registrar_tiempo(user))
    boton(v, "Ver mis registros", lambda: ver_registros(user))


def ver_datos(user):
    texto = (
        f"Nombre: {user.get_nombre()}\n"
        f"Correo: {user.get_correo()}\n"
        f"Rol: {user.get_rol()}\n"
        f"RUT: {user.get_rut()}"
    )
    messagebox.showinfo("Mis datos", texto)

# -------- REGISTRO --------

def registrar_tiempo(user):
    v = tk.Toplevel(root)
    v.configure(bg=BG)
    v.title("Registrar tiempo")
    v.geometry("420x420")
    v.resizable(False, False)

    tk.Label(v, text="REGISTRAR TIEMPO", bg=BG, fg=FG, font=("Arial", 16)).pack(pady=12)

    fecha = input_box(v, "Fecha")
    hora = input_box(v, "Hora")
    desc = input_box(v, "Descripción")
    proyecto = input_box(v, "ID de proyecto")

    def guardar():
        if not validar(fecha.get(), hora.get(), desc.get(), proyecto.get()):
            messagebox.showwarning("Aviso", "Completa todos los campos.")
            return

        sql = (
            "INSERT INTO Registro (fecha, hora, descripcion, Empleado_idEmpleado, Proyecto_idProyecto) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        if ejecutar_query(
            sql,
            (fecha.get(), hora.get(), desc.get(), user.get_id(), proyecto.get()),
            commit=True
        ):
            messagebox.showinfo("Éxito", "Registro de tiempo guardado.")
            v.destroy()

    boton(v, "Guardar registro", guardar)


def ver_registros(user):
    filas = ejecutar_query(
        "SELECT idRegistro, fecha, hora, descripcion, Proyecto_idProyecto FROM Registro WHERE Empleado_idEmpleado = %s",
        (user.get_id(),),
        fetch_all=True
    )
    lineas = [f"{f[0]} | {f[1]} {f[2]} | {f[3]} | Proyecto {f[4]}" for f in filas] if filas else []
    mostrar_lista("Mis registros", lineas)

# ---------------- MAIN ----------------

def actualizar_estado_inicio():
    if existe_admin():
        status_label.config(text="Inicia sesión para continuar.", fg="#99aab5")
    else:
        status_label.config(text="No hay administrador registrado. Registra al primer administrador.", fg="#ffcc00")


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

boton(buttons_frame, "Registrar administrador", registrar_admin)
boton(buttons_frame, "Iniciar sesión", login)
boton(buttons_frame, "Salir", root.quit)

status_label = tk.Label(root, text="", bg=BG, fg="#99aab5", font=("Arial", 11))
status_label.pack(pady=12)

actualizar_estado_inicio()

root.mainloop()
