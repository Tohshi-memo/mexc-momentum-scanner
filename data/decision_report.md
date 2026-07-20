# Decision Report

- generated_at: 2026-07-20T03:01:15.335590+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9076**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=9076, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.81% | **+0.73%** |
| LIMIT_BB3S | 2/18 | 11.1% | +5.43% | **+0.60%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.22% | **+0.44%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.05% | **+0.05%** |
| MARKET_LONG | 20/20 | 100.0% | -0.03% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$109.69** / 初期 $100.00 (+9.69%)
- 確定トレード: 119件 (TP 43 / SL 71 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -3.31% 残高後 $109.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$398.82** / 初期 $100.00 (+298.82%)
- 確定: 3138件 (Win 985 / Loss 1001 / Flat 1152) / skip 2499件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.14% 残高後 $398.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.74** / 初期 $100.00 (+25.74%)
- 確定: 1037件 (Win 266 / Loss 218 / Flat 553) / skip 1450件
- 成長率目線: 平均log +0.000221 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0943 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $125.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.90** / 初期 $100.00 (+0.90%)
- 確定: 275件 (Win 94 / Loss 131 / Flat 50) / pending 4件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000179 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $100.90

## 6. Latest Market Context

- 更新: 2026-07-20T03:01:08.818827+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64804.1
- Funnel: target 885 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +50.93% | $89,289,830.04 |
| ACE/USDT:USDT | +45.38% | $3,271,856.98 |
| PUMPFUN/USDT:USDT | +21.59% | $17,030,556.50 |
| PROM/USDT:USDT | +16.54% | $2,143,559.93 |
| ANSEM/USDT:USDT | +14.55% | $1,927,476.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +2.27% | +2.26% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.06% | +2.05% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.18% | +1.17% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.14% | +1.14% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +1.13% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
