import random
import json

import telebot
from telebot import types


"""Caminho do arquivo de configuração do tipo JSON."""
caminho_configuracao = 'config.json'

"""Grupos de mensagens suportados na configuração"""
grupos_validos = [
    "inscricao-concluida", "inscricao-ja-realizada",
    "cancelar-inscricao-concluida", "cancelar-inscricao-nao-inscrito",
    "respostas-agressivas", "resposta-concordar-agressivamente"
]


# Na thread inicial, configuramos e aguardamos as respostas do bot
if __name__ == "__main__":
    # Abrimos o arquivo de configuração como leitura
    with open(caminho_configuracao, mode='rt', encoding='utf-8') as arquivo:
        # Carregamos o JSON a partir do arquivo
        configuracao = json.load(arquivo)

    # Abrimos o arquivo de mensagens como leitura
    with open(configuracao['caminho-mensagens'], mode='rt', encoding='utf-8') as arquivo:
        # Carregamos o JSON a partir do arquivo
        mensagens = json.load(arquivo)

    # Com o token, registramos o bot
    bot = telebot.TeleBot(configuracao['token'])


    def salvar_configuracao():
        """Salva a configuração do bot no arquivo."""
        with open(caminho_configuracao, mode='wt', encoding='utf-8') as arquivo:
            json.dump(configuracao, arquivo, indent='\t')


    def pegar_mensagem_aleatoria(grupo):
        """Pega uma mensagem específica de um grupo determinado."""
        # Conferimos se o grupo é válido
        if grupo not in grupos_validos:
            raise ValueError('Grupo de mensagens inválido!')

        return random.choice(mensagens[grupo])


    # Registramos os handlers

    @bot.message_handler(commands=['inscrever'])
    def inscrever(mensagem):
        """Confere se o chat que enviou o comando '/inscrever' está inscrito e o inscreve se necessário."""
        # Conferimos se já é inscrito
        if mensagem.chat.id in configuracao['inscritas']:
            msg = pegar_mensagem_aleatoria('inscricao-ja-realizada')
            bot.send_message(mensagem.chat.id, msg)
        else:
            # Se não é, inscrevemos o ID e salvamos o JSON
            configuracao['inscritas'].append(mensagem.chat.id)
            salvar_configuracao()
            msg = pegar_mensagem_aleatoria('inscricao-concluida')
            bot.send_message(mensagem.chat.id, msg)


    @bot.message_handler(commands=['cancelar_inscricao'])
    def desinscrever(mensagem):
        """Confere se o chat que enviou o comando '/cancelar_inscricao' está inscrito e o desinscreve se necessário."""
        # Conferimos se o chat não está inscrito
        if mensagem.chat.id not in configuracao['inscritas']:
            msg = pegar_mensagem_aleatoria('cancelar-inscricao-nao-inscrito')
            bot.send_message(mensagem.chat.id, msg)
        else:
            # Se usuário foi inscrito, removemos e salvamos o JSON
            configuracao['inscritas'].remove(mensagem.chat.id)
            salvar_configuracao()
            msg = pegar_mensagem_aleatoria('cancelar-inscricao-concluida')
            bot.send_message(mensagem.chat.id, msg)


    @bot.message_handler(content_types=['text'])
    def receber_resposta(mensagem):
        # Ignoramos chats não inscritos
        if mensagem.chat.id not in configuracao['inscritas']:
            return

        # Conferimos as possibilidades de resposta de concordar
        valor = random.random()
        msg = None

        # Verificamos se temos que responder agressivamente
        if valor <= configuracao['probabilidade-resposta-concordar']:
            # Pegamos uma mensagem aleatória
            msg = pegar_mensagem_aleatoria('resposta-concordar-agressivamente')

        elif valor <= configuracao['probabilidade-resposta-agressiva']:
            # Pegamos uma mensagem aleatória
            msg = pegar_mensagem_aleatoria('respostas-agressivas')

        # Se vamos responder, enviamos a resposta
        if msg is not None:
            # Substituímos os termos disponíveis
            msg = msg.replace('{NOME}', mensagem.from_user.first_name)
            # Enviamos a mensagem respondendo a que recebemos
            bot.send_message(mensagem.chat.id, msg, reply_to_message_id=mensagem.message_id)


    # Início do programa

    def main():
        """Inicia o laço que responde às mensagens."""
        bot.polling()


    # Na thread inicial, executamos 'main()'
    main()
