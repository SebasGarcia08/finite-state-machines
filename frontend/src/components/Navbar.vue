<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <div class="container">
        <b-navbar-brand class="mb-1"> Automatron </b-navbar-brand>
        <Sidebar />
      </div>
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
