<template>
  <v-app id="inspire">
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
          <v-icon id="delete" right color="grey darken-1" @click="onOpen"
            >mdi-account-minus</v-icon
          >
        </v-list-item-icon>
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
import Logout from "./components/Dialogs/Logout.vue";
import Delete from "./components/Dialogs/Delete.vue";

export default {
  components: {
    Logout,
    Delete
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
  components: {
    Logout,
  },
  methods: {
    onOpen(event) {
      this.targetId = event.currentTarget.id;
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
  computed: {
    user_name: function () {
      return this.$store.getters.get_username;
    },
  },
  watch: {
    search_word(new_word) {
      this.$store.commit("search", new_word);
    },
  },
};
</script>
