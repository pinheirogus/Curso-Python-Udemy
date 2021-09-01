import cv2

######################################################################################################################
"""
Importando imagem
"""
######################################################################################################################
# img = cv2.imread("Resources/saida_fotos_gus-10.jpg")
#
# cv2.imshow("Output", img)
# cv2.waitKey(0)

######################################################################################################################
"""
Importando video
"""
######################################################################################################################
#
# videoCap = cv2.VideoCapture("Resources/gus_talking.mkv")
#
# while True:
#     success, img = videoCap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
######################################################################################################################
"""
Importando webcam
"""
######################################################################################################################

# ID 0 is default webcam
webCamCap = cv2.VideoCapture(0)


# ID 3 is for width
webCamCap.set(3, 640)
#ID 4 is for height
webCamCap.set(4, 480)
#ID 10 is for brightness
webCamCap.set(10, 100)

while True:
    success, img = webCamCap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break