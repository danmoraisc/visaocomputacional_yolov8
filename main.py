import datetime
import cv2
from video_detection import video_detection
from webcam_detection import webcam_detection
from youtube_detection import youtube_object_detection


def main():
    video_detection(modelo='n')  # Chame a função desejada com o parametro correspondente ao modelo, dentre os disponiveis (n,s,m,l,x)

if __name__ == "__main__":
    main()


