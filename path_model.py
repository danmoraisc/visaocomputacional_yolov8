def obter_model_path(modelo):
    modelos_paths = {
        'n': "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8n.onnx",
        's': "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8s.onnx",
        'm': "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8m.onnx",
        'l': "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8l.onnx",
        'x': "models/Modelos YoloV8 640x480/otimizado_cpu/yolov8x.onnx"
    }

    return modelos_paths.get(modelo, f"Modelo {modelo} inválido")

#print(obter_model_path('l'))
