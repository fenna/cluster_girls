from sklearn.ensemble import RandomForestClassifier

def feature_importance(clf, X, clusters):
    clf.fit(X, clusters)

    # Feature importance opvragen
    importances = clf.feature_importances_

    # Visualiseer de feature importance
    feature_names = X.columns  # Stel dat je dataset kolomnamen heeft
    importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})

    # Sorteer op basis van importance
    importance_df = importance_df.sort_values(by='Importance', ascending=False)

    # Plot de feature importance
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 20))
    plt.barh(importance_df['Feature'], importance_df['Importance'])
    plt.xlabel('Feature Importance')
    plt.title('Feature Importance van Cluster Classificatie')
    plt.gca().invert_yaxis()
    plt.show()

clf = RandomForestClassifier(n_estimators=100, random_state=42)
feature_importance(clf, data, labels)
