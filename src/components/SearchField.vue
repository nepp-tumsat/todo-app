<template>
  <div>
    <v-btn
      v-if="!searching && $store.state.loggedIn"
      @click="searching = true"
      icon
    >
      <v-icon>mdi-magnify</v-icon>
    </v-btn>

    <v-text-field
      v-if="searching"
      v-model="search_word"
      v-click-outside="onClickOutsideStandard"
      prepend-inner-icon="mdi-magnify"
      autofocus
      outlined
    />
  </div>
</template>

<script>
export default {
  name: "SearchField",
  data: () => ({
    searching: false,
    search_word: "",
  }),
  watch: {
    search_word(new_word) {
      this.$store.commit("search", new_word);
    },
  },
  methods: {
    onClickOutsideStandard() {
      // v-click-outsideに式を渡しても代入されなかった
      this.searching = false;

      this.search_word = "";
      this.$store.commit("search", "");
    },
  },
};
</script>

<style scoped>
/deep/ .v-text-field {
  width: 500px;
}
</style>
