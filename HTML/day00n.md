### 表格居中与合并 ###
- 知识点
	- 居中：align="center"
	- 横向合并：colspan="3"
	- 纵向合并：rowspan="2"

###  
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>表格居中与合并</title>
	</head>
	<body border="0">
		<table border="1">
			<tr>
				<td rowspan="2" align="center">排序方法</td>
				<td colspan="3" align="center">时间复杂度</td>
				<td rowspan="2">稳定性</td>
				<td rowspan="2">代码复杂度</td>
			</tr>
			<tr>
				<td>最坏情况</td>
				<td>平均情况</td>
				<td>最好情况</td>
			</tr>
			<tr>
				<td>冒泡排序</td>
				<td>O(n^2)</td>
				<td>O(n^2)</td>
				<td>O(n)</td>
				<td>稳定</td>
				<td>简单</td>
			</tr>
			<tr>
				<td>直接选择排序</td>
				<td>O(n^2)</td>
				<td>O(n^2)</td>
				<td>O(n^2)</td>
				<td>不稳定</td>
				<td>简单</td>
			</tr>
			<tr>
				<td>直接插入排序</td>
				<td>O(n^2)</td>
				<td>O(n^2)</td>
				<td>O(n^2)</td>
				<td>稳定</td>
				<td>简单</td>
			</tr>
			<tr>
				<td>快速排序</td>
				<td>O(n^2)</td>
				<td>O(nlogn)</td>
				<td>O(nlogn)</td>
				<td>不稳定</td>
				<td>较复杂</td>
			</tr>
			<tr>
				<td>堆排序</td>
				<td>O(nlogn)</td>
				<td>O(nlogn)</td>
				<td>O(nlogn)</td>
				<td>不稳定</td>
				<td>复杂</td>
			</tr>
			<tr>
				<td>归并排序</td>
				<td>O(nlogn)</td>
				<td>O(nlogn)</td>
				<td>O(nlogn)</td>
				<td>稳定</td>
				<td>较复杂</td>
			</tr>
			<tr>
				<td>希尔排序</td>
				<td></td>
				<td>O(1.3n)</td>
				<td></td>
				<td>不稳定</td>
				<td>较复杂</td>
			</tr>
		</table>
	</body>
	</html>