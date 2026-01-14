from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario
from mini_biblioteca.emprestimos import Emprestimo


def main():
    usuario = Usuario(nome="Carlos", id_usuario="U001")
    livro = Livro(titulo="Python Básico", autor="Guido", codigo="L001")

    emprestimo = Emprestimo(livro=livro, usuario=usuario)

    print(f"Livro disponível após empréstimo? {livro.disponivel}")
    print(f"Empréstimo ativo? {emprestimo.ativo}")

    emprestimo.devolver()

    print(f"Livro disponível após devolução? {livro.disponivel}")
    print(f"Empréstimo ativo após devolução? {emprestimo.ativo}")


if __name__ == "__main__":
    main()
