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
      <!-- <v-alert text type="info" v-show="!show_list">
        <div>サブタスクはありません</div>
      </v-alert> -->
      <div v-for="sub_task in sub_tasks" :key="sub_task.id">
        <v-list-item
          @click="doneTask(sub_task.id)"
          :class="{ 'blue lighten-5': sub_task.done }"
        >
          <template v-slot:default>
            <v-list-item-action>
              <v-checkbox
                :input-value="sub_task.done"
                color="primary"
              ></v-checkbox>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title
                :class="{ '.text-decoration-line-through': sub_task.done }"
              >
                {{ sub_task.sub_task }}
              </v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-btn @click.stop="deleteTask(sub_task.id)" icon>
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
import axios from "axios";

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
      sub_tasks: [],
      dummy_id: 2,
    };
  },
  computed: {
    // show_list: function () {
    //   console.log(this.sub_tasks);
    //   return this.sub_tasks.length > 0 ? true : false;
    // },
    sub_tasks_obj: function () {
      return this.$store.getters.get_all_subtasks_obj;
    },
  },
  watch: {
    task() {
      this.sub_tasks = this.sub_tasks_obj[this.task.id];
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
      // task_idがあればsubtaskを追加可能
      axios
        .post(process.env.FLASK_HOST + "/task/" + this.task.id + "/subtask", {
          subtask_name: this.newSubtaskTitle,
          user_id: this.$store.state.user_id,
        })
        .then((res) => {
          const new_subtask = res.data;
          console.log(new_subtask);
          π;
          console.log("type", typeof new_subtask);
          console.log("subtask_id", new_subtask.id);
          this.sub_tasks.push({
            id: new_subtask.id,
            title: new_subtask.sub_task,
            done: new_subtask.done,
          });
        })
        .catch((err) => {
          console.log("err", err);
        });
    },
    doneTask(task_id) {
      let task = this.sample_list.filter((task) => task.id === task_id)[0];
      task.done = !task.done;
    },
    deleteTask(id) {
      this.sample_list = this.sample_list.filter((task) => task.id !== id);
    },
  },
  created: function () {
    this.sub_tasks = this.sub_tasks_obj[this.task.id];
  },
};
</script>
