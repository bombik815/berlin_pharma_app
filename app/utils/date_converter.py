from datetime import datetime
from typing import Union


def format_date(date_input: Union[str, datetime]) -> str:
    """Преобразование даты и времени или строки в формат строки даты ГГГГ-ММ-ДД"""
    if isinstance(date_input, datetime):
        return date_input.strftime("%Y-%m-%d")

    try:
        date_obj = datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            raise ValueError(
                "Неверный формат даты. Ожидается 'YYYY-MM-DD HH:MM:SS' или 'YYYY-MM-DD'"
            )
