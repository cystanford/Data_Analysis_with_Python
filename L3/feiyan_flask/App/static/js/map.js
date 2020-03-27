//世界地图
function echartsWorld(scales, data) {
    var mapName = 'world'
    //console.log(data);    
    let scales1 = echarts.init(document.getElementById(scales));
    var option = {
        //滑入的弹窗
        tooltip: {
            trigger: 'item',
            triggerOn: 'mousemove',
            backgroundColor: 'rgba(0,0,0,.8)',
            show: true,
            formatter: function(params) {
            	if (isNaN(params.value)) {params.value=0;}
            	//console.log(params.value);
                var tipHtml = `<div style="width:100px;height:50px;background:rgba(227,227,227,0.1);">
                <div style="width:100%;height:20px; text-align:center;">
                    <span style="color:#fff;font-size:16px;">${params.name}</span>
                </div>
                <div style="">
                    <p style="color:#fff;font-size:12px;">
                         累计确诊：
                        <span style="color:#11ee7d;">${params.value}</span>人</p>
                </div>
            </div>
            </div>`
                return tipHtml;
            }
        },
        backgroundColor: "#ffffff",
        visualMap: {
            type: 'piecewise',
            //  根据数据大小跳转颜色
            pieces: [{max: 0,label: '0人',color: '#A9A9A9'}, // 灰色
                {min: 1, max: 9,label: '1-9人',color: '#FFD194'},
                {min: 10, max: 99,label: '1-9人',color: '#FFC085'},
                {min: 100, max: 499, label: '100-499人',color: '#FFA769'},
                {min: 500, max: 999, label: '500-999人',color: '#FF8E59'},
                {min: 1000, max: 9999, label: '1000-9999人',color: '#FF7859'},
                {min: 10000,label: '10000人以上',color: '#FF6250'},
            ],
            color: '#000',
            textStyle: {
                color: '#000',
            },
            visibility: 'off'
        },
        geo: {
            map: 'world',
            zoom: 1.2,
            roam: false,
            label: {
                normal: {
                    show: false,
                    color: '#fff'
                },
                emphasis: {
                    show: true,
                    color: '#fff'
                }
            },
            itemStyle: {
                normal: {
                    areaColor: '#A9A9A9',
                    borderColor: '#fff',
                },
                emphasis: {
                    areaColor: '#FA8072'
                }
            }
        },
        series: [{
            type: 'map',
            mapType: 'world',
            geoIndex: 0,
            data: data,
            label: {
                normal: {
                    show: true,
                    textStyle: {
                        color: '#000',
                        fontSize: 11,
                    }
                }
            },
            zlevel: 5,
        }, ]
    };
    scales1.setOption(option);
}

// 韩国地图
function echartsKorea(scales, data) {
    var mapName = 'korea';
    let scales1 = echarts.init(document.getElementById(scales));
    //console.log(scales1);

    var option = {
        //滑入的弹窗
        tooltip: {
            trigger: 'item',
            triggerOn: 'mousemove',
            backgroundColor: 'rgba(0,0,0,.8)',
            show: true,
            formatter: function(params) {
            	if (isNaN(params.value)) {params.value=0;}
                var tipHtml = `<div style="width:100px;height:50px;background:rgba(227,227,227,0.1);">
                <div style="width:100%;height:20px; text-align:center;">
                    <span style="color:#fff;font-size:16px;">${params.name}</span>
                </div>
                <div style="">
                    <p style="color:#fff;font-size:12px;">
                         累计确诊：
                        <span style="color:#11ee7d;">${params.value}</span>人</p>
                </div>
            </div>
            </div>`
                return tipHtml;
            }
        },
        backgroundColor: "#ffffff", 
        visualMap: {
            type: 'piecewise',
            //  根据数据大小跳转颜色
            pieces: [{max: 0,label: '0人',color: '#A9A9A9'}, // 灰色
                {min: 1, max: 9,label: '1-9人',color: '#FFD194'},
                {min: 10, max: 99,label: '1-9人',color: '#FFC085'},
                {min: 100, max: 499, label: '100-499人',color: '#FFA769'},
                {min: 500, label: '500-999人',color: '#FF8E59'},
            ],
            color: '#000',
            textStyle: {
                color: '#000',
            },
            visibility: 'off'
        },
        geo: {
            map: 'korea',
            zoom: 1.2,
            roam: false,
            label: {
                normal: {
                    show: false,
                    color: '#fff'
                },
                emphasis: {
                    show: true,
                    color: '#fff'
                }
            },
            itemStyle: {
                normal: {
                    areaColor: '#A9A9A9',
                    borderColor: '#fff',
                },
                emphasis: {
                    areaColor: '#FA8072'
                }
            }
        },
        series: [{
            type: 'map',
            mapType: 'korea',
            geoIndex: 0,
            data: data,
            label: {
                normal: {
                    show: false,
                    textStyle: {
                        color: '#000',
                        fontSize: 11,
                    }
                }
            },
            zlevel: 5,
        }, ]
    };
    scales1.setOption(option);
}

