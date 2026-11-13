# chopin-ksu-kernel

Redmi Note 10 Pro 5G（chopin / MT6893）内核编译仓库：在 MIUI 14（V14.0.8.0.TKPCNXM，Android 13，内核 4.14.186-gaa24d707761c）的**设备原厂内核配置**基础上，集成 **KernelSU v0.9.5** 内核态支持，产出可直接替换 boot 分区 kernel 段的 `Image.gz`。

## 为什么是 v0.9.5

KernelSU 自 v1.0 起停止官方支持非 GKI 内核（[issue #1705](https://github.com/tiann/KernelSU/issues/1705)），官方文档明确「最后一个支持非 GKI 的版本是 v0.9.5」。本机是 4.14.186 非 GKI，因此内核侧与 Manager APK 都用 v0.9.5，协议版本对齐（`KSU_VERSION=11872`）。

## 产物要求（唯一硬指标）

- 内核版本串：`Linux version 4.14.186-gaa24d707761c`
- vermagic：`4.14.186-gaa24d707761c SMP preempt mod_unload modversions aarch64`
- 与设备 `/vendor/lib/modules/*.ko`（wlan / bt / fpsgo 等）的 vermagic 完全一致，否则 vendor 模块拒绝加载

`CONFIG_LOCALVERSION="-gaa24d707761c"` + 关闭 `CONFIG_LOCALVERSION_AUTO` + 删掉内核树 `.git`（防止 setlocalversion 追加 `-dirty`/`+`）三件事共同锁死 vermagic。

## 目录

- `.github/workflows/build.yml` — 编译流水线（proton-clang 优先，apt clang-12 兜底）
- `payload.tar.gz` — 内含 `ksu095.tar.gz`（KernelSU v0.9.5 kernel 目录，改名 `kernelsu`）与 `kernel_config`（设备 `/proc/config.gz` 解出的原厂配置）

## 触发

```bash
gh workflow run build.yml -R xiaofan6ya/chopin-ksu-kernel -f mode=full
gh run list -R xiaofan6ya/chopin-ksu-kernel --limit 3
```

`mode=check` 只跑到「只编译 kernelsu 驱动」，用于 5–8 分钟内确认 KSU 代码与 4.14 API 是否兼容。