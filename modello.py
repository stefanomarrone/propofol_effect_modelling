import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pgmpy.models import BayesianNetwork
import sklearn.metrics as metrics
from sklearn.metrics import confusion_matrix, log_loss, f1_score, classification_report, jaccard_score, \
    mean_absolute_error, mean_squared_error
from collections import Counter
from funzioni import calcola_range, elimina_outliers, discretizza_events, trasla, suddividi, elimina_zeri

def prepare(dataframe, columnnames):
    dataframe = dataframe.replace([np.inf, -np.inf], np.nan, inplace=False)
    dataframe = dataframe.dropna(axis=0, how='any', inplace=False)
    dataframe = dataframe.reset_index()
    l = elimina_zeri(dataframe, columnnames)
    dataframe = dataframe.drop(index=l)
    dataframe = dataframe.drop(columns='Unnamed: 0')
    dataframe = dataframe.reset_index()
    patient = dataframe['Patient'].values.tolist()
    conta_occorrenze = dict(Counter(patient))
    time, arg_max = calcola_range(9, conta_occorrenze, dataframe)
    dataframe = elimina_outliers(columnnames, time, dataframe)
    dataframe = trasla(dataframe, time, columnnames)
    dataframe = suddividi(dataframe, time, columnnames)
    dataframe = discretizza_events(arg_max, time, dataframe)
    return dataframe


def prediction(feature, y_predicted, test, tag):
    y_pred_feature = y_predicted[feature].tolist()
    y_test = test[feature].tolist()
    accuracy = metrics.accuracy_score(y_test, y_pred_feature)
    jaccard = jaccard_score(y_test, y_pred_feature, average='weighted')
    mae = mean_absolute_error(y_pred_feature, y_test)
    mse = mean_squared_error(y_test, y_pred_feature)
    row = feature + ";" + str(accuracy) + ";" + str(jaccard) + ";" + str(mae) + ";" + str(mse) + ";\n"
    c = metrics.confusion_matrix(y_test, y_pred_feature)
    d = metrics.ConfusionMatrixDisplay(c)
    d.plot()
    plt.title(feature + ' Confusion Matrix')
    plt.xlabel('Predicted ' + feature)
    plt.ylabel('True ' + feature)
    plt.savefig(feature + "_" + tag + "_prediction.pdf")
    return row


def testing(model, test, tag, causes, colonne):
    x_test = test[causes]
    y_pred = model.predict(x_test)
    csvtext = "feature;accuracy;jaccard;mae;mse;\n"
    for f in colonne:
        row = prediction(f, y_pred, test, tag)
        csvtext += row
    handle = open("results_" + tag + ".csv", 'w')
    handle.write(csvtext)
    handle.close()


df = pd.read_csv('training_completo.csv')
colonne = ['SigmaHR','MuHR','SigmaRR','MuRR','LF','HF']
causes = ['Events','Patient']
df = prepare(df, colonne)
#train/test split
rand = np.random.rand(len(df))<0.8
train = df[rand]
test = df[~rand]
# model construction and fit
edges = [(a, b) for a in causes for b in colonne]
model = BayesianNetwork(edges)
model.fit(train)

causes = ['Events']
testing(model, test, 'no_patients', causes, colonne)
causes = ['Patient', 'Events']
testing(model, test, 'patients', causes, colonne)




#infer=VariableElimination(model)
#x_test = test[colonne]
#y_test = test.drop(columns=['index','Time','Patient']+colonne) #Events
# q = infer.query(variables=colonne)
#
# q1 = infer.query(variables=colonne,evidence={'Patient':'patient_1'}, joint=True)
#
# result=[]
#
# for row in range(0,9):
#     row='patient_'+str(row+1)
#     query_result = infer.query(variables=['MuRR'], evidence={'Patient':row})
#     result.append(query_result)
#
# #result[0].values
# y_prob=list()
# for i in range(0,9):
#     y_prob.append(result[i].values)
# #ho creato una lista di 9 liste
# #nelle liste interne vi sono 4 elementi, ossia la probabilità che si veifichi quella classe per ognuno dei 9pazienti
