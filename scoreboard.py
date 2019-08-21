import matplotlib as mpl
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import database as db

def scoreboard_loop():
    mpl.rcParams['toolbar'] = 'None'
    objects = ('p1','p2','p3','p4','p5','p6','p7','p8','p9','p10')
    y_pos = np.arange(len(objects))
    scores = [18,16,14,12,10,8,6,4,2,1]
    plt.bar(y_pos, scores, align='center', alpha=0)
    plt.ylabel('')
    plt.title('')
    # Uncomment the 2 lines below for fullscreen
    # mng = plt.get_current_fig_manager()           
    # mng.full_screen_toggle()
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()
    while True:
        display_class('male', 'Top Male Competitors')
        display_class('female', 'Top Female Competitors')
        display_class('ind', 'Top 10 Competitors')

def display_class(class_type, class_title):
    delay = 3
    listing = db.get_top_scores(class_type)
    scores = [listing[0][1], listing[1][1], listing[2][1], listing[3][1], listing[4][1], listing[5][1], listing[6][1], listing[7][1], listing[8][1], listing[9][1]]
    objects = (listing[0][0], listing[1][0], listing[2][0], listing[3][0], listing[4][0], listing[5][0], listing[6][0], listing[7][0], listing[8][0], listing[9][0])
    y_pos = np.arange(len(objects))
    bars = plt.bar(y_pos, scores, align='center', alpha=1)
    plt.xticks(y_pos, objects, rotation=30, fontsize=10)
    plt.yticks(fontsize=10)
    plt.ylabel('Score', fontsize=10)
    plt.title(class_title, fontsize=10)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + 0.35, yval + .12, yval, fontsize=10)

    plt.show(block=False)
    plt.pause(delay)
    plt.clf()