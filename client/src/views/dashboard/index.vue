<template>
  <div class="app-container">
    <upload-excel-component :on-success="handleSuccess" :before-upload="beforeUpload" />
  </div>
</template>

<script>
import UploadExcelComponent from '@/components/UploadExcel/index.vue'
import { uploadInfo } from '@/api/excel'

export default {
  name: 'UploadExcel',
  components: { UploadExcelComponent },
  data() {
    return {
    }
  },
  methods: {
    beforeUpload(file) {
      const isLt1M = file.size / 1024 / 1024 < 1

      if (isLt1M) {
        return true
      }

      this.$message({
        message: 'Please do not upload files larger than 1m in size.',
        type: 'warning'
      })
      return false
    },
    handleSuccess({ results, header }) {
      console.log(results)
      uploadInfo(results).then((res) => {
        console.log(res)
        this.$notify({
          title: 'Thành công',
          message: 'Upload file excel thành công',
          type: 'success',
          duration: 2000
        })
      })
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
