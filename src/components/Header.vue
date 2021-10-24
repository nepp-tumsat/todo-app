<template>
  <v-app-bar app color="primary" dark src="mountains.png" prominent>
    <template v-slot:img="{ props }">
      <v-img
        v-bind="props"
        gradient="to top right, rgba(19,84,122,.5), rgba(128,208,199,.8)"
      ></v-img>
    </template>

    <v-app-bar-nav-icon @click="draw"></v-app-bar-nav-icon>
    <v-app-bar-title>Todo App</v-app-bar-title>
    <v-spacer></v-spacer>

    <SearchField />

      <v-btn id="logout" v-if="$store.state.loggedIn" @click="open" icon>
        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </div>
  </v-app-bar>
</template>

<script>
export default {
  name: 'Header',
  components: {
    SearchField: () => import("./SearchField.vue")
  },
  methods: {
    draw() {
      this.$emit("draw")
    },
    open(event) {
      this.$emit("open", event)
    }
  }

};
</script>
