from pydantic import BaseModel, Field

class Translation(BaseModel):
    language: str = Field(description="Язык")
    text: str = Field(description="Перевод")

class TranslatedText(BaseModel):
    traslates: list[Translation] = Field(description="Список переводов")

