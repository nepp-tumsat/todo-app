import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    loggedIn: false,
    token: "",
    user_id: "",
  },
  mutations: {
    login(state, user_id) {
      state.loggedIn = true;
      state.user_id = user_id;
    },
    logout(state, user_id) {
      state.loggedIn = false;
      state.user_id = user_id;
    },
  },
});

export default store;
