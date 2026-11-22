# Decision Report

- generated_at: 2026-11-22T07:11:17.506051+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19362**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.53% / filled 20/20。**
- 全期間 MARKET基準: n=19362, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.53% | **+0.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/17 | 52.9% | +3.40% | **+1.80%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.27% | **+1.21%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.78% | **+1.16%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.34% | **+1.01%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.45% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.16% | **+1.40%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.49% | **+1.12%** |
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +1.19% | **+1.07%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,778.01** / 初期 $100.00 (+1678.01%)
- 確定: 7481件 (Win 2149 / Loss 2408 / Flat 2924) / skip 8442件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ENSO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,778.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$448.15** / 初期 $100.00 (+348.15%)
- 確定: 5127件 (Win 1364 / Loss 1102 / Flat 2661) / skip 7646件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0285 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DCTY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $448.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000301 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T07:11:06.311110+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=59132.4
- Funnel: target 1086 → liquid 106 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +28.29% | $2,209,887.72 |
| PIEVERSE/USDT:USDT | +24.26% | $6,736,267.65 |
| DCTY/USDT:USDT | +20.24% | $1,703,380.01 |
| BLESS/USDT:USDT | +18.17% | $57,554,025.88 |
| SKYAI/USDT:USDT | +16.08% | $1,736,540.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MMT/USDT:USDT | below_1h_threshold | +4.70% | +4.69% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.51% | +4.50% |
| BTW/USDT:USDT | below_1h_threshold | +0.58% | +0.57% |
| KORU/USDT:USDT | below_1h_threshold | +0.24% | +0.23% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +0.18% | +0.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
