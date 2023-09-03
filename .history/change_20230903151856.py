import camelot.io as camelot
import os
os.chdir('C:/Users/EDZ/Desktop')
import cv2

data1= camelot.read_pdf("丽水2019.pdf", pages='70',flavor='stream')
data1[0].to_csv('data1.csv',encoding='utf_8_sig')