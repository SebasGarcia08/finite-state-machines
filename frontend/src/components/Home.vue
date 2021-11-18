<template>
  <div>
    <Navbar />
    <div class="container">
      <b-card bg-variant="light" title="Welcome!">
        <b-card-text>
          This is the website developed to explain copmuting thory algorithms.
          Click "Menu" to see options.
        </b-card-text>
      </b-card>
    </div>
  </div>
</template>
<script>
import Navbar from "./Navbar";

export default {
  name: "Home",
  components: { Navbar }
};
</script>
