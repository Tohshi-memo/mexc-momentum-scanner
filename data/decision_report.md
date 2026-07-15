# Decision Report

- generated_at: 2026-07-15T13:11:14.574757+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8743**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8743, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.40% | **-1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 10/20 | 50.0% | +4.56% | **+2.28%** |
| LIMIT_8PCT | 9/20 | 45.0% | +4.38% | **+1.97%** |
| LIMIT_9PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 11/20 | 55.0% | +1.42% | **+0.78%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +4.16% | **+2.78%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +3.62% | **+2.71%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.79% | **+2.65%** |
| MARKET_LONG | 20/20 | 100.0% | +2.29% | **+2.29%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.64% | **+2.00%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 98件 (TP 34 / SL 62 / EXP 2)
- 最新: MAGMA/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.63** / 初期 $100.00 (+242.63%)
- 確定: 2879件 (Win 901 / Loss 935 / Flat 1043) / skip 2425件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAVE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.82% 残高後 $342.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.14** / 初期 $100.00 (+6.14%)
- 確定: 708件 (Win 167 / Loss 166 / Flat 375) / skip 1446件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1441 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RAVE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 62件 (Win 19 / Loss 39 / Flat 4) / pending 2件 / skip 152件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000329 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAVE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-15T13:11:08.498528+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=65304.0
- Funnel: target 871 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +260.66% | $23,208,465.89 |
| US/USDT:USDT | +39.29% | $5,741,640.67 |
| DODO/USDT:USDT | +37.60% | $11,622,418.99 |
| AEHRSTOCK/USDT:USDT | +35.99% | $4,143,062.86 |
| RAVE/USDT:USDT | +18.56% | $3,136,334.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AEHRSTOCK/USDT:USDT | below_1h_threshold | +3.09% | +2.83% |
| ONDO/USDT:USDT | below_1h_threshold | +1.75% | +1.49% |
| RAVE/USDT:USDT | below_1h_threshold | +1.63% | +1.37% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.45% | +1.19% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.44% | +1.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
