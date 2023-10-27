import numpy as np

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
alpha_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
              'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
              'y': 24, 'z': 25, ' ': 26}

pred_dict = {0 : 'e', 1 : 's', 2 : 'j', 'e': 0, 's': 1, 'j': 2}
p_y = np.log(1/3)

def load_data(file_list):
    counts = np.zeros(27)
    for f in file_list:
        f_opener = open('languageID/' + f, 'r')
        for line in f_opener:
            line = line.rstrip()
            for ch in line:
                counts[alpha_dict[ch]] += 1
    return counts


def bayes():
    file_list_e = ['e0.txt', 'e1.txt', 'e2.txt', 'e3.txt', 'e4.txt', 'e5.txt', 'e6.txt', 'e7.txt', 'e8.txt', 'e9.txt']
    file_list_j = ['j0.txt', 'j1.txt', 'j2.txt', 'j3.txt', 'j4.txt', 'j5.txt', 'j6.txt', 'j7.txt', 'j8.txt', 'j9.txt']
    file_list_s = ['s0.txt', 's1.txt', 's2.txt', 's3.txt', 's4.txt', 's5.txt', 's6.txt', 's7.txt', 's8.txt', 's9.txt']
    counts = load_data(file_list_e)
    tot = np.sum(counts)
    c_e = (counts + .5)/(tot + 27*.5)
    counts = load_data(file_list_s)
    tot = np.sum(counts)
    c_s = (counts + .5) / (tot + 27 * .5)
    counts = load_data(file_list_j)
    tot = np.sum(counts)
    c_j = (counts + .5) / (tot + 27 * .5)
    c_j = np.log(c_j)
    c_s = np.log(c_s)
    c_e = np.log(c_e)
    #CONDITIONAL PROBABILITIES FOR EACH LANGUAGE
    #q3_4(c_e,c_s,c_j)
    q3_7([c_e,c_s,c_j])


def q3_4(c_e,c_s,c_j):
    counts = load_data(['e10.txt'])
    print(counts)
    p_e = 1
    p_s = 1
    p_j = 1
    for val in range(len(counts)):
        p_e *= (c_e[val]*counts[val])
        p_s *= (c_s[val]*counts[val])
        p_j *= (c_j[val]*counts[val])
    print("English P(x|y) = " + str(p_e))
    print("Spanish P(x|y) = " + str(p_s))
    print("Japanese P(x|y) = " + str(p_j))
    print("")
    print("English Posterior = " + str(p_e*p_y))
    print("Spanish Posterior = " + str(p_s * p_y))
    print("Japanese Posterior = " + str(p_j * p_y))

def q3_7(cond_prob):
    conf_mat = np.zeros((3,3))
    for ch in ['e', 's', 'j']:
        for val in range(10, 20):
            conf_mat[predict(cond_prob, ch + str(val) + '.txt')][pred_dict[ch]] += 1
    print(conf_mat)



def predict(cond_p,f):
    counts = load_data([f])
    p = np.ones(3)
    for val in range(len(counts)):
        p[0] += (cond_p[0][val] * counts[val])
        p[1] += (cond_p[1][val] * counts[val])
        p[2] += (cond_p[2][val] * counts[val])
    print(p)
    p = p + p_y
    for val in range(len(p)):
        if(p[val] == np.max(p)):
            print("winner is " + str(pred_dict[val]))
            return val
bayes()