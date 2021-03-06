# Утилита для удаления резервных копий DataExpress

Утилита позволяет удалять резервные копии, создаваемые по принципу описанному в [статье](https://mydataexpress.ru/baza-dannykh-v-oblake-ustanovka-firebird-na-vds.html), через заданное количество дней.

## Использование

```
backups_remove.py [-h] [-d DAYS] path
```

### Параметры
* path - путь к папке backups, обязательный параметр.
* -d days - количетсво дней, начиная от текущего по истечении котрого старые бэкапы будут удалены. По умолчанию = 100, если указано отрицательное число то удаляются все бэкапы.
* -h help - вывод справки

## Примеры
```bash
# Хранение бэкапов 1 год
python3 backups_remove.py -d 365 /home/user/backups
```

## Добавление на сервер и автоматизация через cron

Подразумеватеся что вы прочитали [статью](https://mydataexpress.ru/baza-dannykh-v-oblake-ustanovka-firebird-na-vds.html) и выполнили все действия описанные в разделе "Настройка резервного копирования"

Для добавления утилиты на сервер необходимо:
1. С помощью FileZilla закачать backup_remove.py на сервер в директорию `/home/user`
1. Проверить работу утилиты, все бэкапы должны удалиться (можно поменять -1 на любое другое число и проверить, удалилась часть)
    ```bash
    python3 backups_remove.py -d -1 /home/user/backups
    ls /home/user/backups
    ```
1. Автоматизировать удаление с помощью cron
    ```bash
    sudo nano /etc/crontab
    ```
   Добавить строчку
   ```bash
    30 12 * * * root python3 /home/user/backups_remove.py -d 365 /home/user/backups
    ```
   365 - заменить на нужное число дней


