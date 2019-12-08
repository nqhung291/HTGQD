<template>
  <div class="app-container">
    <div class="filter-container">
      <el-row :gutter="15">
        <el-col :md="8" :sm="12" :xs="24">
          <el-input v-model="listQuery.staff_code" placeholder="ID giao dịch" class="filter-item" @keyup.enter.native="handleFilter" />
        </el-col>
        <el-col :md="8" :sm="12" :xs="24">
          <el-input v-model="listQuery.full_name" placeholder="Tên người gửi" class="filter-item" @keyup.enter.native="handleFilter" />
        </el-col>
        <el-col :md="8" :sm="12" :xs="24">
          <el-input v-model="listQuery.full_name" placeholder="Tên người nhận" class="filter-item" @keyup.enter.native="handleFilter" />
        </el-col>
        <el-col :md="8" :sm="12" :xs="24">
          <el-select v-model="listQuery.status" placeholder="--- Loại giao dịch ---" clearable class="filter-item">
            <el-option v-for="item in statusOptions" :key="item.status" :label="item.description" :value="item.status" />
          </el-select>
        </el-col>
        <el-col :md="8" :sm="12" :xs="24">
          <el-date-picker
            v-model="listQuery.to_date"
            type="date"
            format="dd/MM/yyyy"
            value-format="dd/MM/yyyy"
            placeholder="Thời gian"
            class="filter-item full-width"
          />
        </el-col>
        <el-col :md="8" :sm="12" :xs="24">
          <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
            Search
          </el-button>
        </el-col>
      </el-row>
    </div>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%;"
    >
      <el-table-column label="STT" prop="id" align="center" min-width="50">
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="ID giao dịch" prop="staff_code" align="center" min-width="150">
        <template slot-scope="{row}">
          <span>{{ row.staff_code }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Người gửi" min-width="150" align="center">
        <template slot-scope="{row}">
          <span>{{ row.full_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Người nhận" align="center" min-width="150">
        <template slot-scope="{row}">
          <span>{{ row.email }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Vật phẩm" width="150" align="center">
        <template slot-scope="{row}">
          <span>{{ row.mobile }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Loại hình giao dịch" align="center" min-width="200">
        <template slot-scope="{row}">
          <span>{{ row.team }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Thời gian" align="center" min-width="150">
        <template slot-scope="{row}">
          <span>{{ row.created_date }}</span>
        </template>
      </el-table-column>
    </el-table>

    <pagination
      v-show="total>0"
      :total="total"
      :page-sizes="[10, 25, 50, 100]"
      :page.sync="listQuery.page"
      :limit.sync="listQuery.page_size"
      @pagination="getList"
    />
  </div>
</template>

<script>
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import waves from '@/directive/waves' // waves directive

export default {
  name: 'StaffTable',
  directives: { waves },
  components: { Pagination },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        page_size: 10,
        staffCode: undefined,
        fullName: undefined,
        status: undefined,
        ordering: 'id',
        from_date: undefined,
        to_date: undefined
      },
      statusOptions: [
        {
          status: -1,
          description: 'Chuyển đồ'
        },
        {
          status: 1,
          description: 'Nhận đồ'
        }
      ],
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: 'Edit',
        create: 'Create'
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = false
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    handleDetail(staffId) {
      this.$router.push({ path: `/management-staff/staff-detail/${staffId}/` })
    }
  }
}
</script>
