import pandas as pd
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def find_closest_value_2d(array, target):
    absolute_diff = np.abs(array - target)
    closest_index = np.unravel_index(np.argmin(absolute_diff), array.shape)
    closest_value = array[closest_index]
    return closest_value, closest_index



def get_angle(Xb,Yb,Hb,Xc,Yc,Hc,An= 1000):

    data_head = pd.read_csv("data_head.csv")
    df_int = pd.read_csv("table_int.csv")
    data = pd.read_csv('data.csv')
    d_clos = [i for i in data.columns if '0,' in i]

    x = Xc - Xb
    y = Yc - Yb
    h = Hc - Hb
    abX = abs(x)
    abY = abs(y)
    target_index_RK = 0

    x_flag = 0
    y_flag = 0
    if abX > abY:
        y_flag = 1
        BRK = x
        MRK = y
    if abX < abY:
        x_flag = 1
        BRK = y
        MRK = x
    KoefN =int( abs(MRK / BRK * 1000))
    down = 0
    if x_flag == 1 and x<0 and y>=0 :
        target_index_RK = 2
    elif x_flag == 1 and x>=0 and y<0 :
        target_index_RK = 0
    elif y_flag == 1 and y<0 and x<0 :
        target_index_RK = 1
    elif y_flag == 1 and y>=0 and x>=0:
        target_index_RK = 3
    elif x_flag == 1 and x >= 0 and y >= 0:
        target_index_RK = 4
        down = 1
    elif y_flag == 1 and y >= 0 and x < 0:
        target_index_RK = 5
        down = 1
    elif x_flag == 1 and y < 0 and x < 0:
        target_index_RK = 6
        down = 1
    elif y_flag == 1 and y < 0 and x >= 0:
        target_index_RK = 7
        down = 1
    d_df = df_int[d_clos]



    arr = d_df.to_numpy()
    target = KoefN
    closest_value, closest_index = find_closest_value_2d(arr, target)
    rk_col = closest_index[1]
    rk_row = closest_index[0]


    if down:
        #print(df_int['Unnamed: 17'].tolist()[rk_row])
        angle_change = str(df_int['Unnamed: 17'].tolist()[rk_row])
    else:
        #print(df_int.index[rk_row])
        angle_change = str(df_int.index[rk_row])
    data_head = data_head.dropna(axis=1)
    #print(x_flag,y_flag,target_index_RK,x,y,KoefN)
    angle=str(data_head.to_numpy()[target_index_RK][rk_col])

    to_zero="00"
    angle=angle.replace(to_zero,"",1)
    angle="".join([angle,angle_change])
    #print('KoefN=',KoefN)
    #print('^x=',x)
    #print('^y=',y)
    #print('^angle=',angle)
    return angle,x,y,KoefN