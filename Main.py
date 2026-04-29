import tkinter as tk
from tkinter import messagebox, simpledialog

ROOT_BG = "#e7eefc"
CARD_BG = "#f9fbff"
CARD_BORDER = "#d1dff1"
TEXT_COLOR = "#1f2a4a"
LABEL_COLOR = "#55607f"
FIELD_BG = "#eef4ff"
BTN_BG = "#5f7dff"
BTN_ACTIVE = "#4561d1"
SECONDARY_BG = "#e7efff"


def create_form_label(parent, text):
    return tk.Label(parent, text=text, bg=CARD_BG, fg=LABEL_COLOR, font=("Segoe UI", 10, "bold"))


def create_input(parent, hidden=False):
    frame = tk.Frame(parent, bg=CARD_BG)
    frame.pack(fill="x", pady=8)

    entry_frame = tk.Frame(frame, bg=FIELD_BG, bd=0)
    entry_frame.pack(fill="x", padx=0)

    entry = tk.Entry(entry_frame, bd=0, bg=FIELD_BG, fg=TEXT_COLOR, font=("Segoe UI", 11), show="*" if hidden else "")
    entry.pack(fill="x", padx=12, pady=12)
    return frame, entry


def create_button(parent, text, command, width=28):
    btn = tk.Button(parent, text=text, command=command, bg=BTN_BG, fg="white", activebackground=BTN_ACTIVE,
                    bd=0, font=("Segoe UI", 11, "bold"), cursor="hand2")
    btn.pack(pady=12, ipadx=6, ipady=6)
    return btn


def validar(*fields):
    return all(field and field.strip() != "" for field in fields)


def mostrar_lista(title, lines):
    if not lines:
        messagebox.showinfo(title, "No hay registros para mostrar.")
        return
    messagebox.showinfo(title, "\n".join(lines))


def login_action(email_entry, pass_entry):
    cuenta = email_entry.get().strip()
    contrasena = pass_entry.get()
    if not validar(cuenta, contrasena):
        messagebox.showwarning("Aviso", "Completa todos los campos.")
        return

    if "admin" in cuenta.lower():
        menu_admin()
    else:
        menu_empleado(cuenta or "Empleado Demo")


def build_login_screen():
    card = tk.Frame(root, bg=CARD_BG, bd=1, relief="solid", highlightbackground=CARD_BORDER,
                    highlightcolor=CARD_BORDER, highlightthickness=1)
    card.place(relx=0.5, rely=0.5, anchor="center", width=460, height=520)

    tk.Label(card, text="INICIAR SESIÓN", bg=CARD_BG, fg=TEXT_COLOR, font=("Segoe UI", 20, "bold")).pack(pady=(28, 8))
    tk.Label(card, text="Bienvenido de nuevo, ingresa tus datos para continuar.", bg=CARD_BG, fg=LABEL_COLOR,
             font=("Segoe UI", 10), wraplength=380, justify="center").pack(pady=(0, 24))

    form_frame = tk.Frame(card, bg=CARD_BG)
    form_frame.pack(padx=28, fill="x")

    tk.Label(form_frame, text="Correo electrónico", bg=CARD_BG, fg=LABEL_COLOR, font=("Segoe UI", 9, "bold")).pack(anchor="w")
    email_frame = tk.Frame(form_frame, bg=FIELD_BG)
    email_frame.pack(fill="x", pady=(6, 16))
    email_entry = tk.Entry(email_frame, bd=0, bg=FIELD_BG, fg=TEXT_COLOR, font=("Segoe UI", 11))
    email_entry.pack(fill="x", padx=12, pady=12)

    tk.Label(form_frame, text="Contraseña", bg=CARD_BG, fg=LABEL_COLOR, font=("Segoe UI", 9, "bold")).pack(anchor="w")
    pass_frame = tk.Frame(form_frame, bg=FIELD_BG)
    pass_frame.pack(fill="x", pady=(6, 8))
    pass_entry = tk.Entry(pass_frame, bd=0, bg=FIELD_BG, fg=TEXT_COLOR, font=("Segoe UI", 11), show="*")
    pass_entry.pack(side="left", fill="x", expand=True, padx=(12, 0), pady=12)

    def toggle_password():
        if pass_entry.cget("show") == "":
            pass_entry.config(show="*")
            toggle_button.config(text="👁")
        else:
            pass_entry.config(show="")
            toggle_button.config(text="🙈")

    toggle_button = tk.Button(pass_frame, text="👁", bg=FIELD_BG, fg=LABEL_COLOR, bd=0,
                              font=("Segoe UI", 10), activebackground=FIELD_BG,
                              command=toggle_password, cursor="hand2")
    toggle_button.pack(side="right", padx=8)

    create_button(card, "INGRESAR", lambda: login_action(email_entry, pass_entry))

    footer = tk.Frame(card, bg=SECONDARY_BG, bd=0)
    footer.pack(fill="x", pady=(24, 0), padx=18)
    footer.configure(highlightthickness=0)

    tk.Label(footer, text="No hay un administrador registrado.", bg=SECONDARY_BG, fg=TEXT_COLOR,
             font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(16, 4))
    tk.Label(footer, text="Registra el primer administrador para comenzar.", bg=SECONDARY_BG,
             fg=LABEL_COLOR, font=("Segoe UI", 9), wraplength=360, justify="left").pack(anchor="w")
    create_button(footer, "Registrar administrador", registrar_admin)


