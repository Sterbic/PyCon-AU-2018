from typing import Union, Optional


def get_by_id(id: int) -> Optional[Union[User, Page]]:
    pass


luka: User = get_by_id(1451268501)
pycon_au: Page = get_by_id(221942894648201)
probably_none = get_by_id(-1)
