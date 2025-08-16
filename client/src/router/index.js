import { createRouter, createWebHistory } from "vue-router"
import CourseDetail from "@/pages/CourseDetail.vue"
import Courses from "@/pages/Courses.vue"
import Dashboard from "@/pages/Dashboard.vue"
import Home from "@/pages/Home.vue"
import LoginRegister from "@/pages/LoginRegister.vue"
import Profile from "@/pages/Profile.vue"
import Quiz from "@/pages/Quiz.vue"

const routes = [
    {path: "/", component: Home},
    {path: "/courses", name: 'Home', component: Courses},
    {path: "/courses/:id", name: 'CourseDetail', component: CourseDetail},
    {path: "/profile", name: 'Profile', component: Profile},
    {path: "/quiz/:id", name: 'Quiz', component: Quiz},
    {path: "/login", name: 'Login', component: LoginRegister},
    {path: "/dashboard", name: 'Dashboard', component: Dashboard},
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;