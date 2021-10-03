<template>
  <mdb-container>
    <mdb-card>
      <h3 class="card-header stylish-color white-text text-center font-weight-bold text-uppercase py-4">
        Editable table
      </h3>
      <mdb-card-body>
        <mdb-table-editable
          :columns="columns"
          :rows="rows"
          class="text-center"
          striped
          bordered
          responsive
          pagination
          :display="3"
          :entries="5"
        />
      </mdb-card-body>
    </mdb-card>
  </mdb-container>
</template>

<script>
import {mdbTableEditable, mdbCard, mdbCardBody, mdbContainer} from 'mdbvue';

export default {
  name: 'TableEditablePage',
  components: {
    'mdb-table-editable': mdbTableEditable,
    'mdb-card': mdbCard,
    'mdb-card-body': mdbCardBody,
    'mdb-container' : mdbContainer
  },
  data() {
    return {
      columns: [
        {
          label: 'Name',
          field: 'name',
        },
        {
          label: 'Position',
          field: 'position',
        },
        {
          label: 'Office',
          field: 'office',
        },
        {
          label: 'Age',
          field: 'age',
        },
        {
          label: 'Start date',
          field: 'date',
          sort: 'asc'
        },
        {
          label: 'Salary',
          field: 'salary',
        }
      ],
      rows: [
        {
          name: 'Tiger Nixon',
          position: 'System Architect',
          office: 'Edinburgh',
          age: '61',
          date: '2011/04/25',
          salary: '$320'
        },
        {
          name: 'Garrett Winters',
          position: 'Accountant',
          office: 'Tokyo',
          age: '63',
          date: '2011/07/25',
          salary: '$170'
        },
        {
          name: 'Ashton Cox',
          position: 'Junior Technical Author',
          office: 'San Francisco',
          age: '66',
          date: '2009/01/12',
          salary: '$86'
        },
        {
          name: 'Cedric Kelly',
          position: 'Senior Javascript Developer',
          office: 'Edinburgh',
          age: '22',
          date: '2012/03/29',
          salary: '$433'
        }
      ]
    };
  }
}
</script>
