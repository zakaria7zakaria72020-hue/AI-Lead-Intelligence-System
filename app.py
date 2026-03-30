import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# وظيفة المنطق: تقييم العميل بناءً على الميزانية والكلمات المفتاحية
def evaluate_lead(data):
    budget = data.get('budget', 0)
    interest = data.get('interest', '').lower()
    
    # منطق التفكير (Business Logic)
    if int(budget) > 5000 or "automation" in interest:
        return "HIGH_PRIORITY", "Assign to Senior Consultant"
    return "STANDARD", "Add to Email Nurturing"

@app.route('/webhook', methods=['POST'])
def handle_lead():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data received"}), 400
        
    priority, action = evaluate_lead(data)
    
    # النتيجة التي ستعود لـ n8n أو Slack
    response = {
        "status": "processed",
        "lead_name": data.get('name', 'Unknown'),
        "priority": priority,
        "recommended_action": action,
        "engine": "Zakaria-Logic-v1"
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
