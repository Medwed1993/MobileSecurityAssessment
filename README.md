# MobileSecurityAssessment
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

Установка независимостей dependencies.py, dependencies.exe

sudo python3 dependencies.py

sudo dependencies.exe

![dependencies](https://user-images.githubusercontent.com/79997543/113424746-a9557d00-939e-11eb-9872-f6130f882f6c.png)

1) Подключится к Android емулятору.

adb connect ip:port емулятора

![adb](https://user-images.githubusercontent.com/79997543/113423761-0bad7e00-939d-11eb-91e1-7764f7142ff8.png)

2) Запустить MobSF.

docker run -it --rm -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest

![run_docker](https://user-images.githubusercontent.com/79997543/113422312-74472b80-939a-11eb-988c-da7719a50661.png)

перейти на локальный сайт http://0.0.0.0:8000

![run_browser](https://user-images.githubusercontent.com/79997543/113423790-16681300-939d-11eb-9982-772e9e124d91.png)

3) Запустить script.

python3 json_and_android

ввести apk файл который сканировать

![run](https://user-images.githubusercontent.com/79997543/113423831-2e3f9700-939d-11eb-9284-9522517ef4a8.png)

Папки с результатами сохранятся на Desktop.

![finish](https://user-images.githubusercontent.com/79997543/113423841-313a8780-939d-11eb-8d0d-1f89accb7a8a.png)
