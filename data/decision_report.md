# Decision Report

- generated_at: 2026-07-27T05:31:18.342843+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9596**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=9596, expectancy=-0.02%
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
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.92% | **+0.69%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.67% | **+0.47%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.35% | **+0.33%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.08% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$450.30** / 初期 $100.00 (+350.30%)
- 確定: 3400件 (Win 1078 / Loss 1107 / Flat 1215) / skip 2757件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $450.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1784件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0277 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.10** / 初期 $100.00 (+8.10%)
- 確定: 623件 (Win 209 / Loss 239 / Flat 175) / pending 5件 / skip 440件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000230 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.10

## 6. Latest Market Context

- 更新: 2026-07-27T05:31:10.051156+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=65385.7
- Funnel: target 900 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DIA/USDT:USDT | +19.70% | $7,832,888.07 |
| ON/USDT:USDT | +19.18% | $3,597,903.29 |
| AKE/USDT:USDT | +18.37% | $18,978,717.67 |
| BTW/USDT:USDT | +17.98% | $1,123,863.97 |
| 4/USDT:USDT | +17.60% | $2,535,467.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ON/USDT:USDT | below_1h_threshold | +4.51% | +4.32% |
| NIL/USDT:USDT | below_1h_threshold | +2.46% | +2.26% |
| PROM/USDT:USDT | below_1h_threshold | +1.97% | +1.78% |
| BANK/USDT:USDT | below_1h_threshold | +1.79% | +1.59% |
| BOME/USDT:USDT | below_1h_threshold | +1.46% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
