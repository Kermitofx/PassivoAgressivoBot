# PassivoAgressivoBot

Esse é o bot que, em 3% das mensagens dentro do chat, te responde de forma
agressiva, mas que, em 0,1% das mensagens, concorda com você ainda de forma
agressiva.

Disponível em [@PassivoAgressivoBot](https://t.me/PassivoAgressivoBot) no
[Telegram](https://telegram.org/).


## Configurando o bot

Para executar o bot, é necessário possuir um
[_token_](https://core.telegram.org/bots#generating-an-authorization-token) de
Telegram e escrever no arquivo `config.json`, que é ignorado pelo GitHub para
segurança. Seu exemplo pode ser econtrado abaixo:
```
{
    "caminho-mensagens": "mensagens.json",
    "token": "INSIRA TOKEN AQUI",
    "probabilidade-resposta-agressiva": 0.03,
    "probabilidade-resposta-concordar": 0.001,
    "inscritas": []
}

```

A probabilidade deve ser um valor no invervalo `[ 0, 1 )`. Se a resposta é
de concordar, não será agressiva.

Além da configuração, precisamos ter instalado a API utilizada
[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) através do
comando:
```
$ pip3 install --user pytelegrambotapi
```

E executar:
```
$ python3 passivo-agressivo.py
```


## Resumo de funcionamento

O bot utiliza o arquivo de configuração em formato JSON como banco de dados de
conversas inscritas (que receberão as respostas do bot). Além disso, há um
arquivo JSON para armazenar as mensagens agressivas.

As mensagens podem possuir algumas chaves para serem substituídas por
informações. São elas:

| Chave | Substituto |
|----------------------|
| `{NOME}` | Nome de quem enviou a mensagem |
