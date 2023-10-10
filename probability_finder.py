import pandas as pd
import numpy as np


DataSet = pd.read_csv("training_data.txt", header=None, sep=r'\s{2,}', engine='python')
bgtv = np.array(DataSet.iloc[: , 0])
gwtv = np.array(DataSet.iloc[:, 1])
oocf = np.array(DataSet.iloc[:, 2])
gfc = np.array(DataSet.iloc[:, 3])

bgtv_count = 0
gwtv_count = 0
oocf_count = 0
gfc_count = 0
gwtv_bgtv1 = 0
gwtv_bgtv0 = 0
oocf1_gwtv1 = 0
oocf0_gwtv1 = 0
oocf1_gwtv0 = 0
oocf0_gwtv0 = 0
gfc_oocf1_gwtv1 = 0
gfc_oocf0_gwtv1 = 0
gfc_oocf1_gwtv0 = 0
gfc_oocf0_gwtv0 = 0
for i in range(len(bgtv)):
    if bgtv[i] == 1:
        bgtv_count+=1
    if gwtv[i] == 1:
        gwtv_count+=1
    if oocf[i] == 1:
        oocf_count+=1
    if gfc[i] == 1:
        gfc_count+=1
    if bgtv[i] == 1 and gwtv[i] == 1:
        gwtv_bgtv1+=1
    if bgtv[i] == 0 and gwtv[i] == 1:
        gwtv_bgtv0+=1
    if oocf[i] == 1 and gwtv[i] == 1:
        oocf1_gwtv1+=1
    if oocf[i] == 0 and gwtv[i] == 1:
        oocf0_gwtv1+=1
    if oocf[i] == 1 and gwtv[i] == 0:
        oocf1_gwtv0+=1
    if oocf[i] == 0 and gwtv[i] == 0:
        oocf0_gwtv0+=1
    if oocf[i] == 1 and gwtv[i] == 1 and gfc[i] == 1:
        gfc_oocf1_gwtv1+=1
    if oocf[i] == 0 and gwtv[i] == 1 and gfc[i] == 1:
        gfc_oocf0_gwtv1+=1
    if oocf[i] == 1 and gwtv[i] == 0 and gfc[i] == 1:
        gfc_oocf1_gwtv0+=1
    if oocf[i] == 0 and gwtv[i] == 0 and gfc[i] == 1:
        gfc_oocf0_gwtv0+=1
        

bgtv_prob_1 = bgtv_count/365
bgtv_prob_0 = 1-bgtv_prob_1
gwtv_prob_1 = gwtv_count/365
gwtv_prob_0 = 1-gwtv_prob_1
oocf_prob_1 = oocf_count/365
oocf_prob_0 = 1-oocf_prob_1
gfc_prob_1 = gfc_count/365
gfc_prob_0 = 1-gfc_prob_1
gwtv_bgtv1_prob = gwtv_bgtv1/bgtv_count
gwtv_bgtv0_prob = gwtv_bgtv0/(365-bgtv_count)

print("P(Baseball_game_on_TV) = %.3f" % (bgtv_prob_1))
print("P(Out_of_cat_food) = %.3f" % (oocf_prob_1))

print("P(George_watches_TV | Baseball_game_on_TV = 1) = %.3f" % (gwtv_bgtv1_prob))
print("P(George_watches_TV | Baseball_game_on_TV = 0) = %.3f" % (gwtv_bgtv0_prob))

gfc_oocf1_gwtv1_prob = gfc_oocf1_gwtv1/oocf1_gwtv1
gfc_oocf0_gwtv1_prob = gfc_oocf0_gwtv1/oocf0_gwtv1
gfc_oocf1_gwtv0_prob = gfc_oocf1_gwtv0/oocf1_gwtv0
gfc_oocf0_gwtv0_prob = gfc_oocf0_gwtv0/oocf0_gwtv0

print("P(George_feeds_cat | Out_of_cat_food = 0, George_watches_tv = 0) = %.3f" % (gfc_oocf0_gwtv0_prob))
print("P(George_feeds_cat | Out_of_cat_food = 1, George_watches_tv = 0) = %.3f" % (gfc_oocf1_gwtv0_prob))
print("P(George_feeds_cat | Out_of_cat_food = 0, George_watches_tv = 1) = %.3f" % (gfc_oocf0_gwtv1_prob))
print("P(George_feeds_cat | Out_of_cat_food = 1, George_watches_tv = 1) = %.3f" % (gfc_oocf1_gwtv1_prob))