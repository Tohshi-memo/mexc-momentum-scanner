# Decision Report

- generated_at: 2026-06-12T04:21:42.429576+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6454**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6454, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.71% | **-0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.08% | **+0.70%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.94% | **+0.33%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.13% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| MARKET_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.31% | **+0.85%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.93% | **+0.74%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.94% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$95.65** / 初期 $100.00 (-4.35%)
- 確定トレード: 16件 (TP 2 / SL 13 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$153.70** / 初期 $100.00 (+53.70%)
- 確定: 1330件 (Win 347 / Loss 427 / Flat 556) / skip 1685件
- 成長率目線: 平均log +0.000323 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $153.70

## 4. Latest Market Context

- 更新: 2026-06-12T04:21:39.600652+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=63638.4
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +94.88% | $136,835,815.31 |
| XPL/USDT:USDT | +28.05% | $5,424,569.35 |
| H/USDT:USDT | +23.93% | $39,001,962.42 |
| NAORIS/USDT:USDT | +22.45% | $1,562,539.42 |
| SKYAI/USDT:USDT | +21.60% | $13,879,217.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_relative_strength | +5.16% | +4.92% |
| ESPORTS/USDT:USDT | below_1h_threshold | +4.24% | +4.01% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.70% | +2.46% |
| SPACE/USDT:USDT | below_1h_threshold | +1.59% | +1.36% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.41% | +1.18% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
