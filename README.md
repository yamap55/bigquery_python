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

### 環境変数

下記、公式ドキュメントに沿って作成した認証情報を環境変数に設定する必要がある

```
GOOGLE_APPLICATION_CREDENTIALS=C:\github\bigquery_python\work\secret\bigquery-test-354810-213eebabe17e.json
```

## 必要な権限

- BigQuery 管理者
- ストレージ管理者

※動作させた際の権限

## 参考

- https://cloud.google.com/bigquery/docs/reference/libraries?hl=ja
- https://dev.classmethod.jp/articles/service-account-bigquery-roles/#jobs
