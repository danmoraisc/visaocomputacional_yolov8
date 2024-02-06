import cv2
from yolov8 import YOLOv8
from cap_from_youtube import cap_from_youtube

# # Initialize video
# cap = cv2.VideoCapture("input.mp4")
'''
Essa função aplica o algoritimo YOLOV8 para detecção de objetos em videos diretamente do youtube.
PARAM:
    1. modelo = modelo de yolov8 a ser aplicado:
        'n': modelo nano
        's': modelo pequeno
        'm': modelo medio
        'l': modelo grande
        'x': modelo extragrande
    2. videoUrl = link do youtube (str)
'''

def youtube_object_detection(modelo, videoUrl, start_time='135'):

    #videoUrl = "https://www.youtube.com/watch?v=KBsqQez-O4w" #'https://youtu.be/Snyg0RqpVxY'
    cap = cap_from_youtube(videoUrl, resolution='360p') #720p
    #start_time = 135 # skip os primeiros {start_time} segundos


    cap.set(cv2.CAP_PROP_POS_FRAMES, start_time * cap.get(cv2.CAP_PROP_FPS))

    # out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), cap.get(cv2.CAP_PROP_FPS), (3840, 2160))

    # modelos possiveis
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

    #detector
    yolov8_detector = YOLOv8(model_path, conf_thres=0.5, iou_thres=0.5)

    cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)

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
        cv2.imshow("Detected Objects", combined_img)
        # out.write(combined_img)

    cv2.destroyAllWindows()
    cap.release()
    # out.release()

youtube_object_detection(modelo='s', videoUrl='https://www.youtube.com/watch?v=KBsqQez-O4w')