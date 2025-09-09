# Backup Automation Script

Resposta para a questão de Automação de Ambientes Operacionais.

Aqui veremos o que o script faz e como executá-lo.

---

## O que o script faz

1. **Lista** todos os arquivos dentro da pasta `backupsFrom/`, incluindo:
   - Nome do arquivo  
   - Tamanho (bytes)  
   - Data da última modificação  

2. **Salva o resultado** em `backupsFrom.log`.

3. **Remove** todos os arquivos com mais de 3 dias de criação.

4. **Copia** os arquivos com até 3 dias de criação para `backupsTo/`.

5. **Salva o resultado** da cópia em `backupsTo.log`.

---

## Estrutura de pastas esperada

├── script.py

├── backupsFrom/ # Onde os arquivos de origem ficam

├── backupsTo/ # Onde os arquivos recentes serão copiados


---

## Como executar

### Pré-requisitos
- Python 3 instalado

### Passos
1. No terminal, clone o repositório e adentre a pasta da questão 2:
   ```bash
   git clone https://github.com/joaop-Cardoso/desafio-valcann-backend.git
   cd desafio-valcann-backend
   cd questao-2

2. Crie as pastas necessárias:
    ```bash
    mkdir backupsFrom backupsTo
    ```

3. Coloque alguns arquivos de teste .txt em `backupsFrom/`.

4. Execute o script:
    ```bash
    python3 backupScript.py
    ```
5. Verifique os resultados:
- O log `backupsFrom.log` terá os arquivos originais listados.
- Arquivos com até 3 dias foram copiados para `backupsTo/` e listados em `backupsTo.log`.
- Arquivos antigos (> 3 dias) foram removidos.

---

## Exemplo de saída

### backupsFrom.log
```
Execução em: 2025-09-09 15:00:29.582764
----------------------------------------
Nome: teste.txt | Tamanho: 0 bytes | Criação: 2025-09-09 14:43:30.882909 | Modificação: 2025-09-09 14:43:30.882909

```

### backupsTo.log
```
Execução em: 2025-09-09 15:00:29.582764
----------------------------------------
Nome: teste 2.txt | Tamanho: 0 bytes | Criação: 2025-09-09 14:43:30.882909 | Modificação: 2025-09-09 14:43:30.882909
