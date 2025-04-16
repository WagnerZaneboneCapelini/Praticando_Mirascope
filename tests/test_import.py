"""Test Snap Package Template."""

import praticando_mirascope


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(praticando_mirascope.__name__, str)
