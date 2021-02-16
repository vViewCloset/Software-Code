def color_total():
    from IPython.core.display import HTML
    from IPython.display import Image
    from collections import Counter
    import pandas as pd
    import json

    from plotly.offline import init_notebook_mode, iplot
    import matplotlib.pyplot as plt
    import plotly.graph_objs as go

    from plotly import tools
    import seaborn as sns
    from PIL import Image

    import tensorflow as tf
    import numpy as np

    img = Image.open('camera.png')
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    cutOff = 255

    for item in datas:
        if item[0] >= cutOff and item[1] >= cutOff and item[2] >= cutOff:
            newData.append((255, 255, 255, 0))  #배경제거
        else:
            newData.append(item)

    img.putdata(newData)
    img.save('camera.png', "PNG") # 배경제거 이미지 저장

    #img = Image.open('camera.png')

    # Red = []
    # Green = []
    # Blue = []

    # for x in img:
    #     for y in x:
    #         Red.append(y[0])
    #         Green.append(y[1])
    #         Blue.append(y[2])

    # R_max = max(Red)
    # G_max = max(Green)
    # B_max = max(Blue)

    # R_avg = sum(Red) / len(Red)
    # G_avg = sum(Green) / len(Green)
    # B_avg = sum(Blue) / len(Blue)

    # print("Max Value")
    # print("R : ", R_max)
    # print("G : ", G_max)
    # print("B : ", B_max)

    # print("Avg Value")
    # print("R : ", R_avg)
    # print("G : ", G_avg)
    # print("B : ", B_avg)

    #plt.imshow(img)
    #plt.show()
   
    from PIL import Image
    import urllib
    from io import StringIO

    img=Image.open('camera.png')

    rgbimg=img.convert('RGB')
    average_colors = {}
    def compute_average_image_color(img):
        rgbimg=img.convert('RGB')
        width, height = img.size
        count, r_total, g_total, b_total = 0, 0, 0, 0
        for x in range(0, width):
            for y in range(0, height):
                r, g, b = rgbimg.getpixel((x,y))
                r_total += r
                g_total += g
                b_total += b
                count += 1
        return (r_total/count, g_total/count, b_total/count)

    from IPython.core.display import HTML
    #from IPython.display import Image

    img = Image.open('camera.png')

    average_color = compute_average_image_color(img)
    if average_color not in average_colors:
        average_colors[average_color] = 0
    average_colors[average_color] += 1
   
    for average_color in average_colors:
        average_color1 = (int(average_color[0]),int(average_color[1]),int(average_color[2]))
        image_url = "<span style='display:inline-block; min-width:200px; background-color:rgb"+str(average_color1)+";padding:10px 10px;'>"+str(average_color1)+"</span>"
    #     print (image_url)
  #      display(HTML(image_url))
    
    if int(average_color[0]) >=200:
        string = 'red'
        print('red')
        return string    
    elif int(average_color[1]) >=200:
        string = 'green'
        print('green')
        return string
    elif int(average_color[2]) >=200:
        string = 'blue'
        print('blue')
        return string 
    else:
        string = 'black'
        print('black')
        return string

color_total()
