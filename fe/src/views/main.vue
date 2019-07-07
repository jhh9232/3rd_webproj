<template>
<v-layout align-center justify-center ml-4>
  <v-flex xs12 sm12>
    <h1 class="ml-4 mt-5">채용공고</h1>
    <v-card class="mr-2 ml-2 mb-4 mt-2">
      <v-layout row>
        <v-flex ml-5 mt-5 xs1>
          <h3>필터링</h3>
        </v-flex>
        <v-flex ml-1 mt-4 xs3 sm3 md3 lg3 xl3 d-flex class="mr-1">
          <v-select :items="fieldList" item-text="field" item-value="filterField" v-model="selected" v-on:change="changePosition" label="직무"></v-select>
        </v-flex>
      </v-layout>
      <v-container fluid grid-list-sm>
        <v-layout row wrap>
          <v-flex v-for="item in pagingCompanys" xs6 sm6>
            <v-card class="mr-2 ml-2 mb-4 mt-2 mx-auto companyCard" max-width="500" >
              <div @click="pageLocate(item.Recruit_url)">
              <v-card-title class="ml-2">
                <span class="title headline font-weight-bold ">{{item.Company_title}} </span>
              </v-card-title>
              <v-card-text class="ml-3">
                <span class="font-weight-bold">{{item.Recruit_title}}</span><br><br>
                경력 : {{item.Careers}}<br>
                위치 : {{item.Position}}<br>
                모집기간 : {{item.Deadline}}<br>
              </v-card-text>
            </div>
              <v-card-actions>
                <v-list-tile class="grow">
                  <v-list-tile-avatar color="grey darken-3">
                    <v-img class="elevation-6" src="https://cdn.vuetifyjs.com/images/cards/desert.jpg">
                    </v-img>
                  </v-list-tile-avatar>
                  <v-list-tile-content>
                    <v-list-tile-title>JABARA JOB</v-list-tile-title>
                  </v-list-tile-content>

                  <v-layout align-center justify-end ml-4 mb-2>
                    <v-btn flat small color="orange" @click="postScrapCompany(item)">
                      <v-icon>bookmarks</v-icon>
                      스크랩
                    </v-btn>
                    <v-btn flat small color="blue-grey darken-3" @click="">
                      <v-icon>share</v-icon>
                      공유
                    </v-btn>
                  </v-layout>
                </v-list-tile>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
        <div class="text-xs-center">
          <v-pagination :length="maxPage" :total-visible="7" circle v-on:click.native="paging()" v-model="nowPage"></v-pagination>
        </div>
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
      ],
      companys: [],
      pagingCompanys: [],
      selected: '',
      nowPage: 1,
      startPage: 0,
      endPage: 10,
      maxPage: 0,
      scrapCheck: false,
    }
  },
  mounted() {
    this.getCompanyList()

  },
  methods: {
    //현재 페이지를 계산함
    paging() {
      this.endPage = this.nowPage * 10
      this.startPage = this.endPage - 10
      this.pagingCompanyList()
    },
    //직무를 바꿨을 때 페이지를 초기화 함
    changePosition() {
      this.nowPage = 1
      this.startPage = 0
      this.endPage = 10
      this.getCompanyList()
    },
    //현재 페이지에 맞는 채용공고 리스트를 가져옴
    pagingCompanyList() {
      this.pagingCompanys = this.companys.slice(this.startPage, this.endPage)
    },
    //현재 직무에 맞는 회사 리스트를 가져옴
    getCompanyList() {
      axios.get(`http://localhost:5505/` + this.selected)
        .then((r) => {
          var com = JSON.stringify(r.data)
          this.companys = JSON.parse(com)
          if (this.companys.length) {
            this.pagingCompanys = this.companys.slice(this.startPage, this.endPage)
            this.maxPage = Math.ceil(this.companys.length / 10)
          } else {
            this.pagingCompanys = []
            this.maxPage = 1
          }
        })

    },
    //채용공고를 스크랩함
    postScrapCompany(scrapCompany) {
      var loginId = sessionStorage.getItem('loginId')
      if (loginId == null) {
        alert("로그인 후 이용할 수 있습니다.")
      } else {
        axios.post('http://localhost:3303/scrapCompany/', {
            company: scrapCompany,
            user_id: loginId
          })
          .then((r) => {
            alert("스크랩이 되었습니다.")
            console.log(r)
          })
          .catch((e) => {
            console.error(e.message)
          })
      }
    },
    pageLocate(url) {
      window.open(url, '_blank');
    }
  }
}
</script>
<style>
.companyCard:hover{
  color:gray;
}
</style>
