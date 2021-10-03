<template>
  <div>
    <ul>
      <li><b>S</b> is a finite input alphabet,</li>
      <br/>
      <li><b>R</b> is a finite output alphabet and</li>
      <br/>
      <li><b>Q</b> is a set of states.</li>
      <br/>
    </ul>
    <h2>Input</h2>
    <ul>
      <li>
        <b>N</b>: the number of tests cases
      </li>
      <br>
      <li>
        <b>M</b>: The type of machine. (S or T)
        S for State-assigned (Moore), T for transition-assigned (Mealy)
        <br>
      </li>
      <br>
      <li>
        <b>S</b>: input alphabet separated by spaces
      </li>
      <br/>
      <li>
        <b>R</b>: Output alphabet separated by spaces
      </li>
      <br>
      <li>
        <b>Q</b>: set of states separated by spaces
      </li>
      <br/>
      <li>
        <b>Q0</b>: Initial state
      </li>
      <br/>
      <li>
        <b>Transition table of shape:</b>
        <br>
        |Q| by 2|S| + 1 for Mealy Machines and
        <br>
        |Q| by |S| + 1 for Moore Machines
        <br>
        where each row is separated by spaces
      </li>
      <br/>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Statement'
}
</script>
