import { fileURLToPath, URL } from 'node:url'

import { defineConfig,loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig(({mode})=>{
  const env = loadEnv(mode, process.cwd(), "");
  console.log(env.VUE_APP_BASE_API);
  return {
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host: '0.0.0.0',
    port: 3000,
    open: true,
    proxy: {
      // detail: https://cli.vuejs.org/config/#devserver-proxy
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
