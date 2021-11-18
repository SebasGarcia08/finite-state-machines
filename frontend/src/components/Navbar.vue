<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <Sidebar />
      <b-navbar-brand class="mb-0"> Automata converter</b-navbar-brand>
    </b-navbar>
  </div>
</template>
<script>
import Sidebar from "./Sidebar";
export default {
  components: { Sidebar },
  name: "Navbar"
};
</script>
