ADMINS = [
	"752594294",
	""
]

MSGS = {
	"start_message__no_reg": "Привет! Для начала тебе необходимо выбрать роль, кем ты являешься ✅",
	"start_message__seller": "Стартовое для продавца",
	"start_message__client": "Стартовое для покупателя",
	"start_message__moder": "Стартовое для модератора",

	"choose_category": "Отлично! Теперь вам нужно выбрать категорию товаров, которые вам интересны 🔽🔽🔽",
	"min_cashback": "Введите размер минимального кэшбека, учитываемого при рассылке\n\n<b><u>Например: 20%</u></b>",

	"client_created_success": "Регистрация завершена успешно. Теперь вам будут приходить товары с кэшбеком в выбранной категории!",

	"seller_shop_title": "Отлично! Введите название магазина 🏬",
	"seller_shop_url": "Теперь отправьте мне ссылку на ваш магазин на маркетплейсе",
	"seller_created_success": "Регистрация вас, как продавца, прошла успешно! Теперь вы можете добавлять товары в свой магазин",

	"seller_add_item__0": "Для добавления нового товара необходимо будет заполнить некоторые его параметры\n\nПервое - <u><b>Название товара</b></u>",
	"seller_add_item__1": "Введите <u><b>Описание товара</b></u>",
	"seller_add_item__2": "Отправьте <u><b>Изображение товара</b></u> в сжатом формате",
	"seller_add_item__3": "Отправьте <u><b>Стоимость товара</b></u> обычным числом",
	"seller_add_item__4": "Отправьте <u><b>Размер кэшбека</b></u>\n\nНапример: <em>50%</em>",
	"seller_add_item__link": "Отправьте <u><b>Ссылку</b></u> на товар в магазине",
	"seller_add_item__link_error": "Ошибка! Неверный формат ссылки на товар",
	"seller_add_item__5": "Напиши <u><b>Условия</b></u>, которые нужно выполнить для получения кэшбека",
	"seller_add_item__6": "Выберите <u><b>Категорию</b></u> товара",
	"seller_add_item__7": "Подтвердите правильность данных",
	"seller_add_item__success": "<b>Товар успешно добавлен!</b>",
	"seller_add_item__error": "<b>Добавление товара прервано!</b>",
	"seller_add_item__image_error": "Ошибка! Не удалось получить картинку\n\nОтправьте изображение в сжатом формате",
	"seller_add_item__price_error": "Ошибка! Неверный формат стоимость товара\n\nОтправьте просто число. <b>Например: 5000</b>",
	"seller_add_item__cashback_error": "Ошибка! Неверный формат кэшбека\n\n<b>Пример: 20%</b>",

	"seller_items": "Всего в вашей коллекции <em>{0} товар(ов/а)</em>\n\nНажав на товар вы можете <b>посмотреть</b> его карточку или <b>удалить</b> его",
	"seller_no_items": "В вашей коллекции нет ни одного товара 😢",

	"seller_remove_item_success": "Товар <b><u>{0}</u></b> успешно удален!",

	"seller_edit_item": "Выберите, какой параметр товара вы хотите отредактировать",
	"seller_edit_item__title": "Введите новое <b><u>название</u></b> товара",
	"seller_edit_item__desc": "Введите новое <b><u>описание</u></b> товара",
	"seller_edit_item__price": "Введите новую <b><u>стоимость</u></b> товара",
	"seller_edit_item__image": "Отправьте новое <b><u>изображение</u></b> товара",
	"seller_edit_item__cashback": "Введите новый <b><u>размер кэшбека</u></b> для товара",
	"seller_edit_item__condition": "Введите новое <b><u>условие кэшбека</u></b> для товара",
	"seller_edit_item__link": "Введите новую <b><u>ссылку</u></b> на товар",
	"seller_edit_item__success": "Товар успешно отредактирован!",


	"item_card": "<b><u>{0}</u></b> (<em>{4}</em>)\n\n<em>{1}</em>\n<b>{2}</b> р.\n\nКэшбек: <b>{3}%</b>\nУсловие: <i>{5}</i>",
	"new_item": "<u>Появился новый товар!</u>\n\nСкорее успей купить его и получить кэшбек",

	"admin_menu_start": "Добро пожаловать в меню администратора!",
	"admin_add_cat": "<b>Введите название категории</b>",
	"admin_add_cat_success": "Категория успешно добавлена",
	"admin_remove_cat": "<b>Выберите категорию для удаления</b>",
	"admin_remove_cat_success": "Категория успешно удалена",
	"admin_add_moder_username": "Отправьте телеграм id пользователя, который должен стать модератором",
	"admin_remove_moder_username": "Отправьте телеграм id модератора, которого нужно удалить",
	"admin_add_moder_success": "Модератор успешно добавлен!",
	"admin_add_moder_error": "Не удалось добавить модератора! Пользователь должен быть <u>клиентом</u>\n\nПопробуйте еще раз или отмените операцию",

	"client_show_items": "Выберите категорию товаров",
	"client_no_items": "В данной категории нет товаров 😢",
	"client_close_items_list": "Список товаров закрыт",
	"client_request_created": "Запрос на проверку условий получения кэшбека создан. Ждите, с вами свяжется модератор после проверки условий",
	"client_request_error": "Ваш запрос уже создан и находится на проверке",

	"client_find_items__start": "Отправьте желаемое название товара",

	"moder_no_reqs": "Нет запросов на проверку",
	"moder_request": "Товар: {0} (id: {1})\nСсылка на товар: {2}\nУсловие: {3}\n\nПользователь: {4} | @{5}",
	"moder_request_closed_success": "Запрос успешно закрыт!",

	"cancelled": "Отменено 😢",
}

BUTTONS = {
	"user": {
		"start": [
			"Продавец 🏪",
			"Покупатель 🛒"
		],
		"cancel": [
			"Отмена 🚪"
		]
	},

	"seller": {
		"menu": [
			"Добавить товар ➕",
			"Мои товары 📄",
		],
		"confirm": {
			"accept": "Да ✅",
			"deny": "Нет ❌",
		},
		"items_list": {
			"remove_item__": "Удалить 🗑",
			"edit_item__": "Редактировать ✏",
		},
		"edit_item": {
			"edit_title": "🔵 Название",
			"edit_desc": "🔵 Описание",
			"edit_price": "🔵 Цена",
			"edit_image": "🔵 Изображение",
			"edit_cashback": "🔵 Кэшбек",
			"edit_condition": "🔵 Условие",
			"edit_link": "🔵 Ссылку"
		}
	},

	"client": {
		"menu": {
			"show_items": "Товары 🛒",
			"find_items": "Поиск 🔍",
		},
		"items_list": {
			"back": "⬅ Назад",
			"buy": "🛒 Купить 🛒",
			"next": "Вперед ➡",
			"check": "✅ Проверить ✅",
			"close": "🚪 Закрыть 🚪",
		},
	},

	"admin": {
		"cancel": "Отмена ❌",
		"menu": {
			"add_cat": "Добавить категорию",
			"remove_cat": "Удалить категорию",
			"add_moder": "Добавить модератора",
			"remove_moder": "Удалить модератора"
		}
	},

	"moder": {
		"menu": {
			"check": "Проверить условия"
		},
		"close_req": {
			"close": "Закрыть 📄"
		}
	}
}