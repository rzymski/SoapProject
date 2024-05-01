from tkinter import *
from tkinter import messagebox
import tkinter.font as font


class LoginPanel:
    def __init__(self, parent):
        # Tworzymy nowe okno
        self.window = Toplevel(parent)
        self.window.title("Panel logowania")
        self.window.geometry("600x400")

        # Pole do wpisania loginu
        self.usernameLabel = Label(self.window, text="Login:")
        self.usernameLabel.pack(pady=10)
        self.usernameEntry = Entry(self.window, width=30)
        self.usernameEntry.pack(pady=5)

        # Pole do wpisania hasła
        self.passwordLabel = Label(self.window, text="Hasło:")
        self.passwordLabel.pack(pady=10)
        self.passwordEntry = Entry(self.window, show="*", width=30)
        self.passwordEntry.pack(pady=5)

        # Przycisk do zalogowania
        self.loginButton = Button(self.window, text="Zaloguj się", command=self.login)
        self.loginButton.pack(pady=10)

        # Napis "Nie masz konta, zarejestruj się"
        self.registerLabel = Label(self.window, text="Nie masz konta? Zarejestruj się.", fg="blue", cursor="hand2")
        self.registerLabel.pack(pady=10)

        # Wiązanie zdarzenia kliknięcia do otwarcia rejestracji
        self.registerLabel.bind("<Button-1>", self.register)

    def login(self):
        # Akcja przy logowaniu
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        # Przykładowa walidacja (możesz dodać swoją logikę)
        if username == "admin" and password == "admin":
            messagebox.showinfo("Sukces", "Zalogowano pomyślnie!")
        else:
            messagebox.showwarning("Błąd", "Błędny login lub hasło!")

    def register(self, event):
        # Akcja przy rejestracji
        messagebox.showinfo("Rejestracja", "Przekierowano do rejestracji.")

# Główne okno Tkinter
root = Tk()
root.title("Aplikacja")
root.geometry("400x300")

# Przycisk do otwarcia panelu logowania
Button(root, text="Otwórz panel logowania", command=lambda: LoginPanel(root)).pack(pady=20)

# Uruchomienie pętli głównej Tkinter
root.mainloop()
