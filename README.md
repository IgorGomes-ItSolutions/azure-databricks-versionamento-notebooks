# Versionamento de notebooks no Azure Databricks

Laboratório para o desafio DIO **Controle e Versionamento de Código no Notebook da Azure**. Analisa documentos inteiramente fictícios com Python, PySpark e SQL, incluindo regras de qualidade, filtros, sumarização e gráfico.

## Entregáveis

- [Notebook Databricks em código-fonte](notebooks/01_documentos.py) e [formato Jupyter importável](notebooks/01_documentos.ipynb).
- [CSV fictício](data/documentos.csv) com duplicata e registros inválidos intencionais.
- Regras Python e três testes automatizados.
- CI no GitHub Actions e configuração equivalente em [Azure Pipelines](azure-pipelines.yml).
- [Roteiro de importação, Git, IA e operação](docs/operacao.md).

## Contrato de dados

| Indicador | Resultado esperado |
|---|---:|
| Registros de entrada | 9 |
| Tipos válidos após limpeza | 6 |
| Rejeitados | 2 |
| Duplicatas idênticas removidas | 1 |
| Total de documentos | 194 |
| Total dos tipos acima de 30 | 130 |

Os tipos acima de 30 representam 67,01% do total. Valores negativos e nomes vazios são rejeitados. IDs iguais com conteúdos diferentes causam falha explícita, evitando escolher registros arbitrariamente.

## Validação e estado de execução

Os três testes Python passaram localmente em 03/11/2026, e a sintaxe dos arquivos Python foi validada. A execução do notebook no Azure e a conexão do Azure DevOps estão em preparação; este registro será atualizado com evidências reais. A versão `.ipynb` inicial não contém resultados de execução.

```powershell
python -m unittest discover -s tests -v
python -m compileall -q src notebooks
```

## Organização e aprendizado

Python fornece listas, dicionários, leitura de arquivo e parâmetros. PySpark manipula DataFrames. SQL consulta a view temporária criada pelo notebook. As duas consultas são comparadas por verificações no próprio notebook.

O fluxo de versionamento é branch → revisão → testes → merge → artefato aprovado → importação no workspace. A promoção é manual para evitar execuções e custos inesperados. Código gerado com auxílio de IA deve ser revisado; não há alegação de uso do assistente nativo sem evidência.

## Custos e segurança

Somente dados fictícios; nenhum token ou senha no repositório. Limite autorizado para este laboratório: US$ 5 dos créditos existentes, sem migração da assinatura. A tentativa de plano Databricks Trial foi recusada porque a assinatura é Azure Free Trial; essa tentativa não representa um workspace ou cluster em execução.

As referências oficiais e o roteiro completo estão em [docs/operacao.md](docs/operacao.md).
