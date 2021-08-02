<template>
  <v-card class="pa-md-4 mx-lg-auto" width="800px">
    <v-card-title>
      <span class="text-h3">タスクの編集</span>
    </v-card-title>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-card-text>
        <v-text-field
          v-model="selected_task.title"
          label="タスク名"
          :rules="all_task_Rules"
        ></v-text-field>
        <div class="text-h8">サブタスクリスト</div>
        <v-alert text type="info" v-show="!CanShowList">
          <div>サブタスクはありません</div>
        </v-alert>
        <div
          v-show="CanShowList"
          v-for="subtask in listing_subtasks"
          :key="subtask.id"
        >
          <v-list-item>
            <template v-slot:default>
              <v-list-item-content>
                <v-text-field
                  v-model="subtask.title"
                  label="サブタスク名"
                  :rules="all_task_Rules"
                ></v-text-field>
              </v-list-item-content>
            </template>
          </v-list-item>
        </div>
      </v-card-text>
    </v-form>
    <v-alert text type="error" v-show="show_alert">
      <div>入力に誤りがあります</div>
    </v-alert>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="$emit('close')"> Close </v-btn>
      <v-btn color="blue darken-1" text @click="save_edit"> Save </v-btn>
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
      valid: true,
      show_alert: false,
      all_task_Rules: [(value) => !!value || "入力必須です"],
      store_subtasks: [],
      listing_subtasks: [],
      selected_task: {},
      sample: "",
    };
  },
  watch: {
    task(new_task) {
      this.selected_task = { ...new_task };
      this.store_subtasks = this.$store.state.all_subtasks;
      // deep copy
      this.copy_store_subtasks = this.store_subtasks.map((subtask) => ({
        ...subtask,
      }));
      this.listing_subtasks = this.copy_store_subtasks.filter(
        (subtask) => subtask.task_id === this.selected_task.id
      );
      this.ChangeSubtask = false;
    },
  },
  computed: {
    CanShowList: function () {
      return this.listing_subtasks.length > 0 ? true : false;
    },
  },
  methods: {
    save_edit() {
      if (!this.valid) {
        this.show_alert = true;
        return;
      }
      // 親に渡すのはタスク名とサブタスク全て
      const send_all_task_info = {
        task_info: this.selected_task,
        subtask_info: this.listing_subtasks,
      };
      console.log(send_all_task_info);
      this.$emit("save", send_all_task_info);
    },
  },
  created: function () {
    this.selected_task = { ...this.task };
    this.store_subtasks = this.$store.state.all_subtasks;
    // deep copy
    this.copy_store_subtasks = this.store_subtasks.map((subtask) => ({
      ...subtask,
    }));
    this.listing_subtasks = this.copy_store_subtasks.filter(
      (subtask) => subtask.task_id === this.selected_task.id
    );
  },
};
</script>

<style scoped>
/deep/ .v-text-field {
  width: 400px;
}
</style>
