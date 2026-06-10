# Decision Report

- generated_at: 2026-06-10T07:01:02.061504+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6190**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6190, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +5.40% | **+1.62%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.50% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.06% | **+1.06%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.42% | **+0.93%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.04% | **+0.92%** |
| ASK_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.04** / 初期 $100.00 (+49.04%)
- 確定: 1206件 (Win 300 / Loss 376 / Flat 530) / skip 1545件
- 成長率目線: 平均log +0.000331 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $149.04

## 4. Latest Market Context

- 更新: 2026-06-10T07:00:59.456675+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=61438.4
- Funnel: target 781 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +41.36% | $6,403,893.53 |
| BTW/USDT:USDT | +26.76% | $29,088,561.18 |
| UB/USDT:USDT | +14.14% | $1,831,257.31 |
| BEAT/USDT:USDT | +12.10% | $107,582,730.52 |
| UAI/USDT:USDT | +10.76% | $1,465,269.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAHARA/USDT:USDT | below_1h_threshold | +1.16% | +1.16% |
| STG/USDT:USDT | below_1h_threshold | +0.61% | +0.61% |
| OP/USDT:USDT | below_1h_threshold | +0.32% | +0.31% |
| BTW/USDT:USDT | below_1h_threshold | +0.27% | +0.26% |
| UAI/USDT:USDT | below_1h_threshold | +0.25% | +0.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
