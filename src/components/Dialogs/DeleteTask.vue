<template>
  <v-card max-width="400">
    <v-card-title></v-card-title>
    <v-card-text> 本当に削除してよろしいですか？ </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="green darken-1" text @click="$emit('close')">
        キャンセル
      </v-btn>
      <v-btn color="green darken-1" textx @click="$emit('close')"> 削除 </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "DeleteTask",
};
</script>
