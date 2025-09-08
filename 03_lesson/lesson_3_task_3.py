from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Тверская", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Невский", "20", "50")

mailing = Mailing(to_address, from_address, 500, "AB123456789CD")

print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.postal_code}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в "
    f"{mailing.to_address.postal_code}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
