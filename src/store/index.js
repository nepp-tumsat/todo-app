import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    loggedIn: false,
  },
  mutations: {
    increment(state) {
      state.count++;
    },
  },
});

store.commit("increment");

export default store;
