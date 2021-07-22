<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" app>
      <v-list class="px-2" height="90px">
        <v-list-item-avatar size="80px">
          <img src="https://randomuser.me/api/portraits/women/81.jpg" />
        </v-list-item-avatar>
      </v-list>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h5">
            {{ display_username }}
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense nav>
        <v-list-item v-for="item in items" :key="item.title" :to="item.to" link>
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app color="primary" dark src="mountains.png" prominent>
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(19,84,122,.5), rgba(128,208,199,.8)"
        ></v-img>
      </template>

      <!-- !null = true -->
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-app-bar-title>Todo App</v-app-bar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: false, // navigate barの有無を決める
    items: [
      { title: "Todo", icon: "mdi-format-list-checks", to: "/" },
      { title: "About", icon: "mdi-help-box", to: "/about" },
    ],
    display_username: "",
  }),
  computed: {
    user_name: function () {
      return this.$store.getters.get_username;
    },
  },
  watch: {
    user_name(get_username) {
      this.display_username = get_username;
    },
  },
};
</script>
