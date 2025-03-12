import os

print("API Key:", os.getenv("LANGCHAIN_API_KEY"))
print("Tracing Enabled:", os.getenv("LANGCHAIN_TRACING_V2"))
