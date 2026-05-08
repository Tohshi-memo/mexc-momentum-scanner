# Decision Report

- generated_at: 2026-05-08T02:57:49.020906+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3725**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=3725, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.62% | **+1.45%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.80% | **+1.26%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.39% | **+1.11%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.95% | **+0.88%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.78% | **+0.47%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.82% | **+0.45%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.41%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.44% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$98.83** / 初期 $100.00 (-1.17%)
- 確定トレード: 24件 (TP 6 / SL 16 / EXP 2)
- 最新: PENGUIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 189件 (Win 48 / Loss 64 / Flat 77) / skip 97件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T02:57:42.549245+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=79410.6
- Funnel: target 771 → liquid 184 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.9 >= 65=1, 4h RSI 67.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +33.76% | $1,903,477.06 |
| SATO/USDT:USDT | +23.58% | $8,832,715.66 |
| LAB/USDT:USDT | +20.77% | $214,319,713.63 |
| BSB/USDT:USDT | +18.23% | $3,547,367.35 |
| TST/USDT:USDT | +17.90% | $6,290,256.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +4.34% | +4.70% |
| BSB/USDT:USDT | below_1h_threshold | +4.15% | +4.51% |
| M/USDT:USDT | below_1h_threshold | +4.15% | +4.51% |
| D/USDT:USDT | below_1h_threshold | +1.82% | +2.18% |
| LIGHT/USDT:USDT | below_1h_threshold | +1.73% | +2.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
