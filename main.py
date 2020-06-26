# -*- coding: utf-8 -*-
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import random
import requests
import traceback
from photo import photokek, invert, make_3d
import os
from work_with_database import insert_information_to_database
import sqlite3

vk_session = vk_api.VkApi(token='4a2151457df20731fd1f0b6cf14d491fd5908e7c428df4ee2c'
                                '1bf7e74d7454fddef80690b946d5ef6e035')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '196559740')

sphere = ["возможно", 'лол, нет', 'ахах, даже не надейся, лошара', 'конечно, бро', '100 проц', 'хз']
owner_id = 318741811

db = sqlite3.connect('nicknames.db')
sql = db.cursor()


def tyanki(chat_id, username):
    num = str(random.randint(1, 192))
    random_url = num + '.jpg'
    random_url = '/usr/local/bin/evabot/tyanki/' + random_url
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(random_url)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f"photo{owner_id}_{photo_id}_{access_key}"

    vk.messages.send(peer_id=chat_id + 2000000000, random_id=get_random_id(),
                     message=f'{username}, руки на стол!',
                     attachment=attachment)


def kick(chat_id, username, message):
    urls = ['kick1', 'kick2', 'kick3', 'kick4', 'kick5', 'kick6', 'kick7']
    random_url = random.choice(urls) + '.jpg'
    random_url = '/usr/local/bin/evabot/kicks/' + random_url
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(random_url)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f"photo{owner_id}_{photo_id}_{access_key}"
    if len(message.split(' ')) == 3:
        name = message.split(' ')[2]
        vk.messages.send(peer_id=chat_id + 2000000000, random_id=get_random_id(),
                         message=f'{username} ударил {name} &#128074;',
                         attachment=attachment)
    elif len(message.split(' ')) == 2:
        vk.messages.send(peer_id=chat_id + 2000000000, random_id=get_random_id(),
                         message=f'{username} ударил себя',
                         attachment=attachment)
    else:
        name = message.split(' ')[2]
        text = message.split(' ')
        text.pop(0)
        text.pop(0)
        text.pop(0)
        text = ' '.join(text)
        vk.messages.send(peer_id=chat_id + 2000000000, random_id=get_random_id(),
                         message=f'{username} ударил{name}, '
                                 f'со словами: "{text}" &#128074;',
                         attachment=attachment)


def send_message(chat_id, message):
    vk.messages.send(random_id=get_random_id(),
                     peer_id=chat_id + 2000000000,
                     message=message)


def send_kek(chat_id, username):
    url1 = 'photo1.jpg'
    url2 = 'photo2.jpg'

    upload = vk_api.VkUpload(vk)
    photo1 = upload.photo_messages(url1)
    photo2 = upload.photo_messages(url2)

    owner_id = photo1[0]['owner_id']
    photo_id = photo1[0]['id']
    access_key = photo1[0]['access_key']

    attachment1 = f'photo{owner_id}_{photo_id}_{access_key}'

    owner_id = photo2[0]['owner_id']
    photo_id = photo2[0]['id']
    access_key = photo2[0]['access_key']

    attachment2 = f'photo{owner_id}_{photo_id}_{access_key}'

    vk.messages.send(peer_id=chat_id + 2000000000, random_id=get_random_id(),
                     message=f'{username}, держи',
                     attachment=[attachment1, attachment2])
    os.remove('photo1.jpg')
    os.remove('photo2.jpg')


def send_invert(chat_id, username):
    url_inverted = 'imginverted.jpg'
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(url_inverted)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'

    vk.messages.send(peer_id=chat_id + 2000000000, random_id=get_random_id(),
                     message=f'{username}, держи',
                     attachment=attachment)
    os.remove('imginverted.jpg')


def send_3d(chat_id, username):
    url_3d = 'imgres3d.jpg'
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(url_3d)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'

    vk.messages.send(peer_id=chat_id + 2000000000, random_id=get_random_id(),
                     message=f'{username}, держи',
                     attachment=attachment)
    os.remove('imgres3d.jpg')


