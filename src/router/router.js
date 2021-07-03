import Vue from 'vue'
import Router from 'vue-router'
import Todo from "../views/Todo.vue";
import CreateTodo from "../views/CreateTodo.vue";

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Todo',
      component: Todo
    },
    {
      path: '/create',
      name: 'Create',
      component: CreateTodo
    }
  ]
})