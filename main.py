# -*- coding: utf-8 -*-
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import random
import requests
import traceback
from photo import photokek, invert, make_3d
import os

vk_session = vk_api.VkApi(token='4a2151457df20731fd1f0b6cf14d491fd5908e7c428df4ee2c'
                                '1bf7e74d7454fddef80690b946d5ef6e035')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '196559740')

sphere = ["возможно", 'лол, нет', 'ахах даже не надейся лошара', 'конечно, бро', '100 проц', 'хз']


def tyanki(chat_id, event, username):
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


def kick(chat_id, event, username, message):
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
                         message=f'{username} уебал {name} &#128074;',
                         attachment=attachment)
    elif len(message.split(' ')) == 2:
        vk.messages.send(peer_id=chat_id + 2000000000, random_id=get_random_id(),
                         message=f'{username} уебал себя',
                         attachment=attachment)
    else:
        name = message.split(' ')[2]
        text = message.split(' ')
        text.pop(0)
        text.pop(0)
        text.pop(0)
        text = ' '.join(text)
        vk.messages.send(peer_id=chat_id + 2000000000, random_id=get_random_id(),
                         message=f'{username} уебал {name}, '
                                 f'со словами: "{text}" &#128074;',
                         attachment=attachment)


def send_message(random_id, chat_id, message):
    vk.messages.send(random_id=get_random_id(),
                     peer_id=chat_id + 2000000000,
                     message=message)


def send_kek(chat_id, event, username):
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


def send_invert(chat_id, event, username):
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


def send_3d(chat_id, event, username):
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


while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                message = event.object["text"]
                if message.split(' ')[0].lower() == "ева" or message.split(' ')[0].lower() == "евочка" or \
                        message.split(' ')[0].lower() == "ева,":
                    username = vk.users.get(user_ids=event.object["from_id"])[0]['first_name']
                    command = message.lower().split(' ')
                    command.pop(0)
                    command = ' '.join(command)
                    if command == 'привет':
                        send_message(0, event.chat_id,
                                     f'{username}, приветики!!!')
                    elif command == 'сап':
                        send_message(0, event.chat_id,
                                     f'{username}, сап, омежка :3')
                    elif command == 'салам' or command == 'салам алейкум':
                        send_message(0, event.chat_id,
                                     f'{username}, алейкум асалам,'
                                     f' брат')
                    elif "шар" in command:
                        send_message(0, event.chat_id,
                                     f'{username}, {random.choice(sphere)}')
                    elif command == 'тянка' or command == 'тяночка' or command == 'тян':
                        tyanki(event.chat_id, event, username)
                    elif 'уебать' in command:
                        kick(event.chat_id, event, username, message)
                    elif command == 'фото кек':
                        try:
                            url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                            photokek(url)
                            send_kek(event.chat_id, event, username)
                        except BaseException:
                            send_message(0, event.chat_id, f'{username}, а где картинка ёпта?')
                    elif command == 'фото негатив':
                        try:
                            url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                            invert(url)
                            send_invert(event.chat_id, event, username)
                        except BaseException:
                            send_message(0, event.chat_id, f'{username}, а где картинка ёпта?')

                    elif 'фото 3д' in command:
                        command_3d = command.split(' ')
                        if len(command_3d) == 2:
                            try:
                                url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                                make_3d(url)
                                send_3d(event.chat_id, event, username)
                            except BaseException:
                                send_message(0, event.chat_id, f'{username}, а где картинка ёпта?')
                        else:
                            try:
                                delta = int(command_3d[-1])
                                url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
                                make_3d(url, delta)
                                send_3d(event.chat_id, event, username)
                            except BaseException:
                                send_message(0, event.chat_id,
                                             f'{username}, либо нет пикчи, либо нет цифры')


    except BaseException:
        a = traceback.format_exc()
        print(a)
