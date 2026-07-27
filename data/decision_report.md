# Decision Report

- generated_at: 2026-07-27T10:31:19.444426+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9624**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9624, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +3.28% | **+1.64%** |
| LIMIT_4PCT | 15/20 | 75.0% | +1.87% | **+1.40%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.96% | **+1.19%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.96% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.81% | **+2.11%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.60% | **+2.08%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.00% | **+1.40%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.32% | **+1.12%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.96% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$458.27** / 初期 $100.00 (+358.27%)
- 確定: 3415件 (Win 1083 / Loss 1112 / Flat 1220) / skip 2770件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.74% 残高後 $458.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1812件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0017 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.74** / 初期 $100.00 (+8.74%)
- 確定: 647件 (Win 215 / Loss 245 / Flat 187) / pending 2件 / skip 445件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000351 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $108.74

## 6. Latest Market Context

- 更新: 2026-07-27T10:31:12.666664+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=65334.4
- Funnel: target 901 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +46.26% | $39,840,341.25 |
| ON/USDT:USDT | +39.04% | $4,849,835.70 |
| BTW/USDT:USDT | +32.32% | $2,990,002.31 |
| DIA/USDT:USDT | +32.00% | $10,880,782.76 |
| NIL/USDT:USDT | +29.16% | $2,521,938.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZAMA/USDT:USDT | below_1h_threshold | +2.62% | +2.47% |
| BTW/USDT:USDT | below_1h_threshold | +2.05% | +1.90% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.52% | +1.37% |
| TAG/USDT:USDT | below_1h_threshold | +1.11% | +0.96% |
| B/USDT:USDT | below_1h_threshold | +0.98% | +0.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
