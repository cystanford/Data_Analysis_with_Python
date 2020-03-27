//状图
function echartsColumnarPaim(id) {
    var data = {
        symbol: '%', //数值是否带百分号        --默认为空 ''
        seriesLabel: true, //柱子上方toplabel --默认展示 trur
        barWidth: 10, //柱子宽度               --默认12
        ysplitLine: '#F1F3F5', //y轴横向分割线颜色 --默认#F1F3F5
        legendShow: true, //图例是否展示  --默认展示true
        action: true, //监听x轴（点击label）
        legend: ['当前人数占比', '对比全网人群', '负面占比'], //必选参数
        xAxis: ['18-24', '25-29', '30-34', '35-39', '40-44', '45+'],
        yAxis: [
            ['8.2', '10', '10', '11', '4', '13', '6.3', 7, 7, 8, 7, 0, 1],
            [10, 7, 8, 8, 7, 9, 8, 7, 7, 8, 7, 3, 5],
            ['8.2', '10', '10', '11', '4', '13', '6.3']
        ],
        color: ['#1d428a', '#ff9d00', '#97d2fe'] //柱子颜色 必填参数
    }


    var _this = this;
    var action = data.action || false
    this.activeId = action ? 0 : -1
    var symbol = data.symbol || ' '

    let xAxis = data.xAxis

    // 保留一位小数，可选择性使用
    function utilNumDecimal(x) {
        if (x == 0) return '0.0'
        if (!x) return '-'
        if (isNaN(x)) {
            return '--';
        }
        let f = Math.round(x * 10) / 10;
        let s = f.toString();
        let rs = s.indexOf('.');
        if (rs < 0) {
            rs = s.length;
            s += '.';
        }
        while (s.length <= rs + 1) {
            s += '0';
        }
        return s;
    }

    var myData = (function test() {

        let yAxis = data.yAxis
        let legend = data.legend
        let seriesLabel = data.seriesLabel === false ? false : true
        let seriesArr = []
        let legendArr = []

        yAxis && yAxis.forEach((item, index) => {
            legendArr.push({
                name: legend[index]
            })

            var tempArr = [];
            let num = '';
            item.forEach((value, _) => {
                if (value || value === 0) {
                    num = value
                } else {
                    num = 'null';
                }
                tempArr.push(num);
            })

            seriesArr.push({
                name: legend[index],
                type: 'bar',
                barGap: .4,
                data: tempArr,
                barCategoryGap: '2%',
                barWidth: data.barWidth || 12,
                label: {
                    normal: {
                        show: seriesLabel,
                        formatter: function(data) {
                            return utilNumDecimal(data.value)
                        },
                        position: 'top',
                        textStyle: {
                            color: '#414957',
                            fontStyle: 'normal',
                            fontFamily: '微软雅黑',
                            textAlign: 'left',
                            fontSize: 11,
                        },
                    },
                },
                itemStyle: { //图形样式
                    normal: {
                        color: data.color[index]
                    },
                }
            })
        })
        return {
            seriesArr,
            legendArr
        }

    })()

    // 初始化echart实例，获取dom
    let dom = echarts.init(document.getElementById(id));
    console.log()
        //下面是配置
    var option = {
            backgroundColor: '#fff',
            tooltip: {
                trigger: 'axis',
                formatter: function(params) {
                    var time = '';
                    var str = '';
                    for (var i of params) {
                        time = i.name.replace(/\n/g, '') + '<br/>';
                        if (i.data == 'null' || i.data == null) {
                            str += '<span style="height: 10px;width: 10px;display: inline-block;border-radius: 50%;background:' +
                                data.color[i.seriesIndex] + '"></span> ' + i.seriesName + '：无数据' + '<br/>'
                        } else {
                            str += '<span style="height: 10px;width: 10px;display: inline-block;border-radius: 50%;background:' +
                                data.color[i.seriesIndex] + '"></span> ' + i.seriesName + '：' + i.data + symbol + '<br/>'
                        }

                    }
                    return time + str;
                },
                axisPointer: {
                    type: 'none'
                }
            },
            grid: {
                left: '0%',
                right: '0%',
                top: '10%',
                bottom: '0%',
                containLabel: true
            },
            xAxis: {
                type: 'category',
                data: xAxis,
                axisTick: {
                    show: false,
                },
                triggerEvent: false,
                axisLine: {
                    show: false
                },
                axisLabel: {
                    show: true,
                    interval: '0',
                    textStyle: {
                        color: '#687284',
                        align: 'center',
                        whiteSpace: 'wrap',
                        lineHeight: 15,
                        height: 50,
                        fontSize: 10
                    },
                    color: '#687284',
                },

            },
            yAxis: {
                scale: false,
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                axisLabel: {
                    show: false,
                    textStyle: {
                        color: '#687284'
                    }
                },
                splitLine: {
                    show: false,
                    lineStyle: { // 属性lineStyle（详见lineStyle）控制线条样式
                        color: data.ysplitLine || '#F1F3F5',
                        type: 'solid'
                    },
                },
            },
            series: myData.seriesArr
        }
        //使用刚指定的配置项和数据显示图表
    dom.setOption(option);
}