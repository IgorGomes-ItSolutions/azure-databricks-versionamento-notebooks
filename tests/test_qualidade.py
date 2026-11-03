import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from qualidade import carregar, preparar


class QualidadeTest(unittest.TestCase):
    def test_contrato_dados_ficticios(self):
        bruto = carregar(RAIZ / "data" / "documentos.csv")
        validos, rejeitados, duplicados = preparar(bruto)
        self.assertEqual((len(bruto), len(validos), len(rejeitados), len(duplicados)), (9, 6, 2, 1))
        self.assertEqual(sum(x["quantidade"] for x in validos), 194)
        self.assertEqual([x["documento"] for x in validos if x["quantidade"] > 30],
                         ["intimação", "mandado de prisão", "inquérito"])

    def test_id_conflitante_falha_em_vez_de_escolher_linha(self):
        with self.assertRaisesRegex(ValueError, "ID conflitante"):
            preparar([{"id": "1", "documento": "teste", "quantidade": "2"},
                      {"id": "1", "documento": "teste", "quantidade": "3"}])

    def test_entrada_invalida_e_zero_permitido(self):
        validos, rejeitados, _ = preparar([
            {"id": "1", "documento": " teste ", "quantidade": "0"},
            {"id": "2", "documento": "teste", "quantidade": "abc"},
            {"id": "0", "documento": "teste", "quantidade": "1"}])
        self.assertEqual(validos, [{"id": 1, "documento": "teste", "quantidade": 0}])
        self.assertEqual(len(rejeitados), 2)


if __name__ == "__main__":
    unittest.main()
