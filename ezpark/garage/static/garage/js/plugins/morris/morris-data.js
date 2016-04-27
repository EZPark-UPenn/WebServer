// Morris.js Charts sample data for SB Admin template

$(function() {

    //Area Chart
    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            date: '2016-04-02',
            sales: 2666
        }, {
            date: '2016-04-03',
            sales: 2778
        }, {
            date: '2016-04-04',
            sales: 4912
        }, {
            date: '2016-04-05',
            sales: 3767
        }, {
            date: '2016-04-06',
            sales: 6810
        }, {
            date: '2016-04-07',
            sales: 5670
        }, {
            date: '2016-04-08',
            sales: 4820
        }, {
            date: '2016-04-09',
            sales: 17073
        }, {
            date: '2016-04-10',
            sales: 10687
        }, {
            date: '2016-04-11',
            sales: 8432
        }, {
            date: '2016-04-12',
            sales: 7810
        }, {
            date: '2016-04-13',
            sales: 5670
        }, {
            date: '2016-04-14',
            sales: 3820
        }, {
            date: '2016-04-15',
            sales: 15073
        }, {
            date: '2016-04-16',
            sales: 10687
        }, {
            date: '2016-04-17',
            sales: 6810
        }, {
            date: '2016-04-18',
            sales: 1670
        }, {
            date: '2016-04-19',
            sales: 4820
        }, {
            date: '2016-04-20',
            sales: 13073
        }, {
            date: '2016-04-21',
            sales: 9687
        }],
        xkey: 'date',
        ykeys: ['sales'],
        labels: ['Sales per Day'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });

    // Bar Chart
    Morris.Bar({
        element: 'morris-bar-chart',
        data: [{
            time: '00:00',
            cars: 236
        }, {
            time: '01:00',
            cars: 136
        }, {
            time: '02:00',
            cars: 50
        }, {
            time: '03:00',
            cars: 20
        }, {
            time: '04:00',
            cars: 23
        }, {
            time: '05:00',
            cars: 112
        },{
            time: '06:00',
            cars: 232
        }, {
            time: '07:00',
            cars: 540
        }, {
            time: '08:00',
            cars: 675
        }, {
            time: '09:00',
            cars: 880
        }, {
            time: '10:00',
            cars: 655
        }, {
            time: '11:00',
            cars: 1023
        }, {
            time: '12:00',
            cars: 1527
        }, {
            time: '13:00',
            cars: 1320
        }, {
            time: '14:00',
            cars: 1271
        }, {
            time: '15:00',
            cars: 1130
        }, {
            time: '16:00',
            cars: 920
        }, {
            time: '17:00',
            cars: 1220
        }, {
            time: '18:00',
            cars: 950
        }, {
            time: '19:00',
            cars: 630
        }, {
            time: '20:00',
            cars: 650
        }, {
            time: '21:00',
            cars: 675
        }, {
            time: '22:00',
            cars: 430
        }, {
            time: '23:00',
            cars: 355
        }],
        xkey: 'time',
        ykeys: ['cars'],
        labels: ['Total Cars in Garage'],
        barRatio: 0.4,
        xLabelAngle: 35,
        hideHover: 'auto',
        resize: true
    });

    // Donut Chart
    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "Download Sales",
            value: 12
        }, {
            label: "In-Store Sales",
            value: 30
        }, {
            label: "Mail-Order Sales",
            value: 20
        }],
        resize: true
    });

    // Line Chart
    Morris.Line({
        // ID of the element in which to draw the chart.
        element: 'morris-line-chart',
        // Chart data records -- each entry in this array corresponds to a point on
        // the chart.
        data: [{
            d: '2012-10-01',
            visits: 802
        }, {
            d: '2012-10-02',
            visits: 783
        }, {
            d: '2012-10-03',
            visits: 820
        }, {
            d: '2012-10-04',
            visits: 839
        }, {
            d: '2012-10-05',
            visits: 792
        }, {
            d: '2012-10-06',
            visits: 859
        }, {
            d: '2012-10-07',
            visits: 790
        }, {
            d: '2012-10-08',
            visits: 1680
        }, {
            d: '2012-10-09',
            visits: 1592
        }, {
            d: '2012-10-10',
            visits: 1420
        }, {
            d: '2012-10-11',
            visits: 882
        }, {
            d: '2012-10-12',
            visits: 889
        }, {
            d: '2012-10-13',
            visits: 819
        }, {
            d: '2012-10-14',
            visits: 849
        }, {
            d: '2012-10-15',
            visits: 870
        }, {
            d: '2012-10-16',
            visits: 1063
        }, {
            d: '2012-10-17',
            visits: 1192
        }, {
            d: '2012-10-18',
            visits: 1224
        }, {
            d: '2012-10-19',
            visits: 1329
        }, {
            d: '2012-10-20',
            visits: 1329
        }, {
            d: '2012-10-21',
            visits: 1239
        }, {
            d: '2012-10-22',
            visits: 1190
        }, {
            d: '2012-10-23',
            visits: 1312
        }, {
            d: '2012-10-24',
            visits: 1293
        }, {
            d: '2012-10-25',
            visits: 1283
        }, {
            d: '2012-10-26',
            visits: 1248
        }, {
            d: '2012-10-27',
            visits: 1323
        }, {
            d: '2012-10-28',
            visits: 1390
        }, {
            d: '2012-10-29',
            visits: 1420
        }, {
            d: '2012-10-30',
            visits: 1529
        }, {
            d: '2012-10-31',
            visits: 1892
        }, ],
        // The name of the data record attribute that contains x-visitss.
        xkey: 'd',
        // A list of names of data record attributes that contain y-visitss.
        ykeys: ['visits'],
        // Labels for the ykeys -- will be displayed when you hover over the
        // chart.
        labels: ['Visits'],
        // Disables line smoothing
        smooth: false,
        resize: true
    });

    


});
