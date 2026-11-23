# Decision Report

- generated_at: 2026-11-23T13:11:32.336128+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19446**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19446, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.40% | **+0.88%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.52% | **+0.42%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.86% | **+1.67%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,886.49** / 初期 $100.00 (+1786.49%)
- 確定: 7544件 (Win 2166 / Loss 2427 / Flat 2951) / skip 8463件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ELSA/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $1,886.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$469.95** / 初期 $100.00 (+369.95%)
- 確定: 5206件 (Win 1386 / Loss 1117 / Flat 2703) / skip 7651件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0588 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ELSA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $469.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7606件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000149 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T13:11:20.829507+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=61211.6
- Funnel: target 1088 → liquid 119 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +88.94% | $2,440,916.41 |
| BULLA/USDT:USDT | +42.13% | $3,384,484.21 |
| ARIA/USDT:USDT | +38.61% | $4,806,411.63 |
| EVAA/USDT:USDT | +30.17% | $39,244,728.82 |
| ELSA/USDT:USDT | +26.31% | $2,613,620.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SI/USDT:USDT | below_1h_threshold | +3.62% | +3.76% |
| ARIA/USDT:USDT | below_1h_threshold | +2.27% | +2.41% |
| EVAA/USDT:USDT | below_1h_threshold | +1.48% | +1.62% |
| ELSA/USDT:USDT | below_1h_threshold | +1.18% | +1.32% |
| ALGO/USDT:USDT | below_1h_threshold | +1.08% | +1.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
