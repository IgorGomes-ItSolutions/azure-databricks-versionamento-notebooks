# Versionamento de notebooks no Azure Databricks

Laboratório DIO de análise e qualidade de dados fictícios com Python, PySpark e SQL.

## Visão geral

| Item | Resumo |
|---|---|
| Objetivo | Limpar, validar e analisar documentos fictícios com código versionado |
| Situação | Execução no Azure documentada; testes locais e GitHub Actions aprovados |
| Limite | A esteira Azure Pipelines foi preparada, mas não executada por falta de agente |

## Entregas e organização

- [Notebook em Python](notebooks/01_documentos.py), [Jupyter importável](notebooks/01_documentos.ipynb) e [versão com resultados](notebooks/01_documentos_executado.ipynb).
- [Dados fictícios](data/documentos.csv), [regras de qualidade](src/qualidade.py) e [testes](tests/test_qualidade.py).
- [Workflow de qualidade](.github/workflows/qualidade.yml) e [Azure Pipelines](azure-pipelines.yml).
- [Guia de operação e referências oficiais](docs/operacao.md).

## Como começar

1. Leia o guia de operação.
2. Importe o notebook em um ambiente de estudo compatível.
3. Revise as células, a origem do CSV e os recursos disponíveis antes de executar.
4. Compare as saídas com o contrato abaixo. A execução em nuvem pode consumir créditos.

## Validação

Na raiz do repositório, com Python 3:

```bash
python -m unittest discover -s tests -v
python -m compileall -q src notebooks
```

Os três testes locais foram novamente aprovados na revisão do portfólio de 18/11/2026. Isso não representa uma nova execução no Azure.

| Indicador | Esperado |
|---|---:|
| Entrada | 9 registros |
| Válidos | 6 registros |
| Rejeitados | 2 registros |
| Duplicatas idênticas removidas | 1 |
| Soma das quantidades | 194 |
| Soma dos tipos acima de 30 | 130 |

IDs repetidos com conteúdos divergentes causam falha explícita. A execução em nuvem e suas saídas estão documentadas no [notebook executado](notebooks/01_documentos_executado.ipynb). O gráfico é uma evidência histórica, não uma execução feita pelo visitante.

## Decisões, limites e próximos passos

- Laboratório com dados sintéticos, sem resultados de produção.
- Comparação de resultados Python/PySpark e SQL para exercitar validação.
- A promoção para o ambiente de estudo é manual.
- Não há alegação de execução do Azure Pipelines.
- Próximos passos: revisar resultados, evoluir regras e documentar novas execuções quando realizadas.

## Autoria e aprendizado

Projeto de estudo de Igor Gomes, baseado no desafio DIO **Controle e Versionamento de Código no Notebook da Azure**. Ferramentas de IA apoiam o estudo e o desenvolvimento; os resultados devem ser conferidos por testes e execução.

[Voltar ao portfólio](https://github.com/IgorGomes-ItSolutions)
