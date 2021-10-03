<template>
  <div>
    <ul>
      <li>S is a finite input alphabet,</li>
      <br/>
      <li>R is a finite output alphabet and</li>
      <br/>
      <li>Q is a set of states.</li>
      <br/>
    </ul>
    <h2>Input</h2>
    <ul>
      <li>
        n: the number of tests cases
      </li>
      <br/>
      <li>
        |S|: Length of input alphabet
      </li>
      <br/>
      <li>
        S: input alphabet separated by spaces
      </li>
      <br/>
      <li>
        |R|: Length of output alphabet
      </li>
      <br/>
      <li>
        R: Output alphabet separated by spaces
      </li>
      <br/>
      <li>
        |Q|: Cardinality of set of states
      </li>
      <br/>
      <li>
        Q: set of states separated by spaces
      </li>
      <br/>
      <li>
        Q_0: Initial state
      </li>
      <br/>
      <li>
        Transition table of shape |Q| by 2|S| + 1 where each row is separated by spaces
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
