<template>
<v-app>
  <v-navigation-drawer v-model="drawer" app permanent clipped enable-resize-watcher>
    <v-list>
      <v-container align-center>
        <template v-if="!loginCheck">
          <h3 class="text-xs-center mt-3">로그인</h3>
          <div class="pa-3 mt-3  elevation-1">
            <v-text-field v-model="form.Id" label="ID">
            </v-text-field>
            <v-text-field v-model="form.Pw" label="PASSWORD" type="password">
            </v-text-field>
            <v-btn large block dark color="#F1C40F" class="black--text font-weight-bold" @click="login()">로그인</v-btn>
            <v-btn large block dark color="#F1C40F" class="black--text font-weight-bold" @click="signInPage()">회원가입</v-btn>
          </div>
        </template>
        <template v-if="loginCheck">
          <h3 class="text-xs-center mt-3">회원정보</h3>
          <div class="pa-3 mt-3 elevation-1">
            <v-layout row>
              <v-flex align-center justify-center layout>
                <v-avatar :size="50" color="grey lighten-4">
                  <img src="https://vuetifyjs.com/apple-touch-icon-180x180.png" alt="avatar">
                </v-avatar>
              </v-flex>
              <v-flex>
                <h3>{{loginId}}</h3>
                <h4 class="mt-1">
                  <v-icon :size="15">bookmarks</v-icon>
                  <a href="http://localhost:8080/scrap" style="color:gray">
                    스크랩
                  </a>
                </h4><br>
              </v-flex>
            </v-layout>
            <v-btn large block dark color="#F1C40F" class="black--text font-weight-bold" @click="logout()">로그아웃</v-btn>
          </div>
        </template>
      </v-container>
      <h3 class="text-xs-center mt-3">새로운 알림</h3>
      <v-container align-center>
        <v-flex mb-3 v-for="i in 4" :key="i" xm12 sm12 xl12>
          <v-card color="#FFFFFCC" class="white--text elevation-2" height="50px">
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
          </v-card>
        </v-flex>
      </v-container>
    </v-list>
  </v-navigation-drawer>
  <v-toolbar app color="#2C3E50">
    <!-- <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon> -->
    <v-toolbar-title class="cyan--text"><a href="http://localhost:8080/main">JABARA JOB</a></v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-menu bottom left>
        <v-btn icon slot="activator">
          <v-icon>more_vert</v-icon>
        </v-btn>
      </v-menu>
    </v-toolbar-items>
  </v-toolbar>
  <v-content>
    <router-view />
  </v-content>
</v-app>
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  data() {
    return {
      drawer: null,
      form: {
        Id: '',
        Pw: ''
      },
      loginCheck: false,
      title: this.$apiRootPath,
      loginId: ''
    }
  },
  mounted() {
    if (sessionStorage.getItem('token') != null) {
      this.loginCheck = true
      this.loginId = sessionStorage.getItem('loginId')
    } // zerocho
  },
  methods: {
    login() {
      axios.post('http://localhost:3303/findone', this.form)
        .then(r => {
          sessionStorage.setItem('token', r.data.token) //로컬스토리지에 토큰값 저장
          sessionStorage.setItem('loginId', r.data.token.id) //로컬스토리지에 토큰값 저장
          this.loginId = r.data.token.id
          this.loginCheck = true
        })
        .catch(e => console.error(e.message))
    },
    logout() {
      sessionStorage.removeItem('token');
      sessionStorage.removeItem('loginId');
      this.loginCheck = false
    }
  }
}
</script>
<style type="text/css">
 a:link { color:#00BCD4; text-decoration: none;}
 a:visited { color: #00BCD4; text-decoration: none;}
</style>
