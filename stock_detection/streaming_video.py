import os
import cv2
from reolinkapi import Camera

from imageai.Detection import VideoObjectDetection

def non_blocking():
    print("calling non-blocking")

    def inner_callback(img):
        cv2.imshow("name", maintain_aspect_ratio_resize(img, width=600))
        print("got the image non-blocking")
        key = cv2.waitKey(1)
        if key == ord('q'):
            cv2.destroyAllWindows()
            exit(1)

    c = Camera("192.168.1.112", "admin", "jUa2kUzi")
    # t in this case is a thread
    t = c.open_video_stream(callback=inner_callback)

    print(t.is_alive())
    while True:
        if not t.is_alive():
            print("continuing")
            break
        # stop the stream
        # client.stop_stream()


def object_detection():
    execution_path = os.getcwd()
    c = Camera("192.168.0.105", "admin", "StrongLink123")
    stream = c.open_video_stream()


    camera = cv2.VideoCapture(stream)


    detector = VideoObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path , "yolo.h5")) # Download the model via this link https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0
    detector.loadModel()

    video_path = detector.detectObjectsFromVideo(camera_input=camera,
                                    output_file_path=os.path.join(execution_path, "camera_detected_video")
                                    , frames_per_second=20, log_progress=True, minimum_percentage_probability=30)
    print(video_path)

def blocking():
    c = Camera("192.168.0.105", "admin", "StrongLink123")
    # stream in this case is a generator returning an image (in mat format)
    stream = c.open_video_stream()

    # using next()
    # while True:
    #     img = next(stream)
    #     cv2.imshow("name", maintain_aspect_ratio_resize(img, width=600))
    #     print("got the image blocking")
    # # key = cv2.waitKey(1)
    #     if key == ord('q'):
    #         cv2.destroyAllWindows()
    #         exit(1)

    # or using a for loop
    for img in stream:
        cv2.imshow("name", maintain_aspect_ratio_resize(img, width=600))
        print("got the image blocking")
        key = cv2.waitKey(1)
        if key == ord('q'):
            cv2.destroyAllWindows()
            exit(1)


# Resizes a image and maintains aspect ratio
def maintain_aspect_ratio_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # Grab the image size and initialize dimensions
    dim = None
    (h, w) = image.shape[:2]

    # Return original image if no need to resize
    if width is None and height is None:
        return image

    # We are resizing height if width is none
    if width is None:
        # Calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    # We are resizing width if height is none
    else:
        # Calculate the ratio of the 0idth and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # Return the resized image
    return cv2.resize(image, dim, interpolation=inter)


# Call the methods. Either Blocking (using generator) or Non-Blocking using threads
# non_blocking()
# blocking()
object_detection()import os
import cv2
from reolinkapi import Camera

from imageai.Detection import VideoObjectDetection

def non_blocking():
    print("calling non-blocking")

    def inner_callback(img):
        cv2.imshow("name", maintain_aspect_ratio_resize(img, width=600))
        print("got the image non-blocking")
        key = cv2.waitKey(1)
        if key == ord('q'):
            cv2.destroyAllWindows()
            exit(1)

    c = Camera("192.168.1.112", "admin", "jUa2kUzi")
    # t in this case is a thread
    t = c.open_video_stream(callback=inner_callback)

    print(t.is_alive())
    while True:
        if not t.is_alive():
            print("continuing")
            break
        # stop the stream
        # client.stop_stream()


def object_detection():
    execution_path = os.getcwd()
    c = Camera("192.168.0.105", "admin", "StrongLink123")
    stream = c.open_video_stream()


    camera = cv2.VideoCapture(stream)


    detector = VideoObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path , "yolo.h5")) # Download the model via this link https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0
    detector.loadModel()

    video_path = detector.detectObjectsFromVideo(camera_input=camera,
                                    output_file_path=os.path.join(execution_path, "camera_detected_video")
                                    , frames_per_second=20, log_progress=True, minimum_percentage_probability=30)
    print(video_path)

def blocking():
    c = Camera("192.168.0.105", "admin", "StrongLink123")
    # stream in this case is a generator returning an image (in mat format)
    stream = c.open_video_stream()

    # using next()
    # while True:
    #     img = next(stream)
    #     cv2.imshow("name", maintain_aspect_ratio_resize(img, width=600))
    #     print("got the image blocking")
    # # key = cv2.waitKey(1)
    #     if key == ord('q'):
    #         cv2.destroyAllWindows()
    #         exit(1)

    # or using a for loop
    for img in stream:
        cv2.imshow("name", maintain_aspect_ratio_resize(img, width=600))
        print("got the image blocking")
        key = cv2.waitKey(1)
        if key == ord('q'):
            cv2.destroyAllWindows()
            exit(1)


# Resizes a image and maintains aspect ratio
def maintain_aspect_ratio_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # Grab the image size and initialize dimensions
    dim = None
    (h, w) = image.shape[:2]

    # Return original image if no need to resize
    if width is None and height is None:
        return image

    # We are resizing height if width is none
    if width is None:
        # Calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    # We are resizing width if height is none
    else:
        # Calculate the ratio of the 0idth and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # Return the resized image
    return cv2.resize(image, dim, interpolation=inter)


# Call the methods. Either Blocking (using generator) or Non-Blocking using threads
# non_blocking()
# blocking()
object_detection()