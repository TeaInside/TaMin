from src import app
from src import db
import enum


class Flag(enum.Enum):
    SPAM = "Spam Content"
    RUDE = "Rude Content"
    DUPLICATE = "Duplicate Content"
