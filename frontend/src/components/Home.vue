<template lang="html">
  <div>
    <h1>Automata converter</h1>
    <StatementInput />
    <TableEditablePage />
    <StatementOutput />
    <br>
  </div>
</template>

<script>
import axios from 'axios'
import StatementInput from './StatementInput'
import StatementOutput from './StatementOutput'
import TableEditablePage from './TableEditablePage'

export default {
  name: 'Home',
  components: {
    StatementInput,
    StatementOutput,
    TableEditablePage
  },
  methods: {
    getMessage () {
      const path = 'http://localhost:5000/api/v1.0/message'
      axios.get(path).then((res) => {
        this.message = res.data
      }).catch((err) => console.log(err))
    }
  },
  created () {
  },
  data () {
    return {
      message: 'New message from Vue',
    }
  }
}
</script>
