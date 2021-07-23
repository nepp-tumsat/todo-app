<template>
  <v-snackbar v-model="show" multi-line timeout="2000">
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
  data() {
    return {
      show: false,
    };
  },
  watch: {
    show_snackbar: function (newval, oldval) {
      this.show = this.show_snackbar;
    },
    show: function (newval, oldval) {
      // 閉じる時
      if (!newval) {
        this.$emit("close");
      }
    },
  },
};
</script>