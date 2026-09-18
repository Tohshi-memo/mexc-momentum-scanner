# Decision Report

- generated_at: 2026-09-18T21:56:39.233804+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14950**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=14950, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.25% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.18% | **+1.75%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.43% | **+1.29%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.09% | **+0.71%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,192.04** / 初期 $100.00 (+1092.04%)
- 確定: 5610件 (Win 1683 / Loss 1816 / Flat 2111) / skip 5901件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,192.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$241.67** / 初期 $100.00 (+141.67%)
- 確定: 3173件 (Win 878 / Loss 757 / Flat 1538) / skip 5188件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1915 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $241.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.52** / 初期 $100.00 (+23.52%)
- 確定: 2962件 (Win 879 / Loss 1167 / Flat 916) / pending 0件 / skip 3466件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000559 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $123.52

## 6. Latest Market Context

- 更新: 2026-09-18T21:56:23.724414+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=81194.3
- Funnel: target 1050 → liquid 170 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.0 >= 65=1, 4h RSI 83.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +74.95% | $27,496,174.72 |
| SYN/USDT:USDT | +22.70% | $5,982,788.33 |
| SAGA/USDT:USDT | +22.08% | $4,126,671.52 |
| STRK/USDT:USDT | +19.95% | $8,258,990.28 |
| USELESS/USDT:USDT | +18.60% | $7,567,186.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STRK/USDT:USDT | below_1h_threshold | +3.47% | +3.34% |
| NEAR/USDT:USDT | below_1h_threshold | +3.44% | +3.30% |
| AR/USDT:USDT | below_1h_threshold | +3.26% | +3.13% |
| CNPY/USDT:USDT | below_1h_threshold | +3.19% | +3.06% |
| 1000BONK/USDT:USDT | below_1h_threshold | +3.02% | +2.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
