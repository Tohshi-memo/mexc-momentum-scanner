# Decision Report

- generated_at: 2026-06-10T11:44:42.004849+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6212**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6212, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.68% | **+0.67%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.17% | **+1.09%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.56% | **+0.36%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.75** / 初期 $100.00 (+49.75%)
- 確定: 1228件 (Win 306 / Loss 383 / Flat 539) / skip 1545件
- 成長率目線: 平均log +0.000329 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLEND/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $149.75

## 4. Latest Market Context

- 更新: 2026-06-10T11:44:38.657629+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.58% price=60995.9
- Funnel: target 785 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +52.49% | $13,096,154.19 |
| MAGMA/USDT:USDT | +40.48% | $1,075,544.71 |
| BLEND/USDT:USDT | +36.24% | $1,800,556.76 |
| ESPORTS/USDT:USDT | +35.59% | $27,612,702.39 |
| KAT/USDT:USDT | +23.26% | $1,157,377.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.57% | +5.14% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.91% | +4.48% |
| H/USDT:USDT | below_1h_threshold | +3.34% | +3.91% |
| USOIL/USDT:USDT | below_1h_threshold | +2.20% | +2.77% |
| UKOIL/USDT:USDT | below_1h_threshold | +2.12% | +2.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
