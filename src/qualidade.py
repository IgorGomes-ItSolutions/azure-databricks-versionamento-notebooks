"""Regras didáticas para registros fictícios; sem dependências externas."""
import csv
from pathlib import Path


def carregar(caminho):
    with Path(caminho).open(encoding="utf-8", newline="") as arquivo:
        return list(csv.DictReader(arquivo))


def preparar(registros):
    validos, rejeitados, duplicados = [], [], []
    vistos = {}
    for registro in registros:
        try:
            item = {"id": int(registro["id"]),
                    "documento": registro["documento"].strip(),
                    "quantidade": int(registro["quantidade"])}
            if item["id"] <= 0 or not item["documento"] or item["quantidade"] < 0:
                raise ValueError("id, documento ou quantidade inválidos")
        except (ValueError, TypeError, KeyError, AttributeError):
            rejeitados.append(dict(registro))
            continue
        if item["id"] in vistos:
            if vistos[item["id"]] != item:
                raise ValueError(f"ID conflitante: {item['id']}")
            duplicados.append(item)
            continue
        vistos[item["id"]] = item
        validos.append(item)
    return validos, rejeitados, duplicados
