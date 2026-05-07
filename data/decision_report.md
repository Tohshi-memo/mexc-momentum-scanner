# Decision Report

- generated_at: 2026-05-07T12:32:32.725425+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3624**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=3624, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.78% | **+0.78%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.99% | **+0.94%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.55% | **+0.77%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.82% | **+0.73%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.03% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.53** / 初期 $100.00 (+6.53%)
- 確定: 118件 (Win 37 / Loss 47 / Flat 34) / skip 67件
- 成長率目線: 平均log +0.000536 / 幾何平均 +0.054% per trade / maxDD +2.62%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $106.53

## 4. Latest Market Context

- 更新: 2026-05-07T12:32:29.828493+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=81012.1
- Funnel: target 771 → liquid 183 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +120.21% | $2,530,152.90 |
| B3/USDT:USDT | +101.99% | $11,910,192.89 |
| PENGUIN/USDT:USDT | +73.66% | $3,808,116.59 |
| DOGS/USDT:USDT | +54.30% | $16,530,340.72 |
| NIL/USDT:USDT | +34.15% | $3,224,261.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONDO/USDT:USDT | below_1h_threshold | +3.61% | +3.39% |
| ICP/USDT:USDT | below_1h_threshold | +3.35% | +3.13% |
| DOGS/USDT:USDT | below_1h_threshold | +3.29% | +3.06% |
| WLFI/USDT:USDT | below_1h_threshold | +2.87% | +2.65% |
| SIREN/USDT:USDT | below_1h_threshold | +2.82% | +2.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
