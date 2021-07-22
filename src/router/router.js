import Vue from "vue";
import Router from "vue-router";
import Store from "../store/index.js";
import Todo from "../views/Todo.vue";
import About from "../views/About.vue";
import Login from "../views/Login.vue";

Vue.use(Router);

const router = new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "Todo",
      component: Todo,
      meta: { requiresAuth: true },
    },
    {
      path: "/about",
      name: "About",
      component: About,
      meta: { requiresAuth: true },
    },
    {
      path: "/login",
      name: "Login",
      component: Login,
    },
  ],
});

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requiresAuth) &&
    !Store.state.loggedIn
  ) {
    next({ path: "/login", query: { redirect: to.fullPath } });
  } else {
    next();
  }
});

export default router;
