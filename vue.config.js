const path = require('path')
function resolve (dir) {
  return path.join(__dirname, dir)
}
const port = process.env.port || process.env.npm_config_port || 8080 // dev port
module.exports = {
  lintOnSave: false,
  devServer: {
    port: port,
    overlay: {
      warnings: false,
      errors: true
    },
    proxy: {
      '/api': {
        target: 'http://localhost:5000', // 请求本地 需要jeecg-boot后台项目
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  },
  assetsDir: process.env.NODE_ENV === 'production' ? '../static' : 'static',
  publicPath: process.env.NODE_ENV === 'production' ? './' : '/',
  outputDir: path.resolve(__dirname, '../templates')

}
