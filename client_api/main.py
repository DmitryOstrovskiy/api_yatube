from pyrogram import Client

api_id = 21050232
api_hash = '8a7d1dad6fb9c9b15b34cfd355837f30'

app = Client('my_account', api_id, api_hash)

app.start()
app.send_message(1038958966, 'Привет, это я из кода пишу. Такое задание!')
app.stop()
