# Decision Report

- generated_at: 2026-05-07T13:17:38.040356+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3630**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=3630, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +5.95% | **+2.38%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +3.40% | **+1.87%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.95% | **+1.03%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.31% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.82** / 初期 $100.00 (+8.82%)
- 確定: 124件 (Win 40 / Loss 48 / Flat 36) / skip 67件
- 成長率目線: 平均log +0.000681 / 幾何平均 +0.068% per trade / maxDD +2.62%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KSM/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $108.82

## 4. Latest Market Context

- 更新: 2026-05-07T13:17:35.349590+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=80929.5
- Funnel: target 771 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +87.37% | $11,497,801.70 |
| PENGUIN/USDT:USDT | +72.75% | $3,966,851.70 |
| SATO/USDT:USDT | +68.49% | $2,922,574.67 |
| DOGS/USDT:USDT | +50.29% | $16,866,686.67 |
| NIL/USDT:USDT | +35.93% | $3,472,616.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +3.96% | +4.20% |
| FHE/USDT:USDT | below_1h_threshold | +2.96% | +3.20% |
| SATO/USDT:USDT | below_1h_threshold | +2.47% | +2.71% |
| XPL/USDT:USDT | below_1h_threshold | +2.29% | +2.53% |
| BLESS/USDT:USDT | below_1h_threshold | +1.99% | +2.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
