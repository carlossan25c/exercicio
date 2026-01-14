from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario
from mini_biblioteca.emprestimos import Emprestimo


def test_criar_livro():
    livro = Livro("Python", "Autor", "L1")
    assert livro.disponivel is True


def test_criar_usuario():
    usuario = Usuario("Carlos", "U1")
    assert usuario.nome == "Carlos"


def test_criar_emprestimo():
    livro = Livro("Python", "Autor", "L1")
    usuario = Usuario("Carlos", "U1")
    emprestimo = Emprestimo(livro, usuario)

    assert emprestimo.ativo is True
    assert livro.disponivel is False
