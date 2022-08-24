from http import client
import sys
import os

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self) -> None:
        self.client_id = "AVtfMXZd9wxW19asF-CH9XMsGdzbSBqop8qCgwgR9zWEMlMeX4KOxuuHHiyhv282-SH7xAtl7z3eEmag"
        self.client_secret = "EIck68H4DjvcPZYUrNs9KYXX6qi9H8pbkAsOVZKCjF3uDPXJangx_MrqnNxMX583_9DeoTBY8M8IgXsn"
        self.environment = SandboxEnvironment(
            client_id=self.client_id, client_secret=self.client_secret
        )
        self.client = PayPalHttpClient(self.environment)
