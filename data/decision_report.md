# Decision Report

- generated_at: 2026-08-16T02:46:20.532195+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11711**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.83% / filled 20/20。**
- 全期間 MARKET基準: n=11711, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +3.29% | **+2.96%** |
| LIMIT_ATR | 14/20 | 70.0% | +3.68% | **+2.57%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.40% | **+2.28%** |
| LIMIT_3PCT | 14/20 | 70.0% | +3.15% | **+2.21%** |
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.65% | **+0.36%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.43% | **+0.22%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$636.77** / 初期 $100.00 (+536.77%)
- 確定: 4177件 (Win 1292 / Loss 1357 / Flat 1528) / skip 4095件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.01% 残高後 $636.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.37** / 初期 $100.00 (+55.37%)
- 確定: 1765件 (Win 493 / Loss 414 / Flat 858) / skip 3357件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0440 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $155.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 1626件 (Win 495 / Loss 618 / Flat 513) / pending 0件 / skip 1555件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000105 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: H/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-08-16T02:46:11.994504+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=63110.6
- Funnel: target 985 → liquid 136 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPORTFUN/USDT:USDT | +19.27% | $4,234,688.98 |
| CROSS/USDT:USDT | +13.24% | $1,234,138.44 |
| H/USDT:USDT | +13.07% | $6,283,129.79 |
| BASED/USDT:USDT | +10.66% | $1,740,602.94 |
| AIO/USDT:USDT | +10.22% | $2,757,333.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIO/USDT:USDT | below_1h_threshold | +4.60% | +4.51% |
| US/USDT:USDT | below_1h_threshold | +3.81% | +3.72% |
| ROBO/USDT:USDT | below_1h_threshold | +3.57% | +3.47% |
| PRL/USDT:USDT | below_1h_threshold | +2.18% | +2.08% |
| H/USDT:USDT | below_1h_threshold | +1.02% | +0.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
