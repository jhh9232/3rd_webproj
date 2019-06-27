  <template>
    <v-content>
    <v-container>
  <v-layout justify-center align-center row>
    <v-flex mt-5>
      <v-card class="elevation-3">
        <v-toolbar dark color="success">
          <v-toolbar-title>회원가입</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text>
          <v-form>
            <v-layout row  justify-center align-center>
            <h3 class="mr-3">ID</h3>
            <v-text-field xs4 sm4 md4 lg4 xl4
                v-model="userId"
                label="아이디를 입력하세요"
            >
            </v-text-field>
            <v-btn class="mt-3" flat color="primary">중복확인</v-btn>
          </v-layout>
            <v-layout row  justify-center align-center>
            <h3 class="mr-2 ">PW</h3>
            <v-text-field xs4 sm4 md4 lg4 xl4
                v-model="userPw"
                label="비밀번호를 입력하세요"
                type="password"
            >
            </v-text-field>
          </v-layout>
          <v-layout row justify-center align-center>
          <h3 class="mr-2">PW 확인</h3>
            <v-text-field
                v-model="userPwCheck"
                label="비밀번호를 입력하세요"
                type="password"
            >
            </v-text-field>
          </v-layout>
          <v-layout row justify-center align-center>
          <h3 class="mr-2">Email</h3>
            <v-text-field
                v-model="userEmail"
                label="이메일을 입력하세요"
            >
            </v-text-field>
          </v-layout>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn dark color="success" @click="signup">회원가입</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</v-container>
</v-content>
</template>
