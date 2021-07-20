import Vue from "vue";
import Router from "vue-router";
import Todo from "../views/Todo.vue";
import About from "../views/About.vue";
import Login from "../views/Login.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "Todo",
      component: Todo,
    },
    {
      path: "/about",
      name: "About",
      component: About,
    },
    {
      path: "/login",
      name: "Login",
      component: Login,
    },
  ],
});
