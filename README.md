# Detecção de objetos com YOLOv8 

Este repositório contém uma implementação de detecção de objetos usando YOLO v8 em vídeos. 
O projeto inclui 5 modelos pré-treinados ('n', 's', 'm', 'l', 'x') correspondentes a Nano, Pequeno, Médio, Grande e Extragrande, respectivamente.

## Funcionalidades

O projeto permite a detecção de objetos em vídeos de três maneiras diferentes:

1. **Detecção de vídeo do YouTube:** `youtube_detection.py`
2. **Detecção de vídeo local:** `video_detection.py`
3. **Detecção via webcam:** `webcam_detection.py`

## Uso
Cada script de detecção recebe um modelo YOLO como parâmetro. Os modelos disponíveis são n, s, m, l, e x, onde:

n - nano
s - small
m - medium
l - large
x - extralarge

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas antes de executar o código:

opencv-python 
ultralytics
onnxruntime 
cap-from-youtube

## Licença
Este projeto está licenciado sob a Licença MIT.
