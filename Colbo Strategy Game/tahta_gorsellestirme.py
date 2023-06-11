import cv2
import numpy as np
import time

class TahtaGorsellestirme():


    
    def __init__(self,tahta):
        donusturulmus_tahta = [] #b,g,r
        row_list = []
        for row in tahta:
            for element in row:
                if   element == 0:
                    
                    row_list.append([220,220,220])
                elif   element == 1:
                    row_list.append([30,60,230])
                elif element == 2:
                    row_list.append([0,30,185])
                elif element == 3:
                    row_list.append([235,165,40])
                elif element == 4:
                    row_list.append([185,120,0])
                elif element == 5:
                    row_list.append([30,220,50])
                elif element == 6:
                    row_list.append([0,170,20])
                elif element == 7:
                    row_list.append([0,220,255])
                elif element == 8:
                    row_list.append([0,190,220])
                elif element == 9:
                    row_list.append([120,120,120])
                
            donusturulmus_tahta.append(row_list)
            row_list = []
        
        """
        tahta = np.array([[[49,242,12],[3,125,3],[255,25,0],[255,25,0]],
                               [[0,0,0],[255,1,15],[0,0,0],[255,25,0]],
                               [[0,55,255],[0,0,0],[35,235,22],[255,25,0]],
                               [[0,0,0],[255,1,15],[0,0,0],[255,25,0]]
                               ])
        """
        donusturulmus_tahta = np.array(donusturulmus_tahta)
        tahta = self.arrayBuyutRenkli(donusturulmus_tahta,50)
        tahta = self.izgara_ciz(tahta)
      
        self.goster(tahta)
      
        
    def arrayBuyutRenkli(self,tahta,x=50):
                
        new_tahta = np.zeros(shape=(len(tahta) * x,len(tahta) * x,3))
        for row_index , row in enumerate(tahta):
            
            for index, elem in enumerate(row):
                for k in range(x):
                    for j in range(x):
                        new_tahta[row_index * x + x - j -1,index * x + x - k -1] = elem

       # print(new_tahta.shape)
                
        return new_tahta
        
    def izgara_ciz(self,im):
        
        #yatay
        for x in range(12):
            for y in range(12):
                im[50*y:50*y + 2,:] = [180,180,180]
                im[50*y+50:50*y + 50 + 2,:] = [180,180,180]        
                #dikey
           
                im[:,50 *x:50 * x + 2] = [180,180,180]
                im[:,50 *x + 50:50 * x + 50 + 2] = [180,180,180]        
        
        return im
    def goster(self,tahta):

        cv2.imwrite("tahta.png",tahta)

        #img = cv2.imread("tahta.png")
        #cv2.imshow("Oyun Tahtasi",img)
        #cv2.waitKey(0)

#TahtaGorsellestirme().surec()