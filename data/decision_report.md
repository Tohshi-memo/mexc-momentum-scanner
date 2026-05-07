# Decision Report

- generated_at: 2026-05-07T15:42:42.912339+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3650**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=3650, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.09% | **+0.87%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.53% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.46% | **+1.60%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +2.72% | **+1.49%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +2.48% | **+1.49%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.62% | **+1.44%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$111.05** / 初期 $100.00 (+11.05%)
- 確定: 144件 (Win 45 / Loss 53 / Flat 46) / skip 67件
- 成長率目線: 平均log +0.000728 / 幾何平均 +0.073% per trade / maxDD +2.62%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: QCOMSTOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $111.05

## 4. Latest Market Context

- 更新: 2026-05-07T15:42:36.779110+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=79913.3
- Funnel: target 771 → liquid 183 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.6 >= 65=1, 4h RSI 80.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +98.28% | $10,325,249.22 |
| SATO/USDT:USDT | +87.64% | $3,890,442.09 |
| PENGUIN/USDT:USDT | +62.56% | $4,478,894.42 |
| NIL/USDT:USDT | +53.84% | $5,774,095.54 |
| DOGS/USDT:USDT | +48.71% | $18,110,080.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.92% | +4.19% |
| B3/USDT:USDT | below_1h_threshold | +3.02% | +3.29% |
| NIL/USDT:USDT | below_1h_threshold | +2.54% | +2.81% |
| STRK/USDT:USDT | below_1h_threshold | +1.99% | +2.26% |
| KSM/USDT:USDT | below_1h_threshold | +1.93% | +2.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
