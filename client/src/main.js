import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// global css import
import "./assets/style.css";

// Font Awesome imports
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

// Import specific icons
import { faPhone } from "@fortawesome/free-solid-svg-icons";
import { faEnvelope } from "@fortawesome/free-solid-svg-icons";
import { faLocationDot } from "@fortawesome/free-solid-svg-icons";

// Add icons to the library
library.add(faPhone, faEnvelope, faLocationDot)


const app = createApp(App);

// Register FontAwesomeIcon as a global component
app.component('font-awesome-icon', FontAwesomeIcon
)

app.use(router);
app.mount("#app");
