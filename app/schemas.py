from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
        name: str
        email: str


class StudentOut(StudentCreate):
        id: int

        class Config:
            from_attributes = True