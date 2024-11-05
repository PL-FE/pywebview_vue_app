import { fileURLToPath, URL } from 'node:url'

import { defineConfig,loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig(({mode})=>{
  const env = loadEnv(mode, process.cwd(), "");
  const isproduction = env.VITE_MODE ==='production';
  console.log(env.VITE_VUE_APP_BASE_API);

  return {
  plugins: [
    vue(),
  ],
  base: isproduction ? "/static"  : "/",
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
    build:{
    outDir: "../../gui"
    },
  server: {
    host: '0.0.0.0',
    port: 3000,
    open: true,
    proxy: {
      // detail: https://cli.vuejs.org/config/#devserver-proxy
      // node服务器会执行，但是 pywebview加载静态文件时不会执行
      [env.VITE_VUE_APP_BASE_API]: {
        target: `http://localhost:8000`,
        changeOrigin: true,
        rewrite: (path) => path.replace(new RegExp("^" + env.VITE_VUE_APP_BASE_API), '')
      }
    },
    disableHostCheck: true
  },
  }


})
