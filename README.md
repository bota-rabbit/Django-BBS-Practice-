# 🐘 Django BBS  
PAIZAラーニングで Django を学びながら制作した、簡易SNS風の掲示板アプリです。  
投稿・閲覧・削除を行えるシンプルなBBSで、Webアプリの基本設計を理解するための練習を目的としております。

---

## 🎯 Purpose（目的）
- Djangoの基本（MVT）に触れ、Webアプリ制作の流れを身につける  
- 投稿データの保存・表示・削除のしくみを学ぶ  
- 小規模SNSの基礎構造を理解する  

---

## 🔧 使用技術 / Technologies
- Python  
- Django  
- HTML / CSS  
- SQLite（開発環境の標準DB）

---

## 📌 主な機能
| 機能 | 内容 |
|---|---|
| 📢 投稿作成 | テキストを入力し公開できる |
| 📄 投稿一覧表示 | Mastodon風TLとして時系列で表示 |
| 🗑 投稿削除 | 不要な投稿を削除可能 |
| 🐣 シンプルUI | 拡張に向いた最小構成 |

---

## ✨ フロントエンド
- テンプレートは **Bootstrap5 に対応**  
- スタイルは軽く調整しつつ、UIを崩さないよう最小限の改修  
- 旧バージョン依存のクラスを5系向けに整理済み

---

## 🚀 ローカル環境での実行手順
```bash
git clone https://github.com/あなたのID/django-mastodon-bbs.git
cd django-mastodon-bbs

# 仮想環境（任意）
python -m venv venv

# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
