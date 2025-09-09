Motivos de adotar os índices que foram adotados:
-PRIMARY: 
	Automático ao gerar as tabelas
-Foreign keys: 
	Boas práticas ao permitir mais velocidade em joins, especialmente em EstadoControle que é basicamente de onde sai o histórico.
-name em Benchmark e Controle: 
	Se for comum buscar Benchmark e Controle por nome
-(controleIdFk, dataHora) em EstadoControle:
	Esse é o índice mais importante.
	A tabela EstadoControle provavelmente vai crescer muito rápido, porque cada vez que um controle muda de estado, é inserida uma nova linha.
	Por isso, consultas relacionadas ao estado atual e ao histórico precisam ser eficientes, na verdade tanto pela frequência de uso quanto pela relevância de ser tratar de um histórico.
	Esse índice é fundamental porque:
	Permite localizar rapidamente o estado atual de um controle (último registro por data/hora).
	Otimiza buscas por intervalos de tempo.
	Facilita a recuperação do estado em uma data/hora específica.
	Em resumo, ele atende diretamente aos três cenários propostos no desafio.