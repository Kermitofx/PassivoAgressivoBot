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
    "token": "INSIRA TOKEN AQUI",
    "inscritas": []
}

```

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
conversas inscritas (que receberão as respostas do bot).
