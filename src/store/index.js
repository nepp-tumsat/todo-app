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
    save_user_id(state, user_id) {
      state.loggedIn = true;
      state.user_id = user_id;
    },
    save_user_name(state, user_name) {
      state.user_name = user_name;
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
  actions: {
    login(context, user_info) {
      context.commit("save_user_id", user_info.user_id);
      context.commit("save_user_name", user_info.user_name);
    },
  },
});

export default store;
