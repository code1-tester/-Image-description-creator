from transformers import BlipForConditionalGeneration, BlipProcessor

# Hugging Face에서 사전 학습된 모델과 processor 불러오기
model_name = "Salesforce/blip-image-captioning-large"

# 모델과 processor 불러오기
model = BlipForConditionalGeneration.from_pretrained(model_name)
processor = BlipProcessor.from_pretrained(model_name)

def modify_model(model):
    # 텍스트 생성 설정 변경
    model.generation_config.max_length = 50  # 텍스트 최대 길이 변경
    model.generation_config.num_beams = 10   # 빔 서치 개수 설정

    # 이미지 처리 설정 변경
    model.config.vision_config.image_size = 512  # 이미지 크기 변경
    model.config.vision_config.num_hidden_layers = 24  # 레이어 수 변경

    return model

model = modify_model(model)

print("complete")



