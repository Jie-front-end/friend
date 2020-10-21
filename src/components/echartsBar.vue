<template>
  <div :id="`myChart_${_uid}`" :style="{width:width, height:height}"></div>
</template>
<script>
export default {
  name: 'EchartsBar',
  props: {
    options: Object,
    width: [Number, String],
    height: [Number, String]
  },
  mounted () {
    this.init()
  },
  methods: {
    init () {
      const myChart = this.$echarts.init(document.getElementById(`myChart_${this._uid}`))
      myChart.setOption(this.options)
    }
  }
}
</script>

<style scoped>
</style>
