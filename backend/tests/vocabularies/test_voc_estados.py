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
        "token,title",
        [["PR", "Paraná"], ["SP", "São Paulo"], ["MT", "Mato Grosso"], ["PI", "Piauí"]],
    )
    def test_terms(self, token: str, title: str):
        """Testa os termos existentes no vocabulário."""
        term = self.vocab.getTermByToken(token)
        assert term is not None
        assert term.title == title

    def test_total_terms(self):
        """Testa o total de termos no vocabulário."""
        expected_total = 27  # Total de estados do Brasil
        assert len(self.vocab) == expected_total
