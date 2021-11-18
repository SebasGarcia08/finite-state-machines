<template>
  <div>
    <b-table hover :items="transitions"></b-table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      transitions: [
        {age: 40, first_name: 'Dickerson', last_name: 'Macdonald'},
        {age: 21, first_name: 'Larsen', last_name: 'Shaw'},
        {
          age: 89,
          first_name: 'Geneva',
          last_name: 'Wilson',
          _rowVariant: 'danger'
        },
        {
          age: 40,
          first_name: 'Thor',
          last_name: 'MacDonald'
        },
        {age: 29, first_name: 'Dick', last_name: 'Dunlap'}
      ]
    }
  }
}
</script>
