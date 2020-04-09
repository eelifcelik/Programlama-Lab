import sys
input,output=sys.argv[1],sys.argv[2]
def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list
#bubble_sort(aylar)
#print(aylar)

def my_frequency_with_dict(list):
    frequency_dict = {}
    for item in list:
        item=int(item)
        if item in frequency_dict :
            frequency_dict[item] = frequency_dict[item] + 1
        else:
            frequency_dict[item] = 1
    print(frequency_dict)
    return frequency_dict

def my_mode_with_dict(my_hist_d):
    frequency_max = -1 # we define a max value -1 for comparision with the other frequency values
    mode = -1

    for key in my_hist_d.keys():
        #print(key, my_hist_d[key])
        if my_hist_d[key] > frequency_max:
            frequency_max = my_hist_d[key]
            mode = key
    #print(mode, frequency_max)
    return mode,frequency_max

def medyanBul(dizi):
    dizi= bubble_sort(dizi)
    if len(dizi)%2==1:
        orta = int(len(dizi)/2)+1
        return dizi[orta-1]
    else:
        orta1,orta2=dizi[int(len(dizi)/2)],dizi[int(len(dizi)/2)-1]
        return (orta1+orta2)/2



def ListeOrtalama(liste):
    toplam = 0
    s=0
    for item in liste:
        toplam += int(item)
        s += 1
    #print(int(toplam/s))
    return int(toplam/s)



with open(input+"input_hw_2.csv", "r") as dosya:
    data = []
    data1 = dosya.read()
    data_line = data1.split(';')
    data.append(data_line)
    # print(data_line)
    date = []
    ayir = []
    for i in range(3, len(data_line), 3):
        #print(data_line[i])
        ayir.append(data_line[i].split("-"))

    aylar = []
    for i in range(len(ayir)):
        aylar.append(int(ayir[i][1]))

bubble_sort(aylar)
a = my_frequency_with_dict(aylar)
listeYeni = [a[i] for i in a]
#print(medyanBul(listeYeni),ListeOrtalama(listeYeni))


with open(output+"180401055_hw_2_output.txt", "w") as dosya:

    dosya.write("Medyan :"+ "" + str(medyanBul(listeYeni))+"\n")
    dosya.write("Ortalama:" + ""+ str(ListeOrtalama(listeYeni)))