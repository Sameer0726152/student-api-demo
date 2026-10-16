from pydantic import BaseModel, ConfigDict


class StudentCreate(BaseModel):
        name: str
        email: str


class StudentOut(StudentCreate):
        model_config = ConfigDict(from_attributes=True)
        id: int