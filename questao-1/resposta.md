## QUESTÃO 1: Motivos de adotar os índices que foram definidos

- **PRIMARY**  
  - Criado automaticamente ao gerar as tabelas.  

- **Foreign Keys**  
  - Seguem boas práticas ao permitir mais velocidade em *joins*, especialmente em `EstadoControle`, que é basicamente de onde sai o histórico.  

- **`name` em Benchmark e Controle**  
  - Útil se for comum buscar Benchmark e Controle pelo nome.  

- **`(controleIdFk, dataHora)` em EstadoControle**  
  - Este é o índice mais importante.  
  - A tabela `EstadoControle` provavelmente vai crescer muito rápido, porque a cada mudança de estado de um controle, é inserida uma nova linha.  
  - Por isso, consultas relacionadas ao **estado atual** e ao **histórico** precisam ser eficientes, tanto pela frequência de uso quanto pela relevância do histórico.  
  - Este índice é fundamental porque:  
    - Permite localizar rapidamente o **estado atual** de um controle (último registro por data/hora).  
    - Otimiza buscas por **intervalos de tempo**.  
    - Facilita a recuperação do **estado em uma data/hora específica**.  
  - **Em resumo:** atende diretamente aos três cenários propostos no desafio.
