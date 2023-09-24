from pydantic import BaseModel

class AbstractBattery(BaseModel):
    """
    This is an abstract battery class
    """
    size: float
    inverter_size: float
    efficiency: float
