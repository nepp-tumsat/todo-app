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
          <v-text-field
            v-model="name"
            label="Name"
            :rules="[required]"
          ></v-text-field>

          <v-text-field
            v-model="password"
            label="password"
            v-bind:type="showPassword ? 'text' : 'password'"
            v-bind:append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword"
            :rules="[required]"
          ></v-text-field>

          <v-text-field
            v-model="email"
            label="email"
            :rules="[required, email_rule]"
          ></v-text-field>

          <v-alert text type="error" v-show="error_message">
            <div>{{ error_message }}</div>
          </v-alert>

          <v-btn tile @click="register" color="primary">
            <v-icon left> mdi-account-plus </v-icon>
            register
          </v-btn>

          <v-btn tile @click="clear"> clear </v-btn>

          <v-btn
            tile
            :to="'/login'"
            class="mr-4"
            color="success"
            absolute
            bottom
            right
          >
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
      email_rule: (v) => /.+@.+\..+/.test(v) || "正しいEmailを入力してください",
      required: (v) => !!v || "必ず入力してください",
      valid: true,
      showPassword: false,
      error_message: "",
    };
  },
  methods: {
    register() {
      if (!this.$refs.form.validate()) {
        return;
      }
      axios
        .post(process.env.FLASK_HOST + "/user", {
          user_name: this.name,
          password: this.password,
          email: this.email,
        })
        .then((res) => {
          const user_info = res.data.user_info;
          const user_id = user_info.id;
          const user_name = user_info.name;
          this.$store.commit("login", {
            user_id: user_id,
            user_name: user_name,
          });
          this.$router.push("/");
        })
        .catch((err) => {
          if (!err.response) {
            this.error_message = "ネットワークエラーです";
            return;
          }
          this.error_message = err.response.data.message;
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
