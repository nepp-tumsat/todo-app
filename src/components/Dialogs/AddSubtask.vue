<template>
  <v-card class="pa-md-4 mx-lg-auto" width="800px">
    <v-card-title>
      <div class="mx-n4">
        <span class="text-h4">サブタスク追加</span>
      </div>
    </v-card-title>
    <v-card-text>
      <div class="py-2">
        <span class="text-h5">TASK: {{ task.title }}</span>
      </div>
      <div>
        <v-text-field
          class="ma-10"
          v-model="newSubtaskTitle"
          label="Add subtask"
          @click:append="addSubTask"
          @keydown.enter="addSubTask"
          append-icon="mdi-plus"
        >
        </v-text-field>
      </div>
      <div class="text-h8">サブタスクリスト</div>
      <v-alert text type="info" v-show="!show_list">
        <div>サブタスクはありません</div>
      </v-alert>
      <div v-show="show_list" v-for="task in sample_list" :key="task.id">
        <v-list-item
          @click="doneTask(task.id)"
          :class="{ 'blue lighten-5': task.done }"
        >
          <template v-slot:default>
            <v-list-item-action>
              <v-checkbox :input-value="task.done" color="primary"></v-checkbox>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title
                :class="{ '.text-decoration-line-through': task.done }"
              >
                {{ task.title }}
              </v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-btn @click.stop="deleteTask(task.id)" icon>
                <v-icon color="primary lighten-1">mdi-delete</v-icon>
              </v-btn>
            </v-list-item-action>
          </template>
        </v-list-item>
        <v-divider></v-divider>
      </div>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="$emit('close')"> Close </v-btn>
      <v-btn color="blue darken-1" text @click="$emit('addsave')"> Save </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "AddSubtask",
  props: {
    task: {
      type: Object,
      require: true,
    },
  },
  data() {
    return {
      newSubtaskTitle: "",
      subtask_Rules: [
        (v) => !!v || "subtask is required",
        (v) => (v && v.length <= 0) || "subtask must be less than 0 characters",
      ],
      sample_list: [
        {
          id: 1,
          title: "sample1",
          done: false,
        },
        {
          id: 2,
          title: "sample2",
          done: false,
        },
      ],
      dummy_id: 2,
    };
  },
  computed: {
    show_list: function () {
      return this.sample_list.length > 0 ? true : false;
    },
  },
  methods: {
    list_subtask() {
      this.sub_tasks = [
        {
          title: "sample1",
        },
      ];
    },
    addSubTask() {
      const new_subtask = {
        title: this.newSubtaskTitle,
        id: this.dummy_id + 1,
        done: false,
      };
      this.sample_list.push(new_subtask);
      this.newSubtaskTitle = "";
      this.dummy_id += 1;
    },
    doneTask(task_id) {
      let task = this.sample_list.filter((task) => task.id === task_id)[0];
      task.done = !task.done;
    },
    deleteTask(id) {
      console.log("aaa");
      this.sample_list = this.sample_list.filter((task) => task.id !== id);
    },
  },
};
</script>
