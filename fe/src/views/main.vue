<template>
<v-layout align-center justify-center ml-4>
  <v-flex xs12 sm12>
<h1 class="ml-4 mt-5">채용공고</h1>
    <v-card class="mr-2 ml-2 mb-4 mt-2">
      <v-layout row wrap>
        <v-flex ml-5 xs3 sm3>
          <v-text-field v-model="search" label="Search" required></v-text-field>
        </v-flex>
        <v-flex mt-3>
          <v-btn flat color="orange">검색아이콘</v-btn>
        </v-flex>
      </v-layout>
      <v-layout row>
        <v-flex ml-5 mt-4 xs1><h3>필터링</h3></v-flex>
        <v-flex  ml-1 xs2 sm2 md1 lg1 xl1 d-flex class="mr-1">
          <v-select :items="items" label="직무"></v-select>
        </v-flex>
        <v-flex  ml-5 xs2 sm2 md1 lg1 xl1 d-flex class="mr-1">
          <v-select :items="items" label="근무지역"></v-select>
        </v-flex>
        <v-flex  ml-5 xs2 sm2 md1 lg1 xl1 d-flex class="mr-1">
          <v-select :items="items" label="기업형태"></v-select>
        </v-flex>
        <v-flex mt-3>
          <v-btn flat color="orange">상세검색</v-btn>
        </v-flex>
      </v-layout>
      <v-container fluid grid-list-sm>
        <v-layout row wrap>
          <v-flex v-for="i in 6" :key="i" xs6 sm6>
            <v-card>
              <v-img src="https://cdn.vuetifyjs.com/images/cards/desert.jpg" aspect-ratio="2.75"></v-img>
              <v-card-title primary-title>
                <div>
                  <h3 class="headline mb-0">Kangaroo Valley Safari</h3>
                  <div> {{ card_text }} </div>
                </div>
              </v-card-title>

              <v-card-actions>
                <v-btn flat color="orange">Share</v-btn>
                <v-btn flat color="orange">Explore</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
      <v-footer class="mt-5"></v-footer>
    </v-card>
  </v-flex>
</v-layout>
</template>
<script>
export default {
  name: 'App',
  data() {
    return {

    }
  },
  mounted() {},
  methods: {}
}
</script>
