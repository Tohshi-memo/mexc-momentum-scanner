# Decision Report

- generated_at: 2026-05-06T10:32:32.604396+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3443**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3443, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=-1.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.31% | **-1.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.38% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.84% | **+1.47%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.43% | **+1.34%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.67% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.72% | **+0.95%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 5件 (Win 0 / Loss 2 / Flat 3) / skip 0件
- 成長率目線: 平均log -0.002005 / 幾何平均 -0.200% per trade / maxDD +1.00%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $99.00

## 4. Latest Market Context

- 更新: 2026-05-06T10:32:30.081632+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=82147.6
- Funnel: target 769 → liquid 202 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +49.31% | $11,824,893.10 |
| BILL/USDT:USDT | +42.62% | $1,591,299.68 |
| ZEC/USDT:USDT | +34.69% | $756,124,838.84 |
| B3/USDT:USDT | +34.60% | $1,488,047.40 |
| STORJ/USDT:USDT | +33.30% | $2,740,091.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.79% | +4.56% |
| DASH/USDT:USDT | below_1h_threshold | +2.92% | +2.69% |
| STORJ/USDT:USDT | below_1h_threshold | +2.61% | +2.38% |
| ENA/USDT:USDT | below_1h_threshold | +2.57% | +2.34% |
| NEAR/USDT:USDT | below_1h_threshold | +2.41% | +2.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
