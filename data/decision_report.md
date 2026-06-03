# Decision Report

- generated_at: 2026-06-03T00:45:02.775607+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5509**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=5509, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.43% | **+1.43%** |
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.67% | **+0.47%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.52% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.23% | **+0.23%** |
| MARKET_LONG | 20/20 | 100.0% | +0.18% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 977件 (Win 229 / Loss 300 / Flat 448) / skip 1093件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-03T00:45:00.400484+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.47% price=67046.6
- Funnel: target 771 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +39.18% | $13,220,308.76 |
| GENIUS/USDT:USDT | +20.61% | $1,119,218.86 |
| LIT/USDT:USDT | +18.48% | $6,927,848.29 |
| BBSTOCK/USDT:USDT | +16.51% | $1,825,997.78 |
| ESPORTS/USDT:USDT | +15.31% | $8,080,610.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GENIUS/USDT:USDT | below_1h_threshold | +4.94% | +4.46% |
| ZEC/USDT:USDT | below_1h_threshold | +4.32% | +3.85% |
| NEAR/USDT:USDT | below_1h_threshold | +4.19% | +3.72% |
| H/USDT:USDT | below_1h_threshold | +3.91% | +3.44% |
| MYX/USDT:USDT | below_1h_threshold | +3.20% | +2.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
