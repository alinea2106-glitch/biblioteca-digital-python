from src.main import listar_documentos

def test_listar_documentos():
    resultado = listar_documentos()
    assert isinstance(resultado, dict)
