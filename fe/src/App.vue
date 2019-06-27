<template>
<v-app>
  <v-navigation-drawer v-model="drawer" app permanent clipped>
    <v-list >
      <h3 class="text-xs-center mt-3">로그인</h3>
      <div class="pa-3 mt-3  elevation-1">
        <v-text-field v-model="userId" label="ID">
        </v-text-field>
        <v-text-field v-model="userPw" label="PASSWORD" type="password">
        </v-text-field>
        <v-btn large block dark color="#36724F" @click="login()">로그인</v-btn>
      </div>
      <h3 class="text-xs-center mt-3">새로운 알림</h3>
      <v-container align-center>
        <v-flex mb-3 v-for="i in 4" :key="i" xm12 sm12 xl12>
          <v-card color="#FFFFFC" class="white--text elevation-2" height="50px">
            <v-layout row>
              <v-flex xs7>
                <v-card-title primary-title>
                  <div> 
                    <div class="headline">test</div>
                    <div>test test</div>
                  </div>
                </v-card-title>
              </v-flex>
              <v-flex xs5 mt-1>
                <v-img src="https://cdn.vuetifyjs.com/images/cards/halcyon.png" height="40px" contain></v-img>
              </v-flex>
            </v-layout>
            <v-divider dark></v-divider>
          </v-card>
        </v-flex>
      </v-container>
    </v-list>
  </v-navigation-drawer>
  <v-toolbar app dark color="#1F8938">
    <!-- <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon> -->
    <v-toolbar-title class="white--text">JABARA JOB</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-menu bottom left>
        <v-btn icon slot="activator">
          <v-icon>more_vert</v-icon>
        </v-btn>
        <!--
          <v-list>
            <v-list-tile @click="">
              <v-list-tile-title>로그인</v-list-tile-title>
            </v-list-tile>
            <v-list-tile @click="">
              <v-list-tile-title>로그아웃</v-list-tile-title>
            </v-list-tile>
          </v-list>
        -->
      </v-menu>
    </v-toolbar-items>
  </v-toolbar>
  <v-content>
    <router-view />
  </v-content>
</v-app>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      drawer: null,
      userId: '',
      userPw: '',
      title: this.$apiRootPath
    }
  },
  mounted() {},
  methods: {}
}
</script>
