<template>
  <div>
    <Navbar></Navbar>
    <br />
    <div class="container">
      <b-card title="Definition" bg-variant="light">
        <b-card-text>
          <StatementIntro />
        </b-card-text>
      </b-card>
      <br />
      <b-card title="Input format" bg-variant="light">
        <StatementInput />
      </b-card>
      <br />
      <b-form-textarea
        v-model="input"
        id="textarea"
        placeholder="Enter something..."
        rows="10"
        max-rows="6"
      ></b-form-textarea>
      <br />
      <b-card title="Output format" bg-variant="light">
        <StatementOutput />
      </b-card>
      <b-button
        @click="solve()"
        class="justify-content-center"
        block
        variant="success"
        >Solve!
      </b-button>
      <b-card title="Solution" bg-variant="light">
        <b-form-textarea
          plaintext
          :value="solution"
          max-rows="1000"
          id="solution-textarea"
        ></b-form-textarea>
      </b-card>
      <br />
    </div>
  </div>
</template>
<script>
import Navbar from "../Navbar.vue";
import StatementInput from "./StatementInput";
import StatementOutput from "./StatementOutput";
import StatementIntro from "./StatementIntro";

export default {
  name: "CYK",
  components: { Navbar, StatementInput, StatementOutput, StatementIntro }
};
</script>
