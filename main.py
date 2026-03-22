from dotenv import load_dotenv
load_dotenv()

from core.monitor import monitor

if __name__ in "__main__":
    perfumes = ["https://www.anmyperfumes.com.br/vulcan-feu-eau-de-parfum-compartilhavel-french-avenue",
                "https://www.anmyperfumes.com.br/kayaan-classic-eau-de-parfum-compartilhavel-al-wataniah",
                "https://www.anmyperfumes.com.br/snjtttjp4-phantom-parfum-masculino-paco-rabanne",
                "https://www.anmyperfumes.com.br/armani-code-parfum-masculino-giorgio-armani"]
    
    monitor(perfumes)