<template>
  <div class="app-container">
    <div class="icons-container">
      <el-dropdown v-for="item of svgIcons" :key="item" @command="handleCommand">
        <div class="icon-item">
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="exchange">Chuyển đồ</el-dropdown-item>
            <el-dropdown-item command="delete">Xóa</el-dropdown-item>
          </el-dropdown-menu>
          <svg-icon :icon-class="item" />
          <span>{{ item }}</span>
        </div>
      </el-dropdown>
    </div>

    <el-dialog title="Chuyển đồ" :visible.sync="exchangeFormVisible">
      <el-form ref="dataForm" :model="exchange" label-position="left" label-width="100px" style="width: 600px; margin-left:50px;">
        <el-form-item label="Người nhận" prop="receiverId">
          <el-input v-model="exchange.receiverId" />
        </el-form-item>
        <el-form-item label="SỐ lượng" prop="quantity">
          <el-input v-model="exchange.quantity" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="exchangeFormVisible = false">
          Cancel
        </el-button>
        <el-button type="primary">
          Confirm
        </el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import svgIcons from './svg-icons'
export default {
  name: 'Icons',
  data() {
    return {
      exchangeFormVisible: false,
      svgIcons,
      exchange: {
        receiverId: undefined,
        quantity: 0
      }
    }
  },
  methods: {
    handleCommand(command) {
      if (command === 'exchange') {
        this.exchangeFormVisible = true
        this.$nextTick(() => {
          this.$refs['dataForm'].clearValidate()
        }
        )
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.icons-container {
  margin: 10px 20px 0;
  overflow: hidden;

  span {
    display: block;
    font-size: 16px;
    margin-top: 20px;
  }

  .icon-item {
    margin: 30px;
    height: 50px;
    text-align: center;
    width: 80px;
    float: left;
    font-size: 30px;
    color: #24292e;
    cursor: pointer;
  }
}
</style>
