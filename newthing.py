from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image
from googletrans import Translator  # 오류 뜨면 이거 설치 pip install googletrans==4.0.0-rc1
import chagemodel

# 로컬 경로에서 모델과 프로세서 불러오기
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = AutoModelForImageTextToText.from_pretrained("Salesforce/blip-image-captioning-base")

# 이미지 불러오기
image_path = "./example_image/marat-musabirov.jpg"  # 이미지 파일 경로
image = Image.open(image_path)

model = chagemodel.modify_model(model)

# 이미지 캡셔닝
inputs = processor(image, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=50)
caption = processor.decode(outputs[0], skip_special_tokens=True)

# 번역기
translator = Translator()
korean_caption = translator.translate(caption, src="en", dest="ko").text
print("한글 캡션:", korean_caption)
