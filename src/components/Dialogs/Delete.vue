<template>
  <v-card width="270px" class="mx-auto pt-5">
    <v-card-text class="justify-center">
      <span class="text-h6"> Todo Appから退会しますか？</span>
    </v-card-text>
    <v-card-actions class="justify-center">
      <v-btn color="primary" text @click="$emit('delete')"> 退会 </v-btn>
      <v-btn color="primary" text @click="$emit('close')"> キャンセル </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Delete",
};
</script>
