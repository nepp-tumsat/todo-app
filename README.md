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

# DBアクセス

```
// ホストマシンからDBにアクセス
$ mysql -h 127.0.0.1 -P 3306 -uuser -p

// 使用するデータベースを指定
mysql> USE todo_app
```
