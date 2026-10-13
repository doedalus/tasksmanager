from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column(nullable=True)
    is_completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now())