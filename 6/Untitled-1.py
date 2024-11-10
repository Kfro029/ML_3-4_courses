from sklearn.datasets import load_iris
import pandas as pd

# Загрузка данных
iris = load_iris()
iris_data = iris.data
iris_feature_names = iris.feature_names

# Создание DataFrame
df = pd.DataFrame(iris_data, columns=iris_feature_names)

# Ответ на вопрос 1
rows, cols = df.shape
answer = f"{rows},{cols}"
print(answer)
