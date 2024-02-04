import tkinter as tk
from tkinter import messagebox, IntVar, ttk
import subprocess
import os

# Déclaration des variables globales
root = None
clean_temp_var = None
clean_windows_temp_var = None
clean_prefetch_var = None
clean_update_cache_var = None
clean_windows_components_var = None

def execute_powershell_script():
    try:
        # Chemin vers votre script PowerShell
        script_path = os.path.join(os.path.dirname(__file__), "cleandows.ps1")

        # Arguments à passer au script PowerShell
        arguments = [
            "-ExecutionPolicy", "Bypass",
            "-File", script_path,
            "-CleanTemp", str(clean_temp_var.get()),
            "-CleanWindowsTemp", str(clean_windows_temp_var.get()),
            "-CleanPrefetch", str(clean_prefetch_var.get()),
            "-CleanUpdateCache", str(clean_update_cache_var.get()),
            "-CleanWindowsComponents", str(clean_windows_components_var.get())
        ]

        # Commande pour exécuter le script PowerShell
        command = ["powershell.exe"] + arguments

        # Exécution de la commande
        subprocess.run(command, check=True)

        # Exemple de message de succès (à remplacer par votre logique réelle)
        messagebox.showinfo("Success", "The cleaning was executed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"The cleaning failed successfully : {str(e)}")
    finally:
        # Afficher à nouveau la fenêtre principale
        root.deiconify()

def toggle_menu(menu_frame):
    # Cette fonction bascule la visibilité du menu
    menu_frame.grid_forget() if menu_frame.grid_info() else menu_frame.grid(row=1, column=0, padx=10, pady=10)

def create_settings_frame(parent_frame):
    # Création du cadre de paramètres
    menu_frame = tk.Frame(parent_frame, bg="#f8f9fa")

    global clean_temp_var, clean_windows_temp_var, clean_prefetch_var, clean_update_cache_var, clean_windows_components_var
    clean_temp_var = IntVar(value=1)
    clean_windows_temp_var = IntVar(value=1)
    clean_prefetch_var = IntVar(value=1)
    clean_update_cache_var = IntVar(value=1)
    clean_windows_components_var = IntVar(value=1)

    clean_temp_checkbox = ttk.Checkbutton(menu_frame, text="Clean Temp folder", variable=clean_temp_var)
    clean_temp_checkbox.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    clean_windows_temp_checkbox = ttk.Checkbutton(menu_frame, text="Clean Windows Temp folder", variable=clean_windows_temp_var)
    clean_windows_temp_checkbox.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    clean_prefetch_checkbox = ttk.Checkbutton(menu_frame, text="Clean Prefetch folder", variable=clean_prefetch_var)
    clean_prefetch_checkbox.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    clean_update_cache_checkbox = ttk.Checkbutton(menu_frame, text="Clean Windows Update cache", variable=clean_update_cache_var)
    clean_update_cache_checkbox.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    clean_windows_components_checkbox = ttk.Checkbutton(menu_frame, text="Clean Windows components cache", variable=clean_windows_components_var)
    clean_windows_components_checkbox.grid(row=4, column=0, padx=10, pady=5, sticky="w")

    return menu_frame

def main():
    global root, clean_temp_var, clean_windows_temp_var, clean_prefetch_var, clean_update_cache_var, clean_windows_components_var

    root = tk.Tk()
    root.title("Cleandows")

    # Couleur de fond pour la fenêtre principale
    root.configure(bg="#f8f9fa")

    # Ajout d'un en-tête stylisé
    header_label = tk.Label(root, text="Welcome to Cleandows", font=("Helvetica", 18), bg="#79443b", fg="white", padx=10, pady=10)
    header_label.grid(row=0, column=0, sticky="ew")

    # Ajout d'une description
    description_label = tk.Label(root, text="Windows cleaning tool", font=("Helvetica", 12), bg="#f8f9fa", padx=10, pady=10)
    description_label.grid(row=2, column=0, sticky="ew")

    # Ajout d'un cadre pour les options de nettoyage
    settings_frame = create_settings_frame(root)
    settings_frame.grid(row=3, column=0, padx=10, pady=10)

    # Ajout d'un bouton "Clean Windows"
    clean_button = tk.Button(root, text="Clean Windows", font=("Helvetica", 14), bg="#79443b", fg="white", padx=20, pady=10, relief="flat", 
                             command=lambda: [root.withdraw(), execute_powershell_script()])
    clean_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    # Ajout d'un pied de page
    footer_label = tk.Label(root, text="by juliolgs", font=("Helvetica", 10), bg="#79443b", fg="white", padx=10, pady=5)
    footer_label.grid(row=7, column=0, sticky="ew")

    root.mainloop()

if __name__ == "__main__":
    main()
