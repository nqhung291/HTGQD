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
          <el-input v-model="listQuery.university" placeholder="Đại học" class="filter-item" @keyup.enter.native="handleFilter" />
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

    <div class="result-table-container" style="margin-top: 20px">
      <h1 class="text-center">Danh sách ứng viên</h1>
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
        <el-table-column label="Chuyên ngành" min-width="200" align="center">
          <template slot-scope="{row}">
            <span>{{ row.major }}</span>
          </template>
        </el-table-column>
        <el-table-column label="GPA (/10)" min-width="200" align="center">
          <template slot-scope="{row}">
            <span>{{ row.gpa }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Điểm TOEIC (/10)" min-width="200" align="center">
          <template slot-scope="{row}">
            <span>{{ row.english }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Đại học" min-width="200" align="center">
          <template slot-scope="{row}">
            <span>{{ row.university }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Mức lương mong muốn ($)" min-width="200" align="center">
          <template slot-scope="{row}">
            <span>{{ row.salary }}</span>
          </template>
        </el-table-column>
      </el-table>

    </div>
  </div>
</template>

<script>
import waves from '@/directive/waves'
import { fetchCandidateList } from '@/api/candidate'

export default {
  directives: { waves },
  data() {
    return {
      tableKey: 0,
      list: null,
      listLoading: true,
      total: 0,
      tableVisible: false,
      listQuery: {
        // page: 1,
        // page_size: 10,
        name: undefined,
        major: undefined,
        gpa: undefined,
        english: undefined,
        university: undefined,
        salary: undefined
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
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
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
