<template>
  <div class="app-container">
    <strong>Đăng ký thông tin ứng viên</strong>
    <div style="margin-top: 20px">
      <el-row :gutter="20">
        <el-col :xs="24" :sm="24" :md="12" class="border border-gray">
          <el-form ref="signInForm" :rules="rule" :model="candidateData" label-position="left" label-width="200px">
            <el-form-item label="Họ và tên" prop="name">
              <el-input v-model="candidateData.name" />
            </el-form-item>
            <el-form-item label="Email" prop="email">
              <el-input v-model="candidateData.email" />
            </el-form-item>
            <el-form-item label="Trường Đại học" prop="university">
              <el-input-number v-model="candidateData.university" />
            </el-form-item>
            <el-form-item label="Chuyên ngành" prop="major">
              <el-input v-model="candidateData.major" />
            </el-form-item>
            <el-form-item label="Chuyên ngành" prop="major">
              <el-input v-model="candidateData.major" />
            </el-form-item>
            <el-form-item label="GPA" prop="major">
              <el-input-number v-model="candidateData.gpa" min="0" max="4" />
            </el-form-item>
            <el-form-item label="Điểm TOEIC" prop="english">
              <el-input-number v-model="candidateData.english" min="0" max="990" />
            </el-form-item>
            <el-form-item label="Mức lương mong muốn" prop="salary">
              <el-input v-model.number="candidateData.salary" />
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      candidateData: {
        name: undefined,
        email: undefined,
        university: undefined,
        major: undefined,
        gpa: 0,
        english: 0,
        salary: undefined
      }
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
