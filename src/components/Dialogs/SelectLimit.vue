<template>
  <v-date-picker scrollable v-model="date" width="400px">
    <v-spacer></v-spacer>
    <v-btn text color="primary" @click="$emit('close')"> Cancel </v-btn>
    <v-btn text color="primary" @click="select_limit"> OK </v-btn>
  </v-date-picker>
</template>

<script>
export default {
  name: "SelectLimit",
  props: {
    task: {
      type: Object,
      require: true,
    },
  },
  data() {
    return {
      date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
        .toISOString()
        .substr(0, 10),
      selected_task: this.task,
    };
  },
  methods: {
    select_limit() {
      this.selected_task.limit_at = this.date;
      this.$emit("select_limit", this.selected_task);
    },
  },
};
</script>
