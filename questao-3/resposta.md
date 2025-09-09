
## Questão 3: Descrição em detalhes para automação do processo utilizando a perspectiva Problema → Causa → Solução

### 1. Problema: Empacotamento manual
- **Causa:** Não existe pipeline automatizado para buildar os componentes.  
- **Solução:** Criar um **pipeline de CI/CD com GitHub Actions** que:  
  - Executa `npm ci`  
  - Roda testes automatizados (`npm test`)  
  - Gera build do frontend (`npm run build`)  
  - Empacota o backend (`npm install --production` ou build do TypeScript)  
  - Produz **artefatos versionados** (Docker image ou `.zip`) prontos para deploy.

---

### 2. Problema: Deploy manual em homologação e produção
- **Causa:** Falta de automação no deploy, feito via cópia manual.  
- **Solução:**  
  - Usar **Docker + Docker Compose** ou **Kubernetes** para padronizar o deploy.  
  - Configurar **pipelines separados**:  
    - Deploy automático em **homologação**: sempre que um PR é mergeado em `develop`.  
    - Deploy em **produção**: via **approval step** após validação em homologação.

---

### 3. Problema: Retrabalho e risco de inconsistência entre ambientes
- **Causa:** Repetição do processo manual aumenta a chance de subir versões diferentes.  
- **Solução:**  
  - Versionar a aplicação em **Docker images com tags** (`app:1.0.3`).  
  - Usar a **mesma imagem** em homologação e produção.  
  - Adicionar **pipeline de promoção**: se a versão `1.0.3` for validada em homologação → promover para produção.
