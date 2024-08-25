# Elasticsearch Search Tutorial

This directory contains a starter Flask project used in the Search tutorial.

1. Create a venv
```
python3 -m venv .venv
```

2. Activate the venv
```
source .venv/bin/activate
```

3. Install the requirements
```
pip install -r requirements.txt
```

4. Start Elasticsearch in Docker container
```
docker run -p 127.0.0.1:9200:9200 -d --name elasticsearch \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  -e "xpack.license.self_generated.type=trial" \
  -v "elasticsearch-data:/usr/share/elasticsearch/data" \
  docker.elastic.co/elasticsearch/elasticsearch:8.15.0
```

4. Populate the Elasticsearch index
```
flask reindex
```

