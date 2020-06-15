import os
from dotenv import load_dotenv
import vk_api
import telegram
import requests
import argparse


def post_vk(image_path, text_path):
    vk_session = vk_api.VkApi(login=vk_user_login, token=vk_user_token)
    vk = vk_session.get_api()

    upload = vk_api.VkUpload(vk_session)

    photo = upload.photo(
        image_path,
        album_id=272857318,
        group_id=195764581
    )
    with open(text_path, 'r') as caption:
        vk.wall.post(owner_id='-{}'.format(vk_group_id), message=caption.read(), from_group=1,
                     attachments='photo-{}_{}'.format(vk_group_id, photo[0]['id']))


def post_telegram(image_path, text_path):
    bot = telegram.Bot(token=telegram_token)
    with open(text_path, 'r') as caption:
        bot.send_photo(chat_id=telegram_channel, photo=open(image_path, 'rb'))
        bot.send_message(chat_id=telegram_channel, text=caption.read())


def post_facebook(image_path, text_path):
    url = "https://graph.facebook.com/v7.0/{}/photos".format(facebook_group_id)
    files = {'file': open(image_path, 'rb')}
    with open(text_path, 'r') as caption:
        payrole = {
            'caption': caption.read(),
            'access_token': facebook_token,
        }
        response = requests.post(url, files=files, data=payrole)


def parse_console_arguments():
    parser = argparse.ArgumentParser(description='Постинг в VK, Telegram, Facebook')
    parser.add_argument('image', help='Путь к изображению')
    parser.add_argument('text', help='Путь к тексту')
    parser.add_argument('-sf', '--skip_facebook', help='Не выкладывать в Facebook.', action='store_false')
    parser.add_argument('-st', '--skip_telegram', help='Не выкладывать в Telegram.', action='store_false')
    parser.add_argument('-sv', '--skip_vk', help='Не выкладывать во Вконтакте.', action='store_false')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    load_dotenv()

    vk_user_token = os.getenv('VK_USER_TOKEN')
    vk_user_login = os.getenv('VK_USER_LOGIN')
    vk_group_id = os.getenv('VK_GROUP_ID')

    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_channel = os.getenv('TELEGRAM_CHANEL_ID')

    facebook_token = os.getenv('FACEBOOK_TOKEN')
    facebook_group_id = os.getenv('FACEBOOK_GROUP_ID')

    args = parse_console_arguments()

    if args.skip_facebook:
        post_facebook(args.image, args.text)

    if args.skip_vk:
        post_vk(args.image, args.text)

    if args.skip_telegram:
        post_telegram(args.image, args.text)
