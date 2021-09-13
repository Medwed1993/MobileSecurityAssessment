# MobileSecurityAssessment


## API describe
The data is accessed via standard HTTPS requests encoded in UTF-8. Data is sent and received in JSON format.
Main domain: https://********

### Upload file into system
API to upload a file. Supported file types are apk, zip, ipa and appx.

#### Request example:
----------------------------------------------------------------------
```
POST /upload/ HTTP/1.1
Host: ********
Content-Length: 37040983
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36
X-Requested-With: XMLHttpRequest
X-CSRFToken: i7TN6d1pyFAr5tOte3O8nfUCN9ozyDKUJcJHCgAhqtDQiisLv5zJdcXutd36e3ET
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary3pHsu1Yah8bUrZJ5
Accept: */*
Origin: http://0.0.0.0:8000
Referer: http://0.0.0.0:8000/
Accept-Encoding: gzip, deflate
Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close

------WebKitFormBoundary3pHsu1Yah8bUrZJ5
Content-Disposition: form-data; name="file"; filename="tetsapp.apk"
Content-Type: application/vnd.android.package-archive
```
----------------------------------------------------------------------

#### Response example:
----------------------------------------------------------------------
```
HTTP/1.1 200 OK
Server: gunicorn
Date: Mon, 13 Sep 2021 07:43:26 GMT
Connection: close
Content-Type: application/json; charset=utf-8
Access-Control-Allow-Origin: *
Content-Length: 144

{"analyzer": "static_analyzer", "status": "success", "hash": "3a55c64114904d23b4b5afc17213f59c", "scan_type": "apk", "file_name": "tetsapp.apk"}
```
----------------------------------------------------------------------

### Return result

## Deploy describe





Developing mobile security testing tools

Инструенты, которые применяются для работы.
adb
objection 
MobSF
Эмулятор девайса.

Задачи системы: проводить автоматизированное тестирования мобильного приложения для Android.
Приложение предназначено для локального использования или в локальной сети.

Описание работы системы.


Будет использовать клиент-серверная архитектура. 
Бэк-энд пишется на питоне, весь сервер упаковывается в докер контейнер.
Фронт пишеться на WPF.

Алгоритм работы прилжения.

Через веб-сайт загружаем apk файл.
Файл загружается в статический сканнер MobSF.
Приложение устанавливается непосредственно на эмулятор.
На основе статического анализа выполняются действия по RootCheck и SSL Pinning. При наличии этих защитных механизмов - выполняется функциоанал objection.
Дальше выполняется предварительный запуск мобильного приложения и проверяем, какие есть уязвимости.
На основании наденных уязвимостей формируется отчет, который возвращает данные в web-форме.


Установочный файл:
Выполняется развертывание всех необходимых инструментов и зависимостей.
Поднимает локальный веб-сервер в который доступ по 8888 порту

Агоритм анализа

1) Загрузка файла в MobSF через API. Для этого нужно API-ключ подтягивать автоматически.
2) Результаты анализа MobSF: Manifest analysis, Code analysis, Network analysis, Permissions analysis
3) Старт анализа с помощью оbjection начинается почсле окончания сканирования MobSF. Выполняется запуск приложения при учете различных механизмах защиты.
4) Отчет выводиться в HTML форме.

Инструкция по использованию.

Установка независимостей dependencies.py

sudo python3 dependencies.py

![dependencies](https://user-images.githubusercontent.com/79997543/113424746-a9557d00-939e-11eb-9872-f6130f882f6c.png)

1) Подключится к Android емулятору.

adb connect ip:5555 емулятора

![adb](https://user-images.githubusercontent.com/79997543/113423761-0bad7e00-939d-11eb-91e1-7764f7142ff8.png)

2) Запустить script.

python3 mobsa.py exampl.apk

![run](https://user-images.githubusercontent.com/79997543/132571877-daafbeb6-a72a-40c7-836f-2ce50264b9e8.png)
![run2](https://user-images.githubusercontent.com/79997543/132572010-86edd3d0-96c2-4ae5-af99-72f2eb6bc506.png)

Папки с результатами сохранятся на Desktop.

![folder](https://user-images.githubusercontent.com/79997543/113423796-19fb9a00-939d-11eb-97f0-a9d2d8062e36.png)
