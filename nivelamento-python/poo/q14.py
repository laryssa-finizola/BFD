class Livro:    
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

l1 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling")
l2 = Livro("Matéria escura", " Blake Crouch")


print(f"Título: {l1.titulo}, Autor: {l1.autor}")
print(f"Título: {l2.titulo}, Autor: {l2.autor}")