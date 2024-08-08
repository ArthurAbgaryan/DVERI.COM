from django.db import models

class categories(models.Model):
    title = models.CharField(max_length=250,verbose_name='Название',null=True)
    parent_id = models.PositiveIntegerField(null=True,
                                            help_text='Идентификатор родительской категории')
    lft = models.PositiveIntegerField(null=True,
                                      help_text='Параметр lft (хранение деревьев nested set). Может быть использовано для простой сортировки.')
    rgt = models.PositiveIntegerField(null=True,
                                      help_text='Параметр rgt (хранение деревьев nested set)')
    class Meta:
        def __str__(self):
            return self.title
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'
    def __str__(self):
        return self.title

class categoriesImport(models.Model):
    json_file = models.FileField(upload_to='uploads/')
    date_published = models.DateTimeField(auto_now_add=True)

class color_groups(models.Model):
    title = models.CharField(max_length=2500,help_text='Название',null=True)
    position = models.IntegerField(null=True, help_text='Позиция сортировки')

    class Meta:
        def __str__(self):
            return self.title
        verbose_name = 'Группа цветов'
        verbose_name_plural = 'Группы цветов'

class colors(models.Model):
    color_group_id = models.PositiveIntegerField(null=True, verbose_name='Идентификатор группы цветов')
    title = models.CharField(max_length=250, null=True, verbose_name='Название')
    picture = models.URLField(null=True, verbose_name='картинка' ,help_text = 'url изображения')
    position = models.PositiveIntegerField(null=True, help_text='Позиция сортировки', verbose_name='Позиция')
class product_tes(models.Model):
    title = models.CharField(max_length = 250,null=True)
    json_field = models.JSONField(null=True)
    def __str__(self):
        return self.title
class glasses(models.Model):
    title = models.CharField(max_length=250, verbose_name='Стекло', null=True)
    class Meta:
        verbose_name = 'Стекло'
        verbose_name_plural = 'Стёкла'


class accessory_groups(models.Model):
    title = models.CharField(max_length=250, null=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Группа комплектующих'
        verbose_name_plural = 'Группы комплектующих'

class accessories(models.Model):
    accessory_group_id = models.PositiveIntegerField(null=True,
                                                     verbose_name = 'Идентификатор группы аксессуаров')
    title = models.CharField(max_length=250, null=True, verbose_name='Название')
    pictures = models.JSONField(null=True,verbose_name='Картинка')
    quantity = models.IntegerField(null=True, verbose_name='Количество в базовом комплекте')
    price = models.PositiveIntegerField(null = True, verbose_name='Розничная цена')
    price_dealer = models.PositiveIntegerField(null = True, verbose_name='Дилерская цена')
    discount = models.PositiveIntegerField(null=True, verbose_name='Рознична скидка')
    discount_dealer = models.PositiveIntegerField(null=True,verbose_name='Дилерская скидка')
    label = models.CharField(max_length=250, null=True,verbose_name='Лейбл (статус)')
    vendor_code = models.CharField(max_length=250,null=True, verbose_name='Артикул')
    is_telescopic= models.BooleanField(null=True)
    class Meta:
        verbose_name = 'Комплектующие'
        verbose_name_plural = 'Комплектующие'

class properties(models.Model):
    title = models.CharField(max_length=250, null=True)
    is_accessory = models.BooleanField(null=True,
                                       help_text='Используется во вкладке Фурнитура у входных дверей')
    position = models.PositiveIntegerField(null=True, verbose_name='Позиция')

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
class property_values(models.Model):
    property_id = models.PositiveIntegerField(verbose_name='Идентификатор характеристики',null = True)
    product_id = models.PositiveIntegerField(verbose_name='Идентификатор товара',null=True)
    title = models.CharField(max_length=2500, null= True, verbose_name='Название')

    class Meta:
        verbose_name='Значение характеристик'
        verbose_name_plural = 'Значение характеристик'

class attributes(models.Model):
    title = models.CharField(max_length=250,verbose_name='Название',null=True)
    position = models.PositiveIntegerField(verbose_name='Позиция в карточке товара',null=True)
    class Meta:
        verbose_name = 'Атрибут'
        verbose_name_plural = 'Атрибуты'

class attributeValues(models.Model):
    attribute_id = models.PositiveIntegerField(verbose_name='Идентификатор атрибута',null=True)
    title = models.CharField(null=True, verbose_name='Название',max_length=250)
    is_generation_hidden = models.IntegerField(null=True)
    generation_title = models.CharField(max_length=2500,help_text='Название для генерации названия опции (если не задано, берётся из title)',null=True)
    description = models.CharField(max_length=2000,verbose_name='Описание (подсказка)', null=True)
    position =models.PositiveIntegerField(null=True, verbose_name='Позиция в карточке товара')
    class Meta:
        verbose_name = 'Значение атрибута'
        verbose_name_plural = 'Значение атрибутов'

class trademarks(models.Model):
    title = models.CharField(max_length=250, null=True,verbose_name='Название')
    url = models.URLField(null=True, verbose_name='url изображения')
    class Meta:
        verbose_name = 'Торговая марка'
        verbose_name_plural = 'Торговые марки'

class products(models.Model):
    title=models.CharField(max_length=250,null=True,verbose_name='Название')
    url = models.URLField(null=True, help_text='Ссылка на сайте')
    category_id = models.PositiveIntegerField(null=True,help_text='Идентификатор категории')
    accessory_group_id	= models.PositiveIntegerField(null=True,help_text='Идентификатор группы аксессуаров')
    color_id = models.PositiveIntegerField(null=True,help_text='Идентификатор цвета')
    glass_id = models.PositiveIntegerField(null=True,help_text='Идентификатор стекла')
    trademark_id = models.PositiveIntegerField(null=True, help_text='Идентификатор торговой марки')
    price = models.IntegerField(null=True, verbose_name='Розничная цена')
    price_dealer = models.IntegerField(null=True,verbose_name='Дилерская цена')
    discount = models.IntegerField(null=True,verbose_name='Розничная скидка')
    discount_dealer = models.IntegerField(null=True,verbose_name='Диллерская скидка')
    label = models.CharField(max_length=250,verbose_name='Лейбл',null=True)
    vendor_code	=models.CharField(max_length=250,null=True, verbose_name='Артикул')
    position = models.PositiveIntegerField(verbose_name='Позиция внутри родительского класса', null=True)
    pictures = models.JSONField(null=True,help_text='Картинки в трех размерах')
    options = models.JSONField(null=True, verbose_name='Опции',help_text='Содержит опции товара (размеры)')
    properties = models.JSONField(null=True,help_text='Содержит описание товара (характеристики)')
    accessory_properties = models.JSONField(null=True,help_text='Содержит фурнитуру входных дверей')
    analogs = models.JSONField(null=True,verbose_name='Содержит аналоги товаров (похожий товар от другого производителя или другая модификация)')
    related_products = models.JSONField(null=True,help_text='Содержит товары из блока "C этим товаров также покупают"')