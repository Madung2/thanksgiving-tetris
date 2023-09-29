# 파이썬 이미지 사용
FROM python:3.9-slim

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev

# 파이썬 라이브러리 설치
RUN pip install pygame pygbag

# 커맨드 실행
CMD ["pygbag", "tetris"]