def registrar_admin():
    window = tk.Toplevel(root)
    window.configure(bg=ROOT_BG)
    window.title("Registrar administrador")
    window.geometry("420x460")
    window.resizable(False, False)

    card = tk.Frame(window, bg=CARD_BG, bd=1, relief="solid", highlightbackground=CARD_BORDER,
                    highlightcolor=CARD_BORDER, highlightthickness=1)
    card.pack(fill="both", expand=True, padx=18, pady=18)

    tk.Label(card, text="REGISTRAR ADMINISTRADOR", bg=CARD_BG, fg=TEXT_COLOR,
             font=("Segoe UI", 16, "bold")).pack(pady=18)

    fields = []
    for label in ["Nombre completo", "RUT", "Correo electrónico", "Contraseña"]:
        tk.Label(card, text=label, bg=CARD_BG, fg=LABEL_COLOR, font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=18, pady=(10, 0))
        entry_bg = tk.Frame(card, bg=FIELD_BG)
        entry_bg.pack(fill="x", padx=18, pady=6)
        entry = tk.Entry(entry_bg, bd=0, bg=FIELD_BG, fg=TEXT_COLOR, font=("Segoe UI", 11), show="*" if label == "Contraseña" else "")
        entry.pack(fill="x", padx=12, pady=12)
        fields.append(entry)

    def guardar():
        if not validar(*(field.get() for field in fields)):
            messagebox.showwarning("Aviso", "Completa todos los campos.")
            return
        messagebox.showinfo("Demo", "Administrador registrado en la interfaz demo.")
        window.destroy()
        menu_admin()

    create_button(card, "Guardar administrador", guardar)
    create_button(card, "INGRESAR", lambda: window.destroy())


