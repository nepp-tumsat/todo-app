<template>
  <v-card max-width="400">
    <v-card-title></v-card-title>
    <v-card-text>
      タスク「{{ task_title }}」 を削除してよろしいですか？
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="green darken-1" text @click="$emit('close')">
        キャンセル
      </v-btn>
      <v-btn color="green darken-1" text @click="$emit('delete')"> 削除 </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "DeleteTask",
  props: {
    task_title: {
      type: String,
    },
  },
};
</script>
