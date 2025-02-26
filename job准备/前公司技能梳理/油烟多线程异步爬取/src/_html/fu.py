class FuHtml:
    text = """
<!DOCTYPE _html>
<_html>
  <head>
    <title>油烟系统-油烟数据</title>
	<meta http-equiv="pragma" content="no-cache"/>
	<meta http-equiv="cache-control" content="no-cache"/>
	<meta http-equiv="expires" content="0"/>    
	<meta name="robots" content="nofollow" />
	<link href="../css/jquery-ui/jquery-ui-1.10.4.custom.min.css" rel="stylesheet" type="text/css" />
	<link href="../css/sys.css" rel="stylesheet" type="text/css" />
	<script type="text/javascript" src="../js/jquery-3.6.0.min.js"></script><script type="text/javascript" src="../js/jquery-migrate-3.3.2.min.js"></script>
	<script type="text/javascript" src="../js/jquery-ui-1.10.4.custom.min.js"></script>
	<script type="text/javascript" src="../js/sys.js"></script>
	<script type="text/javascript" src="../js/work.js"></script>
<script type="text/javascript">
	page_url="yyRealTimeValue_list.jsp";
	link1_name="油烟系统",link2_name="油烟数据",link2_url="yyRealTimeValue_list.jsp";
</script>
 </head>
<body>

<div class="clear">
	<select id="sel_area" class="float_l border_b" style="width:140px;margin-top:8px;margin-left:5px;" onchange="dataResift('area',$(this).val())">
		<option value="all">全部地区</option>
		
			<option value='785' >徐汇区</option>
		
			<option value='3888' >徐家汇街道</option>
		
			<option value='3889' >湖南路街道</option>
		
			<option value='3890' >天平路街道</option>
		
			<option value='3891' >枫林路街道</option>
		
			<option value='3892' >斜土路街道</option>
		
			<option value='3894' >康健新村街道</option>
		
			<option value='3895' >虹梅路街道</option>
		
			<option value='3896' >田林街道</option>
		
			<option value='3897' >凌云路街道</option>
		
			<option value='3898' >龙华街道</option>
		
			<option value='3899' >华泾镇</option>
		
			<option value='3903' >漕河泾新兴技术开发区</option>
		
			<option value='3893' >长桥街道</option>
		
			<option value='3900' >漕河泾街道</option>
		
	</select>
	<select id="sel_supplier" class="float_l border_b" style="margin-top:8px;margin-left:5px;" onchange="dataResift('supplier',$(this).val())">
		<option value="all">全部供应商</option>
	
			<option value='1' >供应商公用调试</option>
	
			<option value='2' >开发公司调试帐号</option>
	
			<option value='3' >上海广聆环保科技</option>
	
			<option value='5' >上海政宝环保科技</option>
	
			<option value='7' >上海中映信息科技</option>
	
			<option value='8' >上海富程环保工程</option>
	
			<option value='9' >上海勤世环保科技</option>
	
			<option value='10' >上海卓荃电子科技</option>
	
			<option value='11' >衡智远科技（深圳）</option>
	
			<option value='12' >无锡锐丰源环境科技</option>
	
			<option value='13' >上海龙涤环保技术工程</option>
	
			<option value='14' >上海辉瀚环保科技</option>
	
			<option value='15' >上海景瑄环保科技</option>
	
			<option value='16' >上海叶榕环保设备工程</option>
	
			<option value='17' >山东威盟士科技</option>
	
			<option value='18' >上海茂净环境科技</option>
	
			<option value='19' >上海汇星辰餐饮</option>
	
			<option value='20' >北京万维盈创科技发展</option>
	
			<option value='21' >埃尔斯虏森空气净化系统(上海)</option>
	
			<option value='22' >上海厨亦安设备安装工程</option>
	
	</select>
	<select class="float_l border_b" style="margin-top:8px;margin-left:5px;" onchange="dataResift('idx',$(this).val())">
		<option value="all">全部级别</option>
		<option value="0" >未定义</option>
		<option value="1" >优</option>
		<option value="2" >良</option>
		<option value="3" >中</option>
		<option value="4" >差</option>
	</select>
	<span class="float_l" style="margin-top:6px;margin-left:5px;">需警报：</span>
	<select class="float_l border_b" style="margin-top:8px;" onchange="dataResift('needAlarm',$(this).val())">
		<option value="all">全部</option>
		<option value="1" >是</option>
		<option value="0" >否</option>
	</select>
	<span class="float_l" style="margin-top:6px;margin-left:5px;">已警报：</span>
	<select class="float_l border_b" style="margin-top:8px;" onchange="dataResift('hasAlarm',$(this).val())">
		<option value="all">全部</option>
		<option value="1" >是</option>
		<option value="0" >否</option>
	</select>
	<div class="float_l" style="margin-top:6px;margin-left:5px;">
		<input type="text" class="border_b input_date" id="date1" style="width:85px;position:relative;" value="2024-03-01" readonly="readonly"/>
		-
		<input type="text" class="border_b input_date" id="date2" style="width:85px;position:relative;" value="2024-03-18" readonly="readonly"/>
		&nbsp;
		<a class='cur_poi blue2' onclick="goDateRange('2024-02-01','2024-02-29')" title="2024-02-01~2024-02-29">上月</a>
		&nbsp;
		<a class='cur_poi blue2' onclick="goDateRange('2024-03-11','2024-03-17')" title="2024-03-11~2024-03-17">上周</a>
		&nbsp;
		<a class='cur_poi blue2' onclick="goDateRange('2024-03-01','2024-03-18')" title="2024-04-01~2024-04-30">本月</a>
		&nbsp;
		<a class='cur_poi blue2' onclick="goDateRange('2024-03-25','2024-03-31')" title="2024-03-25~2024-03-31">下周</a>
		&nbsp;
		<a class='cur_poi blue2' onclick="goDateRange('2024-04-01','2024-04-30')" title="2024-04-01~2024-04-30">下月</a>
	</div>
	<div class="float_r" style="margin-right:5px;margin-top:6px;">
		<span class="float_l" style="margin-left:5px;">店名：</span>
		<input id="shop" class="border_b float_l" style="width:100px;height:22px;" value="付小姐在成都"/>
		<span class="float_l" style="margin-left:5px;">设备编号：</span>
		<input id="key1" class="border_b float_l" style="border-right:0px;width:100px;height:22px;" value=""/>
		<input type="button" class="float_l bg_blue4 color_f" style="width:50px;height:24px;border:0px;" value="搜 索" onclick="dataRefind2()"/>
		<div class="clear"></div>
	</div>
	<div class="clear"></div>
</div>
<table class="table_1" style="clear:both;margin-top:5px;">
	<tr class="tr_head">
		<td>地区</td>
		<td>餐饮店/地址</td>
		<td>设备编号/供应商</td>
		<td style="width:70px;">进烟浓度<br/>mg/m³</td>
		<td style="width:70px;">排烟浓度<br/>mg/m³</td>
		<td style="width:60px;">风机电<br/>A</td>
		<td style="width:60px;">净化器<br/>A</td>
		<td style="width:50px;">级别</td>
		<td style="width:50px;">需报警</td>
		<td style="width:50px;">已报警</td>
		<td style="width:140px;">归属时段<br/>上报时间</td>
	    <td style="width:100px;" colspan='2'>基本操作</td>
	</tr>
<tbody>

	<tr id="tr_30664006" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.016</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 22:20<div class='color_a'>2024-03-18 22:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30664006" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30664006,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30663942" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.039</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 22:10<div class='color_a'>2024-03-18 22:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30663942" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30663942,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30663861" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.084</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 22:00<div class='color_a'>2024-03-18 22:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30663861" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30663861,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30663776" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.081</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 21:50<div class='color_a'>2024-03-18 22:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30663776" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30663776,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30663687" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.048</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 21:40<div class='color_a'>2024-03-18 21:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30663687" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30663687,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30663594" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.049</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 21:30<div class='color_a'>2024-03-18 21:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30663594" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30663594,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30663505" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.043</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 21:20<div class='color_a'>2024-03-18 21:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30663505" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30663505,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30663411" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.112</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 21:10<div class='color_a'>2024-03-18 21:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30663411" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30663411,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30663318" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.126</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 21:00<div class='color_a'>2024-03-18 21:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30663318" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30663318,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30663219" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.054</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 20:50<div class='color_a'>2024-03-18 21:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30663219" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30663219,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30663119" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.063</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 20:40<div class='color_a'>2024-03-18 20:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30663119" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30663119,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30663015" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.072</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 20:30<div class='color_a'>2024-03-18 20:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30663015" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30663015,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30662900" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.084</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 20:20<div class='color_a'>2024-03-18 20:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30662900" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30662900,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30662811" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.471</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 20:10<div class='color_a'>2024-03-18 20:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30662811" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30662811,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30662713" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.068</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 20:00<div class='color_a'>2024-03-18 20:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30662713" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30662713,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30662607" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.053</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 19:50<div class='color_a'>2024-03-18 20:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30662607" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30662607,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30662502" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.137</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 19:40<div class='color_a'>2024-03-18 19:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30662502" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30662502,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30662397" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.095</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 19:30<div class='color_a'>2024-03-18 19:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30662397" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30662397,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30662292" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.057</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 19:20<div class='color_a'>2024-03-18 19:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30662292" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30662292,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30662183" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.137</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 19:10<div class='color_a'>2024-03-18 19:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30662183" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30662183,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30662077" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.037</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 19:00<div class='color_a'>2024-03-18 19:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30662077" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30662077,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30661969" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.08</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 18:50<div class='color_a'>2024-03-18 19:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30661969" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30661969,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30661860" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.096</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 18:40<div class='color_a'>2024-03-18 18:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30661860" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30661860,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30661758" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.067</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 18:30<div class='color_a'>2024-03-18 18:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30661758" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30661758,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30661655" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.054</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 18:20<div class='color_a'>2024-03-18 18:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30661655" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30661655,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30661543" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.052</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 18:10<div class='color_a'>2024-03-18 18:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30661543" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30661543,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30661441" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.081</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 18:00<div class='color_a'>2024-03-18 18:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30661441" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30661441,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30661344" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.059</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 17:50<div class='color_a'>2024-03-18 18:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30661344" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30661344,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30661241" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.034</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 17:40<div class='color_a'>2024-03-18 17:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30661241" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30661241,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30661142" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.039</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 17:30<div class='color_a'>2024-03-18 17:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30661142" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30661142,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30661044" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.033</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 17:20<div class='color_a'>2024-03-18 17:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30661044" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30661044,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30660945" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.218</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 17:10<div class='color_a'>2024-03-18 17:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30660945" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30660945,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30660843" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.07</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 17:00<div class='color_a'>2024-03-18 17:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30660843" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30660843,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30660747" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.087</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 16:50<div class='color_a'>2024-03-18 17:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30660747" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30660747,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30660656" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.042</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 16:40<div class='color_a'>2024-03-18 16:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30660656" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30660656,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30660555" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.062</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 16:30<div class='color_a'>2024-03-18 16:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30660555" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30660555,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30660463" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.337</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 16:20<div class='color_a'>2024-03-18 16:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30660463" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30660463,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30660363" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.034</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 16:10<div class='color_a'>2024-03-18 16:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30660363" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30660363,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30660275" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.059</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 16:00<div class='color_a'>2024-03-18 16:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30660275" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30660275,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30660172" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.028</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 15:50<div class='color_a'>2024-03-18 16:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30660172" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30660172,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30660081" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.033</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 15:40<div class='color_a'>2024-03-18 15:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30660081" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30660081,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30659985" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.033</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 15:30<div class='color_a'>2024-03-18 15:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30659985" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30659985,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30659891" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.027</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 15:20<div class='color_a'>2024-03-18 15:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30659891" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30659891,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30659799" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.047</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 15:10<div class='color_a'>2024-03-18 15:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30659799" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30659799,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30659706" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.048</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 15:00<div class='color_a'>2024-03-18 15:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30659706" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30659706,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30659608" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.036</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 14:50<div class='color_a'>2024-03-18 15:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30659608" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30659608,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30659519" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.027</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 14:40<div class='color_a'>2024-03-18 14:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30659519" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30659519,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30659428" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.029</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 14:30<div class='color_a'>2024-03-18 14:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30659428" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30659428,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30659335" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.025</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 14:20<div class='color_a'>2024-03-18 14:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30659335" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30659335,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30659244" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.026</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 14:10<div class='color_a'>2024-03-18 14:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30659244" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30659244,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30659150" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.042</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 14:00<div class='color_a'>2024-03-18 14:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30659150" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30659150,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30659043" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.041</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 13:50<div class='color_a'>2024-03-18 14:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30659043" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30659043,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30658949" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.041</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 13:40<div class='color_a'>2024-03-18 13:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30658949" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30658949,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30658849" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.027</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 13:30<div class='color_a'>2024-03-18 13:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30658849" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30658849,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30658744" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.025</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 13:20<div class='color_a'>2024-03-18 13:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30658744" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30658744,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30658650" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.042</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 13:10<div class='color_a'>2024-03-18 13:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30658650" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30658650,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30658542" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.019</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 13:00<div class='color_a'>2024-03-18 13:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30658542" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30658542,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30658441" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.127</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 12:50<div class='color_a'>2024-03-18 13:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30658441" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30658441,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30658333" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.073</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 12:40<div class='color_a'>2024-03-18 12:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30658333" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30658333,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30658232" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.036</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 12:30<div class='color_a'>2024-03-18 12:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30658232" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30658232,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30658126" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.029</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 12:20<div class='color_a'>2024-03-18 12:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30658126" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30658126,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30658025" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.039</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 12:10<div class='color_a'>2024-03-18 12:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30658025" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30658025,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30657922" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.026</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 12:00<div class='color_a'>2024-03-18 12:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30657922" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30657922,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30657822" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.037</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 11:50<div class='color_a'>2024-03-18 12:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30657822" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30657822,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30657713" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.066</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 11:40<div class='color_a'>2024-03-18 11:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30657713" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30657713,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30657601" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.032</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 11:30<div class='color_a'>2024-03-18 11:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30657601" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30657601,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30657540" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.036</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 11:20<div class='color_a'>2024-03-18 11:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30657540" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30657540,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30657436" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.415</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 11:10<div class='color_a'>2024-03-18 11:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30657436" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30657436,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30657334" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.202</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 11:00<div class='color_a'>2024-03-18 11:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30657334" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30657334,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30657228" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.028</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 10:50<div class='color_a'>2024-03-18 11:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30657228" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30657228,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30657127" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.025</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 10:40<div class='color_a'>2024-03-18 10:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30657127" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30657127,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30657025" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.024</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 10:30<div class='color_a'>2024-03-18 10:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30657025" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30657025,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30656920" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.02</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 10:20<div class='color_a'>2024-03-18 10:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30656920" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30656920,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30656823" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.022</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 10:10<div class='color_a'>2024-03-18 10:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30656823" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30656823,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30656720" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.034</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 10:00<div class='color_a'>2024-03-18 10:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30656720" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30656720,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30656621" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.027</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 09:50<div class='color_a'>2024-03-18 10:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30656621" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30656621,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30656525" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.026</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 09:40<div class='color_a'>2024-03-18 09:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30656525" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30656525,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30656438" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.036</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-18 09:30<div class='color_a'>2024-03-18 09:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30656438" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30656438,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30652608" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.02</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 22:00<div class='color_a'>2024-03-17 22:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30652608" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30652608,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30652514" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.02</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 21:50<div class='color_a'>2024-03-17 22:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30652514" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30652514,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30652421" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.05</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 21:40<div class='color_a'>2024-03-17 21:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30652421" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30652421,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30652324" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.068</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 21:30<div class='color_a'>2024-03-17 21:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30652324" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30652324,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30652225" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.061</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 21:20<div class='color_a'>2024-03-17 21:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30652225" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30652225,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30652125" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.049</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 21:10<div class='color_a'>2024-03-17 21:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30652125" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30652125,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30652013" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.108</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 21:00<div class='color_a'>2024-03-17 21:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30652013" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30652013,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30651954" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.162</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 20:50<div class='color_a'>2024-03-17 21:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30651954" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30651954,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30651881" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.18</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 20:40<div class='color_a'>2024-03-17 20:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30651881" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30651881,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30651781" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.117</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 20:30<div class='color_a'>2024-03-17 20:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30651781" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30651781,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30651683" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.174</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 20:20<div class='color_a'>2024-03-17 20:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30651683" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30651683,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30651582" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.186</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 20:10<div class='color_a'>2024-03-17 20:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30651582" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30651582,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30651459" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.175</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 20:00<div class='color_a'>2024-03-17 20:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30651459" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30651459,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30651369" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.278</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 19:50<div class='color_a'>2024-03-17 20:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30651369" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30651369,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30651266" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.148</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 19:40<div class='color_a'>2024-03-17 19:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30651266" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30651266,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30651160" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.172</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 19:30<div class='color_a'>2024-03-17 19:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30651160" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30651160,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30651062" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.433</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 19:20<div class='color_a'>2024-03-17 19:30</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30651062" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30651062,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30650955" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.251</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 19:10<div class='color_a'>2024-03-17 19:20</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30650955" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30650955,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30650851" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.187</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 19:00<div class='color_a'>2024-03-17 19:10</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30650851" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30650851,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30650743" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.402</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 18:50<div class='color_a'>2024-03-17 19:00</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30650743" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30650743,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30650635" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.277</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 18:40<div class='color_a'>2024-03-17 18:50</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30650635" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30650635,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

	<tr id="tr_30650528" class="tr_default">
	    <td>徐家汇街道</td>
	    <td>
	    	付小姐在成都<div class='color_a'>徐家汇街道殷家角居委会天钥桥路580号</div>   
	    </td>
	    <td>qinshi_31010320210010<div class='color_a'>上海勤世环保科技有限公司</div></td>
	    <td>0</td>
	    <td>0.342</td>
	    <td>0</td>
	    <td>0</td>
	    <td>优</td>
	    <td>否</td>
	    <td>否</td>
	    <td>2024-03-17 18:30<div class='color_a'>2024-03-17 18:40</div></td>
		<td style="width:50px;"><a href="yyRealTimeValue_info.jsp?id=30650528" class='cur_poi blue2'>详情</a></td>
		<td style="width:50px;"><a class='cur_poi blue2 ' onclick="rowDel(30650528,'../yyRealTimeValueDel.php')">删除</a></td>
	</tr>

</tbody>
</table>

<div class='clear align_r color_2' style="margin-top:5px;font-size:14px">
	<input type="button" class='bg_green5 color_f border_d' style="height:24px;width:200px;" value="导出当前搜索条件的全部结果" onclick="dataExcel()"/>
	<span>
	[1]&nbsp;&nbsp;<a class='cur_poi' onclick='gotoPage(2)'>下一页</a>&nbsp;&nbsp;
		第<input id='page' class="border_b" style='width:40px;height:18px;margin-bottom:-1px;margin-left:2px;margin-right:2px;'/>页 <input type='button' class="bg_2 color_f" style='width:30px;height:22px;font-size:12px;' value='Go' onclick='gotoPage()'/>
	</span>
	<select id="sel_pageSize" class="border_b" style="width:80px;" onchange="dataResift('pagesize',$(this).val())">
		<option value="10">10条/页</option>
		<option value="20">20条/页</option>
		<option value="50">50条/页</option>
		<option value="100">100条/页</option>
	</select>
</div>
<div id="shadow" style="z-index:900;display:none;position:fixed;left:0px;top:0px;right:0px;bottom:0px;background-color:#000000;opacity:0.3;filter:alpha(opacity=30);"></div>
<div id="working" class="positionable absolute align_c" style="z-index:999;display:none;border:1px solid #84A0C4;background-color:#ffffff;width:300px;padding:40px 0px">
	<img alt='请稍候' src="../image/pub/working.gif"/>
</div>

  </body>
</_html>
"""