# Decision Report

- generated_at: 2026-09-23T09:21:29.081391+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15423**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.89% / filled 20/20。**
- 全期間 MARKET基準: n=15423, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.89% | **+0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +2.44% | **+1.71%** |
| LIMIT_3PCT | 14/20 | 70.0% | +2.34% | **+1.64%** |
| LIMIT_BB3S | 6/11 | 54.5% | +2.66% | **+1.45%** |
| LIMIT_5PCT | 6/20 | 30.0% | +4.83% | **+1.45%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.52% | **+1.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.77% | **+1.50%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.69% | **+1.27%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +1.73% | **+1.21%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.27% | **+1.08%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.75% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,203.81** / 初期 $100.00 (+1103.81%)
- 確定: 5894件 (Win 1739 / Loss 1889 / Flat 2266) / skip 6090件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAKE/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,203.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.23** / 初期 $100.00 (+148.23%)
- 確定: 3372件 (Win 930 / Loss 788 / Flat 1654) / skip 5462件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0192 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $248.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.73** / 初期 $100.00 (+21.73%)
- 確定: 3135件 (Win 923 / Loss 1233 / Flat 979) / pending 1件 / skip 3761件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000168 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZAMA/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $121.73

## 6. Latest Market Context

- 更新: 2026-09-23T09:21:17.799947+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=85892.5
- Funnel: target 1061 → liquid 189 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAKE/USDT:USDT | +213.08% | $3,819,931.27 |
| SHROOM/USDT:USDT | +66.77% | $1,345,100.14 |
| MET/USDT:USDT | +32.18% | $1,123,253.72 |
| ALLO/USDT:USDT | +26.45% | $3,161,542.31 |
| PENGU/USDT:USDT | +19.36% | $19,398,923.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_relative_strength | +5.00% | +4.98% |
| GRASS/USDT:USDT | below_1h_threshold | +2.98% | +2.96% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.26% | +2.24% |
| SHROOM/USDT:USDT | below_1h_threshold | +2.11% | +2.09% |
| INJ/USDT:USDT | below_1h_threshold | +1.94% | +1.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
