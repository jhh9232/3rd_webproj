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
                v-model="userId"
                label="아이디를 입력하세요"
            >
            </v-text-field>
            <v-btn class="mt-3" flat color="primary">중복확인</v-btn>
          </v-layout>
        </v-flex>
        <v-flex  xs12 sm8 md5 lg5 xl5>
            <v-layout row  justify-center align-center>
            <h3 class="mr-2 ">PW</h3>
            <v-text-field xs4 sm4 md4 lg4 xl4
                v-model="userPw"
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
                    v-model="userPwCheck"
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
                    v-model="userEmail"
                    label="이메일을 입력하세요"
                >
                </v-text-field>
              </v-layout>
            </v-flex>
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
                <v-btn dark color="success" @click="">회원가입</v-btn>
              </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
</template>
<script>
export default {
  name: 'App',
  data() {
    return {}
  },
  mounted() {},
  methods: {}
}
</script>
