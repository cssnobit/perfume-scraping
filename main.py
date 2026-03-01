from monitor import monitor, HISTORY_FILE, save_history
import os
import json

def initialize():
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=4)

if __name__ in "__main__":
    perfumes = ["https://www.anmyperfumes.com.br/vulcan-feu-eau-de-parfum-compartilhavel-french-avenue",
                "https://www.anmyperfumes.com.br/kayaan-classic-eau-de-parfum-compartilhavel-al-wataniah",
                "https://www.anmyperfumes.com.br/stronger-with-you-intensely-eau-de-parfum-feminino-giorgio-armani",
                "https://www.anmyperfumes.com.br/armani-code-parfum-masculino-giorgio-armani"]
    
    initialize()
    monitor(perfumes)