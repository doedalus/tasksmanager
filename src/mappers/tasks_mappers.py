from src.schemas.tasks_schemas import TaskSchema
from src.models.tasks_models import Task


def from_model_to_schema(model: Task) -> TaskSchema:
    return TaskSchema(
        id=model.id,
        title=model.title,
        description=model.description,
        is_completed=model.is_completed,
        created_at=model.created_at,
    )
