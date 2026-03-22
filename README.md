# 🧴 Perfume Price Monitor

Um monitor simples de preços de perfumes que faz scraping de lojas online e avisa quando há queda de preço.

## 🚀 Funcionalidades

* Consulta preços automaticamente
* Detecta quando o preço cai
* Salva histórico local em JSON
* Envia alertas via Discord (webhook)

## 🛠️ Tecnologias

* Python
* Requests
* JSON
* Web Scraping

## 📁 Estrutura do Projeto

```
perfume-scraping/
│
├── main.py
├── core/
│   ├── monitor.py
│   └── storage.py
├── scrapers/
│   └── anmy.py
├── notifications/
│   ├── discord.py
│   └── dispatcher.py
└── files/
│   └── history.json
```

## ▶️ Como usar

1. Instale as dependências:

```
pip install requests
```

2. Configure as URLs dos produtos no código

3. Execute o script:

```
python main.py
```

## 🔔 Notificações

O sistema envia alertas via webhook do Discord quando detecta queda de preço.

## 📌 Observações

* O scraping no momento só coleta dados do site AnMY Perfumes
* Projeto em evolução (futuramente com suporte a múltiplos sites e Telegram)

---

Feito para estudo, recreação e principalmente para automação pessoal 🚀
