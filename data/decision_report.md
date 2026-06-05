# Decision Report

- generated_at: 2026-06-05T16:46:05.194357+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5730**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=5730, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +3.13% | **+3.13%** |
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.53% | **+2.41%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.64% | **+2.11%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.57% | **+0.94%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +2.18% | **+1.20%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.57% | **+0.32%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.09% | **+0.06%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | -0.06% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1011件 (Win 239 / Loss 313 / Flat 459) / skip 1280件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T16:46:01.581642+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.82% price=60903.3
- Funnel: target 773 → liquid 159 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.3 >= 65=1, 4h RSI 66.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EPIC/USDT:USDT | +11.46% | $2,899,363.46 |
| HOME/USDT:USDT | +10.73% | $8,982,815.67 |
| BABY/USDT:USDT | +6.95% | $14,060,265.94 |
| ZEC/USDT:USDT | +5.80% | $1,141,170,270.12 |
| BILL/USDT:USDT | +4.24% | $3,508,827.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_relative_strength | +5.73% | +4.91% |
| ZEST/USDT:USDT | below_1h_threshold | +4.39% | +3.56% |
| BILL/USDT:USDT | below_1h_threshold | +4.24% | +3.42% |
| BSB/USDT:USDT | below_1h_threshold | +3.58% | +2.76% |
| LIT/USDT:USDT | below_1h_threshold | +3.08% | +2.26% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
