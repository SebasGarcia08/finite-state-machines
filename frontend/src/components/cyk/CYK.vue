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
import axios from "axios";

export default {
  name: "CYK",
  components: { Navbar, StatementInput, StatementOutput, StatementIntro },
  methods: {
    solve() {
      axios
        .post("http://localhost:5000/api/v1.0/cyk/solve", {
          input: this.input
        })
        .then(response => {
          this.solution = response.data;
        })
        .catch(err => alert(err));
    }
  },
  data() {
    return {
      input:
        "2\n" +
        "baaba\n" +
        "S\n" +
        "S A B C\n" +
        "a b\n" +
        "S -> AB | BC\n" +
        "A -> BA | a\n" +
        "B -> CC | b\n" +
        "C -> AB | a\n" +
        "aaabbbcc\n" +
        "S\n" +
        "S A B C D E F\n" +
        "a b c\n" +
        "S -> AB\n" +
        "A -> CD | CF\n" +
        "B -> c | EB\n" +
        "C -> a\n" +
        "D -> b\n" +
        "E -> c\n" +
        "F -> AD\n",
      solution: ""
    };
  }
};
</script>
