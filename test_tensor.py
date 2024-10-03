from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage


def test_tensor_banner_navigation(driver):
    # Шаг 1: Переход на sbis.ru и переход в Контакты
    sbis_page = SbisPage(driver)
    sbis_page.open("https://sbis.ru/")
    sbis_page.go_to_contacts()

    # Шаг 2: Найти баннер "Тензор" и кликнуть по нему
    sbis_page.click_tensor_banner()

    # Шаг 3: Переход на tensor.ru и проверка блока "Сила в людях"
    tensor_page = TensorPage(driver)
    assert tensor_page.is_people_power_visible(), "Блок 'Сила в людях' не найден"

    # Шаг 4: Клик на "Подробнее" и проверка открытия страницы "О компании"
    tensor_page.click_more()
    assert tensor_page.is_about_page_visible(), "Страница 'О компании' не открылась"

    # Шаг 5: Проверка одинаковых размеров фотографий в разделе "Работаем"
    image_sizes = tensor_page.get_image_sizes()
    first_size = image_sizes[0]
    for size in image_sizes:
        assert (
            size == first_size
        ), f"Изображение {size} имеет другой размер чем {first_size}"
