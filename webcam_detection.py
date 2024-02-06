import cv2
from yolov8 import YOLOv8


def webcam_detection(modelo):

    # Inicializa a captura de vídeo da webcam
    cap = cv2.VideoCapture(0)

    #modelos possiveis
    if modelo == 'n': # modelo nano
        model_path = "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8n.onnx"
    elif modelo == 's': # modelo pequeno
        model_path = "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8s.onnx"
    elif modelo == 'm': # modelo medio
        model_path = "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8m.onnx"
    elif modelo == 'l': # modelo grande
        model_path = "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8l.onnx"
    elif modelo == 'x': # modelo extragrande
        model_path = "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8x.onnx"
    else:
        return f"Modelo {modelo} inválido"

    # Caminho do modelo YOLOv8 pré-treinado
    #model_path = "models/yolov8s.onnx"
    yolov8_detector = YOLOv8(model_path, conf_thres=0.5, iou_thres=0.5)

    cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
    while cap.isOpened(): # Loop enquanto a captura de vídeo estiver aberta

        # Lê um frame do vídeo
        ret, frame = cap.read()

        if not ret: # Verifica se o frame foi lido corretamente
            break # Se não, interrompe o loop

        # Atualiza o localizador de objetos (detector YOLOv8)
        boxes, scores, class_ids = yolov8_detector(frame)

        # Desenha as detecções no frame
        combined_img = yolov8_detector.draw_detections(frame)
        cv2.imshow("Detected Objects", combined_img)

        # Pressione a tecla 'q' para parar a detecção
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#webcam_detection(modelo='x')