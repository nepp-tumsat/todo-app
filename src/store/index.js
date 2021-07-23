import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    loggedIn: false,
    token: "",
    user_id: "",
    user_name: "",
  },
  mutations: {
    // １つの関数に対して引数は１つのみ
    login(state, user_info) {
      state.loggedIn = true;
      state.user_id = user_info.user_id;
      state.user_name = user_info.user_name;
    },
    logout(state) {
      state.loggedIn = false;
      state.user_id = "";
      state.user_name = "";
    },
  },
  getters: {
    get_username(state) {
      return state.user_name;
    },
  },
});

export default store;