def registrar_empleado():
    window = tk.Toplevel(root)
    window.configure(bg=ROOT_BG)
    window.title("Registrar empleado")
    window.geometry("420x620")
    window.resizable(False, False)

    card = tk.Frame(window, bg=CARD_BG, bd=1, relief="solid", highlightbackground=CARD_BORDER,
                    highlightcolor=CARD_BORDER, highlightthickness=1)
    card.pack(fill="both", expand=True, padx=18, pady=18)

    tk.Label(card, text="REGISTRAR EMPLEADO", bg=CARD_BG, fg=TEXT_COLOR,
             font=("Segoe UI", 16, "bold")).pack(pady=18)

    labels = ["Nombre completo", "RUT", "Correo electrónico", "Contraseña", "Rol", "Teléfono", "Salario", "Fecha de inicio", "ID Departamento"]
    for label in labels:
        tk.Label(card, text=label, bg=CARD_BG, fg=LABEL_COLOR, font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=18, pady=(10, 0))
        entry_bg = tk.Frame(card, bg=FIELD_BG)
        entry_bg.pack(fill="x", padx=18, pady=6)
        tk.Entry(entry_bg, bd=0, bg=FIELD_BG, fg=TEXT_COLOR, font=("Segoe UI", 11), show="*" if label == "Contraseña" else "").pack(fill="x", padx=12, pady=12)

    def guardar():
        messagebox.showinfo("Demo", "Empleado registrado en la interfaz demo.")
        window.destroy()

    create_button(card, "Guardar empleado", guardar)


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
    window.configure(bg=ROOT_BG)
    window.title("Registrar departamento")
    window.geometry("420x360")
    window.resizable(False, False)

    card = tk.Frame(window, bg=CARD_BG, bd=1, relief="solid", highlightbackground=CARD_BORDER,
                    highlightcolor=CARD_BORDER, highlightthickness=1)
    card.pack(fill="both", expand=True, padx=18, pady=18)

    tk.Label(card, text="REGISTRAR DEPARTAMENTO", bg=CARD_BG, fg=TEXT_COLOR,
             font=("Segoe UI", 16, "bold")).pack(pady=18)

    for label in ["Nombre del departamento", "Gerente"]:
        tk.Label(card, text=label, bg=CARD_BG, fg=LABEL_COLOR, font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=18, pady=(10, 0))
        entry_bg = tk.Frame(card, bg=FIELD_BG)
        entry_bg.pack(fill="x", padx=18, pady=6)
        tk.Entry(entry_bg, bd=0, bg=FIELD_BG, fg=TEXT_COLOR, font=("Segoe UI", 11)).pack(fill="x", padx=12, pady=12)

    def guardar():
        messagebox.showinfo("Demo", "Departamento registrado en la interfaz demo.")
        window.destroy()

    create_button(card, "Guardar departamento", guardar)


def listar_departamentos():
    lines = [
        "1 | Sistemas | Ana Demo",
        "2 | Ventas | Carlos Demo"
    ]
    mostrar_lista("Departamentos", lines)


def registrar_proyecto():
    window = tk.Toplevel(root)
    window.configure(bg=ROOT_BG)
    window.title("Registrar proyecto")
    window.geometry("420x380")
    window.resizable(False, False)

    card = tk.Frame(window, bg=CARD_BG, bd=1, relief="solid", highlightbackground=CARD_BORDER,
                    highlightcolor=CARD_BORDER, highlightthickness=1)
    card.pack(fill="both", expand=True, padx=18, pady=18)

    tk.Label(card, text="REGISTRAR PROYECTO", bg=CARD_BG, fg=TEXT_COLOR,
             font=("Segoe UI", 16, "bold")).pack(pady=18)

    for label in ["Nombre del proyecto", "Descripción", "Fecha de inicio"]:
        tk.Label(card, text=label, bg=CARD_BG, fg=LABEL_COLOR, font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=18, pady=(10, 0))
        entry_bg = tk.Frame(card, bg=FIELD_BG)
        entry_bg.pack(fill="x", padx=18, pady=6)
        tk.Entry(entry_bg, bd=0, bg=FIELD_BG, fg=TEXT_COLOR, font=("Segoe UI", 11)).pack(fill="x", padx=12, pady=12)

    def guardar():
        messagebox.showinfo("Demo", "Proyecto registrado en la interfaz demo.")
        window.destroy()

    create_button(card, "Guardar proyecto", guardar)


def listar_proyectos():
    lines = [
        "1 | Proyecto A | Demo de interfaz",
        "2 | Proyecto B | Demo de interfaz"
    ]
    mostrar_lista("Proyectos", lines)


