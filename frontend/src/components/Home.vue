<template lang="html">
  <div>
    <Navbar />
    <br>
    <div class="container">
      <b-card title="Definition" bg-variant="light">
        <b-card-text>
          <StatementIntro/>
        </b-card-text>
      </b-card>
      <br>
      <b-card title="Input format" bg-variant="light">
        <StatementInput/>
      </b-card>
      <br>
      <b-form-textarea
        id="textarea"
        placeholder="Enter something..."
        rows="10"
        max-rows="6"
      ></b-form-textarea>
      <br>
      <b-card title="Output format" bg-variant="light">
        <StatementOutput/>
      </b-card>
      <br>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import StatementInput from './StatementInput'
import StatementOutput from './StatementOutput'
import StatementIntro from './StatementIntro'
import Navbar from './Navbar'

export default {
  name: 'Home',
  components: {
    StatementInput,
    StatementOutput,
    Navbar,
    StatementIntro
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
      message: 'New message from Vue'
    }
  }
}
</script>
