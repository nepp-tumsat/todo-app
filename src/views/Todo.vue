<template>
  <div class='home'>
    <v-btn
      @click="addUser"
    >
      user追加
    </v-btn>
    <v-text-field
      v-model="newTaskTitle"
      @click:append="addTask"
      @keyup.enter="addTask"
      class="pa-3"
      outlined
      label="Add Task"
      append-icon="mdi-plus"
      clearable
      :rules="rules.task"
      required
    ></v-text-field>
    <v-list
      class="pt-0"
      flat
    >
      <div
        v-for="task in tasks"
        :key="task.id"
      >
      <!-- <EditTask v-show="Open_item === 'Edit'" :item="item" @close="closeDialog"/>
      <AddSubTask v-show="Open_item === 'Add Subtask'" :item="item" /> -->
      <DeleteTask v-show="Open_item === 'Delete'" :Open_item="Open_item" :task="task" @close="closeDialog"/>
        <v-list-item
          @click="doneTask(task.id)"
          :class="{ 'blue lighten-5' : task.done }"
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
                :class="{ '.text-decoration-line-through' : task.done }"
              >
              {{ task.title }}
              </v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-menu offset-y>
                <template v-slot:activator="{ on }">
                  <v-btn
                    color="primary"
                    dark
                    v-on="on"
                    icon
                  >
                    <v-icon color="primary lighten-1">
                      mdi-dots-horizontal-circle
                    </v-icon>
                  </v-btn>
                </template>
                <v-list>
                  <v-list-item
                    v-for="(item, index) in items"
                    :key="index"
                    @click="selectDialog(item.title)"
                  >
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
          </v-list-item-action>
          </template>
        </v-list-item>
        <v-divider></v-divider>
      </div>
    </v-list>

    <div>
      <v-snackbar
        v-model="snackbar"
        timeout=1000
        multi-line
      >
        Add New Task!!
        <template v-slot:action="{ attrs }">
          <v-btn
            color="pink"
            text
            v-bind="attrs"
            @click="snackbar = false"
          >
            Close
          </v-btn>
        </template>
      </v-snackbar>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import EditTask from '../components/Dialogs/EditTask.vue'
import AddSubTask from '../components/Dialogs/AddSubTask.vue'
import DeleteTask from '../components/Dialogs/DeleteTask.vue'

export default {
  name: 'Todo',
  components: {
    EditTask,
    AddSubTask,
    DeleteTask,
  },
  data() {
    return {
      dialog: false,
      day: this.todoDay(),
      date: new Date().getDate(),
      ord: this.nth(new Date().getDate()),
      year: new Date().getFullYear(),
      newTaskTitle: '',
      tasks: [],
      snackbar: false,
      rules: {
        task: [val => (val || '').length > 0 || 'This field is required']
      },
      items: [
        { title: 'Edit' },
        { title: 'Add Subtask' },
        { title: 'Delete' },
        { title: 'Sort' },
      ],
      Open_item: '',
      user_id: 0,
    }
  },
  methods: {
    addUser() {
      axios.get(process.env.FLASK_HOST + '/adduser')
        .then((res) => {
          console.log(res.data.message)
          }
        ).catch((err) => {
          console.log(err)
        })
    },
    selectDialog(item) {
      this.Open_item = item;
    },
    closeDialog() {
      this.Open_item = ''

    },
    addTask() {
      if (this.newTaskTitle.length < 1) {
        return
      }
      let newTask = {
        id: Date.now(),
        title: this.newTaskTitle,
        done: false
      };
      axios.post(process.env.FLASK_HOST + '/create',
        {
          user_id: 1,
          task_name: this.newTaskTitle
        }
      ).then((res) => {
        this.tasks.push(newTask);
        this.newTaskTitle = ''
        this.snackbar = true;
      }).catch((err)=> {
        console.log(err)
      })
    },
    doneTask(id) {
      let task = this.tasks.filter(task => task.id === id)[0]
      task.done = !task.done
    },
    deleteTask(id) {
      this.tasks = this.tasks.filter(task => task.id !== id)
    },
    todoDay() {
      const d = new Date();
      const days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
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
    }
  },
  filters: {
    capitalize: function (value) {
      if (!value) return "";
      value = value.toString();
      return value.charAt(0).toUpperCase() + value.slice(1);
    }
  },
  created: function() {
    // TODO: fix
    this.user_id = 1
    axios.get(process.env.FLASK_HOST + '/list')
    .then(res => {
      console.log(this.tasks)
      console.log('res', res)
      // tasksは配列
      // this.tasks = res.data.tasks
    }).catch(err => {
      console.log('err')
      let newTask = {
        id: Date.now(),
        title: "sample",
        done: false
      };
      this.tasks.push(newTask);
    })
  }
}
</script>>