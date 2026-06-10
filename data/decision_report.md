# Decision Report

- generated_at: 2026-06-10T09:24:18.600452+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6206**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6206, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.39% | **+0.15%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.80% | **+2.80%** |
| ASK_LONG | 20/20 | 100.0% | +2.10% | **+2.10%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +2.28% | **+1.37%** |
| LIMIT_ATR_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +2.04% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$153.55** / 初期 $100.00 (+53.55%)
- 確定: 1222件 (Win 306 / Loss 378 / Flat 538) / skip 1545件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $153.55

## 4. Latest Market Context

- 更新: 2026-06-10T09:24:15.634277+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.57% price=60881.9
- Funnel: target 785 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +47.28% | $10,116,847.47 |
| ESPORTS/USDT:USDT | +37.55% | $26,164,419.66 |
| KAT/USDT:USDT | +23.82% | $1,042,351.90 |
| UB/USDT:USDT | +21.46% | $2,476,743.77 |
| BEAT/USDT:USDT | +17.67% | $102,135,493.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.35% | +2.92% |
| UB/USDT:USDT | below_1h_threshold | +2.17% | +2.74% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.24% | +1.81% |
| WLFI/USDT:USDT | below_1h_threshold | +1.07% | +1.64% |
| BEAT/USDT:USDT | below_1h_threshold | +0.90% | +1.47% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
