import tkinter as tk
import tkinter.ttk as ttk
import pyautogui
import random
import string
import time
import threading

def generer_chiffres_aleatoires(longueur):
    return ''.join(random.choices(string.digits, k=longueur))

def generer_caracteres_aleatoires(longueur):
    return ''.join(random.choices(string.ascii_letters, k=longueur))

def taper_combinaison_et_valider(combinaison):
    print("Combinaison générée:", combinaison)
    pyautogui.typewrite(combinaison)
    pyautogui.press('enter')

def saisir_chiffres_et_valider(longueur, delai_pause):
    try:
        combinaisons = set()
        while not arret_code_chiffres:
            if longueur:
                combinaison = generer_chiffres_aleatoires(longueur)
            else:
                combinaison = generer_chiffres_aleatoires(random.randint(1, 15))
            if combinaison not in combinaisons:
                combinaisons.add(combinaison)
                taper_combinaison_et_valider(combinaison)
            time.sleep(delai_pause)

        print("Fini chiffres")

    except Exception as e:
        print(f"Erreur : {e}")

def saisir_caracteres_et_valider(longueur, delai_pause):
    try:
        combinaisons = set()
        while not arret_code_caracteres:
            if longueur:
                combinaison = generer_caracteres_aleatoires(longueur)
            else:
                combinaison = generer_caracteres_aleatoires(random.randint(1, 15))
            if combinaison not in combinaisons:
                combinaisons.add(combinaison)
                taper_combinaison_et_valider(combinaison)
            time.sleep(delai_pause)

        print("Fini caractères")

    except Exception as e:
        print(f"Erreur : {e}")

def executer_code_en_clic_chiffres():
    global arret_code_chiffres
    arret_code_chiffres = False
    bouton_demarrer_chiffres.pack_forget()
    bouton_arreter_chiffres.pack(pady=5)

    longueur = int(saisie_chiffres.get()) if saisie_chiffres.get() else None
    delai_pause = float(saisie_delai.get()) if saisie_delai.get() else 0.1
    threading.Thread(target=saisir_chiffres_et_valider, args=(longueur, delai_pause)).start()

def executer_code_en_clic_caracteres():
    global arret_code_caracteres
    arret_code_caracteres = False
    bouton_demarrer_caracteres.pack_forget()
    bouton_arreter_caracteres.pack(pady=5)

    longueur = int(saisie_caracteres.get()) if saisie_caracteres.get() else None
    delai_pause = float(saisie_delai.get()) if saisie_delai.get() else 0.1
    threading.Thread(target=saisir_caracteres_et_valider, args=(longueur, delai_pause)).start()

def arreter_execution_chiffres():
    global arret_code_chiffres
    arret_code_chiffres = True
    bouton_arreter_chiffres.pack_forget()
    bouton_demarrer_chiffres.pack(pady=5)

def arreter_execution_caracteres():
    global arret_code_caracteres
    arret_code_caracteres = True
    bouton_arreter_caracteres.pack_forget()
    bouton_demarrer_caracteres.pack(pady=5)

racine = tk.Tk()
racine.title("brute force")
racine.geometry("600x400")

racine.configure(bg="#0078d4")

etiquette_chiffres = tk.Label(racine, text="Nombre de chiffres à générer (laissez vide pour aucune limite) :", bg="#0078d4", fg="white", font=("Arial", 12))
etiquette_chiffres.pack(pady=10)

saisie_chiffres = tk.Entry(racine, font=("Arial", 12), justify="center")
saisie_chiffres.pack(pady=5)

etiquette_delai = tk.Label(racine, text="Délai de pause entre chaque génération (en secondes) :", bg="#0078d4", fg="white", font=("Arial", 12))
etiquette_delai.pack(pady=10)

saisie_delai = tk.Entry(racine, font=("Arial", 12), justify="center")
saisie_delai.pack(pady=5)
saisie_delai.insert(0, "0.1")

style = ttk.Style()
style.configure("RoundedButton.TButton", padding=6, relief="flat", background="#005a9e", foreground="blue")

bouton_demarrer_chiffres = ttk.Button(racine, text="Démarrer la génération de chiffres", command=executer_code_en_clic_chiffres, style="RoundedButton.TButton")
bouton_demarrer_chiffres.pack(pady=10)

bouton_arreter_chiffres = ttk.Button(racine, text="Arrêter la génération de chiffres", command=arreter_execution_chiffres, style="RoundedButton.TButton")
bouton_arreter_chiffres.pack(pady=5)
bouton_arreter_chiffres.pack_forget()

arret_code_chiffres = False

etiquette_caracteres = tk.Label(racine, text="Longueur de la série de caractères à générer (laissez vide pour aucune limite) :", bg="#0078d4", fg="white", font=("Arial", 12))
etiquette_caracteres.pack(pady=10)

saisie_caracteres = tk.Entry(racine, font=("Arial", 12), justify="center")
saisie_caracteres.pack(pady=5)

bouton_demarrer_caracteres = ttk.Button(racine, text="Démarrer la génération de caractères", command=executer_code_en_clic_caracteres, style="RoundedButton.TButton")
bouton_demarrer_caracteres.pack(pady=10)

bouton_arreter_caracteres = ttk.Button(racine, text="Arrêter la génération de caractères", command=arreter_execution_caracteres, style="RoundedButton.TButton")
bouton_arreter_caracteres.pack(pady=5)
bouton_arreter_caracteres.pack_forget()

arret_code_caracteres = False

racine.mainloop()
