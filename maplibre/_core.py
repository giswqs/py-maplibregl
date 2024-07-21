from __future__ import annotations

from pydantic import BaseModel as BaseModel_
from pydantic import ConfigDict


class MapLibreBaseModel(BaseModel_):
    model_config = ConfigDict(
        validate_assignment=True, extra="forbid", use_enum_values=True
    )

    def to_dict(self) -> dict:
        return self.model_dump(by_alias=True, exclude_none=True)
