import sqlite3
import os
import openpyxl
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from tkinter import filedialog, messagebox
import tkinter as tk
from tkinter import ttk

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", "minesys.db")

def conectar():
    return sqlite3.connect(DB_PATH)

def ventana_filtros(titulo, tabla, columnas, col_fecha, col_estado):
    """
    Abre una ventana con filtros de fecha y estado.
    Retorna (filas, descripcion_filtro) o (None, None) si cancela.
    """
    resultado = {"filas": None, "filtro": None}

    win = tk.Toplevel()
    win.title(f"Filtros — {titulo}")
    win.geometry("420x320")
    win.grab_set()
    win.resizable(False, False)

    tk.Label(win, text=f"Filtros de exportación — {titulo}",
             font=("Arial", 12, "bold")).pack(pady=12)

    frm = tk.Frame(win)
    frm.pack(padx=20, fill="x")

    # Rango de fechas
    tk.Label(frm, text="Desde (YYYY-MM-DD):", anchor="w").grid(row=0, column=0, sticky="w", pady=6)
    e_desde = tk.Entry(frm, width=20)
    e_desde.grid(row=0, column=1, padx=8)

    tk.Label(frm, text="Hasta (YYYY-MM-DD):", anchor="w").grid(row=1, column=0, sticky="w", pady=6)
    e_hasta = tk.Entry(frm, width=20)
    e_hasta.grid(row=1, column=1, padx=8)

    # Filtro por estado
    tk.Label(frm, text="Estado (opcional):", anchor="w").grid(row=2, column=0, sticky="w", pady=6)
    e_estado = tk.Entry(frm, width=20)
    e_estado.grid(row=2, column=1, padx=8)

    tk.Label(frm, text="Categoría (opcional):", anchor="w").grid(row=3, column=0, sticky="w", pady=6)
    e_categoria = tk.Entry(frm, width=20)
    e_categoria.grid(row=3, column=1, padx=8)

    def aplicar():
        desde    = e_desde.get().strip()
        hasta    = e_hasta.get().strip()
        estado   = e_estado.get().strip().lower()
        categoria = e_categoria.get().strip().lower()

        con = conectar()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {tabla}")
        filas = cur.fetchall()
        con.close()

        filtro_desc = []

        # Filtro por fecha
        if col_fecha is not None and (desde or hasta):
            filtradas = []
            for f in filas:
                fecha_val = str(f[col_fecha])
                if desde and fecha_val < desde:
                    continue
                if hasta and fecha_val > hasta:
                    continue
                filtradas.append(f)
            filas = filtradas
            if desde:
                filtro_desc.append(f"Desde: {desde}")
            if hasta:
                filtro_desc.append(f"Hasta: {hasta}")

        # Filtro por estado
        if col_estado is not None and estado:
            filas = [f for f in filas if estado in str(f[col_estado]).lower()]
            filtro_desc.append(f"Estado: {estado}")

        # Filtro por categoría (busca en toda la fila)
        if categoria:
            filas = [f for f in filas if any(categoria in str(v).lower() for v in f)]
            filtro_desc.append(f"Categoría: {categoria}")

        resultado["filas"]  = filas
        resultado["filtro"] = " | ".join(filtro_desc) if filtro_desc else "Sin filtro"
        win.destroy()

    def sin_filtro():
        con = conectar()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {tabla}")
        resultado["filas"]  = cur.fetchall()
        resultado["filtro"] = "Sin filtro"
        con.close()
        win.destroy()

    frm_btns = tk.Frame(win)
    frm_btns.pack(pady=18)
    tk.Button(frm_btns, text="✅ Aplicar filtro", bg="#1a5c8a", fg="white",
              font=("Arial", 9, "bold"), relief="flat", padx=10, pady=4,
              command=aplicar).pack(side="left", padx=6)
    tk.Button(frm_btns, text="📋 Sin filtro", bg="#555", fg="white",
              font=("Arial", 9), relief="flat", padx=10, pady=4,
              command=sin_filtro).pack(side="left", padx=6)
    tk.Button(frm_btns, text="❌ Cancelar", bg="#8a1a1a", fg="white",
              font=("Arial", 9), relief="flat", padx=10, pady=4,
              command=win.destroy).pack(side="left", padx=6)

    win.wait_window()
    return resultado["filas"], resultado["filtro"]


def exportar_con_filtro_excel(titulo, tabla, columnas, col_fecha, col_estado):
    filas, filtro = ventana_filtros(titulo, tabla, columnas, col_fecha, col_estado)
    if filas is None:
        return
    if len(filas) == 0:
        messagebox.showwarning("Sin resultados", "No hay registros con ese filtro.")
        return

    archivo = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel", "*.xlsx")],
        title="Guardar Excel"
    )
    if not archivo:
        return

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = titulo[:31]

    # Fila de filtro aplicado
    ws.append([f"Filtro: {filtro}"])
    ws.append(list(columnas))
    for fila in filas:
        ws.append(list(fila))

    wb.save(archivo)
    messagebox.showinfo("✅ Exportado",
                        f"Excel guardado con {len(filas)} registros.\nFiltro: {filtro}")


def exportar_con_filtro_pdf(titulo, tabla, columnas, col_fecha, col_estado):
    filas, filtro = ventana_filtros(titulo, tabla, columnas, col_fecha, col_estado)
    if filas is None:
        return
    if len(filas) == 0:
        messagebox.showwarning("Sin resultados", "No hay registros con ese filtro.")
        return

    archivo = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF", "*.pdf")],
        title="Guardar PDF"
    )
    if not archivo:
        return

    doc = SimpleDocTemplate(archivo, pagesize=landscape(A4),
                            rightMargin=1.5*cm, leftMargin=1.5*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    elementos = []
    elementos.append(Paragraph(f"Reporte — {titulo}", styles["Title"]))
    elementos.append(Paragraph(f"Filtro aplicado: {filtro}", styles["Normal"]))
    elementos.append(Spacer(1, 0.4*cm))

    data = [list(columnas)] + [list(f) for f in filas]
    tabla_pdf = Table(data, repeatRows=1)
    tabla_pdf.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0),  colors.HexColor("#1a3a5c")),
        ("TEXTCOLOR",     (0,0), (-1,0),  colors.white),
        ("FONTNAME",      (0,0), (-1,0),  "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,-1), 8),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [colors.HexColor("#ebf3fb"), colors.white]),
        ("GRID",          (0,0), (-1,-1), 0.5, colors.grey),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    elementos.append(tabla_pdf)
    elementos.append(Spacer(1, 0.3*cm))
    elementos.append(Paragraph(f"Total registros: {len(filas)}", styles["Normal"]))

    doc.build(elementos)
    messagebox.showinfo("✅ Exportado",
                        f"PDF guardado con {len(filas)} registros.\nFiltro: {filtro}")