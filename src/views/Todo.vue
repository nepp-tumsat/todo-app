<template>
  <div class='home pa-6'>
    <h1>Todo Page</h1>
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
      todos: [
        {
          title: 'Sample',
          done: false
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