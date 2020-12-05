from typing import Optional

from traveller_app.constants.characteristics import CHARACTERISTIC_NAMES
from traveller_app.models.character_personal import Characteristic


class CharacteristicsController:
    def __init__(self):
        self.__characteristics = {}
        for characteristic in CHARACTERISTIC_NAMES:
            self.__characteristics[characteristic] = Characteristic(characteristic)

    def get_characteristic(self, name) -> Optional[Characteristic]:
        characteristic = self.__characteristics.get(name)
        if not characteristic:
            return None
        return Characteristic.from_characteristic(characteristic)


    def update_characteristic(self, name: Optional[str] = None, level: Optional[int] = None) -> None:
        '''
        Update a characteristic with a name and level or an instance of the characteristic with valid name a level.
        :param name: Name of the characteristic to modify
        :param level: New level of the characteristic
        :param instance: An instance of the Characteristic to replace the old instance
        :return: Any
        '''
        new_characteristic = None
        if name and level and self.__characteristics.get(name):

            new_characteristic = Characteristic(name, level)