from app.settings import Settings


def test_settings_defaults():
    s = Settings()
    assert s.app_name == "my-site"
