<template>
<v-layout align-center justify-center ml-4>
  <v-flex xs12 sm12>
    <h1 class="ml-4 mt-5">스크랩</h1>
    <v-card class="mr-2 ml-2 mb-4 mt-2">
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
    getScrapCompany() {
      var user_id = sessionStorage.getItem('loginId')
      axios.get(`http://localhost:3303/getScrapCompany/${user_id}`)
        .then((r) => {
          this.companys = r.data.msg
          console.log(this.companys)
          this.pagingCompanys = this.companys.slice(this.startPage, this.endPage)
          this.maxPage = Math.ceil(this.companys.length / 10)
        })
        .catch((e) => {
          console.error(e.message)
        })
    },
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
      this.pagingCompanys()
    },
    pagingCompanyList() {
      this.pagingCompanys = this.companys.slice(this.startPage, this.endPage)
    }
  }
}
</script>
