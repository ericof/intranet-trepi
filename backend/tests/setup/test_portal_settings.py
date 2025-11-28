"""Portal settings tests."""

from plone import api

import pytest


class TestPortalSettings:
    """Test portal settings."""

    @pytest.mark.parametrize(
        "key,expected",
        [
            ("plone.site_title", "Intranet do TRE-PI"),
            ("plone.email_from_name", "Intranet do TRE-PI"),
            ("plone.email_from_address", "intranet@tre-pi.jus.br"),
            ("plone.smtp_host", "localhost"),
            ("plone.smtp_port", 25),
            ("plone.navigation_depth", 4),
            ("plone.twitter_username", "ericof"),
            ("plone.default_language", "pt-br"),
            (
                "plone.available_languages",
                [
                    "pt-br",
                ],
            ),
            ("plone.portal_timezone", "America/Sao_Paulo"),
            (
                "plone.available_timezones",
                [
                    "America/Sao_Paulo",
                ],
            ),
        ],
    )
    def test_settings(self, portal, key: str, expected: str | int | list[str]):
        """Test that the portal title is set correctly."""
        value = api.portal.get_registry_record(key)
        assert value == expected
