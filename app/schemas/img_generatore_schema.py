from pydantic import BaseModel

from app.utils.fields_constraints import ImgGeneratorTextField


class ImgGeneratorSchema(BaseModel):
    text: ImgGeneratorTextField
