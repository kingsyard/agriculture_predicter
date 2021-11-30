

import numpy as np;
import pandas as pd;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle


from yield_code import yield_fn


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

features_list=['area',             'temperature',
                    'wind_speed',           'precipitation',
                      'humidity',                       'N',
                             'P',                       'K',
                    'AHMEDNAGAR',                   'AKOLA',
                      'AMRAVATI',              'AURANGABAD',
                          'BEED',                'BHANDARA',
                      'BULDHANA',              'CHANDRAPUR',
                         'DHULE',              'GADCHIROLI',
                        'GONDIA',                 'HINGOLI',
                       'JALGAON',                   'JALNA',
                      'KOLHAPUR',                   'LATUR',
                        'NAGPUR',                  'NANDED',
                     'NANDURBAR',                  'NASHIK',
                     'OSMANABAD',                 'PALGHAR',
                      'PARBHANI',                    'PUNE',
                        'RAIGAD',               'RATNAGIRI',
                        'SANGLI',                  'SATARA',
                    'SINDHUDURG',                 'SOLAPUR',
                         'THANE',                  'WARDHA',
                        'WASHIM',                'YAVATMAL',
                   'Kharif',             'Rabi',
                   'Summer',             'Whole Year ',
                     'Arhar/Tur',                   'Bajra',
                   'Castor seed',            'Cotton(lint)',
                          'Gram',               'Groundnut',
                         'Jowar',                 'Linseed',
                         'Maize',       'Moong(Green Gram)',
                    'Niger seed',      'Other  Rabi pulses',
       'Other Cereals & Millets',     'Other Kharif pulses',
                          'Ragi',       'Rapeseed &Mustard',
                          'Rice',               'Safflower',
                       'Sesamum',                'Soyabean',
                     'Sugarcane',               'Sunflower',
                       'Tobacco',                    'Urad',
                         'Wheat',          'other oilseeds',
                            2004,                      2005,
                            2006,                      2007,
                            2008,                      2009,
                            2010,                      2011,
                            2012,                      2013,
                            2014,             'Maharashtra',
                        'chalky',                    'clay',
                         'loamy',                   'peaty',
                         'sandy',                    'silt',
                         'silty']


features_list1=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]




from recamandation_code import recondation_fn


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html') 

    
   


@app.route('/production')
def production(): 
    return render_template('index.html')


@app.route('/production/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    print(features_list1,features_list)

    int_features = [str(x) for x in request.form.values()]



    print("output from web page  ",int_features)

    #features_list1[83]=int_features[0]



    state_ind=features_list.index(int_features[0])

    print(state_ind)

    features_list1[state_ind]=1



    print(int_features[1])


    


    print(features_list.index('DHULE'))


    dist_ind=features_list.index(int_features[1])

    print(dist_ind)

    features_list1[dist_ind]=1

    season_ind=features_list.index(int_features[2])

    features_list1[season_ind]=1

    crop_ind=features_list.index(int_features[3])

    features_list1[crop_ind]=1

    features_list1[0]=float(int_features[4])


    features_list1[1]=float(int_features[5])

    features_list1[2]=float(int_features[6])


    features_list1[3]=float(int_features[7])


    features_list1[4]=float(int_features[8])


    soil_ind=features_list.index(int_features[9])

    features_list[soil_ind]=1

    features_list1[5]=float(int_features[10])

    features_list1[6]=float(int_features[11])

    features_list1[7]=float(int_features[12])





    a=features_list1


    print(a)

    output_yield=yield_fn(features_list1)


    return render_template('index.html', prediction_text='Yield  will be    {} kg for Hectare '.format(output_yield[0]*1000))

@app.route('/crop')
def crop():
     return render_template('crop.html')



@app.route('/crop/predict1',methods=['POST'])
def predict1():
    '''
    For rendering results on HTML GUI
    '''
    int_features1 = [str(x) for x in request.form.values()]
    int_features2=['1','2','3','4','5','6']
    a1=int_features1[0]
    a2=int_features1[1]
    a3=int_features1[2]
    a4=int_features1[3]

    
    a5=int_features1[4]
    a6=int_features1[5]
    a7=int_features1[6]
    
    
    
   # int_features21 = np.array(int_features2)




  #  int_features11 = int_features21.reshape(1, -1)
   # prediction1 = model1.predict(int_features11)

    output1 = recondation_fn(a1,a2,a3,a4,a5,a6,a7)
   # resultcrop = {value:key for key, value in croplist.items()}
    print(output1)
    
    
 
    

    

    return render_template('crop.html', prediction1_text='You will get best Yield if you cultivate  {} '.format(output1[0]))



if __name__ == "__main__":
    app.run(debug=True)
