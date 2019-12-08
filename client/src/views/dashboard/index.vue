<template>
  <div class="app-container">
    <upload-excel-component :on-success="handleSuccess" />
    <div v-show="tableVisible" class="result-table-container" style="margin-top: 20px">
      <h1 class="text-center">Bảng xếp hạng</h1>
      <el-table
        :key="tableKey"
        v-loading="listLoading"
        :data="list"
        border
        fit
        highlight-current-row
        style="width: 100%;"
      >
        <el-table-column label="Xếp hạng" prop="id" align="center" width="100">
          <template slot-scope="{row}">
            <span>{{ row.rank }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Họ và tên" min-width="200" align="center">
          <template slot-scope="{row}">
            <span>{{ row.name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Số điểm" align="center" width="100">
          <template slot-scope="{row}">
            <span>{{ row.point }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Điểm 1" width="90" align="center">
          <template slot-scope="{row}">
            <span>{{ row.point1 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Điểm 2" align="center" width="90">
          <template slot-scope="{row}">
            <span>{{ row.point2 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Điểm 3" align="center" width="90">
          <template slot-scope="{row}">
            <span>{{ row.point3 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Điểm 4" align="center" width="90">
          <template slot-scope="{row}">
            <span>{{ row.point4 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Điểm 5" align="center" width="90">
          <template slot-scope="{row}">
            <span>{{ row.point5 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Điểm 6" align="center" width="90">
          <template slot-scope="{row}">
            <span>{{ row.point6 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Điểm 7" align="center" width="90">
          <template slot-scope="{row}">
            <span>{{ row.point7 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Điểm 8" align="center" width="90">
          <template slot-scope="{row}">
            <span>{{ row.point8 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Điểm 9" align="center" width="90">
          <template slot-scope="{row}">
            <span>{{ row.point9 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Điểm 10" align="center" width="90">
          <template slot-scope="{row}">
            <span>{{ row.point10 }}</span>
          </template>
        </el-table-column>
      </el-table>

    </div>
  </div>
</template>

<script>
import UploadExcelComponent from '@/components/UploadExcel/index.vue'
import { uploadInfo } from '@/api/excel'
import { mappingObject } from '@/utils/mapping'

export default {
  name: 'UploadExcel',
  components: { UploadExcelComponent },
  data() {
    return {
      tableKey: 0,
      list: null,
      listLoading: true,
      tableVisible: false
    }
  },
  methods: {
    handleSuccess({ results, header }) {
      this.tableVisible = false
      this.$notify({
        title: 'Thành công',
        message: 'Upload file excel thành công',
        type: 'success',
        duration: 3000
      })
      // mapping object
      const requestData = mappingObject(results)
      uploadInfo(requestData).then((response) => {
        console.log(response)
        this.list = response.data.data
        this.listLoading = false
        this.tableVisible = true
      })
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
