from datetime import datetime

from sqladmin import ModelView

from app.core.models import RegistrationCertificate

"""DOC-HELPERS https://aminalaee.dev/sqladmin/configurations/ """
"""
Defines the configuration settings for the RegistrationCertificate model view in the admin panel.

    Columns displayed: id, trade_Name, reg_Cert_Number, createAt_Reg_Cer
    Columns excluded from details view: id
    Columns searchable by default: trade_Name, reg_Cert_Number
    Columns sortable by default: trade_Name

    Settings:
        - Deletion allowed: Yes
        - Singular name: "Регистрационный сертификат"
        - Plural name: "Регистрационные сертификаты"
        - Icon: "fa-solid fa-certificate"
"""


# noinspection PyTypeChecker
class RegistrationCertificateAdmin(ModelView, model=RegistrationCertificate):
    group_name = "Мастер данных"

    column_labels = {
        RegistrationCertificate.trade_Name: "Наименование",
        RegistrationCertificate.reg_Cert_Number: "Номер РУ",
        RegistrationCertificate.createAt_Reg_Cer: "Дата регистрации",
    }

    save_as = True

    column_list = [
        # RegistrationCertificate.id,
        RegistrationCertificate.trade_Name,
        RegistrationCertificate.reg_Cert_Number,
        RegistrationCertificate.createAt_Reg_Cer,
        RegistrationCertificate.is_Active,
    ]
    # column_details_exclude_list = [RegistrationCertificate.id]
    column_searchable_list = [
        RegistrationCertificate.trade_Name,
        RegistrationCertificate.reg_Cert_Number,
        RegistrationCertificate.is_Active,
    ]
    column_sortable_list = [
        RegistrationCertificate.trade_Name,
    ]
    column_default_sort = [
        (RegistrationCertificate.trade_Name, True),
    ]
    # column_formatters = {RegistrationCertificate.trade_Name: lambda m, a: m.trade_Name[:10]}

    can_delete = True
    name = "Регистрационный сертификат"
    name_plural = "Регистрационные сертификаты"
    icon = "fa-solid fa-certificate"

    page_size = 50
    page_size_options = [25, 50, 100, 200]
