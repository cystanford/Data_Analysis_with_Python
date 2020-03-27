//温度统计曲线图
function echartsColumnarSum(id) {
    // 初始化echart实例，获取dom
    let dom = echarts.init(document.getElementById(id));
    console.log()
        //下面是配置
    var option = {
            color: ["#1d428a", "#d01010"],
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            legend: {
                orient: 'vertical',
                right: '5%',
                align: 'left',
                top: '5%',
                textStyle: {
                    color: '#8C8C8C'
                },
                data: ['18-24岁中男性占比', '35-岁中女性占比']
            },
            grid: {
                left: '0%',
                right: '0%',
                top: '10%',
                bottom: '0%',
                containLabel: true
            },
            series: [{
                name: 'demo',
                type: 'pie',
                center: ['40%', '50%'],
                radius: ['40%', '60%'],
                avoidLabelOverlap: false,
                label: {
                    normal: {
                        show: true,
                        position: 'outter',
                        formatter: "{d}%"
                    }

                },
                labelLine: {
                    normal: {
                        show: true
                    }
                },
                data: [
                    { value: 335, name: '18-24岁中男性占比' },
                    { value: 310, name: '35-岁中女性占比' },
                ]
            }]
        }
        //使用刚指定的配置项和数据显示图表
    dom.setOption(option);
}