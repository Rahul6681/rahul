from google import genai

# PASTE YOUR API KEY HERE
API_KEY = 

client = genai.Client(api_key=API_KEY)

print("Checking available models...")
try:
    # This lists every model your key can access
    for m in client.models.list():
        print(f"Model found: {m.name}")
except Exception as e:

    print(f"Error: {e}")
