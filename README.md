# Image generator

### Установите зависимости
```bazaar
python -m pip install -r requirements.txt
```

### В app/settings создайте .env, где укажите 
```bazaar
DEEPAI_API_KEY=ваш апи ключ
DEEPAI_GENERATE_IMG_URL=https://api.deepai.org/api/text2img
```

### из корня запустите приложение
```bazaar
python app/main.py
```

### swagger
```bazaar
http://127.0.0.1:8000/api/images_editor/swagger
```

### пример запроса
```bazaar
curl -X 'POST' \
  'http://127.0.0.1:8000/api/image_editor/image_generator/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "белый котик на машине за рулем"
}'
```
