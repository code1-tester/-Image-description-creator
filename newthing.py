from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image
from googletrans import Translator  # 설치 필요: pip install googletrans==4.0.0-rc1
import chagemodel  # chagemodel.py 파일에서 modify_model 함수 사용

# 모델과 프로세서 초기화
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = AutoModelForImageTextToText.from_pretrained("Salesforce/blip-image-captioning-base")
model = chagemodel.modify_model(model)

translator = Translator()

def generate_caption(image_path):

    try:
        # 이미지 로드
        image = Image.open(image_path)

        # 이미지 캡션 생성
        inputs = processor(image, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=50)
        caption = processor.decode(outputs[0], skip_special_tokens=True)

        # 캡션 번역 (영어 -> 한국어)
        translated_caption = translator.translate(caption, src="en", dest="ko").text

        return caption, translated_caption
    except Exception as e:
        return "Error generating caption", str(e)
