#ifndef HEADER_H
#define HEADER_H

unsigned long returnFactorial(unsigned short num);
//  尽量不要在头文件中进行赋值操作，如果非要赋值，请使用以下方式
//  static const 使变量不会被重复定义
static const unsigned short headerNum = 5;

#endif