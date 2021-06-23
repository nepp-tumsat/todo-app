<template>
  <v-app>
      <v-container class="mt-12">
        <v-row class="mt-6" justify="center">
          <v-list subheader two-line flat>
            <v-subheader class="subheading" v-if="todos.length == 0">You have 0 Tasks, add some</v-subheader>
            <v-subheader class="subheading" v-else="todos.length == 1">Your Tasks</v-subheader>

            <v-list-item-group>
              <v-list-item v-for="(todo, i) in todos">
                <template #default="{ active, toggle }">
                  <v-list-item-action>

                    <v-checkbox v-model="active" @click="toggle"></v-checkbox>
                  </v-list-item-action>

                  <v-list-item-content>
                    <v-list-item-title :class="{
                      done: active
                      }">{{ todo.title | capitalize }}
                    </v-list-item-title>
                    <v-list-item-subtitle>Added on: {{ date }}{{ ord }} {{ day }} {{ year }}</v-list-item-subtitle>
                  </v-list-item-content>
                  <v-btn fab ripple small color="red" v-if="active" @click="removeTodo(i)">
                    <v-icon class="white--text">mdi-close</v-icon>
                  </v-btn>
                </template>
              </v-list-item>
            </v-list-item-group>

          </v-list>
        </v-row>
        <v-row class="mt-6" justify="center">
          <v-btn to="/create" active-class="blue">
            <v-icon
              dark
              left
            >
            mdi-clipboard-plus
            </v-icon>
          to Register
          </v-btn>
          <v-
          <v-dialog
            v-model="dialog"
            persistent
            max-width="600px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="primary"
                dark
                v-bind="attrs"
                v-on="on"
              >
                Show Detail
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">Task</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        label="Task Name"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        label="Limit Date"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12">
                      <div>サブタスク</div>
                      <v-text-field
                        label="ここにサブタスクをボタンで表示"
                        required
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="dialog = false"
                >
                  Close
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="dialog = false"
                >
                  Save
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'TodoList',
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
  }
}
</script>>