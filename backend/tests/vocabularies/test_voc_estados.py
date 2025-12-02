from trepi.intranet import PACKAGE_NAME
from zope.schema.vocabulary import SimpleVocabulary

import pytest


class TestVocabEstados:
    name = f"{PACKAGE_NAME}.vocabulary.estados"

    @pytest.fixture(autouse=True)
    def _setup(self, get_vocabulary, portal):
        """Configura o vocabulário para os testes.

        get_vocabulary: Fixture para obter o vocabulário registrado.
                        Definida em pytest-plone.
        portal: Fixture do portal Plone.
                Definida em pytest-plone.
        """
        self.vocab = get_vocabulary(self.name, portal)

    def test_vocabulary(self):
        assert self.vocab is not None
        assert isinstance(self.vocab, SimpleVocabulary)

    @pytest.mark.parametrize(
        "token",
        ["PR", "SP", "MT", "PI"],
    )
    def test_token(self, token: str):
        """Verifica se o token existe no vocabulário."""
        assert token in list(self.vocab.by_token)
