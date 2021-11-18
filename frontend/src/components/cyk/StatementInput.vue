<template>
  <div>
    <ul>
      <li><b>N</b>: the number of tests cases</li>
      <li>
        <b>w</b>: the input string to determine whether it is produced by the
        grammar.
        <br />
      <li><b>S</b>: Start variable</li>
      <li><b>V</b>: Variables separated by spaces</li>
      <li>
        <b>Grammar (in Chomsky Normal Form):</b>
        <br />
        |V|, each variable has a set of productions in the form: variable -> production | production | ...         
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Statement"
};
</script>
