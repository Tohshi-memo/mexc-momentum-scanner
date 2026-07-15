# Decision Report

- generated_at: 2026-07-15T13:26:14.771748+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8744**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8744, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.80% | **-0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 9/20 | 45.0% | +4.18% | **+1.88%** |
| LIMIT_8PCT | 8/20 | 40.0% | +3.93% | **+1.57%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_6PCT | 10/20 | 50.0% | +1.37% | **+0.69%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.82% | **+2.11%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.93% | **+2.05%** |
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +2.88% | **+1.73%** |
| MARKET_LONG | 20/20 | 100.0% | +1.69% | **+1.69%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 98件 (TP 34 / SL 62 / EXP 2)
- 最新: MAGMA/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.63** / 初期 $100.00 (+242.63%)
- 確定: 2879件 (Win 901 / Loss 935 / Flat 1043) / skip 2426件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAVE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.82% 残高後 $342.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.14** / 初期 $100.00 (+6.14%)
- 確定: 709件 (Win 167 / Loss 166 / Flat 376) / skip 1446件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1420 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: B3/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 62件 (Win 19 / Loss 39 / Flat 4) / pending 2件 / skip 153件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000329 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAVE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-15T13:26:08.939336+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=65250.2
- Funnel: target 871 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +263.82% | $24,403,365.81 |
| DODO/USDT:USDT | +43.97% | $11,897,607.16 |
| US/USDT:USDT | +39.33% | $5,886,526.23 |
| AEHRSTOCK/USDT:USDT | +35.26% | $4,178,803.64 |
| RAVE/USDT:USDT | +20.41% | $3,304,905.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +3.32% | +3.15% |
| DODO/USDT:USDT | below_1h_threshold | +3.17% | +2.99% |
| AEHRSTOCK/USDT:USDT | below_1h_threshold | +3.09% | +2.91% |
| PEPE/USDT:USDT | below_1h_threshold | +2.62% | +2.44% |
| AKE/USDT:USDT | below_1h_threshold | +2.17% | +1.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
