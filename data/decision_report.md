# Decision Report

- generated_at: 2026-07-27T04:01:16.712675+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9593**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.70% / filled 20/20。**
- 全期間 MARKET基準: n=9593, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.86% | **+1.68%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.94% | **+1.46%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.69% | **+0.48%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | -0.94% | **-0.24%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.28% | **-0.27%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -2.13% | **-0.32%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -1.06% | **-0.48%** |

## 2. $100 Live Portfolio

- 残高: **$107.46** / 初期 $100.00 (+7.46%)
- 確定トレード: 144件 (TP 50 / SL 89 / EXP 5)
- 最新: NIGHT/USDT:USDT TP_HIT PnL +4.75% 残高後 $107.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$450.30** / 初期 $100.00 (+350.30%)
- 確定: 3400件 (Win 1078 / Loss 1107 / Flat 1215) / skip 2754件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $450.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1781件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0073 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.29** / 初期 $100.00 (+8.29%)
- 確定: 620件 (Win 209 / Loss 238 / Flat 173) / pending 6件 / skip 440件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000067 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DIA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $108.29

## 6. Latest Market Context

- 更新: 2026-07-27T04:01:11.083068+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=65256.1
- Funnel: target 898 → liquid 143 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DIA/USDT:USDT | +21.03% | $7,293,440.79 |
| CXMTSTOCK/USDT:USDT | +18.94% | $2,171,727.52 |
| 4/USDT:USDT | +18.19% | $2,440,885.90 |
| AKE/USDT:USDT | +17.34% | $16,805,670.32 |
| UB/USDT:USDT | +14.00% | $4,114,071.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CROSS/USDT:USDT | below_1h_threshold | +0.87% | +0.88% |
| DIA/USDT:USDT | below_1h_threshold | +0.62% | +0.62% |
| UB/USDT:USDT | below_1h_threshold | +0.41% | +0.42% |
| NIL/USDT:USDT | below_1h_threshold | +0.28% | +0.29% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +0.21% | +0.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
