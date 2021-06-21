const path = require('path');
// const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin')
const { VueLoaderPlugin } = require("vue-loader");

const env = process.env.NODE_ENV
const target = env === 'development'?'web':['web', 'es5']

module.exports = {
  mode: 'development',
  devtool: 'inline-source-map', // デバッグしやすくする
  entry: './src/index.js', // エントリポイント,
  target: target,
  // 出力先(絶対パスを指定する必要がある)
  output: {
    // __dirnameはパスの先頭
    path: path.resolve(__dirname, "dist"), // 絶対パス -> 文字列結合しないのはOSによって/が違うから
    filename: 'main.js',
  },
  devServer: {
    open:true,
    host: '0.0.0.0',
    port: 3031,
    hot: true,
    watchOptions: {
        poll: 1000
    },
    // webpackの扱わないファイル(HTMLや画像など)が入っているディレクトリ
    contentBase: path.resolve(__dirname, "public")
  },
  watch: true, // ファイル変更を検知して自動コンパイルする
  watchOptions: {
    ignored: '/node_modules/'
  },
  // Loader
  module: {
    rules: [
      {
        test: /\.s(c|a)ss$/,
        use: [
          'vue-style-loader',
          'css-loader',
          {
            loader: 'sass-loader',
            // Requires >= sass-loader@^8.0.0
            options: {
              implementation: require('sass'),
              sassOptions: {
                indentedSyntax: true // optional
              },
            }
          }
        ]
      },
      // Vueの中にあるcssを読み取るのに必要
      {
        test: /\.css$/,
        use: ["vue-style-loader", "css-loader"]
      },
      {
        test: /\.vue$/,
        exclude: /node_modules/,
        use: [
          'vue-loader'
        ]
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        options: {
          presets: ['@babel/preset-env']
        }
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif|ico)$/i,
        exclude: /node_modules/,
        loader: 'file-loader',
        options: {
          outputPath: 'img',
        }
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin(),// vue-loaderを使う場合に記述
    new HtmlWebpackPlugin({ // /public/index.htmlの部分
      title:'TODO APP',
      template: path.resolve(__dirname, 'public/index.html'),
      url:'/static/img/',
      inject: 'body',
      hash: true,
    })
  ],
  // resolve: {
  //   alias: {
  //     vue$: 'vue/dist/vue.esm.js'
  //   }
  // }
}