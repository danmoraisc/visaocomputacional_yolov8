import cv2
from yolov8 import YOLOv8
import time


def video_detection(modelo):
    # variável para cálculo do tempo de execução
    inicio = time.time()

    videoUrl = 'videos/highway_traffic_10sec.mp4'
    cap = cv2.VideoCapture(videoUrl)

    # modelos possiveis
    if modelo == 'n':  # modelo nano
        model_path = "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8n.onnx"
    elif modelo == 's':  # modelo pequeno
        model_path = "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8s.onnx"
    elif modelo == 'm':  # modelo medio
        model_path = "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8m.onnx"
    elif modelo == 'l':  # modelo grande
        model_path = "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8l.onnx"
    elif modelo == 'x':  # modelo extragrande
        model_path = "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8x.onnx"
    else:
        return f"Modelo {modelo} inválido"

    # detector
    yolov8_detector = YOLOv8(model_path, conf_thres=0.6, iou_thres=0.5)

    cv2.namedWindow("Video Detection", cv2.WINDOW_NORMAL)

    while cap.isOpened():

        # Press key q to stop
        if cv2.waitKey(1) == ord('q'):
            break

        try:
            # Read frame from the video
            ret, frame = cap.read()
            if not ret:
                break
        except Exception as e:
            print(e)
            continue

        # Update object localizer
        boxes, scores, class_ids = yolov8_detector(frame)

        combined_img = yolov8_detector.draw_detections(frame)
        cv2.imshow('Video Detection', combined_img)
        # out.write(combined_img)

    cv2.destroyAllWindows()
    cap.release()

    # tempo de execução
    fim = time.time()
    tempo_execucao = fim - inicio
    print(f'Tempo de execução: {tempo_execucao} segundos')
    print(f'Algoritmo concluído.')


video_detection(modelo='n')
