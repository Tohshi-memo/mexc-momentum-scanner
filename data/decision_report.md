# Decision Report

- generated_at: 2026-07-09T07:05:30.881180+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8523**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8523, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.10% | **+0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +3.85% | **+1.16%** |
| LIMIT_7PCT | 7/20 | 35.0% | +1.60% | **+0.56%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| ASK | 20/20 | 100.0% | +0.14% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.62% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_ATR_LONG | 6/20 | 30.0% | +1.08% | **+0.33%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.57% | **+0.31%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$104.09** / 初期 $100.00 (+4.09%)
- 確定トレード: 83件 (TP 30 / SL 52 / EXP 1)
- 最新: NES/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$322.88** / 初期 $100.00 (+222.88%)
- 確定: 2711件 (Win 857 / Loss 907 / Flat 947) / skip 2373件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VANRY/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $322.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1292件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-07-09T07:05:25.754972+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=62922.6
- Funnel: target 851 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +104.85% | $8,168,598.42 |
| VANRY/USDT:USDT | +21.72% | $7,794,193.82 |
| SKYAI/USDT:USDT | +20.94% | $17,462,382.26 |
| CAP/USDT:USDT | +15.86% | $1,902,050.99 |
| BASED/USDT:USDT | +13.02% | $2,485,866.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.04% | +3.06% |
| ANSEM/USDT:USDT | below_1h_threshold | +0.69% | +0.71% |
| TLM/USDT:USDT | below_1h_threshold | +0.61% | +0.63% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.34% | +0.36% |
| BLESS/USDT:USDT | below_1h_threshold | +0.34% | +0.36% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
