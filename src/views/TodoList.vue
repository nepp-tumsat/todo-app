<template>
  <v-app>
      <v-container class="mt-12">
        <v-row class="mt-6" justify="center">
          <v-data-table :headers="tableHeaders" :items="tableItems"></v-data-table>
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
  data() {
    return {
      dialog: false,
      tableHeaders: [
        { text: "Name", value: "name" },
        { text: "Age", value: "age" },
        { text: "Gender", value: "gender" }
      ],
      tableItems: [
        { name: "Taro", age: 20, gender: "Male" },
        { name: "Hanako", age: 18, gender: "Female" },
        { name: "Ichiro", age: 25, gender: "Male" }
      ]
    }
  }
}
</script>>