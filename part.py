from faker.providers import BaseProvider
from collections import OrderedDict


class CustomPartProvider(BaseProvider):
    """Custom Ethnic Provider"""

    PARTS: OrderedDict[str, float] = OrderedDict([
    ("Head", 0.15),
    ("Shoulders", 0.15),
    ("Chest", 0.15),
    ("Back", 0.15),
    ("Stomach", 0.05),
    ("Waist", 0.05),
    ("Hands", 0.05),
    ("Wrists", 0.05),
    ("Thighs", 0.15),
    ("Feet", 0.10)
    ])

    def part(self) -> str:
        return self.random_elements(self.PARTS, length=1, use_weighting=True)[0]
    
