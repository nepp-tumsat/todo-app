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

# flaskでDB作成
```
# コンテナの中に入る
$ docker exec -it todo_app bash

> flask db init # migrationディレクトリ作成
> flask db migrate -m "マイグレーションのコメント" # マイグレーションの実施
> flask db upgrade # マイグレーション実行

```

# DBアクセス

```
// ホストマシンからDBにアクセス
$ mysql -h 127.0.0.1 -P 3306 -uuser -p

// 使用するデータベースを指定
mysql> USE todo_app
```
