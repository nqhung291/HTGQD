export function mappingObject(input) {
  const list = []
  input.forEach(element => {
    list.push({
      id: element['STT'],
      name: element['Họ tên'],
      point1: element['Điểm 1'],
      point2: element['Điểm 2'],
      point3: element['Điểm 3'],
      point4: element['Điểm 4'],
      point5: element['Điểm 5'],
      point6: element['Điểm 6'],
      point7: element['Điểm 7'],
      point8: element['Điểm 8'],
      point9: element['Điểm 9'],
      point10: element['Điểm 10']
    })
  })

  return list
}
