#!/bin/sh

#node_modulesインストール
echo "npm install"
npm install

#vue起動
echo "npm run serve. "
npm run serve --host 0.0.0.0 --port 3031

#メモを出力
echo "localhost:18080"