<template>
  <div class="home">
    <v-btn @click="addUser"> user追加 </v-btn>
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
      <v-alert text type="info" v-show="!show_list">
        <div>タスクはありません</div>
      </v-alert>
      <draggable v-model="tasks" :disable="!Isdraggable">
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
                        <v-list-item-title>{{ menu.title }}</v-list-item-title>
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
      />
      <add-subtask
        v-show="Open_menu === 'Add Subtask'"
        :task="selected_task"
        @close="closeDialog"
        @addsave="onAddSave"
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
        @click="Open_menu = false"
      >
        Stop Sorting
      </v-btn>
    </div>
    <div>
      <v-snackbar v-model="snackbar" timeout="1000" multi-line>
        Add New Task!!
        <template v-slot:action="{ attrs }">
          <v-btn color="pink" text v-bind="attrs" @click="snackbar = false">
            Close
          </v-btn>
        </template>
      </v-snackbar>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import EditTask from "../components/Dialogs/EditTask.vue";
import AddSubtask from "../components/Dialogs/AddSubtask.vue";
import DeleteTask from "../components/Dialogs/DeleteTask.vue";

const draggable = require("vuedraggable");
export default {
  name: "Todo",
  components: {
    EditTask,
    AddSubtask,
    DeleteTask,
    draggable: draggable,
  },
  data() {
    return {
      dialog: false,
      day: this.todoDay(),
      date: new Date().getDate(),
      ord: this.nth(new Date().getDate()),
      year: new Date().getFullYear(),
      newTaskTitle: "",
      tasks: [],
      sub_tasks: {},
      snackbar: false,
      menus: [
        { title: "Edit" },
        { title: "Add Subtask" },
        { title: "Delete" },
        { title: "Sort" },
      ],
      Open_menu: "",
      selected_task: {},
      user_id: 1,
      dragging: false,
    };
  },
  computed: {
    Isdraggable: function () {
      return this.Open_menu === "Sort" ? true : false;
    },
    show_list: function () {
      return this.tasks.length > 0 ? true : false;
    },
    reversed_tasks: function () {
      return this.tasks.slice().reverse();
    },
  },
  methods: {
    addUser() {
      axios
        .get(process.env.FLASK_HOST + "/adduser")
        .then((res) => {
          console.log(res.data.message);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    selectDialog(menu, task) {
      this.selected_task = task;
      this.Open_menu = menu.title;
      if (this.Open_menu !== "Sort") {
        this.dialog = true;
      }
      console.log("dialog", this.dialog);
      console.log(this.Open_menu);
      console.log(this.selected_task);
    },
    closeDialog() {
      this.Open_menu = "";
      this.dialog = false;
      this.selected_task = {};
      console.log("close dialog");
    },
    addTask() {
      if (this.newTaskTitle.length < 1) {
        alert("タスク名を入力してください");
        return;
      }
      if (event.keyCode !== 13) return;
      axios
        .post(process.env.FLASK_HOST + "/task", {
          user_id: 1,
          task_name: this.newTaskTitle,
        })
        .then((res) => {
          const task_info = res.data;
          this.tasks.push({
            id: task_info.id,
            title: task_info.task,
            done: false,
          });
          this.newTaskTitle = "";
          this.snackbar = true;
        })
        .catch((err) => {
          console.log("err", err);
        });
    },
    doneTask(task_id) {
      let task = this.tasks.filter((task) => task.id === task_id)[0];
      task.done = !task.done;
    },
    onDelete() {
      // TODO: API接続
      this.tasks = this.tasks.filter(
        (task) => task.id !== this.selected_task.id
      );
      this.Open_menu = "";
      this.dialog = false;
      this.selected_task = {};
    },
    onAddSave() {},
    onEditSave() {},
    todoDay() {
      const d = new Date();
      const days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
      ];
      return days[d.getDay()];
    },
    nth(d) {
      if (d > 3 && d < 21) return "th";
      switch (d % 10) {
        case 1:
          return "st";
        case 2:
          return "nd";
        case 3:
          return "rd";
        default:
          return "th";
      }
    },
  },
  filters: {
    capitalize: function (value) {
      if (!value) return "";
      value = value.toString();
      return value.charAt(0).toUpperCase() + value.slice(1);
    },
  },
  created: function () {
    // TODO: fix
    axios
      .get(process.env.FLASK_HOST + "/task")
      .then((res) => {
        this.tasks = res.data.map(function (task) {
          return {
            id: task.id,
            title: task.task,
            done: false,
          };
        });
        console.log(this.tasks);
      })
      .catch((err) => {
        console.log("err", err);
      });
    // subtask
    this.sub_tasks = {
      1: [
        {
          id: 1,
          title: "sub_task1",
          done: false,
        },
      ],
    };
    // axios.get(process.env.FLASK_HOST + "/subtask").then((res) => {
    // res = {task_id: [sub_task1, sub_task2, ...]}
    // this.sub_tasks = {'1':[{}, {},]}
    // Object.keys(res.data).forEach()
    // });
  },
};
</script>
