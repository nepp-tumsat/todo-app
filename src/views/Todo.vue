<template>
  <div class='home'>
    <v-list
      class="pt-0"
      flat
    >
      <div
        v-for="task in tasks"
        :key="task.id"
      >
        <v-list-item>
          <template v-slot:default="{ active, }">
            <v-list-item-action>
              <v-checkbox
                :input-value="active"
                color="primary"
              ></v-checkbox>
            </v-list-item-action>

            <v-list-item-content>
              <v-list-item-title>{{ task.title }}</v-list-item-title>
            </v-list-item-content>
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
      tasks: [
        {
          id: 1,
          title: 'Wake up '
        },
        {
          id: 2,
          title: 'Get bananas'
        },
        {
          id: 3,
          title: 'Eat bananas'
        }

      ],
    }
  },
  methods: {
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