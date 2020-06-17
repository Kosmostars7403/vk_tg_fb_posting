# Скрипт постинга в VK, Telegram, Facebook

Скрипт для одновременного или выборочного постинга по соц. сетям.

### Как установить

Для запуска программы у вас уже должен быть установлен Python 3. 

Установите зависимости командой в терминале:

```
$ pip install -r requirements.txt
```

Чтобы начать постинг, в каждой соц сети придется получить токен.
1. для телеграмм [инструкция](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)
2. для VK [инструкция](https://devman.org/qna/63/kak-poluchit-token-polzovatelja-dlja-vkontakte/)
3. для Facebook [инструкция](https://developers.facebook.com/docs/graph-api/explorer/)

После всех мучений с получением токенов создайте файл .env и заполните следующим образом:

`VK_USER_TOKEN`=ваш_токен_ВК

`VK_USER_LOGIN`=ваш_логин_ВК

`VK_GROUP_ID`=id_вашей_группы_ВК(цифры из ссылки на группу)

`VK_ALBUM_ID`=id_альбома_вашей_группы_ВК(цифры из ссылки на альбом группы вк)

`TELEGRAM_TOKEN`=токен_телеграм_бота

`TELEGRAM_CHANEL_ID`=ссылка_на_канал(например: @my_channel_is_awesome)

`FACEBOOK_TOKEN`=токен_фейсбук

`FACEBOOK_GROUP_ID`=id_группы_фейсбук(цифры из ссылки на группу)

### Пример запуска
Скрипт принимает на вход два обязательных аргумента, путь до изображения и путь до текстового файла с самим постом(*.txt)
```
$python3 vk_tg_fb_posting.py image.jpg text.txt
```

Используя дополнительные аргументы, вы можете пропустить постинг в определенную соцсеть.
1. `-pf` или `--post_facebook` - выложить в Facebook
2. `-pv` или `--post_vk` - выложить во Вконтакте
3. `-pt` или `--post_telegram` - выложить в Телеграм

Пример:
```
$python3 vk_tg_fb_posting.py image.jpg text.txt -pt
```
Такой ввод запустит скрипт на постинг только в телеграм!

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
