# Decision Report

- generated_at: 2026-06-02T02:33:03.132385+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5389**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.89% / filled 20/20。**
- 全期間 MARKET基準: n=5389, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.89% | **+1.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.42% | **+2.42%** |
| MARKET | 20/20 | 100.0% | +1.89% | **+1.89%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.74% | **+0.96%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.29% | **+0.19%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.14% | **-0.07%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.45% | **-0.41%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 83件 (TP 24 / SL 56 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.94** / 初期 $100.00 (+31.94%)
- 確定: 903件 (Win 210 / Loss 271 / Flat 422) / skip 1047件
- 成長率目線: 平均log +0.000307 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.07% 残高後 $131.94

## 4. Latest Market Context

- 更新: 2026-06-02T02:33:00.579968+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=70752.7
- Funnel: target 776 → liquid 147 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +28.33% | $10,455,337.42 |
| LAB/USDT:USDT | +14.86% | $195,461,730.90 |
| WLD/USDT:USDT | +13.44% | $137,306,305.19 |
| RIF/USDT:USDT | +13.30% | $1,099,608.68 |
| H/USDT:USDT | +11.65% | $57,655,667.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.80% | +4.62% |
| H/USDT:USDT | below_1h_threshold | +4.77% | +4.59% |
| STG/USDT:USDT | below_1h_threshold | +4.70% | +4.51% |
| EPIC/USDT:USDT | below_1h_threshold | +4.19% | +4.01% |
| ZEC/USDT:USDT | below_1h_threshold | +3.64% | +3.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
