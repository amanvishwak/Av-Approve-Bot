from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20389440"))
    API_HASH = getenv("API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
    BOT_TOKEN = getenv("BOT_TOKEN", "7025013171:AAEG_5OQ2uBhknzbAzhcVec2MtVMFnVQ3Pc")
    FSUB = getenv("FSUB", "AV_BOTz_UPDATE")
    CHID = int(getenv("CHID", "-1002102037760"))
    SUDO = list(map(int, getenv("SUDO", "5977931010").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://aman991932:aman@cluster0.qp6vfyg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
