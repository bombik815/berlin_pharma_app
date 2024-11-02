from datetime import datetime

from sqladmin import ModelView

from app.core.models.registration_certificate import RegistrationCertificate
from app.core.models.release_form import ReleaseForm

"""DOC-HELPERS https://aminalaee.dev/sqladmin/configurations/ """
"""
Defines the configuration settings for the registration_certificate model view in the admin panel.

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
class Registration_Certificate_Admin(ModelView, model=RegistrationCertificate):
    group_name = "Мастер данных"

    column_labels = {
        RegistrationCertificate.trade_Name: "Наименование",
        RegistrationCertificate.reg_Cert_Number: "Номер РУ",
        RegistrationCertificate.createAt_Reg_Cer: "Дата регистрации",
        RegistrationCertificate.release_forms: "Форма выпуска",
        RegistrationCertificate.is_Active: "Активен",
    }

    save_as = True

    column_list = [
        RegistrationCertificate.trade_Name,
        RegistrationCertificate.reg_Cert_Number,
        RegistrationCertificate.createAt_Reg_Cer,
        RegistrationCertificate.is_Active,
        RegistrationCertificate.release_forms,
    ]
    # column_details_exclude_list = [registration_certificate.id]
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

    can_delete = True
    name = "Регистрационный сертификат"
    name_plural = "Регистрационные сертификаты"
    icon = "fa-solid fa-certificate"

    page_size = 50
    page_size_options = [25, 50, 100, 200]


class Release_Form_Admin(ModelView, model=ReleaseForm):
    group_name = "Мастер данных"

    column_labels = {
        ReleaseForm.primary_packaging: "Первичная упаковка",
        ReleaseForm.count_primary_packaging: "Кол-во первичной уп в потребительской уп",
        ReleaseForm.id_drug_name: "Наименование препарата",
        ReleaseForm.gtin: "GTIN",
        ReleaseForm.is_active: "Активен",
        ReleaseForm.registration_certificate_id: "ID РУ",
    }
    save_as = True

    column_list = [
        ReleaseForm.primary_packaging,
        ReleaseForm.count_primary_packaging,
        ReleaseForm.id_drug_name,
        ReleaseForm.gtin,
        ReleaseForm.is_active,
        ReleaseForm.registration_certificate_id,
    ]

    can_delete = True
    name = "Форма выпуска"
    name_plural = "Формы выпуска"
    icon = "fa-solid fa-certificate"

    page_size = 50
    page_size_options = [25, 50, 100, 200]
