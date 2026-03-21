from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

DEFAULT_LIMIT = "6 per minute"

Rate_Limit = Limiter(
    get_remote_address,
    default_limits=[DEFAULT_LIMIT],
    storage_uri="redis://localhost:6379"
)