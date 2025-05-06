# 📄 PDF Invoice Generator (Flask + WeasyPrint)

![デモ画像](https://via.placeholder.com/800x400?text=PDF+Invoice+Generator+Demo)

## 📋 プロジェクト概要

Flask と WeasyPrint を組み合わせた Web ベースの PDF 請求書生成アプリケーションです。ユーザーは Web フォームに顧客情報や商品詳細を入力するだけで、プロフェッショナルな請求書 PDF を即座に生成・ダウンロードできます。実務での請求書作成業務や帳票自動生成ツールとしてすぐに活用できる実用的なアプリケーションです。

## 🔧 使用技術

- **バックエンド**: Python 3.8+, Flask 2.2.0+
- **PDF 生成**: WeasyPrint 60.1+
- **フロントエンド**: HTML5, CSS3, JavaScript, Bootstrap 5
- **その他**: SVG (ロゴ表示), 日本語フォントサポート

## 🔄 処理の流れ

```
[ユーザー] → フォーム入力 → [Flask アプリ] → データ処理・計算 → HTML テンプレート生成 
→ [WeasyPrint] → PDF 変換 → [保存・表示] → [ユーザー]
```

1. ユーザーが Web フォームに顧客情報・商品情報を入力
2. Flask がフォームデータを受け取り、合計金額・税額を計算
3. HTML テンプレートにデータを埋め込み
4. WeasyPrint が HTML を PDF に変換
5. 生成された PDF をサーバーに保存
6. ユーザーに PDF 表示・ダウンロードのリンクを提供

## ✨ 特徴・工夫した点

### 技術面
- **非依存型アーキテクチャ**: データベース不要で即座に起動・実行可能
- **レスポンシブなフォーム設計**: JavaScript による動的な明細項目の追加・削除
- **ファイル管理システム**: タイムスタンプによるユニークなファイル名生成と履歴管理
- **内部 SVG ロゴ**: 外部画像に依存せず、アプリケーション単体で完結

### ユーザー体験
- **直感的な UI**: Bootstrap フレームワークによるモダンで使いやすいインターフェース
- **即時プレビュー**: 生成後すぐに PDF を表示可能
- **履歴管理**: 過去に生成した PDF の一覧表示と再ダウンロード

### ビジネス価値
- **業務効率化**: 手作業での請求書作成時間を大幅に削減
- **カスタマイズ容易**: HTML/CSS 知識があれば帳票デザインを自由に変更可能
- **コスト削減**: 有料の請求書ソフトウェアや帳票システムの代替として

## 🔌 セットアップ手順

### 前提条件
- Python 3.8 以上
- pip (Python パッケージマネージャー)

### インストール

```bash
# リポジトリのクローン
git clone https://github.com/yourusername/pdf-invoice-generator-flask.git
cd pdf-invoice-generator-flask

# 仮想環境のセットアップ
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存パッケージのインストール
pip install -r requirements.txt

# WeasyPrint の依存パッケージをインストール (OS 別)
# Ubuntu/Debian:
# apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

# macOS:
# brew install cairo pango gdk-pixbuf libffi

# Windows:
# GTK3インストーラー (https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer) を使用

# アプリケーションの実行
python app.py
```

ブラウザで http://127.0.0.1:5000 にアクセスして利用開始します。

## 📸 デモ画面キャプチャ

### 入力フォーム画面
![入力フォーム](https://via.placeholder.com/800x500?text=入力フォーム画面)

### 生成された PDF 請求書
![PDF 請求書](https://via.placeholder.com/800x500?text=生成されたPDF請求書)

### 履歴管理画面
![履歴画面](https://via.placeholder.com/800x500?text=履歴管理画面)

## 📂 プロジェクト構成

```
pdf-invoice-generator-flask/
├── app.py                 # Flask アプリケーションのメインファイル
├── templates/             # HTML テンプレート
│   ├── index.html         # 入力フォーム画面
│   ├── invoice_template.html  # PDF 生成用テンプレート
│   └── history.html       # 履歴表示画面
├── static/                # 静的ファイル
│   └── css/
│       └── style.css      # カスタム CSS
├── generated/             # 生成された PDF の保存フォルダ
├── requirements.txt       # 依存パッケージリスト
└── README.md              # プロジェクト説明
```

## 🚀 将来の拡張計画

- ユーザー認証システムの導入
- 顧客データベースとの連携
- メール送信機能の実装
- 複数テンプレートの切り替え機能
- 請求書の自動ナンバリングと管理
- API エンドポイントの提供
- 多言語対応

## 💡 実用ユースケース

- フリーランサーの請求書発行
- 小規模事業者の見積書・納品書作成
- 社内経費精算書の自動生成
- イベント参加証の発行
- 各種証明書の生成

## 📚 学んだこと・開発の振り返り

このプロジェクトを通じて、以下の技術的チャレンジに取り組みました：

1. **HTML から PDF への変換技術**: WeasyPrint を使用して Web コンテンツを印刷用フォーマットに変換
2. **動的フォーム処理**: JavaScript を活用した明細項目の追加・削除機能
3. **ファイルシステム管理**: 一意のファイル名生成とディレクトリ構造の設計
4. **レスポンシブ デザイン**: 様々なデバイスでの使いやすさを考慮した UI 設計

## 🔗 参考リソース

- [Flask 公式ドキュメント](https://flask.palletsprojects.com/)
- [WeasyPrint ドキュメント](https://doc.courtbouillon.org/weasyprint/stable/)
- [Bootstrap 公式サイト](https://getbootstrap.com/)

## 👨‍💻 コントリビューション

貢献は歓迎します！バグ報告、機能リクエスト、プルリクエストなどをお待ちしています。

## 📜 ライセンス

MIT License

## 📧 コンタクト

質問や提案があれば、[GitHub Issues](https://github.com/yourusername/pdf-invoice-generator-flask/issues) で問い合わせるか、email@example.com までご連絡ください。
