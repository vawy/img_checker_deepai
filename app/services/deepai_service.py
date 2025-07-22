from fastapi import HTTPException
import httpx

from app.settings import settings


class DeepAiService:
    @staticmethod
    async def generate_img(text: str):
        """Send text to DeepAi and get image."""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url=settings.DEEPAI_GENERATE_IMG_URL,
                    data={"text": text},
                    headers={"api-key": settings.DEEPAI_API_KEY},
                    timeout=5.0
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        finally:
            await client.aclose()
