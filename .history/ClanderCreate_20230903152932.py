import camelot.io as camelot
import cv2

data1= camelot.read_pdf("PgtPreclass.pdf",flavor='stream')
data1[0].to_csv('data1.csv',encoding='utf_8_sig')