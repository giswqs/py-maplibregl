from shiny.session import Session, get_current_session

from .map import Map


class MapProxy(Map):
    def __init__(self, id_: str) -> None:
        self.id = id_
        self._map_options = {}
        self._calls = []

    async def render(self, session: Session = get_current_session()):
        await session.send_custom_message(
            f"pymaplibregl-{self.id}", {"id": self.id, "calls": self._calls}
        )
