from __pickle_processing__ import writeFile

def log_loss(y_true,y_pred):
	from sklearn.metrics import log_loss
	x = log_loss(y_true,y_pred)
	print(str(x))
	return x

def confusionMatrix(y_test, preds):
	from sklearn.metrics import confusion_matrix
	tn, fp, fn, tp = confusion_matrix(y_test, preds).ravel()
	print("True Negative: " + str(tn) + " False Positive: " + str(fp) + " False Negative: " + str(
		fn) + " True Positive: " + str(tp))


def fit_Naive_bayes(train_data,target_data):
	from sklearn.model_selection import train_test_split
	from sklearn.naive_bayes import MultinomialNB
	X_train, X_test, y_train, y_test = train_test_split(train_data, target_data, test_size=0.2, random_state=42)

	cls = MultinomialNB().fit(X_train,y_train)

	from sklearn.metrics import accuracy_score

	# preds = cls.predict_proba(X_test)
	preds = cls.predict(X_test)
	accuracy = accuracy_score(y_test, preds)
	print("Accuracy:", str(accuracy))
	confusionMatrix(y_test, preds)

	writeFile(cls, "MultinomialNB" ,"models\\")