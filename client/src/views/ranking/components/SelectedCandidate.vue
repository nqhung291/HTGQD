<template>
  <div class="table-container" style="margin-top: 20px">
    <h1 class="text-center">Danh sách ứng viên đánh giá</h1>
    <el-table
      :key="tableKey"
      ref="selectedCandidateTable"
      v-loading="listLoading"
      :data="listSelectedCandidate"
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
      <el-table-column label="Thái độ làm việc" min-width="150" align="center">
        <template slot-scope="{row}">
          <span>{{ row.attitude }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Làm việc nhóm" min-width="150" align="center">
        <template slot-scope="{row}">
          <span>{{ row.team_work }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Kỹ năng giao tiếp" min-width="150" align="center">
        <template slot-scope="{row}">
          <span>{{ row.communication_skill }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Kinh nghiệm làm việc" min-width="150" align="center">
        <template slot-scope="{row}">
          <span>{{ row.experience }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Thao tác" align="center" width="100">
        <template slot-scope="{row}">
          <el-button title="Xóa nhân viên" size="small" icon="el-icon-close" circle @click="handleDeleteStaff(row)" />
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  props: {
    listSelectedCandidate: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      tableKey: 0,
      totalStaff: 0,
      listLoading: false
    }
  },
  methods: {
    handleDeleteStaff(row) {
      this.listSelectedCandidate.splice(this.listSelectedCandidate.indexOf(row), 1)
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
