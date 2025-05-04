#n=num pazienti
#copy è train_copy opp test_copy
import numpy as np
import itertools
def calcola_range (n, conta_occorrenze,copy):
    #per utilizzare la stessa funzione in entrambi i casi, perchè cambiano i nomi dei patient_
    m = list()
    for j in range(1, n+1):
        string = 'patient_' + str(j)
        m.append(conta_occorrenze[string])
    # quindi creo una lista con tutti i valori delle occorrenze
    #pochè prendo i valori delle chiavi, ossia i nomi dei pazienti
    #ma queste sono il numero di occorrenze, quello che mi serve sono gli indici di inizio e fine
    cum_sum = list(itertools.accumulate(m))
    # faccio la cum sum perchè mi servono i valori cumulati
    cum_sum = [0] + cum_sum
    # aggiungo lo 0 per facilitarmi nella creazione dei range
    time = list() #sarà la lista dei range dei pazienti
    #se n=6 paz[0]=patient_1
    #se n=3 paz[0]=patiient_7
    for i in range(0,n):
        time.append(range(cum_sum[i], cum_sum[i + 1]))
    # ora devo tener conto dei massimi relativi, ma in realt ami serve l'argmax perchè mi devo fermare proprio alla riga corrispondente al
    # massimo del paziente rispetto al range in cui mi trovo
    arg_max=list()
    for i in range(0,n):
        arg_max.append(copy['Events'][time[i]].argmax())
    # così facendo se ad esempio il massimo del paziente2 si trova dopo 86 righe dall'inizio delle sue osservazioni mi restituicse 86, ma
    # mi serve quello reativo a utta la struttura del dataset
    for i in range(0, n):
        arg_max[i] = arg_max[i] + cum_sum[i]
    return time, arg_max

def elimina_outliers(colonne,time,copy):
    for j in colonne:
        for i in time:
            q_1 = np.percentile(copy[j][i], 25)
            q_3 = np.percentile(copy[j][i], 75)
            r = abs(q_3 - q_1)
            lower = q_1 - 1.5 * r
            upper = q_3 + 1.5 * r
            media=np.mean(copy[j][i])
            for k in i:
                if ((float(copy[j][k]) <= upper) and (float(copy[j][k]) >= lower)):
                    1
                else:
                    copy.loc[k, j] = media
    return copy
def discretizza_colonne(colonne,copy,length):
    for j in colonne:
        m = float(copy[j].min())
        for i in range(0, length):
            value = list(copy[j])
            value = float(value[i])
            copy.loc[i, j] = value - m
        #for i in range(0,length):
            M = float(copy[j].max())
            if (value <= M / 4):
                copy.loc[i, j] = 1
            if (value > M / 4) and (value <= M / 2):
                copy.loc[i, j] = 2
            if (value > M / 2) and (value <= 3 * M / 4):
                copy.loc[i, j] = 3
            if (value > 3 * M / 4):
                copy.loc[i, j] = 4
def discretizza_colonne_2 (colonne,copy,time):
    for j in colonne:
        for i in time:
            m=float(copy[j][i].min())
            for k in i:
                copy.loc[k,j]=float(copy[j][k])-m
            M=float(copy[j][i].max())
            value=float(copy[j][k])
            if (value <= M / 4):
                copy.loc[i, j] = 1
            if (value > M / 4) and (value <= M / 2):
                copy.loc[i, j] = 2
            if (value > M / 2) and (value <= 3 * M / 4):
                copy.loc[i, j] = 3
            if (value > 3 * M / 4):
                copy.loc[i, j] = 4
def discretizza_events (arg_max,time,copy):
    for k, j in zip(arg_max, time):
        for i in j:
            value = float(list(copy['Events'])[i])
            if (value == 0) and i < k:
                copy.loc[i, 'Events'] = 0
            if (value > 0) and (value < 1) and i <= k:
                copy.loc[i, 'Events'] = 1
            if (value >= 1) and (value < 2) and i <= k:
                copy.loc[i, 'Events'] = 2
            if (value >= 2) and (value < 3) and i <= k:
                copy.loc[i, 'Events'] = 3
            if (value >= 3) and (value < 4) and i <= k:
                copy.loc[i, 'Events'] = 4
            if (value >= 4) and (value < 5) and i <= k:
                copy.loc[i, 'Events'] = 5
            if i > k and (value < 5) and (value >= 3.75):
                copy.loc[i, 'Events'] = 6
            if i > k and (value < 3.75) and (value >= 2.5):
                copy.loc[i, 'Events'] = 7
            if i > k and (value < 2.5) and (value >= 1.25):
                copy.loc[i, 'Events'] = 8
            if i > k and (value < 1.25) and (value >= 0):
                copy.loc[i, 'Events'] = 9
    return copy
def trasla(copy,time,colonne):
    for j in colonne:
        for i in time:
            m=float(copy[j][i].min())
            for k in i :
                copy.loc[k,j]=float(copy[j][k])-m
    return copy

def suddividi (copy, time, colonne):
    for j in colonne:
        for i in time:
            M=float(copy[j][i].max())
            for k in i:
                value=float(copy[j][k])
                if (value<M/4):
                    copy.loc[k,j]=1
                if value >=M/4 and value <M/2:
                    copy.loc[k,j]=2
                if value<3*M/4 and value >=M/2:
                    copy.loc[k,j]=3
                if value>=3*M/4:
                    copy.loc[k,j]=4
    return copy


#drop tutte le altre colonne che non servono
def elimina_zeri(copy, colonne):
    copy=copy[colonne]
    length = copy.shape[0]
    l = list()
    for i in range(0,length):
        value = copy.iloc[i]
        value = set(value)
        if value == {0.0}:
            l.append(i)
    return l