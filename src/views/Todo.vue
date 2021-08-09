<template>
  <div class="home">
    <v-text-field
      v-model="newTaskTitle"
      @click:append="addTask"
      @keydown.enter="addTask"
      class="pa-3"
      outlined
      label="Add Task"
      append-icon="mdi-plus"
      clearable
    ></v-text-field>
    <v-list class="pt-0" flat>
      <v-alert text type="info" v-show="!CanShowList">
        <div>タスクはありません</div>
      </v-alert>
      <draggable v-model="show_tasks" :disable="!Isdraggable">
        <div v-for="task in reversed_tasks" :key="task.id">
          <v-list-item
            @click="doneTask(task.id)"
            :class="{ 'blue lighten-5': task.done }"
          >
            <template v-slot:default>
              <v-list-item-action>
                <v-checkbox
                  :input-value="task.done"
                  color="primary"
                ></v-checkbox>
              </v-list-item-action>

              <v-list-item-content>
                <v-list-item-title
                  :class="{ '.text-decoration-line-through': task.done }"
                >
                  {{ task.title }}
                </v-list-item-title>
              </v-list-item-content>
              <v-spacer></v-spacer>
              <v-list-item-icon v-if="task.limit_at">
                <v-icon left color="grey darken-1">mdi-calendar-month</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>
                  {{ task.limit_at }}
                </v-list-item-title>
              </v-list-item-content>

              <v-list-item-action>
                <v-menu offset-y>
                  <template v-slot:activator="{ on }">
                    <v-btn color="primary" dark v-on="on" icon>
                      <v-icon color="primary lighten-1">
                        mdi-dots-horizontal-circle
                      </v-icon>
                    </v-btn>
                    <v-btn v-show="Isdraggable" icon>
                      <v-icon color="primary lighten-1">
                        mdi-view-headline
                      </v-icon>
                    </v-btn>
                  </template>
                  <v-list>
                    <div v-for="menu in menus" :key="menu.title">
                      <v-list-item @click="selectDialog(menu, task)">
                        <v-list-item-title>
                          {{ menu.title }}
                        </v-list-item-title>
                        <v-list-item-icon v-if="task.limit_at">
                          <v-icon right color="grey darken-1">{{
                            menu.icon
                          }}</v-icon>
                        </v-list-item-icon>
                      </v-list-item>
                    </div>
                  </v-list>
                </v-menu>
              </v-list-item-action>
            </template>
          </v-list-item>
          <v-divider></v-divider>
        </div>
      </draggable>
    </v-list>
    <v-dialog v-model="dialog" width="unset">
      <edit-task
        v-show="Open_menu === 'Edit'"
        :task="selected_task"
        @close="closeDialog"
        @save="onEditSave"
      />
      <add-subtask
        v-show="Open_menu === 'Add Subtask'"
        :task="selected_task"
        @close="closeDialog"
        @add_save="onAddSubTask"
      />
      <select-limit
        v-show="Open_menu === 'Select Limit'"
        :task="selected_task"
        @close="closeDialog"
        @select_limit="onSelectLimit"
      />
      <delete-task
        v-show="Open_menu === 'Delete'"
        :task="selected_task"
        @close="closeDialog"
        @delete="onDelete"
      />
    </v-dialog>
    <div v-show="Open_menu === 'Sort'">
      <v-btn
        x-large
        min-width="300"
        fixed
        bottom
        color="success"
        :style="{ left: '50%', transform: 'translateX(-50%)' }"
        @click="SortEnd"
      >
        Stop Sorting
      </v-btn>
    </div>
    <div>
      <snack-bar
        v-show="show_snackbar"
        :show_snackbar="show_snackbar"
        :message="snackbar_message"
        @close="OnCloseSnackbar"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import EditTask from "../components/Dialogs/EditTask.vue";
import AddSubtask from "../components/Dialogs/AddSubtask.vue";
import SelectLimit from "../components/Dialogs/SelectLimit.vue";
import DeleteTask from "../components/Dialogs/DeleteTask.vue";
import SnackBar from "../components/Shared/SnackBar.vue";

