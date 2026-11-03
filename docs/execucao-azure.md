# Execução no Azure Databricks

Workspace real criado em 03/11/2026, East US, Premium/Serverless. A assinatura Azure existente foi preservada; não foi migrada para pagamento conforme o uso.

O console exibiu que não suporta controle automatizado de navegador. A importação foi realizada pela CLI oficial Databricks v1.23.0 após autorização OAuth manual do titular. Não foram exportados tokens para o repositório.

Objetos importados e verificados pela API:

- `notebooks/01_documentos`: objeto NOTEBOOK, linguagem Python.
- `data/documentos.csv`: objeto FILE com os nove registros fictícios.

## Tentativa em modo econômico

- Run: `1085585563550588`.
- Modo: `STANDARD`.
- Resultado da tarefa: `TIMEDOUT`.
- Duração total informada: 188.747 ms.
- A tarefa permaneceu aguardando compute; nenhum resultado de Spark/SQL é atribuído a essa tentativa.

O tempo de inicialização normal do modo econômico pode ser de quatro a seis minutos, conforme a [documentação oficial](https://learn.microsoft.com/en-us/azure/databricks/jobs/run-serverless-jobs). O limite curto configurado para o laboratório interrompeu essa tentativa.

A esteira Azure DevOps foi criada, mas não encontrou agente disponível. Os três testes de regras Python e a compilação passaram no GitHub Actions. A execução de Spark/SQL é uma verificação distinta desses testes.

## Execução concluída

Após autorização específica do titular, foi usada uma nova execução em `PERFORMANCE_OPTIMIZED`, sem alterar a assinatura:

- Run: `323963490686739`; tarefa: `913857914583256`.
- Estado: `TERMINATED / SUCCESS`.
- Preparação: 6 segundos; execução: 57 segundos; total: 63,888 segundos.
- Resultado: 9 linhas brutas, 6 válidas, 2 rejeitadas, 1 duplicata removida.
- Soma: 194; média por tipo: 32,33.
- Filtro SQL e PySpark: intimação 51, mandado de prisão 45, inquérito 34.
- Verificações de equivalência e totais passaram; gráfico gerado.

O notebook executado no repositório foi reconstruído a partir das saídas reais fornecidas por `jobs export-run`. Metadados de identidade e configurações internas do export foram omitidos; as tabelas, stdout e PNG foram preservados. O campo `execucao` no notebook registra essa proveniência.

Não foi usado o assistente nativo do Databricks. O auxílio de IA ocorreu na elaboração do código neste agente, com validação automatizada e execução real no Azure. O Azure Repos contém o snapshot inicial do código (`35532af`); a documentação e as evidências posteriores estão no GitHub.
