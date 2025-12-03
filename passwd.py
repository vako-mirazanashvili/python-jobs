import re
import hashlib

def mot_de_passe_valide(mdp):
    return (
        len(mdp) >= 8
        and re.search(r"[A-Z]", mdp)
        and re.search(r"[a-z]", mdp)
        and re.search(r"[0-9]", mdp)
        and re.search(r"[!@#$%^&*]", mdp)
    )

while True:
    mdp = input("Choisissez un mot de passe : ")

    if mot_de_passe_valide(mdp):
        print("✔️ Mot de passe valide.")
        break
    else:
        print("\n❌ Mot de passe invalide !")
        print("Il doit contenir : min 8 caractères, 1 maj, 1 min, 1 chiffre, 1 caractère spécial.\n")


hash_mdp = hashlib.sha256(mdp.encode()).hexdigest()

print("\n🔐 Mot de passe haché (SHA-256) :")
print(hash_mdp)
