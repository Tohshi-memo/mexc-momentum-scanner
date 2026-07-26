# Decision Report

- generated_at: 2026-07-26T09:11:12.840497+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9568**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9568, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.54% | **-0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.04% | **+0.76%** |
| LIMIT_BB3S | 3/18 | 16.7% | +2.88% | **+0.48%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.26% | **+0.44%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.08% | **+0.31%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.23% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.94% | **+5.94%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.04% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +2.57% | **+0.64%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.15% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$459.42** / 初期 $100.00 (+359.42%)
- 確定: 3396件 (Win 1078 / Loss 1103 / Flat 1215) / skip 2733件
- 成長率目線: 平均log +0.000449 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $459.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$138.20** / 初期 $100.00 (+38.20%)
- 確定: 1221件 (Win 338 / Loss 273 / Flat 610) / skip 1758件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0859 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $138.20

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.85** / 初期 $100.00 (+8.85%)
- 確定: 611件 (Win 206 / Loss 234 / Flat 171) / pending 2件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000316 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.85

## 6. Latest Market Context

- 更新: 2026-07-26T09:11:06.095840+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64475.7
- Funnel: target 898 → liquid 118 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +63.22% | $38,673,485.17 |
| DIA/USDT:USDT | +43.10% | $2,327,553.69 |
| PIEVERSE/USDT:USDT | +41.74% | $4,127,889.35 |
| BANK/USDT:USDT | +23.56% | $92,432,223.00 |
| SHIB/USDT:USDT | +17.07% | $76,346,756.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.60% | +3.56% |
| RIF/USDT:USDT | below_1h_threshold | +2.49% | +2.45% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.05% | +1.01% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.90% | +0.86% |
| VVV/USDT:USDT | below_1h_threshold | +0.84% | +0.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
