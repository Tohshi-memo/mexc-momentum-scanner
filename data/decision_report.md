# Decision Report

- generated_at: 2026-07-20T09:01:13.016277+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9102**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9102, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.14% | **-1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +1.89% | **+0.76%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_BB3S | 4/16 | 25.0% | +0.35% | **+0.09%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.19% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +7.79% | **+3.90%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.39% | **+1.92%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.44% | **+0.65%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.72% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$401.86** / 初期 $100.00 (+301.86%)
- 確定: 3164件 (Win 988 / Loss 1003 / Flat 1173) / skip 2499件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $401.86

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.73** / 初期 $100.00 (+26.73%)
- 確定: 1063件 (Win 276 / Loss 218 / Flat 569) / skip 1450件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0605 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $126.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.82** / 初期 $100.00 (+0.82%)
- 確定: 301件 (Win 99 / Loss 133 / Flat 69) / pending 5件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000201 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $100.82

## 6. Latest Market Context

- 更新: 2026-07-20T09:01:05.451611+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=64032.6
- Funnel: target 884 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +109.75% | $13,679,815.40 |
| BANK/USDT:USDT | +60.52% | $109,438,215.42 |
| EVAA/USDT:USDT | +31.13% | $5,507,839.70 |
| PROM/USDT:USDT | +22.04% | $3,082,753.64 |
| PUMPFUN/USDT:USDT | +18.25% | $25,990,028.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SONYSTOCK/USDT:USDT | below_1h_threshold | +1.38% | +1.38% |
| B/USDT:USDT | below_1h_threshold | +1.20% | +1.20% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.74% | +0.74% |
| MARSTOCK/USDT:USDT | below_1h_threshold | +0.74% | +0.74% |
| TSEMSTOCK/USDT:USDT | below_1h_threshold | +0.64% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
