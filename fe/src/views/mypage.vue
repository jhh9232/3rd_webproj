<template>
<v-layout align-center justify-center mt-4 ml-4>
  <v-flex xs12 sm12>
    <h1 class="ml-4 mt-4">마이페이지</h1>
    <v-card class="mr-2 ml-2 mb-4 mt-2">
      <v-container grid-list-md ml-4>
        <v-layout row wrap>
          <v-flex xs4 sm4 md4 align-center justify-center layout text-xs-center mt-4>
            <v-avatar :size="150" color="grey lighten-4">
              <img src="https://vuetifyjs.com/apple-touch-icon-180x180.png" alt="avatar">
            </v-avatar>
          </v-flex>
          <template v-if="!modification">
            <v-flex xs5 sm5 md5 align-center justify-center mt-5>
              <h2>ID: {{user.Id}}</h2>
              <h2 class="mt-2">Email: {{user.email}}</h2>
              <h2 class="mt-2">Field:</h2>
            </v-flex>
          </template>
          <v-flex xs5 sm5 md5 align-center justify-center mt-3>
            <template v-if="modification">
              <h2>ID: {{user.Id}}</h2>
              <v-text-field v-model="putUser.email" label="Email"></v-text-field>
              <v-select :items="fieldList" item-text="field" item-value="filterField" v-model="putUser.newcomer" label="직무"></v-select>
            </template>
          </v-flex>
        </v-layout>
        <v-layout class="justify-end mr-5">
          <template v-if="!modification">
            <v-btn flat class="mt-3" color="teal" @click="userModifyClick">수정</v-btn>
          </template>
          <template v-if="modification">
            <v-btn flat class="mt-3" color="teal" @click="putUserModify">적용</v-btn>
            <v-btn flat class="mt-3" color="teal" @click="userModifyClick">취소</v-btn>
          </template>
        </v-layout>
      </v-container>
      <!--
      <v-container>
        <h2 class="ml-2 mt-2">최근 본 공고</h2>
        <v-layout row wrap mt-4>
          <v-flex v-for="i in 3" :key="i" xs3 sm3 md3 lg3 xl3 mr-4>
            <v-card>
              <v-img src="https://cdn.vuetifyjs.com/images/cards/desert.jpg" aspect-ratio="2.75"></v-img>
              <v-card-title primary-title>
                <div>
                  <h3 class="headline mb-0">Kangaroo Valley Safari</h3>
                  <div> </div>
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
    -->
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
      user: {
        Id: '',
        email: '',
        newcomer: ''
      },
      modification: false,
      putUser: {
        id: '',
        email: '',
        newcomer: ''
      },
      fieldList: [{
          field: '전체',
          filterField: ''
        }, {
          field: '웹프로그래머',
          filterField: 'web'
        }, {
          field: '응용프로그래머',
          filterField: 'appliccation'
        }, {
          field: '시스템 프로그래머',
          filterField: 'system'
        },
        {
          field: 'DBA 데이터베이스',
          filterField: 'database'
        }, {
          field: '네트워크, 서버, 보안',
          filterField: 'network'
        }, {
          field: '웹기획 PM',
          filterField: 'webplan'
        }, {
          field: '웹마케팅',
          filterField: 'webmarketing'
        },
        {
          field: '컨텐츠, 사이드운영',
          filterField: 'contents'
        }, {
          field: 'HTML, 퍼블리싱, UI개발',
          filterField: 'htmlui'
        }, {
          field: '웹디자인',
          filterField: 'webdesign'
        }, {
          field: 'QA테스터, 검증',
          filterField: 'tester'
        },
        {
          field: '게임',
          filterField: 'game'
        }, {
          field: 'ERP, 시스템 설계 및 분석',
          filterField: 'erp'
        }, {
          field: 'IT, 디자인, 컴퓨터 강사',
          filterField: 'teacher'
        },
        {
          field: '동영상제작, 편집',
          filterField: 'video'
        }, {
          field: '빅데이터, 인공지능(AI)',
          filterField: 'bigdata_ai'
        }, {
          field: '소프트웨어 하드웨어',
          filterField: 'sw_hw'
        }
      ]
    }
  },
  mounted() {
    //회원 정보 저장
    this.user.Id = sessionStorage.getItem('loginId')
    this.user.email = sessionStorage.getItem('email')
    this.user.newcomer = sessionStorage.getItem('newcomer')

  },
  methods: {
    // 수정, 적용 버튼 클릭
    userModifyClick() {
      this.putUser.Id = this.user.Id
      this.modification = !this.modification
    },
    //회원 정보 수정
    putUserModify() {
      this.putUser.id = this.user.Id
      console.log(this.putUser)
      axios.put('http://localhost:3303/update/', this.putUser)
        .then(r => {
          alert("수정되었습니다.")
          sessionStorage.removeItem('email')
          sessionStorage.removeItem('newcomer')

          this.getModifyUser();
          this.userModifyClick()
        })
        .catch(e => {
          console.log(e.message)
        })
    },
    //바뀐 회원 정보를 가져옴
    getModifyUser() {
      axios.post('http://localhost:3303/findone', this.user)
        .then(r => {
          sessionStorage.setItem('email', r.data.token.email)
          sessionStorage.setItem('newcomer', r.data.token.newcomer)

          this.user.email = sessionStorage.getItem('email')
          this.user.newcomer = sessionStorage.getItem('newcomer')
        })
        .catch(e => {
          console.error(e.message)
        })
    },
  }
}
</script>
