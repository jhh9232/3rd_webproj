  <template>
    <v-layout align-center justify-center ml-4>
      <v-flex xs12 sm12>
    <h1 class="ml-4 mt-5">회원가입</h1>
        <v-card class="mr-2 ml-2 mb-4 mt-2">
          <v-form class="ml-4">
            <v-flex  xs12 sm8 md5 lg5 xl5>
            <v-layout row align-center>
            <h3 class="mr-3">ID</h3>
            <v-text-field
                v-model="form.Id"
                label="아이디를 입력하세요"
            >
            </v-text-field>
            <v-btn class="mt-3" flat color="primary" @click="" >중복확인</v-btn>
          </v-layout>
        </v-flex>
        <v-flex  xs12 sm8 md5 lg5 xl5>
            <v-layout row  justify-center align-center>
            <h3 class="mr-2">PW</h3>
            <v-text-field xs4 sm4 md4 lg4 xl4
                v-model="form.Pw"
                label="비밀번호를 입력하세요"
                type="password"
            >
            </v-text-field>
              </v-layout>
            </v-flex>
            <v-flex  xs12 sm8 md5 lg5 xl5>
              <v-layout row justify-center align-center>
              <h3 class="mr-2">PW 확인</h3>
                <v-text-field
                    v-model="PwCheck"
                    label="비밀번호를 입력하세요"
                    type="password"
                >
                </v-text-field>
              </v-layout>
            </v-flex>
            <v-flex  xs12 sm10 md8 lg8 xl8>
              <v-layout row justify-center align-center>
              <h3 class="mr-2">Email</h3>
                <v-text-field
                    v-model="form.Email"
                    label="이메일을 입력하세요"
                >
                </v-text-field>
              </v-layout>
            </v-flex>
              <v-layout row>
            <v-flex  xs12 sm10 md8 lg8 xl8>
              <v-layout row justify-center align-center>
              <h3 class="mr-2">관심분야</h3>
                  <v-select :items="fieldList"item-text="field" item-value="filterField" v-model="form.Newcomer" label="분야"></v-select>
                </v-text-field>
              </v-layout>
            </v-flex>
          </v-layout>
            <v-flex  mt-5 xs12 sm10 md8 lg8 xl8>
              <v-layout row>
                <v-flex>
              <h3 class="mr-2">Email 수신 동의</h3>
            </v-flex>
            <v-flex>
              동의
            </v-flex>
            <v-flex>
              비동의
            </v-flex>
              </v-layout>
            </v-flex>
              </v-form>
              <v-card-actions layout>
                <v-spacer></v-spacer>
                <div class="layout mt-5 mb-3">
                <v-btn class="font-weight-bold" color="#F1C40F" @click="signup">회원가입</v-btn>
              </div>
              </v-card-actions>
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
      form: {
        Id: "",
        Pw: "",
        Email: "",
        Newcomer: ""
      },
      PwCheck: "",
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
    }
  },
  mounted() {},
  methods: {
    signup() {
      axios.post('http://localhost:3303/signup', this.form)
        .then(r => {
          if (r.data.success) {
            location.href = "http://localhost:8080/main"
          }
        })
        .catch(e => console.error(e.message))
    }
  }
}
</script>
