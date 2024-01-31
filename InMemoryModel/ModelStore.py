from ModelElements import PoligonalModel, Flash, Camera, Scene
from . import IModelChanger, IModelChangedObserver


class ModelStore:

    def __init__(self):
        self._changeObservrs = IModelChangedObserver()

