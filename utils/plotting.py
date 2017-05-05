import matplotlib.pyplot as plt
import numpy as np
import itertools
from sklearn.metrics import accuracy_score, confusion_matrix

def print_accuracy(accuracy):
    print("Accuracy = {:.1f}%".format(
        accuracy * 100.0
    ))

def plot_2d_samples(samples, labels):
    plt.scatter(
        [s[0] for s, l in zip(samples, labels) if l==1],
        [s[1] for s, l in zip(samples, labels) if l==1],
        c='C0', label='Class 1'
    )
    plt.scatter(
        [s[0] for s, l in zip(samples, labels) if l==0],
        [s[1] for s, l in zip(samples, labels) if l==0],
        c='C1', label='Class 0'
    )
    plt.legend()
    plt.xlabel('word1')
    plt.ylabel('word2')

def plot_2d_trained_svc(samples, labels, svc):
    xmin = min([s[0] for s in samples])
    xmax = max([s[0] for s in samples])
    plot_2d_samples(samples, labels)
    xx = np.linspace(xmin, xmax, 100)
    coefs = svc.coef_[0]
    a = -svc.intercept_[0] / coefs[1]
    b = -coefs[0] / coefs[1]
    plt.plot(xx, a + b*xx, c='C3', label='SVC boundary')
    plt.legend()

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):

    """
    Copied from: scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def pipeline_performance(training_labels, predicted_labels, classes=[0,1]):

    accuracy = accuracy_score(training_labels, predicted_labels)
    cm = confusion_matrix(training_labels, predicted_labels)

    # print the results
    print_accuracy(accuracy)
    plot_confusion_matrix(cm, classes)

def print_top_features(pipeline, vectorizer_name='vectorizer', classifier_name='classifier', n_features=7):
    vocabulary = np.array(pipeline.named_steps[vectorizer_name].get_feature_names())
    coefs = pipeline.named_steps[classifier_name].coef_[0]
    top_feature_idx = np.argsort(coefs)
    top_features = vocabulary[top_feature_idx]
    print("Top clickbait features:")
    print(top_features[-n_features:])
    print("---")
    print("Top news features:")
    print(top_features[:n_features])
