import json
import requests
from model.deepdives import DeepDives


class DRGService():
    def __init__(self):
        self.base_url: str = 'https://drgapi.com'
        self.version: str = '/v1'

    def get_deepdives(self) -> DeepDives | None:
        response = requests.get(url=f'{self.base_url}{self.version}/deepdives',
                                timeout=3)
        if response.status_code == 200:
            data = json.loads(response.text)
            return DeepDives.parse_obj(data)

        return None
