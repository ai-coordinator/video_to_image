# coding : utf-8
import sys
import cv2
import os

image_size = 224

def main():

    dirname = str(sys.argv[1])

    # check output dir
    if os.path.exists('./'+dirname+'_out/') is False:
        os.mkdir('./'+dirname+'_out')

    outdirname = './'+dirname+'_out'

    movie_dir_path = str(sys.argv[1])
    movie_idx = 0
    for movie_name in os.listdir(movie_dir_path):
        try:
            movie_path = os.path.join(movie_dir_path, movie_name)
            if os.path.isdir(movie_path):
                continue

            print('load file %s' % (movie_path))
            cap = cv2.VideoCapture(movie_path)
            filename,ext = os.path.splitext(movie_name)
            movie_idx = movie_idx + 1

            frame_idx = 0
            while True:
                ret, frame = cap.read()
                #print(frame_idx)
                #print(ret,frame)
                if ret is False:
                    continue

#4:3
                # # reisze
                crop_img = cv2.resize(frame, (image_size, image_size))
                # crop
                # crop_img = frame[0:1440, 00:1920]
                out_path = os.path.join(outdirname, filename + '_' + str(frame_idx) + '.jpg')
                print(out_path)

                cv2.imwrite(out_path, crop_img)

                cv2.imshow('src', frame)
                code = cv2.waitKey(1)
                if code == 27:
                    sys.exit()

                frame_idx = frame_idx + 1
        except:
            continue


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        print('python prepro_movie.py DIR_PATH')
