<template>
  <v-app id="inspire">

    <NavBar
      @open="onOpen"
      :drawer=drawer>
    </NavBar>

    <v-app-bar app color="primary" dark src="mountains.png" prominent>
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(19,84,122,.5), rgba(128,208,199,.8)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-app-bar-title>Todo App</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn
        v-if="!searching && $store.state.loggedIn"
        @click="searching = true"
        icon
      >
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-text-field
        v-if="searching"
        v-model="search_word"
        v-click-outside="onClickOutsideStandard"
        prepend-inner-icon="mdi-magnify"
        autofocus
        outlined
      >
      </v-text-field>
        <v-btn id="logout" v-if="$store.state.loggedIn" @click="onOpen" icon>
          <v-icon>mdi-logout</v-icon>
        </v-btn>
      </div>
    </v-app-bar>

    <v-main>
      <v-dialog v-model="dialog" width="unset">
        <logout v-show="targetId === 'logout'" @logout="onLogout" @close="onClose" />
        <delete v-show="targetId === 'delete'" @logout="onDelete" @close="onClose" />
      </v-dialog>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>

export default {
  components: {
    Logout: () => import("./components/Dialogs/Logout.vue"),
    Delete: () => import("./components/Dialogs/Delete.vue"),
    NavBar: () => import("./components/NavBar.vue")
  },
  data: () => ({
    drawer: false, // navigate barの有無を決める
    items: [
      { title: "Todo", icon: "mdi-format-list-checks", to: "/" },
      { title: "About", icon: "mdi-help-box", to: "/about" },
    ],
    searching: false,
    search_word: "",
    dialog: false,
    targetId: ''
  }),
  methods: {
    onOpen(event) {
      this.targetId = event.currentTarget.id
      this.dialog = true;
    },
    onClose() {
      this.dialog = false;
      this.targetId = ''
    },
    onLogout() {
      this.dialog = false;
      this.targetId = ''
      this.$store.commit("logout");
      // TODO: validationできたらtokenの有無で遷移させる
      this.$router.push("/login");
    },
    onDelete() {
      const user_id = this.$store.state.user_id
      // TODO: APIができるまで放置
      // axios
      //   .delete(process.env.FLASK_HOST + '/user/' + user_id)
      //   .then((res)=> {
      //     this.onLogout()
      //   })
      //   .catch((err) => {
      //     console.log('err', err)
      //     this.dialog = false;
      //     this.targetId = ''
      //   });
    },
    onClickOutsideStandard() {
      // v-click-outsideに式を渡しても代入されなかった
      this.searching = false;

      // wordの初期化
      this.search_word = "";
      this.$store.commit("search", "");
    },
  },
  watch: {
    search_word(new_word) {
      this.$store.commit("search", new_word);
    },
  },
};
</script>
