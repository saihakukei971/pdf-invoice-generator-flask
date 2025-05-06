from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from weasyprint import HTML
from datetime import datetime
import os
import json

app = Flask(__name__)

# 生成したPDFの保存先ディレクトリ
GENERATED_FOLDER = 'generated'
if not os.path.exists(GENERATED_FOLDER):
    os.makedirs(GENERATED_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # フォームからデータを取得
    customer_name = request.form['customer_name']
    invoice_date = request.form['invoice_date']
    
    # 明細項目の取得
    items = []
    i = 0
    while f'item_name_{i}' in request.form and request.form[f'item_name_{i}']:
        name = request.form[f'item_name_{i}']
        price = int(request.form[f'item_price_{i}'])
        quantity = int(request.form[f'item_quantity_{i}'])
        subtotal = price * quantity
        
        items.append({
            'name': name,
            'price': price,
            'quantity': quantity,
            'subtotal': subtotal
        })
        i += 1
    
    # 備考欄
    remarks = request.form.get('remarks', '')
    
    # 合計金額の計算
    subtotal_sum = sum(item['subtotal'] for item in items)
    tax = int(subtotal_sum * 0.1)  # 消費税10%
    total = subtotal_sum + tax
    
    # ファイル名の生成（現在日時を含める）
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f"invoice_{timestamp}.pdf"
    output_path = os.path.join(GENERATED_FOLDER, filename)
    
    # 請求書メタデータ
    invoice_data = {
        'customer_name': customer_name,
        'invoice_date': invoice_date,
        'items': items,
        'subtotal': subtotal_sum,
        'tax': tax,
        'total': total,
        'remarks': remarks,
        'invoice_number': f"INV-{timestamp}",  # 請求書番号
        'company_name': '株式会社サンプル',
        'company_address': '東京都渋谷区〇〇町1-2-3',
        'company_tel': '03-1234-5678',
        'company_email': 'info@example.com'
    }
    
    # HTML → PDF変換
    html = render_template('invoice_template.html', **invoice_data)
    HTML(string=html, base_url=request.url).write_pdf(output_path)
    
    # 生成履歴を表示
    return redirect(url_for('history'))

@app.route('/history')
def history():
    files = []
    for filename in os.listdir(GENERATED_FOLDER):
        if filename.endswith('.pdf'):
            filepath = os.path.join(GENERATED_FOLDER, filename)
            creation_time = os.path.getctime(filepath)
            creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
            files.append({
                'filename': filename,
                'created_at': creation_date
            })
    
    # 作成日時の新しい順に並べ替え
    files.sort(key=lambda x: x['created_at'], reverse=True)
    
    return render_template('history.html', files=files)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(GENERATED_FOLDER, filename, as_attachment=True)

@app.route('/view/<filename>')
def view(filename):
    return send_from_directory(GENERATED_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)