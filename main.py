# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np
import re

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def find_closest_value_2d(array, target):
    absolute_diff = np.abs(array - target)
    closest_index = np.unravel_index(np.argmin(absolute_diff), array.shape)
    closest_value = array[closest_index]
    return closest_value, closest_index

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = pd.read_csv('data.csv')
    print(data.head())
    print(data.columns)
    d_clos = [ i for i in data.columns if '0,' in i ]
    #d_clos = d_clos[2:-1]

    epsent_index = [i for i in range(0,101) if i not in data['Unnamed: 0'].tolist() ]
    print(data['Unnamed: 0'].tolist(),epsent_index)
    index_range = epsent_index  # Range of indices from 0 to 100
    data.reset_index(drop=True, inplace=True)

    data.set_index('Unnamed: 0', inplace=True)
    new_df = pd.DataFrame(index=index_range, columns=data.columns)

    # Concatenate the new DataFrame with the original DataFrame
    df_concatenated = pd.concat([data, new_df])
    print(df_concatenated.sort_index())
    print(d_clos)
    df_concatenated = df_concatenated.sort_index()
    df_concatenated.fillna(np.nan,inplace=True)
    for col in df_concatenated.columns:
        df_concatenated[col] = df_concatenated[col].interpolate()
    print(df_concatenated)
    df_int = df_concatenated.astype(int)
    print(df_int)



    Xb = 11370
    Yb = 51590
    Hb = 1000
    Xc = 18250
    Yc = 50720
    Hc = 1000
    An = 1000
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
    print(d_df.head())
    pd.set_option('display.max_rows', None)  # Show all rows
    pd.set_option('display.max_columns', None)  # Show all columns
    pd.set_option('display.expand_frame_repr', False)  # Disable column-wise wrapping
    # Example usage
    arr = d_df.to_numpy()
    target = KoefN
    closest_value, closest_index = find_closest_value_2d(arr, target)
    print(closest_value)  # Output: 6
    print(closest_index)  # Output: (1, 2)
    rk_col = closest_index[1]
    rk_row = closest_index[0]

    data_head= pd.read_csv("data_head.csv")
    if down:
        print(df_int['Unnamed: 17'].tolist()[rk_row])
    else:
        print(df_int.index[rk_row])
    data_head = data_head.dropna(axis=1)
    print(data_head.to_numpy()[target_index_RK][rk_col])

    print(x_flag,y_flag,target_index_RK,x,y,KoefN)
    angle=str(data_head.to_numpy()[target_index_RK][rk_col])
    angle_change = str(df_int['Unnamed: 17'].tolist()[rk_row])
    to_zero="00"
    angle=angle.replace(to_zero,"",1)
    angle="".join([angle,angle_change])
    print('KoefN=',KoefN)
    print('^x=',x)
    print('^y=',y)
    print('^angle=',angle)