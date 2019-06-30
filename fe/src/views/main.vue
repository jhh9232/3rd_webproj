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
            <v-card class="mr-2 ml-2 mb-4 mt-2 mx-auto" max-width="500">
              <v-card-title>
                <v-icon large left>
                  mdi-twitter
                </v-icon>
                <span class="title headline font-weight-bold ">{{item.Company_title}} </span>
              </v-card-title>
              <v-card-text>
                {{item.Recruit_title}}<br>
                경력 : {{item.Careers}}<br>
                위치 : {{item.Position}}<br>
                모집기간 : {{item.Deadline}}<br>
                <br>
                <hr>
                <br>
                지원하기
                <br>
                <span><a>{{item.Recruit_url}}</a></span><br>
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
          filterField: 'all'
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
      selected: 'all',
      nowPage: 1,
      startPage: 0,
      endPage: 10,
      maxPage: 0
    }
  },
  mounted() {
    this.getCompanyList()
    this.getScrapCompany()
  },
  methods: {
    paging() {
      this.endPage = this.nowPage * 10
      this.startPage = this.endPage - 10
      this.pagingCompanyList()
      // console.log('now'+this.nowPage)
      // console.log('start'+this.startPage)
      // console.log('end'+this.endPage)
    },
    changePosition() {
      this.nowPage = 1
      this.startPage = 0
      this.endPage = 10
      this.pagingCompanyList()
    },
    pagingCompanyList() {
      this.pagingCompanys = this.companys.slice(this.startPage, this.endPage)
    },
    getCompanyList() {
      if (this.selected == "all") {
        axios.get(`http://localhost:5505/`)
          .then((r) => {
            var com = JSON.stringify(r.data)
            this.companys = JSON.parse(com)
            this.pagingCompanys = this.companys.slice(this.startPage, this.endPage)
            this.maxPage = Math.ceil(this.companys.length / 10)
          })
      } else {
        axios.get(`http://localhost:5505/` + this.selected)
          .then((r) => {
            var com = JSON.stringify(r.data)
            this.companys = JSON.parse(com)
            this.pagingCompanys = this.companys.slice(this.startPage, this.endPage)
            this.maxPage = Math.ceil(this.companys.length / 10)
          })
      }
    },
    postScrapCompany(scrapCompany) {
      var loginId = sessionStorage.getItem('loginId')
      axios.post('http://localhost:3303/scrapCompany/',{
        company:scrapCompany,
        user_id:loginId})
        .then((r) => {
          alert("스크랩이 되었습니다.")
        })
        .catch((e) => {
          console.error(e.message)
        })
    }
  }
}
</script>
<style>

</style>
