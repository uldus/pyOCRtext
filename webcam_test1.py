import cv2
import time
def cam_save(filename):
	cap = cv2.VideoCapture(0)

	# Check if the webcam is opened correctly
	if not cap.isOpened():
		raise IOError("Cannot open webcam")


	ret, frame = cap.read()
	# уменьшить в 2 раза
	frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
	cv2.imwrite(filename, frame)
	print("Successfully saved")

	cap.release()
	cv2.destroyAllWindows()

def main():
	filename = 'static\\uploads\\'+ time.strftime("%Y%m%d-%H%M%S") +'.jpg'
	cam_save(filename)
if __name__ == '__main__':
    main()