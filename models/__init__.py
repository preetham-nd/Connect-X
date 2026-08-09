# Import models so SQLAlchemy metadata registers tables for create_all().
from models.comment import Comment  # noqa: F401
from models.connection_test import ConnectionTest  # noqa: F401
from models.post import Post  # noqa: F401
from models.profile import Profile  # noqa: F401
from models.user import User  # noqa: F401
