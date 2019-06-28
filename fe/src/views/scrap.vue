<template>
<v-layout align-center justify-center ml-4>
  <v-flex xs12 sm12>
    <h1 class="ml-4 mt-5">스크랩</h1>
    <v-card class="mr-2 ml-2 mb-4 mt-2">
      <v-layout row wrap>
        <v-flex ml-5 xs4 sm4>
          <v-text-field v-model="search" label="Search" required></v-text-field>
        </v-flex>
        <v-flex mt-3>
          <v-btn flat color="orange">검색</v-btn>
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
