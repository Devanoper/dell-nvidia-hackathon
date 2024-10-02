
import os
import shutil
from milvus import default_server
from pymilvus import connections, utility, Collection

# Get connection to DB
connections.connect(host='localhost', port=19530)

# Get collection
collection = Collection(utility.list_collections()[0])

# Delete entities
expr = "id!=''"
collection.delete(expr)

# Query all entities
result = collection.query(expr="id!=''", output_fields=["id"])

# Extract all IDs
id_array = [entity["id"] for entity in result]

# Ensure database is empty
print(id_array)

if os.path.exists("/project/data/documents/.file_cache.json"):
    os.remove("/project/data/documents/.file_cache.json")
    
if os.path.exists("/project/data/documents/.file_cache.lock"):
    os.remove("/project/data/documents/.file_cache.lock")

if os.path.exists("/project/data/documents/.ipynb_checkpoints"):
    shutil.rmtree("/project/data/documents/.ipynb_checkpoints")