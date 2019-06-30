<template>
<v-layout align-center justify-center mt-4 ml-4>
  <v-flex xs12 sm12>
    <h1 class="ml-4 mt-4">마이페이지</h1>
    <v-card class="mr-2 ml-2 mb-4 mt-2">
      <v-container grid-list-md ml-4>
        <v-layout row wrap>
          <v-flex xs4 sm4 md4 align-center justify-center layout text-xs-center>
            <v-avatar :tile="tile" :size="150" color="grey lighten-4">
              <img src="https://vuetifyjs.com/apple-touch-icon-180x180.png" alt="avatar">
            </v-avatar>
          </v-flex>
          <v-flex xs5 sm5 md5 align-center justify-center mt-5>
            <h1>ID</h1>
            <h2>Email@Email.com</h2>
              <v-btn color="orange">수정</v-btn>
          </v-flex>
        </v-layout>
      </v-container>
      <v-driven dark></v-driven>
      <v-container>
        <h2 class="ml-2">최근 본 공고</h2>
        <v-layout row wrap mt-4>
          <v-flex v-for="i in 3" :key="i" xs3 sm3 md3 lg3 xl3 mr-4>
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
    </v-card>
  </v-flex>
</v-layout>
</template>
<script>
import axios from 'axios'
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
