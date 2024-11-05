<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>

  <header >
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about" >About</RouterLink>
         <RouterLink to="/about1" @click="bt01">Primary</RouterLink>
      </nav>
    </div>
  </header>
        <RouterView />


</template>
<script>
import {request} from '@/utils/request.js'
import {useRoute,useRouter} from 'vue-router'
// 组合式才能用
// const route = useRoute()
// console.log("route",route)
export default {
  name: 'App',
  created() {
    console.log("created route",this.$route)
  },
  computed : {
    isFullScreen(){

       console.log("computed route",this.$route.meta.fullScreen)
       // 注意默认值是undefined 不是true 或者 false
       return this.$route.meta.fullScreen===true
    }
  },
    watch: {
    // 监听路由变化，如果路由切换，可以重新计算
    // $route(to) {
    //   console.log("watch route",this.$route.meta.fullScreen)
    //    this.isFullScreenRoute=this.$route.meta.fullScreen===true
    //
    // }
  },
  data(){
    return {
        // isFullScreenRoute: false
    }

  },
  methods:{
    bt01(){

      request('/test',
        {
        "txt": 'test'
      },
      'post'
      ).then(res => {
        console.log(res.data);
      })

    },
    //... other methods...

  }





}


</script>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
