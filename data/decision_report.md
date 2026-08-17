# Decision Report

- generated_at: 2026-08-17T06:36:24.645905+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11808**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.91% / filled 20/20。**
- 全期間 MARKET基準: n=11808, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.13% | **+1.02%** |
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.91% | **+0.82%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.12% | **+0.50%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 9/9 | 100.0% | +3.68% | **+3.68%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.98% | **+0.49%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 185件 (TP 71 / SL 109 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4184件 (Win 1292 / Loss 1363 / Flat 1529) / skip 4185件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.52** / 初期 $100.00 (+55.52%)
- 確定: 1814件 (Win 502 / Loss 425 / Flat 887) / skip 3405件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $155.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.37** / 初期 $100.00 (+18.37%)
- 確定: 1672件 (Win 503 / Loss 635 / Flat 534) / pending 0件 / skip 1605件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000321 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GPS/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $118.37

## 6. Latest Market Context

- 更新: 2026-08-17T06:36:16.140663+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=63569.4
- Funnel: target 986 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GPS/USDT:USDT | +40.72% | $5,027,124.50 |
| PORTAL/USDT:USDT | +28.23% | $16,946,733.05 |
| TUT/USDT:USDT | +21.95% | $7,510,495.88 |
| ONG/USDT:USDT | +10.90% | $1,376,944.18 |
| HFT/USDT:USDT | +10.56% | $2,684,915.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AEON1/USDT:USDT | below_1h_threshold | +4.18% | +4.05% |
| CHIP/USDT:USDT | below_1h_threshold | +3.94% | +3.81% |
| ZEC/USDT:USDT | below_1h_threshold | +3.68% | +3.55% |
| KORU/USDT:USDT | below_1h_threshold | +2.26% | +2.13% |
| SNXX/USDT:USDT | below_1h_threshold | +2.02% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
