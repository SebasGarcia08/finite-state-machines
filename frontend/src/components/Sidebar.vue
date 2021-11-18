<template>
  <div>
    <b-button v-b-toggle.sidebar-no-header>Menu</b-button>
    <b-sidebar
      id="sidebar-no-header"
      aria-labelledby="sidebar-no-header-title"
      no-header
      shadow
    >
      <template #default="{ hide }">
        <div class="p-3">
          <h4 id="sidebar-no-header-title">Options</h4>
          <p>
            Algorithms available:
          </p>
          <nav class="mb-3">
            <b-nav vertical>
              <b-nav-item active href="/fsm" @click="hide"
                >Finite State Machine partitoning</b-nav-item
              >
              <b-nav-item href="/cyk" @click="hide">CYK</b-nav-item>
            </b-nav>
          </nav>
          <b-button variant="primary" block @click="hide">Close</b-button>
        </div>
      </template>
    </b-sidebar>
  </div>
</template>
<script>
export default {
  name: "Sidebar"
};
</script>