// 日本地图
function echartsJapan(scales, data) {
    var mapName = 'japan';
    let scales1 = echarts.init(document.getElementById(scales));
    var option = {
        //滑入的弹窗
        tooltip: {
            trigger: 'item',
            triggerOn: 'mousemove',
            backgroundColor: 'rgba(0,0,0,.8)',
            show: true,
            formatter: function(params) {
            	if (isNaN(params.value)) {params.value=0;}
                var tipHtml = `<div style="width:100px;height:50px;background:rgba(227,227,227,0.1);">
                <div style="width:100%;height:20px; text-align:center;">
                    <span style="color:#fff;font-size:16px;">${params.name}</span>
                </div>
                <div style="">
                    <p style="color:#fff;font-size:12px;">
                         累计确诊：
                        <span style="color:#11ee7d;">${params.value}</span>人</p>
                </div>
            </div>
            </div>`
                return tipHtml;
            }
        },
        backgroundColor: "#ffffff",
        visualMap: {
            type: 'piecewise',
            //  根据数据大小跳转颜色
            pieces: [{max: 0,label: '0人',color: '#A9A9A9'}, // 灰色
                {min: 1, max: 9,label: '1-9人',color: '#FFD194'},
                {min: 10, max: 99,label: '1-9人',color: '#FFC085'},
                {min: 100, max: 499, label: '100-499人',color: '#FFA769'},
                {min: 500, label: '500-999人',color: '#FF8E59'},
            ],
            color: '#000',
            textStyle: {
                color: '#000',
            },
            visibility: 'off'
        },
        geo: {
            map: 'japan',
            zoom: 1.2,
            roam: false,
            label: {
                normal: {
                    show: false,
                    color: '#fff'
                },
                emphasis: {
                    show: true,
                    color: '#fff'
                }
            },
            itemStyle: {
                normal: {
                    areaColor: '#A9A9A9',
                    borderColor: '#fff',
                },
                emphasis: {
                    areaColor: '#FA8072'
                }
            }
        },
        series: [{
            type: 'map',
            mapType: 'japan',
            geoIndex: 0,
            data: data,
            label: {
                normal: {
                    show: true,
                    textStyle: {
                        color: '#000',
                        fontSize: 11,
                    }
                }
            },
            zlevel: 5,
        }, ]
    };
    scales1.setOption(option);
}

// 意大利地图
function echartsItaly(scales, data) {
    var mapName = 'italy';
    let scales1 = echarts.init(document.getElementById(scales));
    var option = {
        //滑入的弹窗
        tooltip: {
            trigger: 'item',
            triggerOn: 'mousemove',
            backgroundColor: 'rgba(0,0,0,.8)',
            show: true,
            formatter: function(params) {
            	if (isNaN(params.value)) {params.value=0;}
                var tipHtml = `<div style="width:100px;height:50px;background:rgba(227,227,227,0.1);">
                <div style="width:100%;height:20px; text-align:center;">
                    <span style="color:#fff;font-size:16px;">${params.name}</span>
                </div>
                <div style="">
                    <p style="color:#fff;font-size:12px;">
                         累计确诊：
                        <span style="color:#11ee7d;">${params.value}</span>人</p>
                </div>
            </div>
            </div>`
                return tipHtml;
            }
        },
        backgroundColor: "#ffffff",
        visualMap: {
            type: 'piecewise',
            //  根据数据大小跳转颜色
            pieces: [{max: 0,label: '0人',color: '#A9A9A9'}, // 灰色
                {min: 1, max: 9,label: '1-9人',color: '#FFD194'},
                {min: 10, max: 99,label: '1-9人',color: '#FFC085'},
                {min: 100, max: 499, label: '100-499人',color: '#FFA769'},
                {min: 500, label: '500-999人',color: '#FF8E59'},
            ],
            color: '#000',
            textStyle: {
                color: '#000',
            },
            visibility: 'off'
        },
        geo: {
            map: 'italy',
            zoom: 1.2,
            roam: false,
            label: {
                normal: {
                    show: false,
                    color: '#fff'
                },
                emphasis: {
                    show: true,
                    color: '#fff'
                }
            },
            itemStyle: {
                normal: {
                    areaColor: '#A9A9A9',
                    borderColor: '#fff',
                },
                emphasis: {
                    areaColor: '#FA8072'
                }
            }
        },
        series: [{
            type: 'map',
            mapType: 'italy',
            geoIndex: 0,
            data: data,
            label: {
                normal: {
                    show: true,
                    textStyle: {
                        color: '#000',
                        fontSize: 11,
                    }
                }
            },
            zlevel: 5,
        }, ]
    };
    scales1.setOption(option);
}

