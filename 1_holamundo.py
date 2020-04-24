import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Captura frame por frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Muestra el output del frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Termino del programa
cap.release()
cv2.destroyAllWindows()