def menu_admin():
    window = tk.Toplevel(root)
    window.configure(bg=ROOT_BG)
    window.title("Panel administrador")
    window.geometry("420x520")
    window.resizable(False, False)

    card = tk.Frame(window, bg=CARD_BG, bd=1, relief="solid", highlightbackground=CARD_BORDER,
                    highlightcolor=CARD_BORDER, highlightthickness=1)
    card.pack(fill="both", expand=True, padx=18, pady=18)

    tk.Label(card, text="PANEL ADMINISTRADOR", bg=CARD_BG, fg=TEXT_COLOR,
             font=("Segoe UI", 18, "bold")).pack(pady=16)

    create_button(card, "Registrar empleado", registrar_empleado)
    create_button(card, "Listar empleados", listar_empleados)
    create_button(card, "Eliminar empleado", eliminar_empleado)
    create_button(card, "Registrar departamento", registrar_departamento)
    create_button(card, "Listar departamentos", listar_departamentos)
    create_button(card, "Registrar proyecto", registrar_proyecto)
    create_button(card, "Listar proyectos", listar_proyectos)


def menu_empleado(name):
    window = tk.Toplevel(root)
    window.configure(bg=ROOT_BG)
    window.title("Panel empleado")
    window.geometry("420x420")
    window.resizable(False, False)

    card = tk.Frame(window, bg=CARD_BG, bd=1, relief="solid", highlightbackground=CARD_BORDER,
                    highlightcolor=CARD_BORDER, highlightthickness=1)
    card.pack(fill="both", expand=True, padx=18, pady=18)

    tk.Label(card, text=f"BIENVENIDO {name}", bg=CARD_BG, fg=TEXT_COLOR,
             font=("Segoe UI", 16, "bold")).pack(pady=16)

    create_button(card, "Ver mis datos", lambda: ver_datos(name))
    create_button(card, "Registrar tiempo", lambda: registrar_tiempo(name))
    create_button(card, "Ver mis registros", lambda: ver_registros(name))


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
    window.configure(bg=ROOT_BG)
    window.title("Registrar tiempo")
    window.geometry("420x420")
    window.resizable(False, False)

    card = tk.Frame(window, bg=CARD_BG, bd=1, relief="solid", highlightbackground=CARD_BORDER,
                    highlightcolor=CARD_BORDER, highlightthickness=1)
    card.pack(fill="both", expand=True, padx=18, pady=18)

    tk.Label(card, text="REGISTRAR TIEMPO", bg=CARD_BG, fg=TEXT_COLOR,
             font=("Segoe UI", 16, "bold")).pack(pady=18)

    for label in ["Fecha", "Hora", "Descripción", "ID de proyecto"]:
        tk.Label(card, text=label, bg=CARD_BG, fg=LABEL_COLOR, font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=18, pady=(10, 0))
        entry_bg = tk.Frame(card, bg=FIELD_BG)
        entry_bg.pack(fill="x", padx=18, pady=6)
        tk.Entry(entry_bg, bd=0, bg=FIELD_BG, fg=TEXT_COLOR, font=("Segoe UI", 11)).pack(fill="x", padx=12, pady=12)

    def guardar():
        messagebox.showinfo("Demo", "Registro de tiempo guardado en la interfaz demo.")
        window.destroy()

    create_button(card, "Guardar registro", guardar)


def ver_registros(name):
    lines = [
        "1 | 2026-04-29 09:00 | Tarea demo | Proyecto A",
        "2 | 2026-04-29 14:00 | Otra tarea demo | Proyecto B"
    ]
    mostrar_lista("Mis registros", lines)


root = tk.Tk()
root.title("Sistema Empresarial")
root.geometry("520x580")
root.configure(bg=ROOT_BG)
root.resizable(False, False)

build_login_screen()

root.mainloop()
