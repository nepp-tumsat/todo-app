<template>
  <v-navigation-drawer v-model="drawer" app>
    <v-list class="px-2" height="90px">
      <v-list-item-avatar size="80px">
        <img src="Nepp.jpg" />
      </v-list-item-avatar>
    </v-list>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="text-h5">
          {{ user_name }}
        </v-list-item-title>
      </v-list-item-content>

      <v-list-item-icon>
        <v-icon id="delete" right color="grey darken-1" @click="open"
          >mdi-account-minus
        </v-icon>
      </v-list-item-icon>
    </v-list-item>

    <v-divider></v-divider>

    <v-list dense nav>
      <v-list-item v-for="item in items" :key="item.title" :to="item.to" link>
        <v-list-item-icon>
          <v-icon>
            {{ item.icon }}
          </v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>
            {{ item.title }}
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "NavBar",
  props: {
    drawer: Boolean,
  },
  data: () => ({
    items: [
      { title: "Todo", icon: "mdi-format-list-checks", to: "/" },
      { title: "About", icon: "mdi-help-box", to: "/about" },
    ],
  }),
  computed: {
    user_name() {
      return this.$store.getters.get_username;
    },
  },
  methods: {
    open(event) {
      this.$emit("open", event);
    },
  },
};
</script>
