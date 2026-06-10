# Decision Report

- generated_at: 2026-06-10T13:30:42.733285+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6215**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6215, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.95% | **+0.59%** |
| ASK | 20/20 | 100.0% | +0.36% | **+0.36%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.17% | **+1.09%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.10% | **+0.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.09% | **+0.76%** |
| ASK_LONG | 20/20 | 100.0% | +0.68% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.00** / 初期 $100.00 (+49.00%)
- 確定: 1229件 (Win 306 / Loss 384 / Flat 539) / skip 1547件
- 成長率目線: 平均log +0.000324 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $149.00

## 4. Latest Market Context

- 更新: 2026-06-10T13:30:40.154784+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=61659.4
- Funnel: target 785 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +54.57% | $17,051,944.63 |
| MAGMA/USDT:USDT | +44.36% | $1,958,880.14 |
| ESPORTS/USDT:USDT | +43.41% | $26,466,512.66 |
| BLEND/USDT:USDT | +33.42% | $2,255,595.87 |
| BTW/USDT:USDT | +30.72% | $32,647,308.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.76% | +4.56% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.84% | +2.63% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +2.65% | +2.44% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.52% | +2.32% |
| UB/USDT:USDT | below_1h_threshold | +2.31% | +2.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
