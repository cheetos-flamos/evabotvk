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
import datetime

vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '196559740')

sphere = ["возможно", 'лол, нет', 'ахах, даже не надейся, лошара', 'конечно, бро', '100 проц', 'хз']
owner_id = 318741811


def send_message(chat_id, message):
    vk.messages.send(random_id=get_random_id(),
                     peer_id=chat_id + 2000000000,
                     message=message)


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


def kick(chat_id, username, kick_command, sex_id):
    try:
        urls = ['kick1', 'kick2', 'kick3', 'kick4', 'kick5', 'kick6', 'kick7']
        random_url = random.choice(urls) + '.jpg'
        random_url = '/usr/local/bin/evabot/kicks/' + random_url
        upload = vk_api.VkUpload(vk)
        photo = upload.photo_messages(random_url)
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        attachment = f"photo{owner_id}_{photo_id}_{access_key}"
        kick_command = kick_command.split(' ')
        kick_command.pop(0)
        if 'тест' in kick_command:
            kick_command.remove('тест')
        kick_command = ' '.join(kick_command)
        if sex_id == 1:
            postfix = 'а'
        else:
            postfix = ''
        if ':' in kick_command:
            kick_command = kick_command.split(':')
            name = kick_command[0]
            with_words = kick_command[1]
            vk.messages.send(peer_id=chat_id + 2000000000, random_id=get_random_id(),
                             message=f'{username} ударил{postfix} {name} со словами: "{with_words}" &#128074;',
                             attachment=attachment)
        else:
            name = kick_command
            vk.messages.send(peer_id=chat_id + 2000000000, random_id=get_random_id(),
                             message=f'{username} ударил{postfix} {name} &#128074;',
                             attachment=attachment)
    except Exception:
        send_message(chat_id, 'Ошибка. Запишите команду, как на примере: "Ева ударить Обама" или '
                              'Ева ударить Обама: получай!')


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
    if (user_id,) not in nicknames:
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
                    time_start = datetime.datetime.now()
                    sender_id = event.object['from_id']
                    sex = vk.users.get(user_ids=sender_id, fields='sex')[0]['sex']
                    username = check_nickname(sender_id)
                    id_chat = event.chat_id
                    command = message.split(' ')
                    command.pop(0)
                    command = ' '.join(command)
                    command_lower = command.lower()
                    if command_lower == 'привет':
                        send_message(id_chat,
                                     f'{username}, приветики!!!')
                    elif command_lower == 'сап':
                        send_message(id_chat,
                                     f'{username}, сап, омежка :3')
                    elif command_lower == 'салам' or command_lower == 'салам алейкум':
                        send_message(id_chat,
                                     f'{username}, алейкум асалам,'
                                     f' брат')
                    elif "шар" in command_lower:
                        send_message(id_chat,
                                     f'{username}, {random.choice(sphere)}')
                    elif 'тянка' in command_lower or 'тяночка' in command_lower or 'тян' in command_lower:
                        tyanki(id_chat, username)
                    elif 'ударить' in command_lower:
                        kick(id_chat, username, command, sex)
                    elif 'фото кек' in command_lower:
                        try:
                            url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                            photokek(url)
                            send_kek(id_chat, username)
                        except BaseException:
                            send_message(id_chat, f'{username}, а где картинка ёпта?')
                    elif 'фото негатив' in command_lower:
                        try:
                            url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                            invert(url)
                            send_invert(id_chat, username)
                        except Exception:
                            send_message(id_chat, f'{username}, а где картинка?')
                    elif 'фото 3д' in command_lower:
                        command_3d = command.split(' ')
                        try:
                            url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                            make_3d(url)
                            send_3d(id_chat, username)
                        except Exception:
                            send_message(id_chat, f'{username}, а где картинка?')
                    elif 'выбери' in command_lower:
                        if ' или ' in command_lower:
                            command_choose = command_lower.split(' ')
                            index = command_choose.index('выбери')
                            command_choose = ' '.join(command_choose[index + 1:]).split(' или ')
                            result = random.choice(command_choose)
                            send_message(id_chat, f'{username}, я думаю, что "{result}"')
                        else:
                            send_message(id_chat, f'{username}, а где "или" ёпта?')
                    elif 'ты меня любишь' in command or 'ты меня не любишь' in command:
                        if sender_id == owner_id:
                            send_message(id_chat, f'Конечно, любимый &#128150; &#128150; &#128150;')
                        else:
                            send_message(id_chat, f'НЕТ, я люблю только моего *id318741811 (создателя)!')
                    elif 'ник ' in command:
                        nickname = command.split(' ')
                        nickname.pop(0)
                        if 'тест' in nickname:
                            nickname.remove('тест')
                        nickname = ' '.join(nickname)
                        if 2 <= len(nickname) < 20:
                            insert_information_to_database(sender_id, nickname)
                            send_message(id_chat, 'Ник установлен!')
                        else:
                            send_message(id_chat, 'Слишком много символов! (максимум 20, минимум 2)')
                    elif 'кто ' in command:
                        users = []
                        dictionary_with_user_data = vk.messages.getConversationMembers(peer_id=id_chat + 2000000000)
                        for user in dictionary_with_user_data['items']:
                            if str(user['member_id'])[0] != '-':
                                users.append(int(user['member_id']))
                        random_user = random.choice(users)
                        user_get = vk.users.get(user_ids=(random_user))
                        user_get = user_get[0]
                        first_name = user_get['first_name']
                        last_name = user_get['last_name']
                        full_name = first_name + " " + last_name
                        send_message(id_chat, f'Уверена, что это {full_name}')
                    time_finish = datetime.datetime.now()
                    time_delta = str(time_finish - time_start).split(':')[2]
                    if ' тест' in command_lower:
                        send_message(id_chat, f'Задача выполнялась: {time_delta} секунд')





    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())
