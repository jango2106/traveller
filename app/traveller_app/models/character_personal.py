from dataclasses import dataclass, field

from traveller_app.constants.modifiers import CHARACTERISTIC_MODIFIERS


@dataclass
class Characteristic:
    name: str
    level: int = field(default=0)

    def __post_init__(self):
        if self.level > 18 or self.level < 0:
            raise ValueError(
                f"Invalid characteristic level. Values can only range from 0 to 18 but {self.level} was found")

    def get_modifier(self):
        for group in CHARACTERISTIC_MODIFIERS.keys():
            if self.level == group or self.level in group:
                return CHARACTERISTIC_MODIFIERS[group]
