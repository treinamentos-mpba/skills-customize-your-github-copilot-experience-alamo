# 📘 Assignment: Jogo da Forca

## 🎯 Objetivo

Pratique strings, listas, seleção aleatória, loops e condicionais construindo um jogo da Forca interativo em Python.

## 📝 Tarefas

### 🛠️ Implementar a Mecânica do Jogo

#### Descrição
Crie a mecânica principal da Forca: escolha uma palavra secreta de uma lista predefinida e permita que a pessoa tente descobri-la informando uma letra por vez.

#### Requisitos
O programa concluído deve:

- Escolher aleatoriamente uma palavra de uma lista predefinida.
- Exibir cada letra ainda não descoberta como `_` e revelar as ocorrências da letra após um palpite correto.
- Começar com 6 tentativas incorretas e diminuir esse total quando a letra informada não estiver na palavra.
- Mostrar o progresso da palavra e o número de tentativas restantes a cada rodada.

### 🛠️ Tratar Palpites e Encerrar a Partida

#### Descrição
Complete o jogo para lidar com palpites repetidos e encerrar a partida quando a palavra for descoberta ou quando não restarem tentativas.

#### Requisitos
O programa concluído deve:

- Aceitar letras maiúsculas ou minúsculas sem diferenciar a caixa.
- Não diminuir as tentativas quando a pessoa informar uma letra que já escolheu.
- Encerrar quando todas as letras da palavra forem descobertas ou quando as tentativas incorretas chegarem a zero.
- Exibir uma mensagem de vitória ou derrota e, em caso de derrota, revelar a palavra secreta.

Exemplo de progresso:

```text
Palavra: _ _ _ _
Tentativas incorretas restantes: 6
Digite uma letra: a
Palavra: _ a _ a
```
