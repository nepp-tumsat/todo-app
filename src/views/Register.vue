<template>
  <v-row style="height: 450px" justify="center" align-content="center">
    <v-col>
      <v-card class="pa-md-4 mx-lg-auto" width="800px">
        <v-card-title>新規登録</v-card-title>
        <form>
          <v-text-field v-model="name" label="Name"></v-text-field>
          <v-text-field v-model="email" label="E-mail"></v-text-field>

          <v-btn class="mr-4" @click="register"> register </v-btn>
          <v-btn @click="clear"> clear </v-btn>
        </form>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      name: "",
      email: "",
      select: null,
      items: ["Item 1", "Item 2", "Item 3", "Item 4"],
      checkbox: false,
    };
  },
  methods: {
    clear() {
      this.name = "";
      this.password = "";
    },
    register() {
      // TODO: API 接続
      // TODO: Validatation
      console.log("submit");
      this.$store.commit("login");
      this.$router.push("/");
    },
  },
};
</script>
