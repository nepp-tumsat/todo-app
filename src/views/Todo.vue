<template>
  <div class='home'>
    <v-text-field
      v-model="newTaskTitle"
      @click:append="addTask"
      @keyup.enter="addTask"
      class="pa-3"
      outlined
      label="Add Task"
      append-icon="mdi-plus"
      hide-details
      clearable
    ></v-text-field>
    <v-list
      class="pt-0"
      flat
    >
      <div
        v-for="task in tasks"
        :key="task.id"
      >
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
              <v-btn
                @click.stop="deleteTask(task.id)"
                icon
              >
                <v-icon color="primary lighten-1">mdi-delete</v-icon>
              </v-btn>
          </v-list-item-action>
          </template>
        </v-list-item>
        <v-divider></v-divider>
      </div>

    </v-list>
  </div>
</template>>

<script>
import axios from 'axios'
export default {
  name: 'Todo',
  // createdでデータベースを読み込んでリスティングする
  data() {
    return {
      dialog: false,
      day: this.todoDay(),
      date: new Date().getDate(),
      ord: this.nth(new Date().getDate()),
      year: new Date().getFullYear(),
      newTaskTitle: '',
      tasks: [
        // {
        //   id: 1,
        //   title: 'Wake up ',
        //   done: false
        // },
        // {
        //   id: 2,
        //   title: 'Get bananas',
        //   done: false
        // },
        // {
        //   id: 3,
        //   title: 'Eat bananas',
        //   done: false
        // }

      ],
    }
  },
  methods: {
    addTask() {
      let newTask = {
        id: Date.now(),
        title: this.newTaskTitle,
        done: false
      };
      this.tasks.push(newTask);
      this.newTaskTitle = ''
    },
    doneTask(id) {
      let task = this.tasks.filter(task => task.id === id)[0]
      task.done = !task.done
    },
    deleteTask(id) {
      this.tasks = this.tasks.filter(task => task.id !== id)
    },
    removeTodo() {
      console.log('REMOVE TODO!')
      this.todos = []
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
    axios.get(process.env.FLASK_HOST + '/list')
    .then(res => {
      console.log('')
    }).catch(err => {
      console.log('err')
    })
  }
}
</script>>