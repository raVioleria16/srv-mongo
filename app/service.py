from rv16_lib import get_object_from_config
from rv16_lib.architecture.base_service import BaseService

from config import SrvConfig


class RegisterService(BaseService):
    def __init__(self):
        super().__init__()
        self.config = get_object_from_config(config_model=SrvConfig)
        self.service_name = self.config.hostname

