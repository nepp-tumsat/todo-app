<template>
  <v-row justify="center">
    <v-dialog
      v-model="Open_item"
      max-width="290"
    >
      <v-card>
        <v-card-title class="text-h5"></v-card-title>
        <v-card-text>
          本当に削除してよろしいですか？
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="green darken-1"
            text
            @click="$emit('close')"
          >
            キャンセル
          </v-btn>
          <v-btn
            color="green darken-1"
            text
            @click="$emit('close')"
          >
            削除
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  name: 'DeleteTask',
  props: {
    Open_item: String,
    required: true
  }
}
</script>