import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- НАСТРОЙКИ TELEGRAM (Вставь свои данные) ---
TELEGRAM_TOKEN = "8967184772:AAHYttr30uDcJkwg63GS0OgWCx4U2apN7HY"
YOUR_CHAT_ID = "823749369"

def send_telegram_message(message):
    """Функция отправки сообщения в твой Telegram"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": YOUR_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Ошибка отправки в Telegram: {e}")

@app.route('/')
def home():
    # Главная страница с повесткой
    return render_template('index.html')

@app.route('/respond', methods=['POST'])
def respond():
    data = request.json
    choice = data.get('choice')
    
    if choice == 'accept':
        # Сообщение ТЕБЕ в Telegram
        send_telegram_message("⚖️ *ДЕЛО № 1707-ИР*:\nОбвиняемая признала вину! Явка на следственный эксперимент 17 июля в 19:00 подтверждена.")
        # Ответ, который отобразится Ирке на экране
        reply = "Ваше чистосердечное признание занесено в протокол. Попытки побега пресекаются. Спецконвой прибудет 17 июля в 19:00. Будьте готовы к допросу."
    
    elif choice == 'appeal':
        send_telegram_message("🚨 *ДЕЛО № 1707-ИР*:\nВнимание! Обвиняемая пытается обжаловать приговор или требует жесткого допроса!")
        reply = "Ходатайство отклонено Верховным Судом Подруг. Смягчение условий невозможно. Согласно ст. 3 Кодекса Девичника, наказание может быть смягчено только путем употребления штрафного коктейля."
    
    else:
        reply = "Ошибка обработки протокола. Попробуйте еще раз."

    return jsonify({"reply": reply})

if name == '__main__':
    # Для Render и других облачных сервисов
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)