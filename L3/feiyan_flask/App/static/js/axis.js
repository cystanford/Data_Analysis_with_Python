//温度统计曲线图
function echartsColumnarAxis(id) {
    // 初始化echart实例，获取dom
    let dom = echarts.init(document.getElementById(id));
    console.log()
        //下面是配置
    var option = {
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            legend: {
                data: ['当前人数占比', '对比全网人群', '负面占比'],
                show: false
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                top: '5%',
                containLabel: true
            },
            xAxis: {
                type: 'value',
                axisTick: {
                    show: false,
                },
                triggerEvent: false,
                axisLine: {
                    show: false
                },
                axisLabel: {
                    show: false,
                }
            },
            yAxis: {
                type: 'category',
                scale: false,
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                axisLabel: {
                    show: true,
                    textStyle: {
                        color: '#687284'
                    },
                },
                splitLine: {
                    show: false,
                },
                data: ['单身', '恋爱', '准备结婚', '已婚未孕', '育婴', '已婚已育', '孝敬期'].reverse(),

            },
            series: [{
                    name: '当前人数占比',
                    type: 'bar',
                    data: [20, 21, 22, 25, 27, 22, 20],
                    color: '#1d428a'
                },
                {
                    name: '对比全网人群',
                    type: 'bar',
                    data: [20, 21, 22, 25, 27, 99, 20],
                    color: '#ff9d00'
                },
                {
                    name: '负面占比',
                    type: 'bar',
                    data: [20, 21, 22, 25, 27, 0, 20, 21, 22, 25, 27, 0],
                    color: '#97d2fe'
                }
            ]
        }
        //使用刚指定的配置项和数据显示图表
    dom.setOption(option);
}