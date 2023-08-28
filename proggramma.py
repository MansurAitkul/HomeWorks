import cv2

def detect_faces(image_path, output_path):

    model_path = "res10_300x300_ssd_iter_140000.caffemodel"
    config_path = "deploy.prototxt"
    net = cv2.dnn.readNetFromCaffe(config_path, model_path)

    image = cv2.imread(image_path)

    height, width = image.shape[:2]
    
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)

    detections = net.forward()
    
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

    cv2.imwrite(output_path, image)

    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

input_image_path = "input.jpg"  # тут две строки ссылка на картинку
output_image_path = "output.jpg"  

detect_faces(input_image_path, output_image_path)