<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
      class="headline">
    TODOリスト
    </v-app-bar>
    <v-main>
      <keep-alive include='TodoList'>
        <router-view></router-view>
      </keep-alive>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',
};
</script>
