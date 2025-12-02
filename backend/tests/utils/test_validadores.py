from trepi.intranet.utils import validadores

import pytest


@pytest.mark.parametrize(
    "value,expected",
    [
        ["1@tre-pi.jus.br", True],
        ["foobar@tre-pi.jus.br", True],
        ["bar-foo@tre-pi.jus.br", True],
        ["1@tre-pi.jus.br.br", False],
        ["foobar@tre-pi.jus.br.br", False],
        ["bar-foo@tre-pi.jus.br.br", False],
        ["ericof@simplesconsultoria.com.br", False],
        ["ti@foo.bar", False],
    ],
)
def test_is_valid_email(value: str, expected: bool):
    """Testa a função is_valid_email."""
    assert validadores.is_valid_email(value) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ["61999528312", True],
        ["65-99952.8312", False],
        ["(61)999528312", False],
        ["6132104100", True],
        ["5132104100", True],
        [" ", False],
        ["(999)1234566", False],
    ],
)
def test_is_valid_telefone(value: str, expected: bool):
    """Testa a função test_is_valid_telefone."""
    assert validadores.is_valid_telefone(value) is expected
