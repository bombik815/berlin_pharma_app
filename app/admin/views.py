from sqladmin import ModelView

from app.core.models import RegistrationCertificate


class RegistrationCertificateAdmin(ModelView, model=RegistrationCertificate):
    column_list = [
        RegistrationCertificate.id,
        RegistrationCertificate.trade_Name,
        RegistrationCertificate.reg_Cert_Number,
        RegistrationCertificate.createAt_Reg_Cer,
    ]
    # column_details_exclude_list = [Users.hashed_password]
    can_delete = True
    name = "Регистрационный сертификат"
    name_plural = "Регистрационные сертификаты"
    icon = "fa-solid fa-certificate"


# class HotelsAdmin(ModelView, model=Hotels):
#     column_list = [c.name for c in Hotels.__table__.c] + [Hotels.rooms]
#     name = "Отель"
#     name_plural = "Отели"
#     icon = "fa-solid fa-hotel"
#
#
# class RoomsAdmin(ModelView, model=Rooms):
#     column_list = [c.name for c in Rooms.__table__.c] + [Rooms.hotel, Rooms.bookings]
#     name = "Номер"
#     name_plural = "Номера"
#     icon = "fa-solid fa-bed"
#
#
# class BookingsAdmin(ModelView, model=Bookings):
#     column_list = [c.name for c in Bookings.__table__.c] + [
#         Bookings.user,
#         # Bookings.room,
#     ]
#     name = "Бронь"
#     name_plural = "Брони"
#     icon = "fa-solid fa-book"
