<template>
  <div class="app-container">
    <h3 style="text-align: center">Đăng ký thông tin ứng viên</h3>
    <div style="margin-top: 20px">
      <el-row :gutter="20">
        <el-form ref="signInForm" :rules="rules" :model="candidateData" label-position="left" label-width="200px">
          <el-col :xs="24" :sm="24" :md="12" :offset="6" class="border border-gray">
            <el-form-item label="Họ và tên" prop="name">
              <el-input v-model="candidateData.name" />
            </el-form-item>
          </el-col>
          <el-col :xs="24" :sm="24" :md="12" :offset="6" class="border border-gray">
            <el-form-item label="Email" prop="email">
              <el-input v-model="candidateData.email" />
            </el-form-item>
          </el-col>
          <el-col :xs="24" :sm="24" :md="12" :offset="6" class="border border-gray">
            <el-form-item label="Trường Đại học" prop="university">
              <el-select v-model="candidateData.university" placeholder="--- Chọn đại học ---" clearable filterable class="filter-item full-width" @focus="getListUniversity">
                <el-option v-for="(item, index) in universityData" :key="index" :label="item.name" :value="item.name" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :xs="24" :sm="24" :md="12" :offset="6" class="border border-gray">
            <el-form-item label="Chuyên ngành" prop="major">
              <el-input v-model="candidateData.major" />
            </el-form-item>
          </el-col>
          <el-col :xs="24" :sm="24" :md="12" :offset="6" class="border border-gray">
            <el-form-item label="GPA" prop="gpa">
              <el-input-number v-model="candidateData.gpa" :min="0" :max="4" />
            </el-form-item>
          </el-col>
          <el-col :xs="24" :sm="24" :md="12" :offset="6" class="border border-gray">
            <el-form-item label="Điểm TOEIC" prop="english">
              <el-input-number v-model="candidateData.english" :min="0" :max="990" />
            </el-form-item>
          </el-col>
          <el-col :xs="24" :sm="24" :md="12" :offset="6" class="border border-gray">
            <el-form-item label="Mức lương mong muốn" prop="salary">
              <el-input v-model.number="candidateData.salary" />
            </el-form-item>
          </el-col>
          <el-col :xs="24" :sm="24" :md="12" :offset="6" class="border border-gray">
            <el-form-item>
              <el-button type="primary" @click="onSubmit">Create</el-button>
              <el-button>Cancel</el-button>
            </el-form-item>
          </el-col>
        </el-form>
      </el-row>
    </div>
  </div>
</template>

<script>
import { fetchUniverisy } from '@/api/university'
import { createCandidate } from '@/api/candidate'
export default {
  data() {
    return {
      candidateData: {
        name: '',
        email: '',
        university: '',
        major: '',
        gpa: 0,
        english: 0,
        salary: 0
      },
      universityData: [],
      rules: {
        name: [
          { required: true, message: 'Họ tên không được bỏ trống', trigger: 'change' }
        ],
        email: [
          { required: true, message: 'Email không được bỏ trống', trigger: 'change' }
        ],
        university: [
          { required: true, message: 'Trường Đại học không được bỏ trống', trigger: 'change' }
        ],
        major: [
          { required: true, message: 'Chuyên ngành không được bỏ trống', trigger: 'change' }
        ],
        gpa: [
          { required: true, message: 'GPA không được bỏ trống', trigger: 'change' }
        ],
        english: [
          { required: true, message: 'Điểm TOEIC không được bỏ trống', trigger: 'change' }
        ],
        salary: [
          { required: true, message: 'Mức lương không được bỏ trống', trigger: 'change' }
        ]
      }
    }
  },
  methods: {
    resetData() {
      this.candidateData = {
        name: undefined,
        email: undefined,
        university: '',
        major: undefined,
        gpa: undefined,
        english: undefined,
        salary: undefined
      }
    },
    onSubmit() {
      this.$refs['signInForm'].validate((valid) => {
        if (valid) {
          createCandidate(this.candidateData).then(response => {
            this.$notify({
              title: 'Thành công',
              message: 'Tạo ứng viên thành công',
              type: 'success',
              duration: 2000
            })
            this.resetData()
            this.$nextTick(() => {
              this.$refs['signInForm'].clearValidate()
            })
          })
        }
      })
    },
    getListUniversity() {
      fetchUniverisy().then(response => {
        this.universityData = response.data
      })
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
