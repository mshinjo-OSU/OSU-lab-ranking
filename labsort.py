{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red245\green245\blue245;\red0\green0\blue0;
\red86\green65\blue25;\red0\green0\blue109;\red144\green1\blue18;\red131\green0\blue165;\red19\green85\blue52;
\red15\green112\blue1;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c96863\c96863\c96863;\cssrgb\c0\c0\c0;
\cssrgb\c41569\c32157\c12941;\cssrgb\c0\c6275\c50196;\cssrgb\c63922\c8235\c8235;\cssrgb\c59216\c13725\c70588;\cssrgb\c6667\c40000\c26667;
\cssrgb\c0\c50196\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 def\cf0 \strokec4  \cf5 \strokec5 compare_labs\cf0 \strokec4 (\cf6 \strokec6 lab1\cf0 \strokec4 , \cf6 \strokec6 lab2\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 """\uc0\u12518 \u12540 \u12470 \u12540 \u12395 2\u12388 \u12398 \u30740 \u31350 \u23460 \u12434 \u27604 \u36611 \u12373 \u12379 \u12390 \u12289 \u12393 \u12385 \u12425 \u12364 \u19978 \u12363 \u12434 \u36820 \u12377 \u12290 """\cf0 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 while\cf0 \strokec4  \cf2 \strokec2 True\cf0 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 print\cf0 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\\n\uc0\u12393 \u12385 \u12425 \u12398 \u30740 \u31350 \u23460 \u12395 \u12424 \u12426 \u33288 \u21619 \u12364 \u12354 \u12426 \u12414 \u12377 \u12363 \u65311 "\cf0 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 print\cf0 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "1: \cf0 \strokec4 \{lab1\}\cf7 \strokec7 "\cf0 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 print\cf0 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "2: \cf0 \strokec4 \{lab2\}\cf7 \strokec7 "\cf0 \strokec4 )\cb1 \
\cb3         choice = \cf5 \strokec5 input\cf0 \strokec4 (\cf7 \strokec7 "\uc0\u36984 \u25246 \u32930 \u65288 1 or 2\u65289 : "\cf0 \strokec4 )\cb1 \
\cb3         \cf8 \strokec8 if\cf0 \strokec4  choice == \cf7 \strokec7 "1"\cf0 \strokec4 :\cb1 \
\cb3             \cf8 \strokec8 return\cf0 \strokec4  lab1\cb1 \
\cb3         \cf8 \strokec8 elif\cf0 \strokec4  choice == \cf7 \strokec7 "2"\cf0 \strokec4 :\cb1 \
\cb3             \cf8 \strokec8 return\cf0 \strokec4  lab2\cb1 \
\cb3         \cf8 \strokec8 else\cf0 \strokec4 :\cb1 \
\cb3             \cf5 \strokec5 print\cf0 \strokec4 (\cf7 \strokec7 "\uc0\u28961 \u21177 \u12394 \u20837 \u21147 \u12391 \u12377 \u12290 1 \u12363  2 \u12434 \u20837 \u21147 \u12375 \u12390 \u12367 \u12384 \u12373 \u12356 \u12290 "\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  \cf5 \strokec5 merge_sort_with_user\cf0 \strokec4 (\cf6 \strokec6 labs\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 """\uc0\u12518 \u12540 \u12470 \u12540 \u12398 \u27604 \u36611 \u12395 \u22522 \u12389 \u12356 \u12390 \u30740 \u31350 \u23460 \u12434 \u12477 \u12540 \u12488 \u12377 \u12427 \u12290 """\cf0 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 if\cf0 \strokec4  \cf5 \strokec5 len\cf0 \strokec4 (labs) <= \cf9 \strokec9 1\cf0 \strokec4 :\cb1 \
\cb3         \cf8 \strokec8 return\cf0 \strokec4  labs\cb1 \
\
\cb3     mid = \cf5 \strokec5 len\cf0 \strokec4 (labs) // \cf9 \strokec9 2\cf0 \cb1 \strokec4 \
\cb3     left = merge_sort_with_user(labs[:mid])\cb1 \
\cb3     right = merge_sort_with_user(labs[mid:])\cb1 \
\
\cb3     merged = []\cb1 \
\cb3     i = j = \cf9 \strokec9 0\cf0 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 while\cf0 \strokec4  i < \cf5 \strokec5 len\cf0 \strokec4 (left) \cf2 \strokec2 and\cf0 \strokec4  j < \cf5 \strokec5 len\cf0 \strokec4 (right):\cb1 \
\cb3         winner = compare_labs(left[i], right[j])\cb1 \
\cb3         \cf8 \strokec8 if\cf0 \strokec4  winner == left[i]:\cb1 \
\cb3             merged.append(left[i])\cb1 \
\cb3             i += \cf9 \strokec9 1\cf0 \cb1 \strokec4 \
\cb3         \cf8 \strokec8 else\cf0 \strokec4 :\cb1 \
\cb3             merged.append(right[j])\cb1 \
\cb3             j += \cf9 \strokec9 1\cf0 \cb1 \strokec4 \
\
\cb3     merged.extend(left[i:])\cb1 \
\cb3     merged.extend(right[j:])\cb1 \
\cb3     \cf8 \strokec8 return\cf0 \strokec4  merged\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 # \uc0\u30740 \u31350 \u23460 \u12398 \u12522 \u12473 \u12488 \u65288 \u12471 \u12515 \u12483 \u12501 \u12523 \u12375 \u12390 \u12362 \u12367 \u12392 \u20559 \u12426 \u12364 \u28187 \u12427 \u65311 \u65289 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 import\cf0 \strokec4  random\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 labs = [\cb1 \
\cb3     \cf7 \strokec7 "\uc0\u21513 \u24029 \u30740 \u31350 \u23460 \u65288 \u12503 \u12521 \u12452 \u12496 \u12471 \u12540 \u20445 \u35703 \u25216 \u34899 \u65289 "\cf0 \strokec4 ,\cb1 \
\cb3     \cf7 \strokec7 "\uc0\u23567 \u23665 \u30000 \u30740 \u31350 \u23460 \u65288 \u21487 \u35222 \u21270 \u24773 \u22577 \u23398 \u65289 "\cf0 \strokec4 , \cb1 \
\cb3     \cf7 \strokec7 "\uc0\u21407 \u30740 \u31350 \u23460 \u65288 \u12452 \u12494 \u12505 \u12540 \u12471 \u12519 \u12531 \u12539 \u12510 \u12493 \u12472 \u12513 \u12531 \u12488 \u65289 "\cf0 \strokec4 , \cb1 \
\cb3     \cf7 \strokec7 "\uc0\u37772 \u21407 \u30740 \u31350 \u23460 \u65288 \u12452 \u12531 \u12479 \u12540 \u12493 \u12483 \u12488 \u12450 \u12503 \u12522 \u12465 \u12540 \u12471 \u12519 \u12531 \u65289 "\cf0 \strokec4 ,\cb1 \
\cb3     \cf7 \strokec7 "\uc0\u31520 \u21407 \u30740 \u31350 \u23460 \u65288 \u35251 \u20809 \u24773 \u22577 \u23398 \u65289 "\cf0 \strokec4 ,\cb1 \
\cb3     \cf7 \strokec7 "\uc0\u26441 \u23665 \u30740 \u31350 \u23460 \u65288 \u24773 \u22577 \u26908 \u32034 \u12539 \u33258 \u28982 \u35328 \u35486 \u20966 \u29702 \u65289 "\cf0 \strokec4 ,\cb1 \
\cb3     \cf7 \strokec7 "\uc0\u23665 \u35199 \u30740 \u31350 \u23460 \u65288 \u29983 \u20307 \u24773 \u22577 \u23398 \u65289 "\cf0 \strokec4 ,\cb1 \
\cb3     \cf7 \strokec7 "\uc0\u21129 \u30740 \u31350 \u23460 \u65288 CAE\u65306 \u35336 \u31639 \u27231 \u25588 \u29992 \u24037 \u23398 \u65289 "\cf0 \strokec4 , \cb1 \
\cb3     \cf7 \strokec7 "\uc0\u19978 \u23713 \u30740 \u31350 \u23460 \u65288 \u25968 \u12360 \u19978 \u12370 \u32068 \u21512 \u12379 \u35542 \u65289 "\cf0 \strokec4 , \cb1 \
\cb3     \cf7 \strokec7 "\uc0\u20304 \u12293 \u26408 \u30740 \u31350 \u23460 \u65288 \u12498 \u12517 \u12540 \u12510 \u12531 \u12467 \u12531 \u12500 \u12517 \u12540 \u12479 \u12452 \u12531 \u12479 \u12521 \u12463 \u12471 \u12519 \u12531 \u65289 "\cf0 \strokec4 , \cb1 \
\cb3     \cf7 \strokec7 "\uc0\u38364 \u25144 \u30740 \u31350 \u23460 \u65288 \u23455 \u39443 \u35336 \u30011 \u27861 \u65289 "\cf0 \strokec4 , \cb1 \
\cb3     \cf7 \strokec7 "\uc0\u22799 \u24029 \u30740 \u31350 \u23460 \u65288 \u24773 \u22577 \u21487 \u35222 \u21270 \u12539 \u12473 \u12509 \u12540 \u12484 \u12487 \u12540 \u12479 \u31185 \u23398 \u65289 "\cf0 \strokec4 , \cb1 \
\cb3     \cf7 \strokec7 "\uc0\u19978 \u38442 \u30740 \u31350 \u23460 \u65288 \u35336 \u37327 \u25991 \u29486 \u23398 \u65289 "\cf0 \strokec4 , \cb1 \
\cb3     \cf7 \strokec7 "\uc0\u26032 \u24196 \u30740 \u31350 \u23460 \u65288 \u12467 \u12531 \u12500 \u12517 \u12540 \u12479 \u25968 \u23398 \u65289 "\cf0 \cb1 \strokec4 \
\cb3 ]\cb1 \
\cb3 random.shuffle(labs)\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 # \uc0\u12477 \u12540 \u12488 \u38283 \u22987 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 print\cf0 \strokec4 (\cf7 \strokec7 "=== \uc0\u30740 \u31350 \u23460 \u33288 \u21619 \u24230 \u12521 \u12531 \u12461 \u12531 \u12464 \u35519 \u26619  ==="\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 sorted_labs = merge_sort_with_user(labs)\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 # \uc0\u32080 \u26524 \u34920 \u31034 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 print\cf0 \strokec4 (\cf7 \strokec7 "\\n=== \uc0\u12354 \u12394 \u12383 \u12398 \u33288 \u21619 \u38918 \u12521 \u12531 \u12461 \u12531 \u12464  ==="\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 for\cf0 \strokec4  i, lab \cf2 \strokec2 in\cf0 \strokec4  \cf5 \strokec5 enumerate\cf0 \strokec4 (sorted_labs, \cf9 \strokec9 1\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf5 \strokec5 print\cf0 \strokec4 (\cf2 \strokec2 f\cf7 \strokec7 "\cf0 \strokec4 \{i\}\cf7 \strokec7 \uc0\u20301 : \cf0 \strokec4 \{lab\}\cf7 \strokec7 "\cf0 \strokec4 )}