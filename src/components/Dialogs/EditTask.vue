<template>
  <v-card class="pa-md-4 mx-lg-auto" width="800px">
    <v-card-title>
      <span class="text-h3">タスクの編集</span>
    </v-card-title>
    <v-card-text>
      <v-text-field v-model="task_title" label="タスク名"></v-text-field>
      <div class="text-h8">サブタスクリスト</div>
      <v-alert text type="info" v-show="!show_list">
        <div>サブタスクはありません</div>
      </v-alert>
      <div v-show="show_list" v-for="sample in sample_list" :key="sample.id">
        <v-list-item>
          <template v-slot:default>
            <v-list-item-content>
              <v-text-field
                v-model="sample.title"
                label="サブタスク名"
              ></v-text-field>
            </v-list-item-content>
          </template>
        </v-list-item>
      </div>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="$emit('close')"> Close </v-btn>
      <v-btn color="blue darken-1" text @click="$emit('save')"> Save </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "EditTask",
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
      sample_task: {
        id: 1,
        title: "task1",
        done: false,
      },
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
    };
  },
  computed: {
    task_title: function () {
      return this.task.title;
    },
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
    doneTask(task_id) {
      let _task = this.sample_list.filter((task) => task.id === task_id)[0];
      _task.done = !_task.done;
    },
    deleteTask(id) {
      console.log("aaa");
      this.sample_list = this.sample_list.filter((task) => task.id !== id);
    },
  },
};
</script>

<style scoped>
/deep/ .v-text-field {
  width: 400px;
}
</style>
