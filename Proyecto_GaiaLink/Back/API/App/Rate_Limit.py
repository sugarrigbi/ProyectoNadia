from flask_limiter.util import get_remote_address
from flask_limiter import Limiter
import os

Rate_Limit = Limiter(
    get_remote_address,
    default_limits=[os.getenv("DEFAULT_LIMIT")],
    storage_uri=os.getenv("REDIS_URL")
)