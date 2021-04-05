# Serving RandomForestClassifier model with FastAPI.

## 1) Clone repo and deploy app.

```
git clone https://github.com/q00Dree/fastapi-iris-classifier.git \
&& cd fastapi-iris-classifier \
&& cd deploy \
&& bash deploy.sh
```

## 2) Try model to classify iris by params.

```
curl --request POST \
  --url http://localhost:8001/api/v1/rfc/predict \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{"sepal_length":3.4,"sepal_width":7.2,"petal_length":2.1,"petal_width":3.5}'
```

## 3) Enjoy =)