const draggable = require("vuedraggable");
export default {
  name: "Todo",
  components: {
    EditTask,
    AddSubtask,
    SelectLimit,
    DeleteTask,
    SnackBar,
    draggable: draggable,
  },
  data() {
    return {
      dialog: false,
      newTaskTitle: "",
      show_tasks: [],
      show_snackbar: false,
      menus: [
        { title: "Edit", icon: "mdi-pencil" },
        { title: "Add Subtask", icon: "mdi-playlist-plus" },
        { title: "Select Limit", icon: "mdi-calendar-edit" },
        { title: "Delete", icon: "mdi-delete" },
        { title: "Sort", icon: "mdi-sort" },
      ],
      Open_menu: "",
      selected_task: {},
      snackbar_message: "",
    };
  },
  computed: {
    // TODO: task_idがあると楽かも

    Isdraggable: function () {
      return this.Open_menu === "Sort" ? true : false;
    },
    CanShowList: function () {
      return this.all_tasks.length > 0 ? true : false;
    },
    reversed_tasks: function () {
      return this.show_tasks.slice().reverse();
    },
    search_word: function () {
      return this.$store.getters.get_search_word;
    },
    all_tasks: function () {
      return this.$store.getters.get_all_tasks;
    },
  },
  watch: {
    search_word(word) {
      this.show_tasks = this.all_tasks.filter(
        (task) => task.title.indexOf(word) !== -1
      );
    },
    all_tasks() {
      // オブジェクトをコピー
      this.show_tasks = [...this.$store.state.all_tasks];
    },
  },
  methods: {
    selectDialog(menu, task) {
      this.selected_task = task;
      this.Open_menu = menu.title;
      if (this.Open_menu !== "Sort") {
        this.dialog = true;
      }
    },
    closeDialog() {
      this.Open_menu = "";
      this.dialog = false;
      this.selected_task = {};
    },
    OnCloseSnackbar() {
      this.show_snackbar = false;
      this.snackbar_message = "";
    },
    addTask() {
      if (this.newTaskTitle.length < 1) {
        alert("タスク名を入力してください");
        return;
      }
      if (event.keyCode === 13 || event.keyCode === undefined) {
        axios
          .post(process.env.FLASK_HOST + "/task", {
            user_id: this.$store.state.user_id,
            task_name: this.newTaskTitle,
          })
          .then((res) => {
            const task_info = res.data;
            const new_task = {
              id: task_info.id,
              title: task_info.task,
              done: false,
            };

            this.all_tasks.push(new_task);
            this.show_tasks.push(new_task);

            this.newTaskTitle = "";
            this.show_snackbar = true;
            this.snackbar_message = "Added Task!";
          })
          .catch((err) => {
            console.log("err", err);
          });
      }
    },
    doneTask(task_id) {
      let task = this.all_tasks.filter((task) => task.id === task_id)[0];
      task.done = !task.done;
    },
    onDelete() {
      // TODO: storeだけ削除すればいい
      const task_id = this.selected_task.id;
      axios
        .patch(process.env.FLASK_HOST + "/task/" + task_id + "/delete")
        .then((res) => {
          const task_info = res.data.task_info;
          this.$store.commit("delete_task", task_info);
          this.show_snackbar = true;
          this.snackbar_message = res.data.message;
        })
        .catch((err) => {
          console.log("err", err);
        });
      this.Open_menu = "";
      this.dialog = false;
    },
    onAddSubTask(subtask_info) {
      const task_id = subtask_info.task_id;
      const subtasks_arr = subtask_info.subtasks_arr;
      axios
        .post(process.env.FLASK_HOST + "/task/" + task_id + "/subtasks", {
          subtasks: subtasks_arr,
          user_id: this.$store.state.user_id,
        })
        .then((res) => {
          const new_subtasks_arr = res.data.new_subtasks_arr;
          // storeに全て追加する
          new_subtasks_arr.forEach((subtask_obj) => {
            this.$store.commit("add_subtask", subtask_obj);
          });
          this.show_snackbar = true;
          this.snackbar_message = "Added New SubTask!";
        })
        .catch((err) => {
          console.log("err", err);
        });
      this.Open_menu = "";
      this.dialog = false;
    },
    onEditSave(all_task_info) {
      const task_info = all_task_info.task_info;

      // subtask_info => [{id:, task_id:, title, done}, ...]
      const subtask_info = all_task_info.subtask_info; // array

      const task_id = task_info.id;

      try {
        this.update_task(task_id, task_info);
        this.update_subtasks(task_id, subtask_info);
        this.snackbar_message = "Edited Tasks!";
      } catch (err) {
        this.snackbar_message = "Internal server Error";
      } finally {
        this.show_snackbar = true;
        this.Open_menu = "";
        this.dialog = false;
        this.selected_task = {};
      }
    },
    update_task(task_id, task_info) {
      axios
        .patch(process.env.FLASK_HOST + "/task/" + task_id, {
          task_name: task_info.title,
        })
        .then((res) => {
          // storeを更新すればshow_taskも更新される
          const res_task_info = res.data.task_info;
          this.$store.commit("update_task", res_task_info);
        })
        .catch((err) => {
          console.log("err", err);
          throw new Error("update_task error");
        });
    },
    update_subtasks(task_id, subtask_info) {
      if (subtask_info.length === 0) {
        return;
      }

      axios
        .patch(process.env.FLASK_HOST + "/task/" + task_id + "/subtasks/", {
          subtask_info: subtask_info,
        })
        .then((res) => {
          const res_subtask_info = res.data.subtask_info;
          this.$store.commit("update_subtask", res_subtask_info);
        })
        .catch((err) => {
          console.log("err", err);
          throw new Error("update_subtask error");
        });
    },
    onSelectLimit(task_info) {
      const limit_date = task_info.limit_at;
      const task_id = this.selected_task.id;

      axios
        .patch(process.env.FLASK_HOST + "/task/" + task_id + "/limit", {
          limit_at: limit_date,
        })
        .then((res) => {
          const res_task_info = res.data.task_info;
          this.$store.commit("update_task", res_task_info);
          this.snackbar_message = "Selected Due Date!";
        })
        .catch((err) => {
          if (!err.response) {
            this.snackbar_message = "ネットワークエラーです";
            return;
          } else {
            this.snackbar_message = err.response.data.message;
          }
        });
      this.Open_menu = "";
      this.dialog = false;
      this.show_snackbar = true;
    },
    SortEnd() {
      this.Open_menu = false;
      this.show_tasks = this.show_tasks.map((task, index) => {
        return {
          id: task.id,
          title: task.title,
          done: false,
          limit_at: task.limit_at,
          sort_position: index + 1,
        };
      });
    },
  },
  created() {
    this.show_tasks = [...this.$store.state.all_tasks];
  },
};
</script>
