# Decision Report

- generated_at: 2026-06-04T04:29:51.923576+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5600**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.62% / filled 20/20。**
- 全期間 MARKET基準: n=5600, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.62% | **+2.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.80% | **+2.80%** |
| MARKET | 20/20 | 100.0% | +2.62% | **+2.62%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.54% | **+2.29%** |
| LIMIT_ATR | 11/20 | 55.0% | +2.37% | **+1.30%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.89% | **+1.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -0.07% | **-0.02%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -1.48% | **-0.74%** |

## 2. $100 Live Portfolio

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定トレード: 94件 (TP 29 / SL 62 / EXP 3)
- 最新: ICP/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.04
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1005件 (Win 239 / Loss 312 / Flat 454) / skip 1156件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LIT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T04:29:49.141621+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=64588.7
- Funnel: target 771 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +27.17% | $24,612,585.95 |
| EPIC/USDT:USDT | +22.19% | $3,902,594.48 |
| BP/USDT:USDT | +21.05% | $1,592,241.55 |
| STO/USDT:USDT | +18.25% | $7,091,544.03 |
| HEI/USDT:USDT | +13.43% | $1,027,709.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +3.12% | +2.73% |
| HEI/USDT:USDT | below_1h_threshold | +2.43% | +2.04% |
| EPIC/USDT:USDT | below_1h_threshold | +1.51% | +1.12% |
| WLFI/USDT:USDT | below_1h_threshold | +1.31% | +0.91% |
| EDGE/USDT:USDT | below_1h_threshold | +1.11% | +0.72% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
