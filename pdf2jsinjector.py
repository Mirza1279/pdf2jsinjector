# =============================== #
# Divine Devil - PDF JS Injector #
# =============================== #
#               .-"      "-.      #
#              /            \     #
#             |,  .-.  .-.  ,|    #
#             | )(_o/  \o_)( |    #
#             |/     /\     \|    #
#             (_     ^^     _)    #
#              \__|IIIIII|__/     #
#               | \IIIIII/ |      #
#               \          /      #
#                `--------`       #
#  PDF JavaScript Injector Tool   #
# Contact: mirzaahmed2723@gmail.com
# Disclaimer: This tool is for testing purpose only, i am not responsible for any misuse.
# ===================================== #

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from PyPDF2 import PdfReader, PdfWriter
import time

def display_banner():
    print("# =============================== #")
    print("# Divine Devil - PDF JS Injector #")
    print("# =============================== #")
    print("#               .-\"      \"-.      #")
    print("#              /            \\     #")
    print("#             |,  .-.  .-.  ,|    #")
    print("#             | )(_o/  \\o_)( |    #")
    print("#             |/     /\\     \\|    #")
    print("#             (_     ^^     _)    #")
    print("#              \\__|IIIIII|__/     #")
    print("#               | \\IIIIII/ |      #")
    print("#               \\          /      #")
    print("#                `--------`       #")
    print("#  PDF JavaScript Injector Tool   #")
    print("# Contact: mirzaahmed2723@gmail.com      #")
    print("#Disclaimer: This tool is for testing purpose only, i am not responsible for any misuse.")
    print("# ===================================== #")
    time.sleep(3)

def select_pdf():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")],
        title="Select a PDF file"
    )
    if file_path:
        pdf_path_var.set(file_path)

def select_js_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("JavaScript Files", "*.js")],
        title="Select a JavaScript file"
    )
    if file_path:
        with open(file_path, "r") as js_file:
            js_code_text.delete("1.0", tk.END)
            js_code_text.insert(tk.END, js_file.read())

def inject_js():
    pdf_path = pdf_path_var.get()
    js_code = js_code_text.get("1.0", tk.END).strip()

    if not pdf_path or not js_code:
        messagebox.showerror("Error", "Please select a PDF and provide JavaScript code.")
        return

    try:
        # Read the existing PDF
        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        # Copy existing pages
        for page in reader.pages:
            writer.add_page(page)

        # Add JavaScript
        writer.add_js(js_code)

        # Save the modified PDF
        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Save Modified PDF"
        )
        if save_path:
            with open(save_path, "wb") as output_pdf:
                writer.write(output_pdf)
            messagebox.showinfo("Success", f"JavaScript injected and saved to {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def drag_and_drop(event):
    file_path = event.data.strip()
    if file_path.endswith(".js"):
        with open(file_path, "r") as js_file:
            js_code_text.delete("1.0", tk.END)
            js_code_text.insert("1.0", js_file.read())
    elif file_path.endswith(".pdf"):
        pdf_path_var.set(file_path)
    else:
        messagebox.showerror("Error", "Unsupported file type. Please use a .js or .pdf file.")

def create_gui():
    global pdf_path_var, js_code_text

    # Create the GUI window
    root = TkinterDnD.Tk()
    root.title("Divine Devil - PDF JS Injector")

    # Banner in GUI
    tk.Label(root, text="Divine Devil - PDF JS Injector", font=("Helvetica", 16, "bold"), fg="red").grid(row=0, column=0, columnspan=3, pady=10)
    tk.Label(root, text="Contact: example@gmail.com", font=("Helvetica", 10, "italic"), fg="blue").grid(row=1, column=0, columnspan=3, pady=5)

    # Path selection
    pdf_path_var = tk.StringVar()
    tk.Label(root, text="PDF File:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    tk.Entry(root, textvariable=pdf_path_var, width=40).grid(row=2, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse PDF", command=select_pdf).grid(row=2, column=2, padx=10, pady=10)

    # JavaScript code input
    tk.Label(root, text="JavaScript Code:").grid(row=3, column=0, padx=10, pady=10, sticky="nw")
    js_code_text = tk.Text(root, height=10, width=50)
    js_code_text.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

    # Upload JavaScript file
    tk.Button(root, text="Browse JS File", command=select_js_file).grid(row=4, column=1, pady=10)

    # Drag and Drop area
    drag_label = tk.Label(root, text="Drag and Drop PDF or JS file here", bg="lightgray", height=3)
    drag_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="we")
    drag_label.drop_target_register(DND_FILES)
    drag_label.dnd_bind("<<Drop>>", drag_and_drop)

    # Inject button
    tk.Button(root, text="Inject JavaScript", command=inject_js, bg="green", fg="white").grid(row=6, column=1, pady=10)

    # Run the GUI loop with graceful exit
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")

# Display banner in console
display_banner()

# Launch the GUI
create_gui()
