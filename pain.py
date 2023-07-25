from faker.providers import BaseProvider
from collections import OrderedDict


class CustomPainProvider(BaseProvider):
    """Custom Ethnic Provider"""

    PAIN: OrderedDict[str, float] = OrderedDict([
        ("1", 0.08),
        ("2", 0.16),
        ("3", 0.22),
        ("4", 0.25),
        ("5", 0.20),
        ("6", 0.09),
        ("7", 0.04),
        ("8", 0.02),
        ("9", 0.01),
        ("10", 0.01)
    ])

    def pain(self) -> str:
        return self.random_elements(self.PAIN, length=1, use_weighting=True)[0]
    
