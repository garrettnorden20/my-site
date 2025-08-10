from app.models import Note


def test_note_model():
    note = Note(content="hi")
    assert note.content == "hi"
