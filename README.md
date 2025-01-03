# trapezoidal_correction_of_screen_video

# 屏幕透视变换工具

这个脚本可以对屏幕进行透视变换。通过选择屏幕上的四个点，计算变换矩阵并实时应用，显示变形后的屏幕。

## 安装依赖

```bash
pip install opencv-python numpy pyautogui pillow
```

## 功能简介

1. **捕捉屏幕**：脚本实时捕捉当前屏幕内容，并在窗口中显示。
2. **选择点**：点击屏幕上的四个点，用于计算透视变换矩阵。
3. **应用变换**：选择完点后，实时显示变换后的屏幕。

### 使用步骤

1. 运行脚本，主窗口会显示当前屏幕内容。
2. **点击四个点**，定义透视变换区域。选择的点会被标记为红色圆圈。
3. 选择完四个点后，脚本自动计算透视变换矩阵并实时显示变换后的屏幕。
4. 按 `ESC` 键退出程序。

## 开源协议

该项目开源，使用MIT许可证。

---

