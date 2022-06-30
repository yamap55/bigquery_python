# python_repository_simple

本リポジトリは BigQuery を Python で触るリポジトリです

## 環境詳細

- Python : 3.9

### 開発手順

1. VS Code 起動
2. 左下の緑色のアイコンクリック
3. 「Remote-Containersa: Reopen in Container」クリック
4. しばらく待つ
   - 初回の場合コンテナー image の取得や作成が行われる
5. 起動したら開発可能

## 準備

- `.env` ファイルをプロジェクトルートに作成
  - とりあえず空ファイルで OK
- [公式のドキュメント](https://cloud.google.com/bigquery/docs/reference/libraries?hl=ja) に従って進める
  - 環境変数は `.env` ファイルに記載する事で開発環境に読み込まれる
  - 必要な権限（ロール）は下記を参照

### 環境変数

下記、公式ドキュメントに沿って作成した認証情報を環境変数に設定する必要がある

```
GOOGLE_APPLICATION_CREDENTIALS=C:\github\bigquery_python\work\secret\bigquery-test-354810-213eebabe17e.json
```

### 必要な権限

- BigQuery 管理者
- ストレージ管理者
  - チュートリアルには記載がないので注意

※動作させた際の権限

## 実行

```
python main.py
```

## 参考

- https://cloud.google.com/bigquery/docs/reference/libraries?hl=ja
- https://dev.classmethod.jp/articles/service-account-bigquery-roles/#jobs
