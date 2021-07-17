const path = require("path");
const webpack = require("webpack");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const { VueLoaderPlugin } = require("vue-loader");

const env = process.env.NODE_ENV;
const target = env === "development" ? "web" : ["web", "es5"];
const ignore_env_vars = new Set([
	"YARN_VERSION",
	"HOSTNAME",
	"PWD",
	"HOME",
	"NODE_VERSION",
	"TERM",
	"SHLVL",
	"PATH",
	"_",
]);

let env_vars = [];
Object.keys(process.env).forEach((key) => {
	if (!ignore_env_vars.has(key)) {
		env_vars.push(key);
	}
});

module.exports = {
	mode: "development",
	devtool: "inline-source-map", // デバッグしやすくする
	entry: "./src/index.js", // エントリポイント,
	target: target,
	// 出力先(絶対パスを指定する必要がある)
	output: {
		// __dirnameはパスの先頭
		path: path.resolve(__dirname, "dist"), // 絶対パス -> 文字列結合しないのはOSによって/が違うから
		filename: "[name].bundle.js",
	},
	devServer: {
		open: true,
		host: "0.0.0.0",
		port: 3031,
		hot: true,
		contentBase: path.resolve(__dirname, "public/"), // サーバーの起点ディレクトリ
		watchOptions: {
			poll: 1000,
			ignored: ["/node_modules/"],
		},
		historyApiFallback: {
			rewrites: [{ from: /^\/*/, to: "/index.html" }],
		},
		// webpackの扱わないファイル(HTMLや画像など)が入っているディレクトリ
		contentBase: path.resolve(__dirname, "public"),
	},
	// Loader
	module: {
		rules: [
			{
				test: /\.s(c|a)ss$/,
				use: [
					"vue-style-loader",
					"css-loader",
					{
						loader: "sass-loader",
						// Requires >= sass-loader@^8.0.0
						options: {
							implementation: require("sass"),
							sassOptions: {
								indentedSyntax: true, // optional
							},
						},
					},
				],
			},
			// Vueの中にあるcssを読み取るのに必要
			{
				test: /\.css$/,
				use: ["vue-style-loader", "css-loader"],
			},
			{
				test: /\.vue$/,
				exclude: /node_modules/,
				use: ["vue-loader"],
			},
			{
				test: /\.js$/,
				loader: "babel-loader",
				exclude: /node_modules/,
				options: {
					presets: ["@babel/preset-env"],
				},
			},
			{
				test: /\.(png|svg|jpg|jpeg|gif|ico)$/i,
				exclude: /node_modules/,
				loader: "file-loader",
				options: {
					outputPath: "img",
				},
			},
		],
	},
	plugins: [
		new VueLoaderPlugin(), // vue-loaderを使う場合に記述
		new HtmlWebpackPlugin({
			// /public/index.htmlの部分
			title: "TODO APP",
			template: path.resolve(__dirname, "public/index.html"),
			url: "/static/img/",
			inject: "body",
			hash: true,
		}),
		new webpack.EnvironmentPlugin(env_vars),
	],
	// resolve: {
	//   alias: {
	//     vue$: 'vue/dist/vue.esm.js'
	//   }
	// }
};
