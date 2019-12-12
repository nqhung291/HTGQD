<template>
  <div class="app-container">
    <div class="filter-container">
      <el-row :gutter="15">
        <el-col :md="8" :sm="12" :xs="24">
          <el-input v-model="listQuery.name" placeholder="Họ và tên" class="filter-item" @keyup.enter.native="handleFilter" />
        </el-col>
        <el-col :md="8" :sm="12" :xs="24">
          <el-input v-model="listQuery.major" placeholder="Chuyên ngành" class="filter-item" @keyup.enter.native="handleFilter" />
        </el-col>
        <el-col :md="8" :sm="12" :xs="24">
          <el-input v-model="listQuery.gpa" placeholder="GPA" class="filter-item" @keyup.enter.native="handleFilter" />
        </el-col>
        <el-col :md="8" :sm="12" :xs="24">
          <el-input v-model="listQuery.english" placeholder="Tiếng anh" class="filter-item" @keyup.enter.native="handleFilter" />
        </el-col>
        <el-col :md="8" :sm="12" :xs="24">
          <el-select v-model="listQuery.university" placeholder="--- Chọn đại học ---" clearable filterable class="filter-item full-width" @focus="getListUniversity">
            <el-option v-for="(item, index) in universityData" :key="index" :label="item.name" :value="item.name" />
          </el-select>
        </el-col>
        <el-col :md="8" :sm="12" :xs="24">
          <el-input v-model="listQuery.salary" placeholder="Mức lương mong muốn" class="filter-item" @keyup.enter.native="handleFilter" />
        </el-col>
        <el-col :span="24" style="text-align: right">
          <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
            Tìm kiếm
          </el-button>
        </el-col>
      </el-row>
    </div>

    <div class="table-container" style="margin-top: 20px">
      <h1 class="text-center">Danh sách ứng viên chưa được đánh giá chi tiết</h1>
      <el-table
        :key="tableKey"
        v-loading="listLoading"
        :data="list"
        border
        fit
        highlight-current-row
        style="width: 100%;"
      >
        <el-table-column label="Họ và tên" min-width="200" align="center">
          <template slot-scope="{row}">
            <span>{{ row.name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Email" min-width="200" align="center">
          <template slot-scope="{row}">
            <span>{{ row.email }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Chuyên ngành" min-width="150" align="center">
          <template slot-scope="{row}">
            <span>{{ row.major }}</span>
          </template>
        </el-table-column>
        <el-table-column label="GPA" min-width="100" align="center">
          <template slot-scope="{row}">
            <span>{{ row.gpa }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Điểm TOEIC" min-width="100" align="center">
          <template slot-scope="{row}">
            <span>{{ row.english }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Đại học" min-width="100" align="center">
          <template slot-scope="{row}">
            <span>{{ row.university }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Mức lương mong muốn ($)" min-width="150" align="center">
          <template slot-scope="{row}">
            <span>{{ row.salary }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Đánh giá ứng viên" align="center" min-width="100" class-name="small-padding fixed-width">
          <template slot-scope="{row}">
            <el-button title="Đánh giá ứng viên" size="small" icon="el-icon-info" circle @click="handleRating(row)" />
          </template>
        </el-table-column>
      </el-table>

      <el-dialog title="Đánh giá chi tiết ứng viên sau phỏng vấn" :visible.sync="dialogVisible">
        <el-form ref="changeTeamForm" :rules="rule" :model="candidateAdditionalRating" label-position="left" label-width="200px">
          <el-form-item label="Thái độ" prop="attitude">
            <el-input-number v-model="candidateAdditionalRating.attitude" :min="0" :max="10" />
          </el-form-item>
          <el-form-item label="Kỹ năng làm việc nhóm" prop="team_work">
            <el-input-number v-model="candidateAdditionalRating.team_work" :min="0" :max="10" />
          </el-form-item>
          <el-form-item label="Kỹ năng giao tiếp" prop="communication_skill">
            <el-input-number v-model="candidateAdditionalRating.communication_skill" :min="0" :max="10" />
          </el-form-item>
          <el-form-item label="Kinh nghiệm làm việc" prop="experience">
            <el-input-number v-model="candidateAdditionalRating.experience" :min="0" :max="10" />
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="handleCloseDialog">
            Cancel
          </el-button>
          <el-button type="primary" @click="handleUpdateCandidate()">
            Confirm
          </el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import waves from '@/directive/waves'
import { fetchCandidateList, updateCandidate } from '@/api/candidate'
import { fetchUniverisy } from '@/api/university'

export default {
  directives: { waves },
  data() {
    return {
      tableKey: 0,
      list: null,
      listLoading: true,
      total: 0,
      tableVisible: false,
      dialogVisible: false,
      listQuery: {
        page: 1,
        page_size: 10,
        name: undefined,
        major: undefined,
        gpa: undefined,
        english: undefined,
        university: undefined,
        salary: undefined,
        is_rated: 0
      },
      candidateAdditionalRating: {
        attitude: 0,
        team_work: 0,
        communication_skill: 0,
        experience: 0
      },
      rowId: undefined,
      rule: {
        attitude: [
          {
            required: true,
            type: 'number',
            message: 'Không được bỏ trống và phải đánh giá trên thang điểm 10',
            minimum: 0,
            maximum: 10,
            trigger: 'change'
          }
        ],
        team_work: [
          {
            required: true,
            type: 'number',
            message: 'Không được bỏ trống và phải đánh giá trên thang điểm 10',
            minimum: 0,
            maximum: 10,
            trigger: 'change'
          }
        ],
        communication_skill: [
          {
            required: true,
            type: 'number',
            message: 'Không được bỏ trống và phải đánh giá trên thang điểm 10',
            minimum: 0,
            maximum: 10,
            trigger: 'change'
          }
        ],
        experience: [
          {
            required: true,
            type: 'number',
            message: 'Không được bỏ trống và phải đánh giá trên thang điểm 10',
            minimum: 0,
            maximum: 10,
            trigger: 'change'
          }
        ]
      },
      universityData: null
    }
  },
  created() {
    this.getList()
  },
  methods: {
    resetData() {
      this.rowId = undefined
      this.candidateAdditionalRating = {
        attitude: 0,
        team_work: 0,
        communication_skill: 0,
        experience: 0
      }
    },
    getList() {
      this.listLoading = true
      fetchCandidateList(this.listQuery).then(response => {
        this.list = response.data
        this.total = this.list.length
        this.listLoading = false
      })
    },
    handleFilter() {
      // this.listQuery.page = 1,
      this.getList()
    },
    handleRating(row) {
      this.resetData()
      this.$nextTick(() => {
        this.$refs['changeTeamForm'].clearValidate()
      })
      this.dialogVisible = true
      this.rowId = row._id.$oid
    },
    handleCloseDialog() {
      this.resetData()
      this.dialogVisible = false
    },
    handleUpdateCandidate() {
      this.$refs['changeTeamForm'].validate((valid) => {
        console.log('valid')
        updateCandidate(this.rowId, this.candidateAdditionalRating).then(response => {
          this.resetData()
          this.dialogVisible = false
          this.getList()
        })
      })
    },
    getListUniversity() {
      fetchUniverisy().then(response => {
        console.log(response.data)
        this.universityData = response.data
      })
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
