import asyncio
import json
from django.utils.decorators import classonlymethod
from django.views import View
from django.http import HttpResponse

phone = "79303821226"
leave_user_phone = "+79914176125"
# TG
api_id = None
api_hash = None

chat_name = "Test"


class AllUsers(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def get(self, request, *args, **kwargs):
        from telethon.sync import TelegramClient as mes

        async with mes(phone, api_id, api_hash) as client:
            my_dialog_id = await get_dialog_id(client)
            users = await client.get_participants(my_dialog_id)
            res = []
            for user in users:
                res.append({'username': user.username, 'id': user.id})
            "Mention [inline mention of a user](tg://user?id=user.id)"
        return HttpResponse(json.dumps(res), status=200)


class Leave(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def get(self, request, *args, **kwargs):
        from telethon.sync import TelegramClient as mes
        async with mes(leave_user_phone, api_id, api_hash) as client:
            my_dialog_id = await get_dialog_id(client)
            await client.delete_dialog(my_dialog_id)
        return HttpResponse(json.dumps("leave"), status=200)


async def get_dialog_id(client):
    my_dialog_id = None
    dialogs = await client.get_dialogs()
    for d in dialogs:
        if d.name == chat_name:
            my_dialog_id = d.id
            break
    return my_dialog_id



# async def main():
#     client = TelegramClient(phone, api_id, api_hash)
#     # client = TelegramClient('+79062570633', api_id, api_hash, proxy=(socks.HTTP, proxy.ip, proxy.port,
#     #                                                         True, proxy.login, proxy.proxy_password))
#     #
#     # client = TelegramClient(phone, api_id, api_hash,
#     #                         device_model='Xiaomi redmi note 7', app_version='Android 9')
#     # client = TelegramClient(phone, api_id, api_hash)
#     # first_name = ['Aaron', 'Abraham', 'Adam', 'Adrian', 'Aidan', 'Alan',
#     #               'Albert', 'Alejandro', 'Alex', 'Alexander', 'Alfred', 'Andrew', 'Angel', 'Anthony', 'Antonio',
#     #               'Ashton', 'Austin', 'Georgy', 'Gleb', 'Danila', 'Vladimir', 'Denis',
#     #               'Yevgeny', 'Ivan', 'Ilia', 'Innokenty', 'Maksim', 'Matvei', 'Matvei', 'Nikolay', 'Pavel',
#     #               'Svyatoslav', 'Ruslan', 'Semyon', 'Yaroslav', 'Yan', 'Filipp', 'Fedor', 'Timofey', 'Stepan'
#     #               ]
#     # last_name = ['Donovan', 'Douglas', 'Dowman', 'Dutton', 'Duncan', 'Dunce', 'Durham', 'Dyson', 'Babcock',
#     #              'Bargeman', 'Baldwin', 'Bargeman', 'Barnes', 'Becker', 'Birch', 'Carrington', 'Carter', 'Cook',
#     #              'Conors', 'Elmers', 'Enderson', 'Faber', 'Farrell', 'Flannagan', 'Fleming', 'Foster', 'Fraser',
#     #              'Gill', 'Goldman', 'Gustman', 'Hamphrey', 'Hardman', 'Harrison', 'Hodges', 'Fedor', 'Freeman',
#     #              'Fisher'
#     #              ]
#     # force_sms - for new users
#     # client.start(phone=phone, force_sms=True, first_name=first_name[random.randint(0, len(first_name) - 1)],
#     #              last_name=last_name[random.randint(0, len(last_name) - 1)])
#     client.start(phone=phone)
#     # channel = client(GetFullChannelRequest("Test"))
#     test_dialog = None
#     for dialog in client.iter_dialogs():
#         if dialog.title == 'Test':
#             test_dialog = dialog
#     users = []
#     for user in client.iter_participants(entity=test_dialog, limit=1000):
#         users.append({'user': user.username, 'id': user.id})
#         print(user.username)
#     return Response({'success': users}, status=status.HTTP_200_OK)
#
#
# @csrf_exempt
# @api_view(["GET"])
# @permission_classes((AllowAny,))
# def get_username(request):
#
#     asyncio.set_event_loop(asyncio.SelectorEventLoop())
#     client = TelegramClient(phone, api_id, api_hash)
#     # client = TelegramClient('+79062570633', api_id, api_hash, proxy=(socks.HTTP, proxy.ip, proxy.port,
#     #                                                         True, proxy.login, proxy.proxy_password))
#     #
#     # client = TelegramClient(phone, api_id, api_hash,
#     #                         device_model='Xiaomi redmi note 7', app_version='Android 9')
#     # client = TelegramClient(phone, api_id, api_hash)
#     # first_name = ['Aaron', 'Abraham', 'Adam', 'Adrian', 'Aidan', 'Alan',
#     #               'Albert', 'Alejandro', 'Alex', 'Alexander', 'Alfred', 'Andrew', 'Angel', 'Anthony', 'Antonio',
#     #               'Ashton', 'Austin', 'Georgy', 'Gleb', 'Danila', 'Vladimir', 'Denis',
#     #               'Yevgeny', 'Ivan', 'Ilia', 'Innokenty', 'Maksim', 'Matvei', 'Matvei', 'Nikolay', 'Pavel',
#     #               'Svyatoslav', 'Ruslan', 'Semyon', 'Yaroslav', 'Yan', 'Filipp', 'Fedor', 'Timofey', 'Stepan'
#     #               ]
#     # last_name = ['Donovan', 'Douglas', 'Dowman', 'Dutton', 'Duncan', 'Dunce', 'Durham', 'Dyson', 'Babcock',
#     #              'Bargeman', 'Baldwin', 'Bargeman', 'Barnes', 'Becker', 'Birch', 'Carrington', 'Carter', 'Cook',
#     #              'Conors', 'Elmers', 'Enderson', 'Faber', 'Farrell', 'Flannagan', 'Fleming', 'Foster', 'Fraser',
#     #              'Gill', 'Goldman', 'Gustman', 'Hamphrey', 'Hardman', 'Harrison', 'Hodges', 'Fedor', 'Freeman',
#     #              'Fisher'
#     #              ]
#     # force_sms - for new users
#     # client.start(phone=phone, force_sms=True, first_name=first_name[random.randint(0, len(first_name) - 1)],
#     #              last_name=last_name[random.randint(0, len(last_name) - 1)])
#     client.start(phone=phone)
#
#     # channel = client(GetFullChannelRequest("Test"))
#     test_dialog = None
#     for dialog in client.iter_dialogs():
#         if dialog.title == 'Test':
#             test_dialog = dialog
#     users = []
#     for user in client.iter_participants(entity=test_dialog, limit=1000):
#         users.append({'user': user.username, 'id': user.id})
#         print(user.username)
#     return Response({'success': users}, status=status.HTTP_200_OK)
#
#
# @csrf_exempt
# @api_view(["GET"])
# @permission_classes((AllowAny,))
# def leave(request):
#     tol_phone = '+79914176125'
#     asyncio.set_event_loop(asyncio.SelectorEventLoop())
#     client = TelegramClient(tol_phone, api_id, api_hash)
#     client.start(phone=tol_phone)
#
#     # channel = client(GetFullChannelRequest("Test"))
#     test_dialog = None
#     for dialog in client.iter_dialogs():
#         if dialog.title == 'Test':
#             dialog.delete()
#             client.delete_dialog(dialog.id)
#
#             return Response({'success': 'Ok'}, status=status.HTTP_200_OK)
#     return Response({'success': 'Not'}, status=status.HTTP_200_OK)