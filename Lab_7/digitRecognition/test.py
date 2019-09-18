#importing required modules
import numpy as np,cv2,imutils
from sklearn.externals import joblib

#reading image
img = cv2.imread('photo_3.jpg')
#resizing image
img = imutils.resize(img,width=300)
#showing original image
#cv2.imshow("Original",img)
#converting image to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#showing grayscale image
#cv2.imshow("Gray Image",gray)

#creating a kernel
kernel = np.ones((40,40),np.uint8)

#applying blackhat thresholding
blackhat = cv2.morphologyEx(gray,cv2.MORPH_BLACKHAT,kernel)


#applying OTSU's thresholding
ret,thresh = cv2.threshold(blackhat,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#performing erosion and dilation
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

#finding countours in image
ret,cnts,hie = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

rects = [cv2.boundingRect(ctr) for ctr in cnts]
rectsO = rects.copy()
rects.sort(key=lambda tup: tup[0])

revarr = []
for i in rects:
    for j, k in enumerate(rectsO):
        if i == k: revarr.append(j)

#loading our ANN model
model = joblib.load('model.pkl')
i = 0
yourtext = []
for c in cnts:
    #print(c)
    try:
        #creating a mask
        mask = np.zeros(gray.shape,dtype="uint8")


        (x,y,w,h) = rects[i]

        hull = cv2.convexHull(cnts[revarr[i]])
        cv2.drawContours(mask,[hull],-1,255,-1)
        mask = cv2.bitwise_and(thresh,thresh,mask=mask)


        #Getting Region of interest
        roi = mask[y-7:y+h+7,x-7:x+w+7]
        roi = cv2.resize(roi,(28,28))
        roi = np.array(roi)
        #reshaping roi to feed image to our model
        roi = roi.reshape(1,784)

        #predicting
        prediction = model.predict(roi)

        yourtext.append(str(int(prediction)))
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
        cv2.putText(img,str(int(prediction)),(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),1)

    except Exception as e:
        print(e)
    i += 1
        
img = imutils.resize(img,width=500)

#showing the output
print(''.join(yourtext))
cv2.imshow('Detection',img)
cv2.imwrite('result2.jpg',img)
cv2.waitKey()
