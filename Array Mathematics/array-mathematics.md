 I just wanted to add some notes regarding reshaping in python since I am not able to wrap my head around it quick enough.

 ```
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)
```
- This would convert the 12 element array into an array of 4 rows and 3 elements.<br>
![image](https://github.com/user-attachments/assets/fee50e3c-d4d9-4c6d-a51d-5972f1f06f38)

> [!WARNING]
> I am just showing various outputs for the same initial array. They are not performed in sequence

`newarr = arr.reshape(1,-1)`
This converts the array into a row-wise 2d matrix as follows: <br>
![image](https://github.com/user-attachments/assets/40bd2fe5-8f19-470d-b13c-d597a8d23f24)

`newarr = arr.reshape(-1,1)`
Output:<br>
![image](https://github.com/user-attachments/assets/5f275bfb-01f7-48ac-9ee0-083cc924f469)

`newarr = arr.reshape(6,2)`
<br>
![image](https://github.com/user-attachments/assets/ac4b4af7-cfda-4efb-99f6-3b8f6bf822ff)

`newarr = arr.reshape(2, 2,-1)` <br>
![image](https://github.com/user-attachments/assets/1db754ec-aacd-48c6-b29f-980e4d7be465)

-Actually there's a lot of variations. I am finding myself confused so I suppose we'd have to try them all to get an understanding how the transformations will be. All the best! 😅