def check_nickname(user_id):
    db = sqlite3.connect('nicknames.db')
    sql = db.cursor()
    sql.execute("SELECT user_id FROM nicknames")
    nicknames = sql.fetchall()
    if (sender_id,) not in nicknames:
        return vk.users.get(user_ids=event.object["from_id"])[0]['first_name']
    else:
        sql.execute(f"SELECT nickname FROM nicknames WHERE user_id = {user_id}")
        nickname_db = sql.fetchall()[0][0]
        db.commit()
        return nickname_db


while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                message = event.object["text"]
                if message.split(' ')[0].lower() == "ева" or message.split(' ')[0].lower() == "евочка" or \
                        message.split(' ')[0].lower() == "ева,":
                    sender_id = event.object['from_id']
                    username = check_nickname(sender_id)
                    id_chat = event.chat_id
                    command = message.lower().split(' ')
                    command.pop(0)
                    command = ' '.join(command)
                    if command == 'привет':
                        send_message(id_chat,
                                     f'{username}, приветики!!!')
                    elif command == 'сап':
                        send_message(id_chat,
                                     f'{username}, сап, омежка :3')
                    elif command == 'салам' or command == 'салам алейкум':
                        send_message(id_chat,
                                     f'{username}, алейкум асалам,'
                                     f' брат')
                    elif "шар" in command:
                        send_message(id_chat,
                                     f'{username}, {random.choice(sphere)}')
                    elif command == 'тянка' or command == 'тяночка' or command == 'тян':
                        tyanki(id_chat, username)
                    elif 'ударить' in command:
                        kick(id_chat, username, message)
                    elif command == 'фото кек':
                        try:
                            url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                            photokek(url)
                            send_kek(id_chat, username)
                        except BaseException:
                            send_message(id_chat, f'{username}, а где картинка ёпта?')
                    elif command == 'фото негатив':
                        try:
                            url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                            invert(url)
                            send_invert(id_chat, username)
                        except BaseException:
                            send_message(id_chat, f'{username}, а где картинка ёпта?')

                    elif 'фото 3д' in command:
                        command_3d = command.split(' ')
                        if len(command_3d) == 2:
                            try:
                                url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                                make_3d(url)
                                send_3d(id_chat, username)
                            except BaseException:
                                send_message(id_chat, f'{username}, а где картинка ёпта?')
                        else:
                            try:
                                delta = int(command_3d[-1])
                                url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                                make_3d(url, delta)
                                send_3d(id_chat, username)
                            except BaseException:
                                send_message(id_chat,
                                             f'{username}, либо нет пикчи, либо нет цифры')
                    elif 'выбери' in command:
                        try:
                            if ' или ' in command:
                                command = command.split(' ')
                                index = command.index('выбери')
                                command = command[index + 1:]
                                command = ' '.join(command)
                                command = command.split(' или ')
                                result = random.choice(command)
                                send_message(id_chat, f'{username}, я думаю, что "{result}"')
                            else:
                                send_message(id_chat, f'{username}, а где "или" ёпта?')
                        except BaseException:
                            pass
                    elif 'ты меня любишь' in command or 'ты меня не любишь' in command:
                        if sender_id == owner_id:
                            send_message(id_chat, f'Конечно, любимый &#128150; &#128150; &#128150;')
                        else:
                            send_message(id_chat, f'НЕТ, я люблю только моего *id318741811 (создателя)!')
                    elif 'ник ' in command:
                        command = command.split(' ')
                        command.pop(0)
                        nickname = command
                        nickname = ' '.join(nickname)
                        if len(command) < 20:
                            insert_information_to_database(sender_id, nickname)
                            send_message(id_chat, 'Ник установлен!')
                        else:
                            send_message(id_chat, 'Слишком много символов! (максимум 20)')



    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())
