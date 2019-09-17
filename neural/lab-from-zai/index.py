from numpy import savetxt, loadtxt #для загрузки-сохранения csv-файлов
from sklearn.ensemble import RandomForestClassifier #собственно он и делает всю работу
from sklearn.externals import joblib #для промежуточных данных
from sklearn import svm

#загружаем обучающие данные и дампаем их в отдельный файл
dataset = loadtxt(open('mnist_train2.csv', 'r'), dtype='f8', delimiter=',', skiprows=1)
joblib.dump(dataset, 'training_set.pkl')
dataset = joblib.load('training_set.pkl')

#точно так же загружаем тестовые
test = loadtxt(open('mnist_test.csv', 'r'), dtype='f8', delimiter=',', skiprows=1)
joblib.dump(test, 'test_set.pkl')
test = joblib.load('test_set.pkl')

target = [x[0] for x in dataset]
train = [x[1:] for x in dataset]

#инициализируем классификатор. Поле kernel указывает на ядро, degree - степень используемого полинома. По дефолту, кстати, стоит 3.
clf_poly2 = svm.SVC(kernel = "poly", degree = 2)
clf_poly2.fit(train, target) #обучили

savetxt('svm_answer.csv', clf_poly2.predict(test), delimiter=',', fmt='%d')