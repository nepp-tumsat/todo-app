import Vue from 'vue'
import Router from 'vue-router'
import TodoList from "../views/TodoList.vue";
import CreateTodo from "../views/CreateTodo.vue";

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'TodoList',
      component: TodoList
    },
    {
      path: '/create',
      // name: 'create',
      component: CreateTodo
    },
    {
      // name: 'edit',
      path: '/edit',
      component: CreateTodo,
      props(route) {
        return {
          ...route.params
        }
      }
    }
  ]
})