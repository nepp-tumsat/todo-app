<template>
  <v-card class="pa-md-4 mx-lg-auto" width="800px">
    <v-card-title>
      <div class="mx-n4">
        <span class="text-h4">サブタスクを追加</span>
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
      <v-alert text type="info" v-show="!CanShowList">
        <div>サブタスクはありません</div>
      </v-alert>
      <div v-for="subtask in listing_subtasks" :key="subtask.id">
        <v-list-item :class="{ 'blue lighten-5': subtask.done }">
          <template v-slot:default>
            <!-- <v-list-item-action>
              <v-checkbox
                :input-value="subtask.done"
                color="primary"
              ></v-checkbox>
            </v-list-item-action> -->
            <v-list-item-content>
              <v-list-item-title
                :class="{ '.text-decoration-line-through': subtask.done }"
              >
                {{ subtask.title }}
              </v-list-item-title>
            </v-list-item-content>
            <!-- <v-list-item-action>
              <v-btn @click.stop="deleteTask(subtask.id)" icon>
                <v-icon color="primary lighten-1">mdi-delete</v-icon>
              </v-btn>
            </v-list-item-action> -->
          </template>
        </v-list-item>
        <v-divider></v-divider>
      </div>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="$emit('close')"> Close </v-btn>
      <v-btn
        color="blue darken-1"
        :disabled="!ChangeSubtask"
        text
        @click="send_save_info"
      >
        Save
      </v-btn>
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
      selected_task: this.task,
      ChangeSubtask: false,
    };
  },
  watch: {
    // 2回目のDialog以降に実行される
    task(new_task) {
      this.selected_task = new_task;
      this.ChangeSubtask = false;
    },
  },
  computed: {
    CanShowList() {
      return this.listing_subtasks.length > 0 ? true : false;
    },
    store_subtasks() {
      return this.$store.getters.get_all_subtasks;
    },
    copy_store_subtasks() {
      return this.store_subtasks.map((subtask) => ({
        ...subtask,
      }));
    },
    listing_subtasks() {
      return this.copy_store_subtasks.filter(
        (subtask) => subtask.task_id === this.selected_task.id
      );
    },
  },
  methods: {
    addSubTask() {
      const add_new_subtask = {
        done: false,
        id: Date.now(), //DB追加前の仮ID
        task_id: this.task.id,
        title: this.newSubtaskTitle,
      };
      this.listing_subtasks.push(add_new_subtask);
      this.ChangeSubtask = true;
      this.newSubtaskTitle = "";
    },

    // ここら辺のメソッドあるけど, REST的にはPATCHなので、ここに含めない方がいいかも
    // doneTask(subtask_id) {
    //   let subtask = this.listing_subtasks.filter(
    //     (subtask) => subtask.id === subtask_id
    //   )[0];
    //   subtask.done = !subtask.done;
    //   this.ChangeSubtask = true;
    //   console.log("store subtask", this.$store.state.all_subtasks);
    //   console.log("this.listing_subtask", this.listing_subtasks);
    // },
    // deleteTask(subtask_id) {
    //   this.listing_subtasks = this.listing_subtasks.filter(
    //     (subtask) => subtask.id !== subtask_id
    //   );
    //   this.ChangeSubtask = true;
    // },
    send_save_info() {
      const already_subtask_ids = this.copy_store_subtasks.map((subtask) => {
        return subtask.id;
      });
      const only_added_subtask_arr = this.listing_subtasks.filter(
        (listing_subtask) => !already_subtask_ids.includes(listing_subtask.id)
      );

      const send_subtask_info = {
        task_id: this.task.id,
        subtasks_arr: only_added_subtask_arr,
      };
      this.$emit("add_save", send_subtask_info);
    },
  },
};
</script>
