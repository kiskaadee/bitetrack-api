from pydantic import BaseModel


class Envelope[T](BaseModel):
    data: list[T]
    total_count: int

