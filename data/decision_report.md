# Decision Report

- generated_at: 2026-06-08T02:36:33.935953+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6023**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6023, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.01% | **+0.60%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_BB3S | 3/18 | 16.7% | +1.48% | **+0.25%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.97% | **+0.44%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$99.07** / 初期 $100.00 (-0.93%)
- 確定トレード: 6件 (TP 1 / SL 4 / EXP 1)
- 最新: LUNC/USDT:USDT EXPIRED PnL +0.53% 残高後 $99.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$153.11** / 初期 $100.00 (+53.11%)
- 確定: 1140件 (Win 279 / Loss 347 / Flat 514) / skip 1444件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $153.11

## 4. Latest Market Context

- 更新: 2026-06-08T02:36:30.558636+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.44% price=62911.3
- Funnel: target 773 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EPIC/USDT:USDT | +32.39% | $1,715,261.97 |
| PIPPIN/USDT:USDT | +22.81% | $6,495,674.79 |
| BEAT/USDT:USDT | +22.50% | $93,816,872.31 |
| BLESS/USDT:USDT | +21.80% | $8,457,817.96 |
| ESPORTS/USDT:USDT | +21.15% | $5,894,094.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.20% | +4.64% |
| LUNC/USDT:USDT | below_1h_threshold | +2.40% | +2.83% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.24% | +2.68% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.88% | +2.32% |
| HYPE/USDT:USDT | below_1h_threshold | +1.41% | +1.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
