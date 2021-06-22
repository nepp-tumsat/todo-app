<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row justify='center' class="ms-5">
          <v-col xs="12" sm="8">
            <v-card>
              <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title>
                        <v-text-field v-model="newTodo" id="newTodo" name="newTodo" label="Type your task" @keyup.enter="addTodo" />
                      </v-list-item-title>
                      <v-btn
                        color="orange"
                        dark
                        v-bind="attrs"
                        v-on="on"
                      >
                        Register
                      </v-btn>
                    </v-list-item-content>
              </v-list-item>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>