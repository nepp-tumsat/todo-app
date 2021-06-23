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
                    </v-list-item-content>
              </v-list-item>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
      <template>
        <v-container
          fluid
          class="pa-0"
        >
          <v-row justify="center">
            <v-col
              cols="12"
              sm="6"
            >
              <div class="text-center">
                <div class="my-2">
                  <v-btn
                    color="warning"
                    dark
                  >
                  Register
                  </v-btn>
                </div>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </template>
    </v-main>
  </v-app>
</template>