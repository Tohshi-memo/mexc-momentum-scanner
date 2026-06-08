# Decision Report

- generated_at: 2026-06-08T02:42:12.726837+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6024**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6024, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.01% | **+0.60%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_BB3S | 3/18 | 16.7% | +1.48% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.44% | **+1.11%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.29% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$99.07** / 初期 $100.00 (-0.93%)
- 確定トレード: 6件 (TP 1 / SL 4 / EXP 1)
- 最新: LUNC/USDT:USDT EXPIRED PnL +0.53% 残高後 $99.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.34** / 初期 $100.00 (+52.34%)
- 確定: 1141件 (Win 279 / Loss 348 / Flat 514) / skip 1444件
- 成長率目線: 平均log +0.000369 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $152.34

## 4. Latest Market Context

- 更新: 2026-06-08T02:42:09.662324+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=62989.0
- Funnel: target 773 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +24.39% | $94,271,120.37 |
| PIPPIN/USDT:USDT | +22.88% | $6,515,159.96 |
| ESPORTS/USDT:USDT | +21.44% | $5,919,864.73 |
| ALLO/USDT:USDT | +20.85% | $43,102,614.30 |
| EPIC/USDT:USDT | +20.41% | $1,768,605.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.89% | +3.20% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.30% | +2.61% |
| NEAR/USDT:USDT | below_1h_threshold | +2.20% | +2.52% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.03% | +2.34% |
| EWY/USDT:USDT | below_1h_threshold | +1.81% | +2.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
