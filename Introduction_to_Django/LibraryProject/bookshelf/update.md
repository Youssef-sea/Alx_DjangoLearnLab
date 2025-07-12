Update Operation

Command:
from bookshelf.models import Book
# 1. Récupérer le livre à mettre à jour
book = Book.objects.get(title="1984") # Assurez-vous d'utiliser le titre actuel du livre
# 2. Modifier l'attribut (ici, le titre)
book.title = "Nineteen Eighty-Four"
# 3. Sauvegarder les changements dans la base de données
book.save()
# Vérifier que le titre a été mis à jour
print(book.title)