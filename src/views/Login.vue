<template>
  <v-card width="400px" class="mx-auto mt-5">
    <v-card-title>ログイン</v-card-title>
    <v-card-text>
      <v-form>
        <v-text-field
          prepend-icon="mdi-account-circle"
          label="ユーザ名"
          v-model="name"
        ></v-text-field>
        <v-text-field
          v-bind:type="showPassword ? 'text' : 'password'"
          v-bind:append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="showPassword = !showPassword"
          prepend-icon="mdi-lock"
          label="パスワード"
          v-model="password"
        >
        </v-text-field>
        <v-alert text type="error" v-show="error_message">
          <div>{{ error_message }}</div>
        </v-alert>
        <v-card-actions class="justify-center">
          <v-btn color="info" @click="login" width="100px">ログイン</v-btn>
        </v-card-actions>
        <v-card-actions class="justify-center">
          <v-btn coler="success" @click="register" width="100px"
            >新規登録</v-btn
          >
        </v-card-actions>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
import axios from "axios";
export default {
  name: "Login",
  data: () => ({
    showPassword: false,
    name: "",
    password: "",
    error_message: "",
  }),
  methods: {
    login() {
      this.error_message = "";
      if (this.name === "" && this.password === "") {
        this.error_message = "ユーザー名とパスワードは必須です";
        return;
      }
      axios
        .post(process.env.FLASK_HOST + "/login", {
          user_name: this.name,
          password: this.password,
        })
        .then((res) => {
          const user_info = res.data.user_info;
          console.log("res", res);
          this.$store.commit("login", user_info);

          this.$router.push("/");
        })
        .catch((err) => {
          console.log(err);
          this.error_message = "ユーザー名かパスワードが違います";
        });
    },
    register() {
      this.$router.push("/register");
    },
  },
};
</script>
