# About This Application

# Setup

```
source aliases.sh
```

# コンテナ起動

```
// Vueコンテナ
todo-front

// flaskコンテナ
todo-back
```

# Database setup

```
# backendコンテナを立ち上げた状態で以下のコマンドを実行
init_migration
```

# flask で DB 作成

```
# コンテナの中に入る
$ docker exec -it todo_back bash

> flask db init # migrationディレクトリ作成
> flask db migrate -m "マイグレーションのコメント" # マイグレーションの実施
> flask db upgrade # マイグレーション実行

```

# DB アクセス

```
// ホストマシンからDBにアクセス
$ mysql -h 127.0.0.1 -P 3306 -uuser -p

// 使用するデータベースを指定
mysql> USE todo_app
```
