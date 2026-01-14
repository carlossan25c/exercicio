import pytest
from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario
from mini_biblioteca.emprestimos import Emprestimo


def test_nao_pode_emprestar_livro_indisponivel():
    livro = Livro("Teste", "Autor", "001")
    usuario1 = Usuario("Ana", "U1")
    usuario2 = Usuario("João", "U2")

    Emprestimo(livro, usuario1)

    with pytest.raises(ValueError):
        Emprestimo(livro, usuario2)


def test_devolver_livro():
    livro = Livro("Teste", "Autor", "001")
    usuario = Usuario("Ana", "U1")
    emprestimo = Emprestimo(livro, usuario)

    emprestimo.devolver()

    assert emprestimo.ativo is False
    assert livro.disponivel is True
