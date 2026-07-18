# Decision Report

- generated_at: 2026-07-18T00:41:24.677682+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8901**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.18% / filled 20/20。**
- 全期間 MARKET基準: n=8901, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.31% | **+0.66%** |
| LIMIT_BB3S | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.73% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.77% | **+0.80%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.11% | **+0.67%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.74% | **+0.44%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.58% | **+0.40%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$368.54** / 初期 $100.00 (+268.54%)
- 確定: 3016件 (Win 938 / Loss 958 / Flat 1120) / skip 2446件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $368.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$112.09** / 初期 $100.00 (+12.09%)
- 確定: 863件 (Win 203 / Loss 174 / Flat 486) / skip 1449件
- 成長率目線: 平均log +0.000132 / 幾何平均 +0.013% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0727 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $112.09

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.71** / 初期 $100.00 (-0.29%)
- 確定: 159件 (Win 51 / Loss 85 / Flat 23) / pending 6件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000179 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $99.71

## 6. Latest Market Context

- 更新: 2026-07-18T00:41:16.587448+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63896.2
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.9 >= 65=1, 4h RSI 71.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +53.25% | $10,569,461.53 |
| AKE/USDT:USDT | +19.87% | $49,065,930.42 |
| CASHCAT/USDT:USDT | +15.71% | $1,223,115.26 |
| BANK/USDT:USDT | +11.28% | $21,604,641.94 |
| CRO/USDT:USDT | +8.02% | $2,278,229.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +2.88% | +2.90% |
| PI/USDT:USDT | below_1h_threshold | +2.80% | +2.81% |
| PYTH/USDT:USDT | below_1h_threshold | +2.73% | +2.74% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +2.14% | +2.16% |
| DODO/USDT:USDT | below_1h_threshold | +1.43% | +1.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
