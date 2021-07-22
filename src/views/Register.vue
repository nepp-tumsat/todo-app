<template>
  <v-row style="height: 450px" justify="center" align-content="center">
    <v-col>
      <v-card
        class="pa-md-4 mx-lg-auto"
        width="800px"
        style="position: relative"
      >
        <v-card-title>ユーザー新規登録</v-card-title>
        <v-form ref="form">
          <v-text-field v-model="name" label="Name"></v-text-field>
          <v-text-field v-model="password" label="password"></v-text-field>
          <v-text-field v-model="email" label="email"></v-text-field>

          <v-alert text type="error" v-show="error_message">
            <div>{{ error_message }}</div>
          </v-alert>

          <v-btn tile @click="register">
            <v-icon left> mdi-account-plus </v-icon>
            register
          </v-btn>
          <v-btn tile @click="clear"> clear </v-btn>
          <v-btn tile :to="'/login'" class="mr-4" absolute bottom right>
            <v-icon left> mdi-keyboard-return </v-icon>
            back
          </v-btn>
        </v-form>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import axios from "axios";
export default {
  name: "Register",
  data() {
    return {
      name: "",
      password: "",
      email: "",
      error_message: "",
    };
  },
  methods: {
    register() {
      // TODO: API 接続
      if (this.name === "" || this.password === "") {
        this.error_message = "名前とパスワードを入力してください";
        return;
      }
      axios
        .post(process.env.FLASK_HOST + "/user", {
          user_name: this.name,
          password: this.password,
          email: this.email,
        })
        .then((res) => {
          const user_id = res.data.user_id;
          const user_name = res.data.username;
          this.$store.dispatch("login", {
            user_id: user_id,
            user_name: user_name,
          });
          this.$router.push("/");
        })
        .catch((err) => {
          console.log("err", err);
        });
    },
    clear() {
      this.name = "";
      this.password = "";
      this.email = "";
    },
  },
};
</script>
