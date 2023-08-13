import { defineConfig } from 'vite'
const path = require('path');

export default defineConfig({
//   root: './src', // directorio de origen de los archivos
  build: {
    outDir: path.resolve(__dirname, '../../static/js'),
    rollupOptions: {
        output: {
            entryFileNames: 'home.js',
            format: 'iife'
          },
        input: './index-home.js',
    }
  },
})