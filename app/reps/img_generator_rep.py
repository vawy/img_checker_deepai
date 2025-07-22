from app.services.deepai_service import DeepAiService


class ImageGeneratorRep:
    def __init__(self, deepai_service: DeepAiService = None):
        self.deepai_service = deepai_service or DeepAiService()

    async def generate_img(self, text: str):
        return await self.deepai_service.generate_img(text=text)
