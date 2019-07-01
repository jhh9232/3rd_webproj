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
            <v-btn large block dark color="#F1C40F" class="black--text font-weight-bold" @click="signupPage()">회원가입</v-btn>
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
                <div class="mt-1">
                  <v-icon :size="17">bookmarks</v-icon>
                  <a href="http://localhost:8080/scrap" style="color:gray">
                    스크랩
                  </a>
                </div>
                <div>
                  <v-icon :size="17">face</v-icon>
                  <a href="http://localhost:8080/mypage" style="color:gray">
                    마이페이지
                  </a>
                </div><br>
              </v-flex>
            </v-layout>
            <v-btn large block dark color="#F1C40F" class="black--text font-weight-bold" @click="logout()">로그아웃</v-btn>
          </div>
        </template>
      </v-container>
      <h3 class="text-xs-center mt-3">새로운 알림</h3>
      <v-container align-center>
        <template v-if="loginCheck">
          <v-flex mb-3 v-for="item in noticeCompanys" xm12 sm12 xl12>
            <v-card color="#FFFFFCC" class="black--text elevation-2" height="50px" @click="noticeCompanyDetail(item)">
              <v-layout row>
                <v-flex xs9 ml-2 mt-1>
                  <div>{{item.Company_title}}</div>
                  <div><small>{{item.Recruit_title.slice(0,17)}}...</small></div>
                </v-flex>
                <v-flex>
                  <v-btn fab flat small color="orange" @click="noticeCompanyDetail(item)">
                    <v-icon>details</v-icon>
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-card>
          </v-flex>
        </template>
        <template v-if="!loginCheck">
          <v-flex mb-3 xm12 sm12 xl12>
            <v-card color="#FFFFFCC" class="black--text elevation-2" height="50px">
              <v-layout justify-center>
                <div>로그인 후 이용할 수 있습니다.</div>
              </v-layout>
            </v-card>
          </v-flex>
        </template>
      </v-container>
    </v-list>
  </v-navigation-drawer>
  <v-toolbar app color="#2C3E50">
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
  <v-dialog v-model="dialog" max-width="550">
    <v-card class="mr-2 ml-4 mb-4 mt-2 mx-auto" max-width="500" @click="pageLocate()">
      <v-card-title>
        <span class="title headline font-weight-bold ml-2">{{com.company_title}} </span>
      </v-card-title>
      <v-card-text class="ml-3">
        <span class="font-weight-bold">{{com.recruit_title}}</span><br>
        경력 : {{com.careers}}<br>
        위치 : {{com.position}}<br>
        모집기간 : {{com.deadline}}<br>
      </v-card-text>
      <v-card-actions>
        <v-list-tile class="grow">
          <v-list-tile-avatar color="grey darken-3">
            <v-img class="elevation-6" src="https://cdn.vuetifyjs.com/images/cards/desert.jpg">
            </v-img>
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>JABARA JOB</v-list-tile-title>
          </v-list-tile-content>

          <v-layout align-center justify-end>
            <v-btn flat color="orange" @click="postScrapCompany(item)">
              <v-icon>bookmarks</v-icon>
              스크랩
            </v-btn>
            <v-btn flat color="blue-grey darken-3" @click="">
              <v-icon>share</v-icon>
              공유
            </v-btn>
          </v-layout>
        </v-list-tile>
      </v-card-actions>
    </v-card>
  </v-dialog>
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
      loginId: '',
      newcomer: '',
      noticeCompanys: [],
      dialog: false,
      com: {
        company_title: '',
        recruit_title: '',
        careers: '',
        position: '',
        deadline: '',
        recruit_url: ''
      }
    }
  },
  mounted() {
    if (sessionStorage.getItem('token') != null) {
      this.loginCheck = true
      this.loginId = sessionStorage.getItem('loginId')
      this.getCompanyList()
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
          this.newcomer = r.data.token.newcomer
          this.getCompanyList()
        })
        .catch(e => {
          alert("아이디나 비밀번호가 잘못되었습니다.")
          console.error(e.message)
        })
    },
    logout() {
      sessionStorage.removeItem('token');
      sessionStorage.removeItem('loginId');
      this.loginCheck = false
      this.noticeCompanys = []
    },
    signupPage() {
      location.href = "http://localhost:8080/signup"
    },
    getCompanyList() {
      axios.get(`http://10.120.73.194:5505/` + this.newcomer)
        .then((r) => {
          var com = JSON.stringify(r.data)
          this.companys = JSON.parse(com)
          console.log(this.companys)
          this.noticeCompanys = this.companys.slice(0, 4)
        })
    },
    noticeCompanyDetail(itemCompany) {
      this.com.company_title = itemCompany.Company_title
      this.com.recruit_title = itemCompany.Recruit_title
      this.com.careers = itemCompany.Careers
      this.com.position = itemCompany.Position
      this.com.deadline = itemCompany.Deadline
      this.com.recruit_url = itemCompany.Recruit_url
      this.dialog = true
    },
    pageLocate(){
      location.href=this.com.recruit_url
    }
  }
}
</script>
<style type="text/css">
a:link {
  color: #00BCD4;
  text-decoration: none;
}

a:visited {
  color: #00BCD4;
  text-decoration: none;
}
</style>
