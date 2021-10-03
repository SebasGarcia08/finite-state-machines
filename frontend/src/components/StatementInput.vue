<template>
  <div>
    <ul>
      <li>
        <b>N</b>: the number of tests cases
      </li>
      <li>
        <b>M</b>: The type of machine. (S or T)
        S for State-assigned (Moore), T for transition-assigned (Mealy)
        <br>
      </li>
      <li>
        <b>S</b>: input alphabet separated by spaces
      </li>
      <li>
        <b>R</b>: Output alphabet separated by spaces
      </li>
      <li>
        <b>Q</b>: set of states separated by spaces, where the first one is the initial state
      </li>
      <li>
        <b>Transition table of shape:</b>
        <br>
        |Q| by 2|S| + 1 for Mealy Machines and
        <br>
        |Q| by |S| + 1 for Moore Machines
        <br>
        where each row is separated by spaces
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Statement'
}
</script>
