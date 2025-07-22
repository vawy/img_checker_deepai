from typing import Annotated

from pydantic import Field

from .fields_length import IMG_GENERATOR_TEXT_LENGTH_FIELD


ImgGeneratorTextField = Annotated[str, Field(max_length=IMG_GENERATOR_TEXT_LENGTH_FIELD)]
