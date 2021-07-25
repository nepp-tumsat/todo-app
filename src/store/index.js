import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    loggedIn: false,
    token: "",
    user_id: "",
    user_name: "",
    search_word: "",
    all_tasks: [],
    all_subtasks: [],
  },
  mutations: {
    // １つの関数に対して引数は１つのみ
    login(state, user_info) {
      state.loggedIn = true;
      state.user_id = user_info.user_id;
      state.user_name = user_info.user_name;
      // task, subtaskの取得(showのみ)
      axios
        .get(process.env.FLASK_HOST + "/user/" + state.user_id + "/all_tasks")
        .then((res) => {
          const res_tasks = res.data.tasks;
          const res_subtasks = res.data.subtasks;

          state.all_tasks = res_tasks.map(function (task) {
            return {
              id: task.id,
              title: task.task,
              done: false,
            };
          });
          state.all_subtasks = res_subtasks.map(function (subtask) {
            return {
              id: subtask.id,
              task_id: subtask.task_id,
              title: subtask.sub_task,
              done: false,
            };
          });
        })
        .catch((err) => {
          console.log("err", err);
        });
    },
    logout(state) {
      state.loggedIn = false;
      state.user_id = "";
      state.user_name = "";
      state.all_tasks = [];
      state.all_subtasks = [];
    },
    search(state, word) {
      state.search_word = word;
    },
    add_subtask(state, subtask) {
      state.subtask.push({
        id: subtask.id,
        task_id: subtask.task_id,
        title: subtask.sub_task,
        done: false,
      });
    },
  },
  getters: {
    get_username(state) {
      return state.user_name;
    },
    get_search_word(state) {
      return state.search_word;
    },
    get_all_tasks(state) {
      return state.all_tasks;
    },
    get_all_subtasks(state) {
      return state.all_subtasks;
    },
  },
});

export default store;
