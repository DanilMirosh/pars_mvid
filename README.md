# pars_mvid
## Давайте попробую описать весь процесс, как можно распарсить интернет-магазин

Распарсил интернет_магазин электроники.
Эта часть скрипта для мониторинга скидок на электронику.
Поработаем над объединением словарей и записью в JSON,
разберем запросы к API.
Установим request в наше виртуальное окружение.
Создадим функцию get_data() в которой будет код скрапера.
Создадим функцию main в которой вызываем нашу функцию.
Идем на сайт м-видео, и посмотрим с чем нам предстоит работать.
Выберем например категорию с планшетами(<Все планшеты>),
и поставим отбор на товар со скидкой (переведем бегунок "Товар со скидкой")
и поставим отбор на товар в наличии (переведем бегунок на "Товар в наличии")
Обратите внимание как будет меняться URL, в него добавляются новые параметры
Само собой такие маркет-плейсы подгружаются динамически,
соответственно данные c большой долей вероятности приходят с API,
сразу забрать все данные не удалось, нашел несколько запросов.
Собрал из них данные, а уже потом комбинировал результат
В браузере открываем 'посмотреть код',
вкладку Network и отправляем GET запрос еще раз.
Первый запрос который нас интересует, будет "listing?categoryid"
В нем среди прочей информации, есть ключ "products",
значением которой выступает список id-шников,
это id-шники товаров которые нам нужно извлечь и передать следующий запрос 
в виде параметра.
Cледующий запрос это "list", и если перейти во вкладу "Payload", 
как раз увидим что одним из параметров идет ключ productsIds, 
со значением в виде списков полученных ранее ID.
Данный запрос уже возвращает нам что-то по интереснее,
а именно всю информацию о запрашиваемых планшетах.
(Бренд, название, изображение, тот же Id и т.д.), но здесь нет прайса.
За прайс отвечает ключ "prices?productids" в нем есть ключ "materialPrices"
значением которого выступает список из словарей, где как раз по привязке с ID
подгружается данные о стоимости, скидках и, бонусах.
Давайте возьмем id какого-нибудь планшета из предыдущего запроса
и попробуем найти его прайс.
Теперь нам все это нужно собрать и записать в один словарь, с которым дальше уже можно делать что захочешь.
Сначала нам нужно отправить запрос и собрать Id товаров, за это у нас отвечает следующий запрос:
listing?categoryid, правой кнопкой и выбираем копировать->копировать как cURL.
Переходим на сайт (curlconverter.com) который позволяет конвертировать curl команды на запросы в различных языках.
Вставляем и у нас появляется готовый код для запроса, копируем и вставляем,
в нашу функцию get_data().
В ПЕЧЕНКАХ нужно обратить внимание на CITY_ID - это id города,
если вы собираетесь парсить несколько городов нужно менять данный параметр.
ID так же можно найти в network.
Ключивым является словарь с параметрами (params), в него мы передаем id котегории,
в нашем случае это 195 (ПЛАНШЕТЫ)
Параметр offset - это пагинация(если будет несколько страниц)
limit - лимит товара на стронице по дифолту равен 24
После отправляем запрос с параметрами, ПЕЧЕНЬКАМИ и заголовками-> получать мы будем JSON.
Нужные нам ID лежат в listing?categoryid->body->products
Создадим переменную и достанем ID.
Сохраним ответ в JSON
Отлично мы получили ID
Дальше на нужно отправить запрос на получение данных о планшетах.
Копируем (list) запрос как cURL и опять идем на сайт curlconverter.com
Видим что вместо параметров у нас теперь передается json_data,
ключем идет productIds это как раз список из полученных нами ранее ID,
Копируем json_data и запрос, вставляем ниже по коду в функцию get_data()
Вместо списка подставляем нашу переменную products_ids, в ответе получаем json
и после сохраняем результат.
Теперь надо собрать цены, скидки и бонусы, за это у нас отвечает запрос
"prices?productids" копируем cURL и опять идем на сайт curlconverter.com
И видим что снова добавляется значение params, значением ключа productIds,
выступают все те же ID, но с одним но, теперь это не список, а строка,
внутри которой через запятую перечислены ID.
Копируем параметры и запрос, вставляем ниже по коду в функцию get_data().
Первым делом склеим список с ID в строку с помощью метода join, разделителем будет запятая.
Вставляем строку в параметры, далее отправляем запрос, получаем json.
И запишем результат в третий файл.
Создадим словарь под наши данные.
Получаем список со словарями в котором хранятся объекты с данными.
Пробегаемся по нему циклом и на каждой итерации забираем ID товара,
базовый прайс, затем прайс со скидкой и количество бонусов.ё
На каждой итерации записываем в наш словарь новую пару, ключем будет ID товара,
а значением словарь с данными в виде базового прайса, прайса со скидкой и бонусов.
После выходим из цикла и записываем данные в json.
Объединение словарей с данными я решил вынести в отдельную функцию get_result().
Читаем словарь с данными по планшетам и следом словарь с прайсами.

Конечно можно было обойтись без записи данных в файлы и все написать в одной функции.
Но я подумал что так будет наглядно и более понятно.

Забираем из словаря с данными, только данные по планшетам,
они находятся в ключе "body" внутри ключа "products".
Пробегаемся циклом по списку словарей и первым делом получаем ID продукта,
далее нам нужно найти совпадения в словаре с прайсами и если такой id там существует,
сохраняем словарь с данными по базовой цене, скидки, и бонусом в переменную prices.
А после создаем новые пары в итоговом словаре с данными, сначала базовый прайс, 
затем прайс со скидкой и количество полученных бонусов.
Выходим из цикла и записываем данные в json.
Вызываем функцию get_result() сразу после get_data().
Получаем итоговый json result, и внизу каждого словаря у нас появились дополнительные пары.
Можно проверить берем прайс, сравниваем на сайте и все ок названия совпадают.
Заметьте что это всего лишь первая страница, если товары популярные то часто присутствует ПАГИНАЦИЯ
