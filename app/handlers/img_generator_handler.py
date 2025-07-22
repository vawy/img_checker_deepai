from fastapi import APIRouter, status

from app.reps.img_generator_rep import ImageGeneratorRep
from app.schemas.img_generatore_schema import ImgGeneratorSchema


router = APIRouter(
    tags=["image_generator"],
    prefix="/image_generator"
)


@router.post(
    path="/generate",
    status_code=status.HTTP_200_OK,
    summary="Generate image with AI.",
    description="Generate image with AI."
)
async def image_generate(body: ImgGeneratorSchema):
    img_generator_rep = ImageGeneratorRep()
    return await img_generator_rep.generate_img(text=body.text)
