# Скрипт постинга в VK, Telegram, Facebook

Скрипт для одновременного или выборочного постинга по соц. сетям.

### Как установить

Для запуска программы у вас уже должен быть установлен Python 3. 

Установите зависимости командой в терминале:

```
$ pip install -r requirements.txt
```

Чтобы начать постин, в каждой соц сети придется получить токен.
1. для телеграмм [инструкция](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)
2. для VK [инструкция](https://devman.org/qna/63/kak-poluchit-token-polzovatelja-dlja-vkontakte/)
3. для Facebook [инструкция](https://developers.facebook.com/docs/graph-api/explorer/)

### Пример запуска
Скрипт принимает на вход два обязательных аргумента, путь до изображения и путь до текстового файла с самим постом(*.txt)
```
$python3 vk_tg_fb_posting.py image.jpg text.txt
```

Используя дополнительные аругменты, вы можете пропустить постинг в определенную соцсеть.
1. `-sf` или `--skip_facebook` - пропустить Facebook
2. `-sv` или `--skip_vk` - пропустить Вконтакте
3. `-st` или `--skip_telegram` - пропустить Телеграм

Пример:
```
$python3 vk_tg_fb_posting.py image.jpg text.txt -sf -sv
```
Такой ввод запустит скрипт на постинг только в телеграм!

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).