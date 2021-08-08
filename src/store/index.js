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
          // create_atとlimit_atの時間が違かったら追加, それ以外は削除
          state.all_tasks = res_tasks.map(function (task) {
            return {
              id: task.id,
              title: task.task,
              done: false,
              limit_at:
                task.limit_at !== task.created_at ? task.limit_at : undefined,
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
      state.all_subtasks.push({
        id: subtask.id,
        task_id: subtask.task_id,
        title: subtask.sub_task,
        done: false,
      });
    },
    update_task(state, task_info) {
      // 一致するtask_idだけ入れ替える
      state.all_tasks = state.all_tasks.map((task) => {
        if (task.id === task_info.id) {
          return {
            id: task_info.id,
            title: task_info.title,
            done: task_info.done,
            limit_at:
              task.limit_at !== task.created_at ? task.limit_at : undefined,
          };
        }
        return task;
      });
    },
    update_subtask(state, subtask_info) {
      const update_subtask_ids = subtask_info.map((subtask) => {
        return subtask.id;
      });

      const hash_subtasks = subtask_info.reduce((hash, subtask) => {
        hash[subtask.id] = subtask;
        return hash;
      }, {});

      state.all_subtasks = state.all_subtasks.map((subtask) => {
        if (update_subtask_ids.includes(subtask.id)) {
          let update_subtask = hash_subtasks[subtask.id];
          return {
            id: update_subtask.id,
            task_id: update_subtask.task_id,
            title: update_subtask.title,
            done: update_subtask.done,
          };
        }
        return subtask;
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
