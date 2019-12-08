<template>
  <div class="app-container">
    <upload-excel-component :on-success="handleSuccess" />
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
    handleSuccess({ results, header }) {
      console.log(results)
      uploadInfo(results).then((res) => {
        console.log(res)
        this.$notify({
          title: 'Thành công',
          message: 'Upload file excel thành công',
          type: 'success',
          duration: 3000
        })
      })
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
