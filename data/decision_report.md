# Decision Report

- generated_at: 2026-07-27T05:56:20.554796+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9597**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=9597, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +0.74% | **+0.59%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.59% | **+0.53%** |
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.10% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.92% | **+0.69%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.67% | **+0.47%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.35% | **+0.33%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.21% | **+0.13%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$450.30** / 初期 $100.00 (+350.30%)
- 確定: 3400件 (Win 1078 / Loss 1107 / Flat 1215) / skip 2758件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $450.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1785件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0098 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.10** / 初期 $100.00 (+8.10%)
- 確定: 624件 (Win 209 / Loss 239 / Flat 176) / pending 5件 / skip 440件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CXMTSTOCK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $108.10

## 6. Latest Market Context

- 更新: 2026-07-27T05:56:13.552760+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=65367.9
- Funnel: target 903 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +25.13% | $19,628,931.37 |
| ON/USDT:USDT | +21.35% | $3,800,149.27 |
| BTW/USDT:USDT | +20.58% | $1,219,364.02 |
| DIA/USDT:USDT | +19.03% | $8,094,963.10 |
| 4/USDT:USDT | +15.49% | $2,572,661.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAFE/USDT:USDT | below_1h_threshold | +4.75% | +4.58% |
| PROM/USDT:USDT | below_1h_threshold | +4.20% | +4.03% |
| PEPE/USDT:USDT | below_1h_threshold | +2.47% | +2.30% |
| BTW/USDT:USDT | below_1h_threshold | +2.17% | +2.00% |
| NIL/USDT:USDT | below_1h_threshold | +2.04% | +1.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
