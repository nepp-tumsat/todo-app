<template>
  <v-app id="inspire">
    <NavBar @open="onOpen" :drawer="drawer" />
    <Header @open="onOpen" @draw="onDraw" />

    <v-main>
      <v-dialog v-model="dialog" width="unset">
        <logout
          v-show="targetId === 'logout'"
          @logout="onLogout"
          @close="onClose"
        />

        <delete
          v-show="targetId === 'delete'"
          @delete="onDelete"
          @close="onClose"
        />
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
    NavBar: () => import("./components/NavBar.vue"),
    SearchField: () => import("./components/SearchField.vue"),
    Header: () => import("./components/Header.vue"),
  },
  data: () => ({
    drawer: false, // navigate barの有無を決める
    dialog: false,
    targetId: "",
  }),
  methods: {
    onOpen(event) {
      this.targetId = event.currentTarget.id;
      this.dialog = true;
    },
    onDraw() {
      this.drawer = !this.drawer;
    },
    onClose() {
      this.dialog = false;
      this.targetId = "";
    },
    onLogout() {
      this.dialog = false;
      this.targetId = "";
      this.$store.commit("logout");
      // TODO: validationできたらtokenの有無で遷移させる
      this.$router.push("/login");
    },
    onDelete() {
      const user_id = this.$store.state.user_id;
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
  },
};
</script>
