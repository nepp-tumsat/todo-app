<template>
  <v-snackbar v-model="show_snackbar" timeout="1000" multi-line>
    {{ message }}
    <template v-slot:action="{ attrs }">
      <v-btn color="pink" text v-bind="attrs" @click="$emit('close')">
        Close
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script>
export default {
  name: "SnackBar",
  props: {
    message: {
      type: String,
      require: true,
    },
    show_snackbar: {
      type: Boolean,
    },
  },
};
</script>