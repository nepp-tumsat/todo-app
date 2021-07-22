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
        <v-card-actions>
          <v-btn color="info" @click="submit">ログイン</v-btn>
          <v-btn coler="success" @click="submit">新規登録</v-btn>
        </v-card-actions>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "Login",
  data: () => ({
    showPassword: false,
    name: "",
    password: "",
    error_message: "",
  }),
  methods: {
    submit() {
      this.error_message = "";
      // TODO: fix
      if (this.name === "user1" && this.password === "password") {
        this.$store.commit("login");
        this.$router.push("/");
      } else {
        this.error_message = "ユーザー名かパスワードが違います";
      }
    },
  },
};
</script>
