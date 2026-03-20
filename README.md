# Exercício 2 — Claude-Autofix-Action

## Introdução

Este exercício tem o objetivo de testar o projeto Claude Autofix Action, disponível em [https://github.com/enriconunes/claude-autofix-action](https://github.com/enriconunes/claude-autofix-action). É importante manter a estrutura de ficheiros original e descrita no README do projeto; assim como proceder às configurações necessárias dentro repositório que forem utilizar. São as seguintes:

---

- **Criar um repositório publico** (com este código)

- **Configurar algumas definições:**  
  `Settings → Actions → General → Workflow permissions`
  - Selecionar **"Read and write permissions"**
  - Marcar **"Allow GitHub Actions to create and approve pull requests"**
  - Clicar **Save**

- **Adicionar chave de API Anthropic:**  
  `Settings → Secrets and variables → Actions → New repository secret`

  | Name | Value |
  |------|-------|
  | `ANTHROPIC_API_KEY` | A tua chave de console.anthropic.com |

---

## Exercício 2 — Quando é útil

Este exercício tem como objetivo mostrar a ferramenta em casos um pouco mais concretos. Enquanto numa divisão é fácil identificar que não podemos dividir por 0, em casos ligeiramente mais elaborados facilmente pode escapar algo que não pretendemos. Aqui pretende-se analisar o código ou fazer logo um commit e PR, para vermos a resposta do agente.
