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
  data() {
    return {
      date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
        .toISOString()
        .substr(0, 10),
    };
  },
  methods: {
    select_limit() {
      this.$emit("select_limit", this.date);
    },
  },
};
</script>