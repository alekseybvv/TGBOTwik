Создаем экземпляр бота

Устанавливаем русский язык в Wikipedia

Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов

Получаем первую тысячу символов

Разделяем по точкам

Отбрасываем всЕ после последней точки

Создаем пустую переменную для текста

Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)

Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место

Теперь при помощи регулярных выражений убираем разметку

Возвращаем текстовую строку

Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе


Функция, обрабатывающая команду /start

Получение сообщений от юзера

запуск бота
