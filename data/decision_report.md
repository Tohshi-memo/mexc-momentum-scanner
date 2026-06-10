# Decision Report

- generated_at: 2026-06-10T14:49:20.978195+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6219**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6219, expectancy=-0.05%
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
| ASK | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.45% | **+0.13%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.09% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.27% | **+1.47%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.20% | **+0.96%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.98% | **+0.84%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.11% | **+0.11%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.20% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.00** / 初期 $100.00 (+49.00%)
- 確定: 1229件 (Win 306 / Loss 384 / Flat 539) / skip 1551件
- 成長率目線: 平均log +0.000324 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $149.00

## 4. Latest Market Context

- 更新: 2026-06-10T14:49:17.897391+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=61918.5
- Funnel: target 785 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.0 >= 65=1, 4h RSI 81.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STRAX/USDT:USDT | +51.05% | $1,000,922.23 |
| STG/USDT:USDT | +50.08% | $19,445,023.57 |
| MAGMA/USDT:USDT | +45.43% | $2,326,661.59 |
| ESPORTS/USDT:USDT | +41.95% | $25,739,348.77 |
| BLEND/USDT:USDT | +32.00% | $2,348,504.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +3.58% | +3.90% |
| BLESS/USDT:USDT | below_1h_threshold | +2.49% | +2.82% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.39% | +2.72% |
| HOME/USDT:USDT | below_1h_threshold | +2.26% | +2.59% |
| OPN/USDT:USDT | below_1h_threshold | +1.89% | +2.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
