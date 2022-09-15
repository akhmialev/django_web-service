from django.db import models


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name="Время")
    order_name = models.CharField(max_length=200, verbose_name="Имя")
    order_phone = models.CharField(max_length=200, verbose_name="Телефон")
    order_status = models.ForeignKey('StatusCrm', on_delete=models.PROTECT, null=True, blank=True,
                                     verbose_name="Статусы")

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class StatusCrm(models.Model):
    status_name = models.CharField(max_length=100, verbose_name="Статус")

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Стату'
        verbose_name_plural = 'Статусы'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заявка")
    comment = models.TextField(verbose_name="Коммнетарий")
    comment_dt = models.DateTimeField(auto_now=True, verbose_name="Дата создания")


    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'