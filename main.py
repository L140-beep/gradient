import matplotlib.pyplot as plt
import numpy as np

def lerp(v0, v1, t): #линейная интерполяция, крутяк
    return (1 - t) * v0 + t * v1 #вычисляется новая RGB, отталкивающаяся от соотношения двух цветов (t) 
    #например, v0 = 255, v1 = 128, t = 0,6; (1 - 0.6) * 255 + 128 * 0.4 = 178.8

size = 5 #Размер картинки
image = np.zeros((size, size, 3), dtype="uint8") #Создаем трехмерный массив, где первые две размерности - поле, а третья - цвет
assert image.shape[0] == image.shape[1] #если не квадрат - шлем куда подальше

#цвета
color1 = [255, 128, 0]
color2 = [0, 128, 255]

# for i, v in enumerate(np.linspace(0, 1, image.shape[0])): #создаем массив из 100 элементов, переходящих от 0 к 1
#     #и означающих переход от одного цвета к другому
#     #i - порядковый номер элемента массива, v - сам элемент
#     r = lerp(color1[0], color2[0], v) #передаем в функцию lerp R и коэффициент (v)
#     g = lerp(color1[1], color2[1], v)
#     b = lerp(color1[2], color2[2], v)
#     image[i, :, :] = [r, g, b] #присваиваем сразу всей строке цвет
#благодаря этому замечательнейшему анализу, я понял, что для поворота на 45 градусов нужно поиграть с методом расположения цветов
#в image, так как мы физически не сможем сделать градиент, когда у нас заполняется сразу вся строка.

for i, v in enumerate(np.linspace(0, 0.5, image.shape[0])):
    x = i 
    y = 0
    print(i)
    while(x >= 0):
        print(x , y)
        r = lerp(color1[0], color2[0], v) 
        g = lerp(color1[1], color2[1], v)
        b = lerp(color1[2], color2[2], v)
        image[y, x, :] = [r, g, b]
        y += 1
        x -= 1

for i, v in enumerate(np.linspace(0.5, 1, image.shape[0])):
    x = size - 1
    y = i
    while(y < size):
        r = lerp(color1[0], color2[0], v) 
        g = lerp(color1[1], color2[1], v)
        b = lerp(color1[2], color2[2], v)
        image[y, x, :] = [r, g, b]
        y += 1
        x -= 1
      
plt.figure(1)
plt.imshow(image)
plt.show()
