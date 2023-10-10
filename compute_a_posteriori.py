import sys

p0h1 = .1
p0h2 = .2
p0h3 = .4
p0h4 = .2
p0h5 = .1
ph1c = 1
ph1l = 0
ph2c = .75
ph2l = .25
ph3c = .5
ph3l = .5
ph4c = .25
ph4l = .75
ph5c = 0
ph5l = 1

def recurse(Q, observation):
    if Q == 0:
        return (p0h1, p0h2, p0h3, p0h4, p0h5, .5, .5)
    
    ph1_prev, ph2_prev, ph3_prev, ph4_prev, ph5_prev, pq_prev_c, pq_prev_l = recurse(Q-1, observation)
    
    f.write("\nAfter Observation %d = %s\n\n" % (Q, observation[Q-1]))
    prob_c = 0
    prob_l = 0
    if observation[Q-1] == 'C':
        ph1_c_new = (ph1c*ph1_prev)/pq_prev_c
        f.write("P(h1 | Q) = %.5f\n" % (ph1_c_new ))
        prob_c += ph1c*ph1_c_new
        
        ph2_c_new = (ph2c*ph2_prev)/pq_prev_c
        f.write("P(h2 | Q) = %.5f\n" % (ph2_c_new ))
        prob_c += ph2c*ph2_c_new
        
        ph3_c_new = (ph3c*ph3_prev)/pq_prev_c
        f.write("P(h3 | Q) = %.5f\n" % (ph3_c_new ))
        prob_c += ph3c*ph3_c_new
        
        ph4_c_new = (ph4c*ph4_prev)/pq_prev_c
        f.write("P(h4 | Q) = %.5f\n" % (ph4_c_new ))
        prob_c += ph4c*ph4_c_new
        
        ph5_c_new = (ph5c*ph5_prev)/pq_prev_c
        f.write("P(h5 | Q) = %.5f\n\n" % (ph5_c_new ))
        prob_c += ph5c*ph5_c_new
        
        
    if observation[Q-1] == 'L':
        ph1_l_new  = (ph1l*ph1_prev)/pq_prev_l
        f.write("P(h1 | Q) = %.5f\n" % (ph1_l_new))
        prob_l += ph1l*ph1_l_new
        
        ph2_l_new  = (ph2l*ph2_prev)/pq_prev_l
        f.write("P(h2 | Q) = %.5f\n" % (ph2_l_new))
        prob_l += ph2l*ph2_l_new
        
        ph3_l_new  = (ph3l*ph3_prev)/pq_prev_l
        f.write("P(h3 | Q) = %.5f\n" % (ph3_l_new))
        prob_l += ph3l*ph3_l_new
        
        ph4_l_new  = (ph4l*ph4_prev)/pq_prev_l
        f.write("P(h4 | Q) = %.5f\n" % (ph4_l_new))
        prob_l += ph4l*ph4_l_new
        
        ph5_l_new  = (ph5l*ph5_prev)/pq_prev_l
        f.write("P(h5 | Q) = %.5f\n\n" % (ph5_l_new))
        prob_l += ph5l*ph5_l_new
            
    
    
    if observation[Q-1] == 'C':
        f.write("Probability that the next candy we pick will be C, given Q: %.5f\n" % (prob_c))
        f.write("Probability that the next candy we pick will be L, given Q: %.5f\n" % (1-prob_c))
        return ph1_c_new, ph2_c_new, ph3_c_new, ph4_c_new, ph5_c_new, prob_c, 1-prob_c
    else:
        f.write("Probability that the next candy we pick will be C, given Q: %.5f\n" % (1-prob_l))
        f.write("Probability that the next candy we pick will be L, given Q: %.5f\n" % (prob_l))
        return ph1_l_new, ph2_l_new, ph3_l_new, ph4_l_new, ph5_l_new, 1-prob_l, prob_l

if (len(sys.argv) > 1):
    observation = sys.argv[1]
    f = open("output.txt", "w")
    f.write("Observation Sequence Q: %s\n" % (observation))
    f.write("Length of Q: %d\n" % (len(observation)))
    ph1_prev, ph2_prev, ph3_prev, ph4_prev, ph5_prev, pq_prev_c, pq_prev_l = recurse(len(observation), observation)
    
else:
    f = open("output.txt", "w")
    f.write("Observation Sequence Q: None\n")
    f.write("Length of Q: 0\n\n")
    f.write("P(h1) = .1\n")
    f.write("P(h2) = .2\n")
    f.write("P(h3) = .4\n")
    f.write("P(h4) = .2\n")
    f.write("P(h5) = .1\n\n")

    f.write("Probability that the next candy we pick will be C, given Q: .5\n")
    f.write("Probability that the next candy we pick will be L, given Q: .5")