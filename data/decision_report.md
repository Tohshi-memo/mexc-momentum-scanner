# Decision Report

- generated_at: 2026-07-25T14:06:16.173675+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9516**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9516, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/19 | 31.6% | +3.40% | **+1.07%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.60% | **+0.32%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.29% | **+1.94%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.30% | **+1.72%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.19% | **+1.07%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.67% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$437.95** / 初期 $100.00 (+337.95%)
- 確定: 3344件 (Win 1057 / Loss 1083 / Flat 1204) / skip 2733件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $437.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$133.52** / 初期 $100.00 (+33.52%)
- 確定: 1170件 (Win 317 / Loss 254 / Flat 599) / skip 1757件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1623 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $133.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.15** / 初期 $100.00 (+7.15%)
- 確定: 563件 (Win 191 / Loss 216 / Flat 156) / pending 5件 / skip 420件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000528 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $107.15

## 6. Latest Market Context

- 更新: 2026-07-25T14:06:09.442646+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64127.8
- Funnel: target 898 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +62.28% | $10,847,232.87 |
| DEXE/USDT:USDT | +54.05% | $120,856,801.76 |
| AKE/USDT:USDT | +27.00% | $44,507,234.25 |
| ESPORTS/USDT:USDT | +21.68% | $15,935,718.40 |
| PROM/USDT:USDT | +20.13% | $4,885,284.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DEXE/USDT:USDT | below_1h_threshold | +2.93% | +2.95% |
| B2/USDT:USDT | below_1h_threshold | +1.54% | +1.56% |
| SYN/USDT:USDT | below_1h_threshold | +1.32% | +1.33% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.04% | +1.06% |
| UB/USDT:USDT | below_1h_threshold | +1.02% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
