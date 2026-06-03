from dataclasses import dataclass

from model.object import Object


@dataclass
class Arco:
    o1: Object
    o2: Object
    peso: int


