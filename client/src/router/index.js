import { createRouter, createWebHistory } from "vue-router";
import About from "@/pages/About.vue";
import Dashboard from "@/pages/Dashboard.vue";
import Home from "@/pages/Home.vue";
import Quiz from "@/pages/Quiz.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/about", name: "About", component: About },
  { path: "/quiz", name: "Quiz", component: Quiz },
  { path: "/dashboard", name: "Dashboard", component: Dashboard },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
