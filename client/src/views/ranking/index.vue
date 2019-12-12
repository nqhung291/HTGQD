<template>
  <div class="app-container">
    <el-row type="flex" justify="space-between">
      <el-col :span="6">
        <el-button type="primary" @click="getListCandidate">
          Chọn ứng viên để đánh giá
        </el-button>
      </el-col>
      <el-col :offset="7">
        <el-button @click="abortRanking">
          Hủy
        </el-button>
        <el-button :disabled="!listSelectedCandidate || listSelectedCandidate.length == 0" type="primary" @click="handleRanking">
          Đánh giá
        </el-button>
      </el-col>
    </el-row>

    <selected-candidate :list-selected-candidate.sync="listSelectedCandidate" />

    <el-dialog title="Danh sách ứng viên" :visible.sync="candidateDialogVisible" width="1280px">
      <div class="filter-container">
        <el-row :gutter="15">
          <el-col :md="8" :sm="12" :xs="24">
            <el-input v-model="candidateQuery.name" placeholder="Họ và tên" class="filter-item" @keyup.enter.native="handleFilter" />
          </el-col>
          <el-col :md="8" :sm="12" :xs="24">
            <!-- <el-input v-model="candidateQuery.university" placeholder="Đại học" class="filter-item" @keyup.enter.native="handleFilter" /> -->
            <el-select v-model="candidateQuery.university" placeholder="--- Chọn đại học ---" clearable filterable class="filter-item full-width" @focus="getListUniversity">
              <el-option v-for="(item, index) in universityData" :key="index" :label="item.name" :value="item.name" />
            </el-select>
          </el-col>
          <el-col :md="8" :sm="12" :xs="24">
            <el-input v-model="candidateQuery.major" placeholder="Chuyên ngành" class="filter-item" @keyup.enter.native="handleFilter" />
          </el-col>
          <el-col :md="8" :sm="12" :xs="24">
            <el-input v-model="candidateQuery.gpa" placeholder="GPA" class="filter-item" @keyup.enter.native="handleFilter" />
          </el-col>
          <el-col :md="8" :sm="12" :xs="24">
            <el-input v-model="candidateQuery.english" placeholder="Tiếng anh" class="filter-item" @keyup.enter.native="handleFilter" />
          </el-col>
          <el-col :md="8" :sm="12" :xs="24">
            <el-input v-model="candidateQuery.salary" placeholder="Mức lương mong muốn" class="filter-item" @keyup.enter.native="handleFilter" />
          </el-col>
          <el-col :span="24" style="text-align: right">
            <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
              Tìm kiếm
            </el-button>
            <el-button v-waves class="filter-item" type="primary" :disabled="!selectedOptions || selectedOptions.length == 0" @click="handleAddCandidate">
              Tiếp tục <i class="el-icon-d-arrow-right" />
            </el-button>
          </el-col>
        </el-row>
      </div>

      <el-table
        :key="tableKey"
        ref="listCandidateTable"
        v-loading="listLoading"
        :data="listCandidate"
        border
        fit
        highlight-current-row
        style="width: 100%;"
        @selection-change="handleSelectionChange"
      >
        <el-table-column
          type="selection"
          width="55"
          align="center"
        />
        <el-table-column label="Họ và tên" min-width="200" align="center">
          <template slot-scope="{row}">
            <span>{{ row.name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Đại học" min-width="100" align="center">
          <template slot-scope="{row}">
            <span>{{ row.university }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Chuyên ngành" min-width="150" align="center">
          <template slot-scope="{row}">
            <span>{{ row.major }}</span>
          </template>
        </el-table-column>
        <el-table-column label="GPA" min-width="80" align="center">
          <template slot-scope="{row}">
            <span>{{ row.gpa }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Điểm TOEIC" min-width="100" align="center">
          <template slot-scope="{row}">
            <span>{{ row.english }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Mức lương mong muốn ($)" min-width="150" align="center">
          <template slot-scope="{row}">
            <span>{{ row.salary }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Thái độ làm việc" min-width="100" align="center">
          <template slot-scope="{row}">
            <span>{{ row.attitude }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Làm việc nhóm" min-width="100" align="center">
          <template slot-scope="{row}">
            <span>{{ row.team_work }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Kỹ năng giao tiếp" min-width="100" align="center">
          <template slot-scope="{row}">
            <span>{{ row.communication_skill }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Kinh nghiệm làm việc" min-width="100" align="center">
          <template slot-scope="{row}">
            <span>{{ row.experience }}</span>
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>

    <el-dialog title="Kết quả đánh giá ứng viên" :visible.sync="rankingDialogVisible">
      <el-table
        :key="rankingTableKey"
        ref="rankingTable"
        :data="listRanking"
        border
        fit
        highlight-current-row
        style="width: 100%;"
      >
        <el-table-column label="Xếp hạng" min-width="100" align="center">
          <template slot-scope="{row}">
            <span>{{ row.rank }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Họ tên" min-width="100" align="center">
          <template slot-scope="{row}">
            <span>{{ row.name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Email" min-width="100" align="center">
          <template slot-scope="{row}">
            <span>{{ row.email }}</span>
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
  </div>
</template>

<script>
import SelectedCandidate from './components/SelectedCandidate'
import waves from '@/directive/waves'
import { fetchCandidateList } from '@/api/candidate'
import { fetchRank } from '@/api/ranking'
import { fetchUniverisy } from '@/api/university'

export default {
  directives: { waves },
  components: { SelectedCandidate },
  data() {
    return {
      tableKey: 0,
      rankingTableKey: 1,
      total: 0,
      totalCandidate: 0,
      listLoading: true,
      universityData: null,
      candidateQuery: {
        // page: 1,
        // page_size: 10,
        name: undefined,
        major: undefined,
        gpa: undefined,
        english: undefined,
        university: undefined,
        salary: undefined,
        is_rated: 1
      },
      candidateDialogVisible: false,
      rankingDialogVisible: false,
      listCandidate: null,
      listSelectedCandidate: [],
      selectedOptions: [],
      listRanking: null
    }
  },
  methods: {
    resetForm() {
      this.listSelectedCandidate = []
    },
    abortRanking() {
      this.resetForm()
    },
    getListCandidate() {
      this.candidateDialogVisible = true
      fetchCandidateList(this.candidateQuery).then((response) => {
        this.listCandidate = response.data
        // this.totalCandidate = response.total
        this.listLoading = false
      })
    },
    handleFilter() {
      // this.staffQuery.page = 1
      this.getListCandidate()
    },
    handleSelectionChange(val) {
      this.selectedOptions = val
    },
    handleAddCandidate() {
      this.candidateDialogVisible = false
      this.listSelectedCandidate = this.listSelectedCandidate.concat(this.selectedOptions)
    },
    handleRanking() {
      fetchRank(this.listSelectedCandidate).then(response => {
        this.listRanking = response.data.data
        this.rankingDialogVisible = true
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
  .item {
    display: block;
    overflow: hidden;
    margin-bottom: 14px;
    line-height: 24px;
  }
</style>
