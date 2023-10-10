#Tim Tran
#1001638285

from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_pdf import PdfPages

round = 0

def KMeans(filename, K):
    DataSet = pd.read_csv(filename, header=None)
    X = np.array(DataSet)
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    counter_4 = 0
    average_1_x = 0
    average_1_y = 0
    average_2_x = 0
    average_2_y = 0
    average_3_x = 0
    average_3_y = 0
    average_4_x = 0
    average_4_y = 0
    cluster_1_x = 0
    cluster_1_y = 0
    cluster_2_x = 0
    cluster_2_y = 0
    cluster_3_x = 0
    cluster_3_y = 0
    cluster_4_x = 0
    cluster_4_y = 0
    
    if K == 2:
        fig2, (ax1, ax2, ax3) = plt.subplots(3)
        plt.figure(1)
        ax1.title.set_text('K = 2 Initial')
        for j in X:
            j[2] = randint(1,K)
            if j[2] == 1:
                ax1.plot(j[0], j[1], 'ro')
                counter_1+=1
                average_1_x+=j[0]
                average_1_y+=j[1]
            elif j[2] == 2:
                ax1.plot(j[0], j[1], 'bo')
                counter_2+=1
                average_2_x+=j[0]
                average_2_y+=j[1]
            elif j[2] == 3:
                ax1.plot(j[0], j[1], 'go')
                counter_3+=1
                average_3_x+=j[0]
                average_3_y+=j[1]
            else:
                ax1.plot(j[0], j[1], 'mo')
                counter_4+=1
                average_4_x+=j[0]
                average_4_y+=j[1]
        average_1_x = average_1_x/counter_1
        average_1_y = average_1_y/counter_1
        cluster_1_x = average_1_x
        cluster_1_y = average_1_y
        average_2_x = average_2_x/counter_2
        average_2_y = average_2_y/counter_2
        cluster_2_x = average_2_x
        cluster_2_y = average_2_y
        ax1.plot(cluster_1_x, cluster_1_y, 'kx')
        ax1.plot(cluster_2_x, cluster_2_y, 'kx')
    elif K == 3:
        fig3, (ax1, ax2, ax3) = plt.subplots(3)
        plt.figure(2)
        ax1.title.set_text('K = 3 Initial')
        for j in X:
            j[2] = randint(1,K)
            if j[2] == 1:
                ax1.plot(j[0], j[1], 'ro')
                counter_1+=1
                average_1_x+=j[0]
                average_1_y+=j[1]
            elif j[2] == 2:
                ax1.plot(j[0], j[1], 'bo')
                counter_2+=1
                average_2_x+=j[0]
                average_2_y+=j[1]
            elif j[2] == 3:
                ax1.plot(j[0], j[1], 'go')
                counter_3+=1
                average_3_x+=j[0]
                average_3_y+=j[1]
            else:
                ax1.plot(j[0], j[1], 'mo')
                counter_4+=1
                average_4_x+=j[0]
                average_4_y+=j[1]
        average_1_x = average_1_x/counter_1
        average_1_y = average_1_y/counter_1
        cluster_1_x = average_1_x
        cluster_1_y = average_1_y
        average_2_x = average_2_x/counter_2
        average_2_y = average_2_y/counter_2
        cluster_2_x = average_2_x
        cluster_2_y = average_2_y
        average_3_x = average_3_x/counter_3
        average_3_y = average_3_y/counter_3
        cluster_3_x = average_3_x
        cluster_3_y = average_3_y
        ax1.plot(cluster_1_x, cluster_1_y, 'kx')
        ax1.plot(cluster_2_x, cluster_2_y, 'kx')
        ax1.plot(cluster_3_x, cluster_3_y, 'kx')
    else:
        fig4, (ax1, ax2, ax3) = plt.subplots(3)
        plt.figure(3)
        ax1.title.set_text('K = 4 Initial')
        for j in X:
            j[2] = randint(1,K)
            if j[2] == 1:
                ax1.plot(j[0], j[1], 'ro')
                counter_1+=1
                average_1_x+=j[0]
                average_1_y+=j[1]
            elif j[2] == 2:
                ax1.plot(j[0], j[1], 'bo')
                counter_2+=1
                average_2_x+=j[0]
                average_2_y+=j[1]
            elif j[2] == 3:
                ax1.plot(j[0], j[1], 'go')
                counter_3+=1
                average_3_x+=j[0]
                average_3_y+=j[1]
            else:
                ax1.plot(j[0], j[1], 'mo')
                counter_4+=1
                average_4_x+=j[0]
                average_4_y+=j[1]
        average_1_x = average_1_x/counter_1
        average_1_y = average_1_y/counter_1
        cluster_1_x = average_1_x
        cluster_1_y = average_1_y
        average_2_x = average_2_x/counter_2
        average_2_y = average_2_y/counter_2
        cluster_2_x = average_2_x
        cluster_2_y = average_2_y
        average_3_x = average_3_x/counter_3
        average_3_y = average_3_y/counter_3
        cluster_3_x = average_3_x
        cluster_3_y = average_3_y
        average_4_x = average_4_x/counter_4
        average_4_y = average_4_y/counter_4
        cluster_4_x = average_4_x
        cluster_4_y = average_4_y
        ax1.plot(cluster_1_x, cluster_1_y, 'kx')
        ax1.plot(cluster_2_x, cluster_2_y, 'kx')
        ax1.plot(cluster_3_x, cluster_3_y, 'kx')
        ax1.plot(cluster_4_x, cluster_4_y, 'kx')
    
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    counter_4 = 0
    previous_mean_1_x = 0
    previous_mean_1_y = 0
    previous_mean_2_x = 0
    previous_mean_2_y = 0
    previous_mean_3_x = 0
    previous_mean_3_y = 0
    previous_mean_4_x = 0
    previous_mean_4_y = 0
    if K == 2:
        round = 0
        plt.figure(1)
        ax2.title.set_text('K = 2 Midway')
        while previous_mean_1_x != average_1_x and previous_mean_1_y != average_1_y and previous_mean_2_x != average_2_x and previous_mean_2_y != average_2_y:
            round+=1
            previous_mean_1_x = average_1_x
            previous_mean_1_y = average_1_y
            previous_mean_2_x = average_2_x
            previous_mean_2_y = average_2_y
            average_1_x = 0
            average_1_y = 0
            average_2_x = 0
            average_2_y = 0
            counter_1 = 0
            counter_2 = 0
            if round == 3:
                for k in X:
                    if k[2] == 1:
                        ax2.plot(k[0], k[1], "ro")
                    else:
                        ax2.plot(k[0], k[1], "bo")
                ax2.plot(cluster_1_x, cluster_1_y, 'kx')
                ax2.plot(cluster_2_x, cluster_2_y, 'kx')
            for j in range(len(X)):
                distance1 = math.hypot(X[j][0]-cluster_1_x, X[j][1]-cluster_1_y)
                distance2 = math.hypot(X[j][0]-cluster_2_x, X[j][1]-cluster_2_y)
                least = min(distance1, distance2)
                if distance1 == least:
                    X[j][2] = 1
                    average_1_x+=X[j][0]
                    average_1_y+=X[j][1]
                    counter_1+=1
                else:
                    X[j][2] = 2
                    average_2_x+=X[j][0]
                    average_2_y+=X[j][1]
                    counter_2+=1
                    
            if counter_1 == 0 or counter_2 == 0:
                print("One or more clusters is/are empty! Please rerun the program!")
                quit()
            average_1_x = average_1_x/counter_1
            average_1_y = average_1_y/counter_1
            cluster_1_x = average_1_x
            cluster_1_y = average_1_y
            average_2_x = average_2_x/counter_2
            average_2_y = average_2_y/counter_2
            cluster_2_x = average_2_x
            cluster_2_y = average_2_y
            
            
        ax3.title.set_text('K = 3 Final')    
        for j in X:
            if j[2] == 1:
                ax3.plot(j[0], j[1], "ro")
            else:
                ax3.plot(j[0], j[1], "bo")
        ax3.plot(cluster_1_x, cluster_1_y, 'kx')
        ax3.plot(cluster_2_x, cluster_2_y, 'kx')
            
    if K == 3:
        round = 0
        plt.figure(2)
        ax2.title.set_text('K = 3 Midway')
        while previous_mean_1_x != average_1_x and previous_mean_1_y != average_1_y and previous_mean_2_x != average_2_x and previous_mean_2_y != average_2_y and previous_mean_3_x != average_3_x and previous_mean_3_y != average_3_y:
            round+=1
            previous_mean_1_x = average_1_x
            previous_mean_1_y = average_1_y
            previous_mean_2_x = average_2_x
            previous_mean_2_y = average_2_y
            previous_mean_3_x = average_3_x
            previous_mean_3_y = average_3_y
            average_1_x = 0
            average_1_y = 0
            average_2_x = 0
            average_2_y = 0
            average_3_x = 0
            average_3_y = 0
            counter_1 = 0
            counter_2 = 0
            counter_3 = 0
            if round == 3:
                for k in X:
                    if k[2] == 1:
                        ax2.plot(k[0], k[1], "ro")
                    elif k[2] == 2:
                        ax2.plot(k[0], k[1], "bo")
                    else:
                        ax2.plot(k[0], k[1], "go")
                            
                ax2.plot(cluster_1_x, cluster_1_y, 'kx')
                ax2.plot(cluster_2_x, cluster_2_y, 'kx')
                ax2.plot(cluster_3_x, cluster_3_y, 'kx')
            for j in range(len(X)):
                distance1 = math.hypot(X[j][0]-cluster_1_x, X[j][1]-cluster_1_y)
                distance2 = math.hypot(X[j][0]-cluster_2_x, X[j][1]-cluster_2_y)
                distance3 = math.hypot(X[j][0]-cluster_3_x, X[j][1]-cluster_3_y)
                least = min(distance1, distance2, distance3)
                if distance1 == least:
                    X[j][2] = 1
                    average_1_x+=X[j][0]
                    average_1_y+=X[j][1]
                    counter_1+=1
                elif distance2 == least:
                    X[j][2] = 2
                    average_2_x+=X[j][0]
                    average_2_y+=X[j][1]
                    counter_2+=1
                else:
                    X[j][2] = 3
                    average_3_x+=X[j][0]
                    average_3_y+=X[j][1]
                    counter_3+=1
            
            if counter_1 == 0 or counter_2 == 0 or counter_3 == 0:
                print("One or more clusters is/are empty! Please rerun the program!")
                quit()    
            average_1_x = average_1_x/counter_1
            average_1_y = average_1_y/counter_1
            cluster_1_x = average_1_x
            cluster_1_y = average_1_y
            average_2_x = average_2_x/counter_2
            average_2_y = average_2_y/counter_2
            cluster_2_x = average_2_x
            cluster_2_y = average_2_y
            average_3_x = average_3_x/counter_3
            average_3_y = average_3_y/counter_3
            cluster_3_x = average_3_x
            cluster_3_y = average_3_y
        ax3.title.set_text('K = 3 Final')
        for j in X:
            if j[2] == 1:
                ax3.plot(j[0], j[1], "ro")
            elif j[2] == 2:
                ax3.plot(j[0], j[1], "bo")
            else:
                ax3.plot(j[0], j[1], "go")
        ax3.plot(cluster_1_x, cluster_1_y, 'kx')
        ax3.plot(cluster_2_x, cluster_2_y, 'kx')
        ax3.plot(cluster_3_x, cluster_3_y, 'kx')
                
    if K == 4:
        round = 0
        plt.figure(3)
        ax2.title.set_text('K = 4 Midway')
        while previous_mean_1_x != average_1_x and previous_mean_1_y != average_1_y and previous_mean_2_x != average_2_x and previous_mean_2_y != average_2_y and previous_mean_3_x != average_3_x and previous_mean_3_y != average_3_y and previous_mean_4_y != average_4_y and previous_mean_4_x != average_4_x and previous_mean_4_y != average_4_y:
            round+=1
            previous_mean_1_x = average_1_x
            previous_mean_1_y = average_1_y
            previous_mean_2_x = average_2_x
            previous_mean_2_y = average_2_y
            previous_mean_3_x = average_3_x
            previous_mean_3_y = average_3_y
            previous_mean_4_x = average_4_x
            previous_mean_4_y = average_4_y
            
            average_1_x = 0
            average_1_y = 0
            average_2_x = 0
            average_2_y = 0
            average_3_x = 0
            average_3_y = 0
            average_4_x = 0
            average_4_y = 0
            counter_1 = 0
            counter_2 = 0
            counter_3 = 0
            counter_4 = 0
            if round == 3:
                for k in X:
                    if k[2] == 1:
                        ax2.plot(k[0], k[1], "ro")
                    elif k[2] == 2:
                        ax2.plot(k[0], k[1], "bo")
                    elif k[2] == 3:
                        ax2.plot(k[0], k[1], "go")
                    else:
                        ax2.plot(k[0], k[1], "mo")
                ax2.plot(cluster_1_x, cluster_1_y, 'kx')
                ax2.plot(cluster_2_x, cluster_2_y, 'kx')
                ax2.plot(cluster_3_x, cluster_3_y, 'kx')
                ax2.plot(cluster_4_x, cluster_4_y, 'kx')
            for j in range(len(X)):
                distance1 = math.hypot(X[j][0]-cluster_1_x, X[j][1]-cluster_1_y)
                distance2 = math.hypot(X[j][0]-cluster_2_x, X[j][1]-cluster_2_y)
                distance3 = math.hypot(X[j][0]-cluster_3_x, X[j][1]-cluster_3_y)
                distance4 = math.hypot(X[j][0]-cluster_4_x, X[j][1]-cluster_4_y)
                least = min(distance1, distance2, distance3, distance4)
                if distance1 == least:
                    X[j][2] = 1
                    average_1_x+=X[j][0]
                    average_1_y+=X[j][1]
                    counter_1+=1
                elif distance2 == least:
                    X[j][2] = 2
                    average_2_x+=X[j][0]
                    average_2_y+=X[j][1]
                    counter_2+=1
                elif distance3 == least:
                    X[j][2] = 3
                    average_3_x+=X[j][0]
                    average_3_y+=X[j][1]
                    counter_3+=1
                else:
                    X[j][2] = 4
                    average_4_x+=X[j][0]
                    average_4_y+=X[j][1]
                    counter_4+=1
            
            if counter_1 == 0 or counter_2 == 0 or counter_3 == 0 or counter_4 == 0:
                print("One or more clusters is/are empty! Please rerun the program!")
                quit()
            average_1_x = average_1_x/counter_1
            average_1_y = average_1_y/counter_1
            cluster_1_x = average_1_x
            cluster_1_y = average_1_y
            average_2_x = average_2_x/counter_2
            average_2_y = average_2_y/counter_2
            cluster_2_x = average_2_x
            cluster_2_y = average_2_y
            average_3_x = average_3_x/counter_3
            average_3_y = average_3_y/counter_3
            cluster_3_x = average_3_x
            cluster_3_y = average_3_y
            average_4_x = average_4_x/counter_4
            average_4_y = average_4_y/counter_4
            cluster_4_x = average_4_x
            cluster_4_y = average_4_y
            
        ax3.title.set_text('K = 4 Final')
        for j in X:
            if j[2] == 1:
                ax3.plot(j[0], j[1], "ro")
            elif j[2] == 2:
                ax3.plot(j[0], j[1], "bo")
            elif j[2] == 3:
                ax3.plot(j[0], j[1], "go")
            else:
                ax3.plot(j[0], j[1], "mo")
        ax3.plot(cluster_1_x, cluster_1_y, 'kx')
        ax3.plot(cluster_2_x, cluster_2_y, 'kx')
        ax3.plot(cluster_3_x, cluster_3_y, 'kx')
        ax3.plot(cluster_4_x, cluster_4_y, 'kx')
    pp = PdfPages('output.pdf')
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(pp, format='pdf')
    pp.close()
    
    
KMeans("ClusteringData.txt", 2)
KMeans("ClusteringData.txt", 3)
KMeans("ClusteringData.txt", 4)