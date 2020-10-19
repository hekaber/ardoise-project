const path = require('path');

module.exports = {
  context: path.join(__dirname),
  entry: "./src/index.js",
      output: {
      filename: '[name].bundle.js',
      path: path.resolve(__dirname + '/../../static/assets', 'js'),
    },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};