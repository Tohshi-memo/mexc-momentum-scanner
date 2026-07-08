# Decision Report

- generated_at: 2026-07-08T07:39:45.388095+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8470**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.43% / filled 20/20。**
- 全期間 MARKET基準: n=8470, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.43% | **+2.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.43% | **+2.43%** |
| ASK | 20/20 | 100.0% | +1.81% | **+1.81%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_BB3S | 3/19 | 15.8% | +2.64% | **+0.42%** |
| LIMIT_1PCT | 14/20 | 70.0% | +0.34% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.71% | **+0.18%** |
| MARKET_LONG | 20/20 | 100.0% | +0.09% | **+0.09%** |
| ASK_LONG | 20/20 | 100.0% | +0.07% | **+0.07%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | -0.27% | **-0.07%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | -0.60% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$104.11** / 初期 $100.00 (+4.11%)
- 確定トレード: 74件 (TP 27 / SL 46 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT TP_HIT PnL +6.66% 残高後 $104.11
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$320.19** / 初期 $100.00 (+220.19%)
- 確定: 2675件 (Win 848 / Loss 898 / Flat 929) / skip 2356件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNDKSTOCK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $320.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 641件 (Win 152 / Loss 158 / Flat 331) / skip 1240件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-08T07:39:39.583434+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=62742.5
- Funnel: target 847 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +58.54% | $63,820,847.11 |
| EDGE/USDT:USDT | +28.02% | $15,600,874.58 |
| NES/USDT:USDT | +15.85% | $1,246,872.85 |
| SYN/USDT:USDT | +12.37% | $5,193,187.94 |
| CLO/USDT:USDT | +8.81% | $1,235,266.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDGE/USDT:USDT | below_1h_threshold | +2.68% | +2.50% |
| CLO/USDT:USDT | below_1h_threshold | +2.29% | +2.10% |
| SLX/USDT:USDT | below_1h_threshold | +1.58% | +1.40% |
| BTW/USDT:USDT | below_1h_threshold | +1.57% | +1.39% |
| NES/USDT:USDT | below_1h_threshold | +1.50% | +1.32% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
