#!! location = "/Min/utils/save_and_load.txt"
##### pickle file load
import pickle
#EF_table = pickle.load(file('entityid_featureid.pkl'))
##### df(dataframe) file load
#uapp = pickle.load(file('data/user_app.df'))

##### text file load
from load.datasets import load_svmlight_file
# X_small_train.shape의 [0]번째는 Sample수, [1]번째는 features수
#X_train, y_train = load_svmlight_file("user_gender 5.txt", n_features=52600)


##### clf_file load(model)
from load.externals import joblib
#filename = "my_model10000.pkl"
#clf = joblib.load(filename)


##### text file
def load(fname):
    ''' load the file using std open'''
    f = open(fname,'r')

    data = []
    for line in f.readlines():
        data.append(line.replace('\n','').split(' '))

    f.close()

    return data





##### data, df file save
from load.datasets import dump_svmlight_file
#f_name = "result.dat"
#dump_svmlight_file(X_test, clf.predict(X_test), f_name);


##### data frame, pickle save
import pickle
#filename="data/profiled_gender.pkl"
#fout = file(filename,"w")
#pickle.dump(userngender[:100],fout)


##### data frame save
from pandas import DataFrame
#DataFrame.save(userngender[100:200], filename)





########## SAVE FILE 1. save all data by one step!!! ##########
#import pickle
#filename="data/profiled_gender.pkl"
#fout = file(filename,"w")
#pickle.dump(userngender,fout)

#load_user0 = pickle.load(file('data/profiled_gender.pkl'))

#load_user0
########## SAVE FILE 2. save & update data by any steps!!! ##########

#load_user1 = pickle.load(file('profiled_gender.pkl'))
#load_user1

#load_user1.update(userngender)
#load_user1

#from pandas import DataFrame
#DataFrame.save(load_user1, "profiled_gender.pkl")