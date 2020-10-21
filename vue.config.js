const path = require('path');
function resolve(dir) {
  return path.join(__dirname, dir)
}

module.exports = {
  lintOnSave: false,
  devServer: {
      overlay: {
          warning: false,
          errors: false
      }
  },
  assetsDir: process.env.NODE_ENV === 'production'? '../static' : 'static',
  publicPath: process.env.NODE_ENV === 'production'? './' : '/',
  outputDir: path.resolve(__dirname, '../templates')
}
