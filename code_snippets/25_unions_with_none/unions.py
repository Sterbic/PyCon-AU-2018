from typing import Union


def get_by_id(id: int) -> Union[User, Page, None]:
    pass


luka: User = get_by_id(1451268501)
pycon_au: Page = get_by_id(221942894648201)
probably_none = get_by_id(-1)
