<template>
<v-layout align-center justify-center ml-4>
  <v-flex xs12 sm12>
    <h1 class="ml-4 mt-5">스크랩</h1>
    <v-card class="mr-2 ml-2 mb-4 mt-2">
      <v-container fluid grid-list-sm>
        <v-layout row wrap>
          <v-flex v-for="item in pagingCompanys" xs6 sm6>
            <v-card class="mr-2 ml-2 mb-4 mt-2 mx-auto companyCard" max-width="500">
              <div @click="pageMove(item.Recruit_url)">
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

                  <v-layout align-center justify-end>
                    <v-btn flat color="orange" @click="deleteScrapCompany(item)">
                      <v-icon>bookmarks</v-icon>
                      삭제
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
      <v-footer class="mt-5"></v-footer>
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
      companys: [],
      pagingCompanys: [],
      nowPage: 1,
      startPage: 0,
      endPage: 10,
      maxPage: 0
    }
  },
  mounted() {
    this.getScrapCompany()
  },
  methods: {
    //스크랩 된 채용공고 리스트를 가져옴
    getScrapCompany() {
      var user_id = sessionStorage.getItem('loginId')
      axios.get(`http://localhost:3303/getScrapCompany/${user_id}`)
        .then((r) => {
          this.companys = r.data.msg
          this.pagingCompanys = this.companys.slice(this.startPage, this.endPage)
          this.maxPage = Math.ceil(this.companys.length / 10)
        })
        .catch((e) => {
          console.error(e.message)
        })
    },
    //스크랩된 채용공고를 삭제함
    deleteScrapCompany(company) {
      var user_id = sessionStorage.getItem('loginId')
      axios.post('http://localhost:3303/deleteScrapCompany', {
          user_id: user_id,
          company_title: company.Company_title
        })
        .then((r) => {
          if(this.pagingCompanys.length<1||this.nowPage>1){
            this.nowPage=this.nowPage-1
            paging()
          }
          this.getScrapCompany()
        })
        .catch((e) => {
          console.error(e.message)
        })
    },
    //페이징
    paging() {
      this.endPage = this.nowPage * 10
      this.startPage = this.endPage - 10
      this.pagingCompanyList()
    },
    //직무가 바뀌었을 때 페이지를 초기화 함
    changePosition() {
      this.nowPage = 1
      this.startPage = 0
      this.endPage = 10
      this.pagingCompanys()
    },
    //현재 페이지에 맞는 채용공고 리스트를 가져옴
    pagingCompanyList() {
      this.pagingCompanys = this.companys.slice(this.startPage, this.endPage)
    },
    //채용공고를 클릭했을 때 외부 페이지로 이동함
    pageMove(url){
      location.href=url
    }
  }
}
</script>
<style>
.companyCard:hover{
  color:gray;
}
</style>
