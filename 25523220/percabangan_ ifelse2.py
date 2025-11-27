user = "admin"
paswd = "python"

username = input("Masukkan Username: ")
password = input("Masukkan Password: ")

if (password == paswd) & (username == user):
    print("Kombinasi username dan password BENAR")
else:
    print("kombinasi username dan password SALAH")