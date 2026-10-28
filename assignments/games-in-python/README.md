# 📘 Assignment: Jogo da Forca

## 🎯 Objective

Pratique strings, listas, seleção aleatória, loops e condicionais construindo um jogo da Forca interativo em Python.

## 📝 Tasks

### 🛠️ Criar o Jogo da Forca

#### Descrição
Implemente um jogo em que a pessoa tenta descobrir uma palavra secreta, informando uma letra por vez. A cada rodada, mostre as letras já descobertas e quantas tentativas incorretas ainda restam.

#### Requisitos
O programa concluído deve:

- Escolher aleatoriamente uma palavra de uma lista predefinida.
- Exibir cada letra ainda não descoberta como `_` e atualizar o progresso após cada palpite correto.
- Solicitar um palpite de uma letra por rodada e aceitar letras maiúsculas ou minúsculas.
- Começar com 6 tentativas incorretas e diminuir esse total quando o palpite não estiver na palavra.
- Não diminuir as tentativas quando a letra já tiver sido escolhida.
- Encerrar quando a palavra for descoberta ou quando não restarem tentativas.
- Exibir uma mensagem indicando vitória ou derrota; em caso de derrota, revelar a palavra secreta.

Exemplo de progresso:

```text
Palavra: _ _ _ _
Tentativas incorretas restantes: 6
Digite uma letra: a
Palavra: _ a _ a
```
