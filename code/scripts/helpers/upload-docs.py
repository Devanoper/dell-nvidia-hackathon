from docs import DocProcessor

p = DocProcessor("/project/data/documents", "/mnt/docs", "http://localhost:8000/uploadDocument", False)
p.process()