<template lang="html">
  <div>
    <p>{{ message }} </p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Main',
  methods: {
    getMessage () {
      const path = 'http://localhost:5000/api/v1.0/message'
      axios.get(path).then((res) => {
        this.message = res.data
      }).catch((err) => console.log(err))
    }
  },
  created () {
    this.getMessage()
  },
  data () {
    return {
      message: 'New message from Vue'
    }
  }
}
</script>
