# Roteiro de operação

## Importar e executar

1. No workspace Azure Databricks, crie uma pasta Git com a URL deste repositório ou importe os arquivos preservando `notebooks/` e `data/`.
2. Abra `notebooks/01_documentos.py` como notebook Databricks. Se a importação tratar o arquivo como texto, importe a versão `.ipynb`.
3. Selecione compute disponível. Em cluster clássico, use nó único, menor VM permitida e término automático de 10 minutos; confira o custo antes de iniciar. Não inicie recursos que ultrapassem o orçamento.
4. Ajuste o widget `arquivo_csv` para o caminho do CSV no workspace, se necessário.
5. Execute todas as células e confira: 9 entradas, 6 válidas, 2 rejeitadas, 1 duplicata e soma 194.
6. SQL usa limite fixo 30; o filtro PySpark usa o widget. Para comparar, mantenha o widget em 30.
7. Exporte `.ipynb` com os resultados fictícios revisados. Encerre o cluster.

## Git e revisão

Crie uma branch (`git switch -c feat/ajuste-filtro`), altere o notebook, rode os testes e abra um pull request. Revise código, nomes de colunas, tratamento de nulos e resultados. Não versionar saídas reais ou credenciais.

## Azure DevOps

`azure-pipelines.yml` contém a esteira de CI: testes Python, compilação e publicação dos notebooks como artefato. Crie um projeto, conecte o repositório e selecione esse YAML. Uma organização nova pode exigir autorização de paralelismo hospedado da Microsoft.

A promoção para o workspace é manual neste laboratório: importe o artefato aprovado e execute com compute controlado. Uma evolução de CD exige conexão de serviço com identidade federada, permissões mínimas e aprovação de ambiente. O YAML não cria clusters nem executa código de nuvem automaticamente.

## IA e revisão humana

O código foi elaborado com auxílio do agente de IA. Não se afirma uso do assistente nativo do Databricks sem evidência de execução nele. Sugestões da IA devem ser verificadas com testes, contratos de dados e comparação SQL/PySpark.

## Fontes

- [CI/CD com Azure DevOps e Databricks](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/ci-cd/azure-devops)
- [Avaliação do Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/getting-started/free-trial)
- [Pastas Git no Databricks](https://learn.microsoft.com/en-us/azure/databricks/repos/)
