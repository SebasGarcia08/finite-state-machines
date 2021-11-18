<template lang="html">
  <div>
    <Navbar />
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
import axios from "axios";
import StatementInput from "./StatementInput";
import StatementOutput from "./StatementOutput";
import StatementIntro from "./StatementIntro";
import Navbar from "./Navbar";
import TransitionTable from "./TransitionTable";

export default {
  name: "Home",
  components: {
    StatementInput,
    StatementOutput,
    Navbar,
    StatementIntro,
    TransitionTable
  },
  methods: {
    solve() {
      axios
        .post("http://localhost:5000/api/v1.0/solve", { input: this.input })
        .then(res => (this.solution = res.data))
        .catch(err => console.log(err));
    }
  },
  created() {},
  data() {
    return {
      message: "New message from Vue",
      solution: "",
      input:
        "5\n" +
        "S\n" +
        "0 1\n" +
        "0 1\n" +
        "A B C D E F\n" +
        "A B D 0\n" +
        "B C E 1\n" +
        "C B F 0\n" +
        "D E A 0\n" +
        "E F B 0\n" +
        "F E C 0\n" +
        "T\n" +
        "a b\n" +
        "0 1 2 3\n" +
        "A B C D\n" +
        "A B 1 C 2\n" +
        "B C 2 D 3\n" +
        "C D 3 A 0\n" +
        "D A 0 B 1\n" +
        "T\n" +
        "a b\n" +
        "0 1 2 3\n" +
        "E F G H I J\n" +
        "E F 1 G 2\n" +
        "F G 2 H 3\n" +
        "G H 3 I 0\n" +
        "H I 0 F 1\n" +
        "I F 1 G 2\n" +
        "J E 0 I 0\n" +
        "T\n" +
        "0 1\n" +
        "0 1\n" +
        "D E F G H\n" +
        "D E 0 D 0\n" +
        "E D 0 F 1\n" +
        "F F 1 D 0\n" +
        "G E 0 H 1\n" +
        "H D 1 G 0\n" +
        "T\n" +
        "0 1\n" +
        "0 1\n" +
        "A B C\n" +
        "A B 0 A 0\n" +
        "B A 0 C 1\n" +
        "C C 1 A 0"
    };
  }
};
</script>
